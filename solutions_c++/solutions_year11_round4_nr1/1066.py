#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>
#include <utility>
#include <algorithm>

#define SQR(X) X*X
#define MAX(X,Y) (X)>(Y)? (X) : (Y)
#define X first
#define Y second

using namespace std;

int main() {
	freopen("in.txt","r",stdin);
	freopen("out123.txt","w",stdout);
	int tcount;
	cin >> tcount;
	for(int tt=1;tt<=tcount;++tt){
		int X,S,R,n; double t;
		cin >> X >> S >> R >> t >> n;
		vector< pair<int, int> > m(n+1);
		int pp=X;
		for(int i=1;i<=n;++i){
			int a,b,sp;
			cin >> a >> b >> sp;
			m[i].X = sp;
			m[i].Y = b-a;
			pp-=(b-a);
		}
		m[0] = make_pair(0,pp);
		double res=0;
		sort(m.begin(),m.end());	
		for(int i=0;i<m.size();++i){
			if (t>0){
				double r = ((double)(m[i].Y))/(double)(R+m[i].X);
				if (r>t){
					double lr = t*(double)(R+m[i].X);
					res += t + ((double)(m[i].Y - lr)) / (double)(S+m[i].X);
					t=0;
				} else {
					res+=r;
					t-=r;
				}
			} else {
				res += ((double)m[i].Y) / (double)(m[i].X+S);
			}
		}
		
		printf("Case #%d: %.9lf\n",tt,res);
	}
	fclose(stdout);
	return 0;
}
