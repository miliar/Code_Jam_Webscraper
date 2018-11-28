#include <iostream>
#include <vector>

using namespace std;

#define For(i,n) for(int i=0;i<(n);++i)
#define Forfrom(i,fr,n) for(int i=(fr);i<(n);++i)

typedef long long LL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;

void addtree(VVLL &v, int x, int y) {
  ++v[x%3][y%3];
}

int main() {
  int n;
  cin >> n;
  For(c,n) {
    cout << "Case #" << (c+1) << ": ";

    VVLL v(3, 3);
    
    long long n, A, B, C, D, x, y, M;
    cin >> n >> A >> B >> C >> D >> x >> y >> M;
    addtree(v, x, y);
    For(i, n-1) {
      x = (A*x+B) % M;
      y = (C*y+D) % M;
      addtree(v, x, y);
    }

    LL num = 0;
    For(i, 9) Forfrom(j, i, 9) Forfrom(k, j, 9) {
      if ((i+j+k)%3 == 0 and (i/3+j/3+k/3)%3==0) {
	LL triplets;
	LL vi = v[i%3][i/3];
	LL vj = v[j%3][j/3];
	LL vk = v[k%3][k/3];
	if (i==j and j==k) {
	  triplets = (vi*(vi-1)*(vi-2))/6;
	}
	else if (i==j) {
	  triplets = ((vi*(vi-1))/2)*vk;
	}
	else if (j==k) {
	  triplets = ((vj*(vj-1))/2)*vi;
	}
	else if (i==k) {
	  triplets = ((vi*(vi-1))/2)*vj;
	}
	else {
	  triplets = vi*vj*vk;
	}
	num += triplets;
      }
    }
    
    cout << num << endl;
  }
}
