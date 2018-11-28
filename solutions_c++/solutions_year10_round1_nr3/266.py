#include <cstdio>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <math.h>
#include <limits.h>
#include <float.h>
#include <algorithm>
#include <iostream>

using namespace std;

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
typedef __int64 LL;
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define FORR(a,s,b) for(int a=s;a<=b;a++)
#define CLR(a,b) memset(a,b,sizeof(a))
#define VI vector<int>
#define VS vector<string>

int n=30;

int r[32][32];

// margin = floor(n/tau)
int margin[1048576];

void doab(int a,int b) {
    r[a][b]=2;
	for(int aa=a,bb=b; (aa-=bb)>0 && bb>0; )
        if(r[aa][bb]==2) { r[a][b]=1; return; }
	for(int aa=a,bb=b; (bb-=aa)>0 && aa>0; )
        if(r[aa][bb]==2) { r[a][b]=1; return; }
}

LL res(int l,int r,int b,int t) {
	if(t<b) return 0;
	if(r<l) return 0;

	if(l==r && b==t) {
		return b<=margin[l] || l<=margin[b];
	}
	if(t<=margin[l] || r<=margin[b]) return
		(r-l+1)*LL(t-b+1);

	if(b>margin[r] && l>margin[t])
		return 0;

	if(r-l > t-b)	{
		int mid = (r+l+1)/2;
		return res(l,mid-1,b,t) + res(mid,r,b,t);
	} else {
		int mid = (t+b+1)/2;
		return res(l,r,b,mid-1) + res(l,r,mid,t);
	}
}


int main()
{
    freopen("c:/gcj/cc.in","rt",stdin);
    freopen("c:/gcj/cc.out","wt",stdout);
	long double tau=5;
	tau = 1+sqrt(tau);
    tau/=2;
	FOR(i,1048576) {
		margin[i] = i/tau;
	}

	r[1][1]=2;

//    printf("** ");
//	FORR(j,1,n) printf("%2d ",j);
//    puts("");

	FORR(i,1,n) {
//        printf("%2d ",i);
		FORR(j,1,n) {
//            if(r[i][j]==0 && i==j)
//               r[i][j]=2;
//            if(r[i][j]==0) continue;
			doab(i,j);
//			printf("%2d ",r[i][j]);
		}
//		puts("");
	}

	int t;
	cin >> t;

	FORR(cn,1,t) {
		cout << "Case #"<<cn<<": ";

		int a1,a2,b1,b2;
		cin >> a1 >> a2 >> b1 >> b2;

		LL m=res(a1,a2,b1,b2);

//		FORR(a,a1,a2) FORR(b,b1,b2) m+= (r[a][b]==1);

		cout << m << "\n";
	}



	return 0;
}

