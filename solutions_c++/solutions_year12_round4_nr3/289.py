#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <cassert>
using namespace std;

typedef long long Int;

Int gcd(Int a, Int b) {
  if(a < b)
	return gcd(b, a);
  if(b == 0)
	return a;
  return gcd(b, a % b);
}

struct Rat {
  Int p, q;
  Rat(Int P=0, int Q=1): p(P), q(Q) {
	if(q < 0) {
	  q *= -1;
	  p *= -1;
	}

	Int d = gcd(abs(p), q);
	p /= d;
	q /= d;
  }
};

Rat operator + (const Rat& a, const Rat& b) {
  return Rat(a.p * b.q + a.q * b.p, a.q * b.q);
}

Rat operator - (const Rat& a) {
  return Rat(-a.p, a.q);
}

Rat operator - (const Rat& a, const Rat& b) {
  return a + (-b);
}

Rat operator * (const Rat& a, const Rat& b) {
  return Rat(a.p * b.p, a.q * b.q);
}

Rat operator / (const Rat& a, const Rat& b) {
  return Rat(a.p * b.q, a.q * b.p);
}

bool operator == (const Rat& a, const Rat& b) {
  return a.p == b.p && a.q == b.q;
}

ostream& operator << (ostream& out, const Rat& a) {
  out << a.p << "/" << a.q;
  return out;
}

vector<int> highest;
vector<Rat> height;

Rat next_slope(Rat i, Rat j, Rat slope) {
  return (j - i) /  (j - i - 1) * slope;
}

bool go(int i, int j, Rat slope);

bool goin(int i, int j, Rat slope) {
  //  cout << "goin(" << i << ", " << j << ", " << slope << ")\n";
  if(i + 1 == j)
	return true;

  //  cout << "Set height " << i+1 << " = " << height[i] << "\n";
  height[i+1] = height[i];
  return go(i+1, j, next_slope(i, j, slope));
}

bool go(int i, int j, Rat slope) {
  //  cout << "go(" << i << ", " << j << ", " << slope << ")\n";
  if(i == j)
	return true;

  int next = highest[i];
  if(next == j) {
	if(height[j] == 0) {
	  height[j] = height[i] + slope * (j - i);
	  //	  cout << "Set height " << j << " = " << height[j] << "\n";
	}
	return goin(i, j, slope);
  } else if(next < j) {
	if(!go(i, next, slope))
	  return false;
	if(!go(next, j, slope))
	  return false;
  } else {
	return false;
  }
  return true;
}


vector<Int> clear_frac(const vector<Rat>& fracs) {
  Int d = 1;
  for(int i=0;i<fracs.size();i++) {
	d = d * fracs[i].q / gcd(d, fracs[i].q);
  }
  vector<Int> ret;
  for(int i=0;i<fracs.size();i++) {
	Rat r = fracs[i] * d;
	assert(r.q == 1);
	ret.push_back(r.p);
  }
  return ret;
}

int main()
{
  int T;
  cin >> T;
  for(int c=1;c<=T;c++) {
	int N;
	cin >> N;
	highest.resize(N-1);
	height.clear();
	height.resize(N);
	for(int i=0;i<N-1;i++) {
	  int H;
	  cin >> H;
	  highest[i] = H-1; // 1-based to 0-based
	}

	height[0] = 1;
	bool ok = go(0, N-1, 1);

	cout << "Case #" << c << ": ";
	if(!ok)
	  cout << "Impossible";
	else {
	  vector<Int> intHeight = clear_frac(height);
	  for(int i=0;i<N;i++) {
		if(i > 0)
		  cout << " ";
		cout << intHeight[i];
	  }
	}
	cout << "\n";
  }
  return 0;
}
