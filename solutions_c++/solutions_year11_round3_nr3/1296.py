#include <fstream>
#include <cmath>

using namespace std;

ifstream in("in");
ofstream out("out");

typedef long long int lli;

lli gcd(lli a, lli b){
	if(abs(b- a) > max(sqrt(a), sqrt(b))) return 1;
	while(1){
		if(a < b) { lli c = a; a = b; b = c; }
		if(a % b) a %= b;
		else break;
	}
	return a / b;
}

void sol(){
	int n;
	lli L, H;
	in >> n >> L >> H;
	int a[n], g;
	in >> g;
	a[0] = g;
	for(int i = 1; i < n; i++){
		in >> a[i];
	//	g = gcd(g, a[i]);
	}
	bool divs;
	for(lli i = L; i <= H; i++){
		divs = true;
		for(int j = 0; j < n; j++) divs &= !(i % a[j] && a[j] % i);
		if(divs){
			out << i;
			return;
		}
	}
	out << "NO";
}

int main(){
	int n;
	in >> n;
	for(int i = 0; i < n; i++)
		out << "Case #" << i + 1 << ": ",
		sol(), out << endl;
}
