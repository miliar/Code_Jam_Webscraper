#include	<cstdio>
#include	<cstdlib>
#include	<cstring>
#include	<string>
#include	<vector>
#include	<cmath>
#include	<algorithm>
#include	<cassert>
#include	<set>
#include	<map>
#include	<queue>
#include	<iostream>
#include <fstream>
using namespace std;
#define pb push_back
#define REP(i,n) for(int i=0;i<(n);i++ ) 

typedef long long LL;
typedef pair<int,int> piii;

//À©Õ¹EuclidÇó½âgcd(a,b)=ax+by
int ext_gcd(int a,int b,int& x,int& y){
	int t,ret;
	if (!b){
		x=1,y=0;
		return a;
	}
	ret=ext_gcd(b,a%b,x,y);
	t=x,x=y,y=t-a/b*y;
	return ret;
}

int main()
{
        int T;
        cin>>T;
        REP(cas,T)
        {
                printf("Case #%d: ",cas+1);
                int N,M,A;
                cin>>N>>M>>A;
                int suc=0;
                int x1,x2,g,y1,y2;
                for (x1=0;x1<=N;x1++)
                        for (x2=0;x2<=N ;x2++)
                                for (y1=0;y1<=M;y1++)
                                        for (y2=0;y2<=M;y2++)
                                                if (x1*y1-x2*y2==A)
                                                {
                                                        suc=1;
                                                        goto lab;
                                                }
                lab:;
                if (suc)
                {
                        printf("0 0 %d %d %d %d\n",x1,y2,x2,y1);
                }
                else
                        puts("IMPOSSIBLE");
        }
        return 0;
}
