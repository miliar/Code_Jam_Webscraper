#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>
#include<algorithm>
#include<utility>
#include<map>
#include<vector>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<cstdlib>
#include<cmath>
using namespace std;
#define F(x,a,b) for(x=a;x<=b;++x)
int main(){
	int C,cc,i,j,t,w,n,tt,k;
	double wp[128],op[128],oo[128],s;
	char p[128][128];
	freopen("ain.txt","r",stdin);
	freopen("aou.txt","w",stdout);
	scanf("%d",&C);
	F(cc,1,C){
		scanf("%d",&n);getchar();
		F(i,0,n-1){
			gets(p[i]);
			t=0;w=0;
			F(j,0,n-1)if(p[i][j]!='.'){
				++t;
				if(p[i][j]=='1')++w;
			}
			wp[i]=(double)w/t;
		}
		F(k,0,n-1){
            tt=0;s=0;
			F(i,0,n-1)if(i!=k && p[k][i]!='.'){++tt;w=0;t=0;
			 F(j,0,n-1)if(j!=k)
			 if(p[i][j]!='.'){
			     	++t;
			     	if(p[i][j]=='1')++w;
		      	}
             s+=(double)w/t;
            }
			op[k]=s/tt;
		}
		F(i,0,n-1){t=0;s=0;
			F(j,0,n-1)
			if(p[i][j]!='.'){
				++t;
				s+=op[j];
			}
			oo[i]=s/t;
		}
		printf("Case #%d:\n",cc);
		F(i,0,n-1)printf("%.8lf\n",0.25*wp[i]+0.5*op[i]+0.25*oo[i]);
	}
	return 0;
}
