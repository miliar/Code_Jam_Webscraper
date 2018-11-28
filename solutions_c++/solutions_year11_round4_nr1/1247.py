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
#include<cctype>
#include<functional>
using namespace std;
#define F(x,a,b) for(x=a;x<=b;++x)
#define LL long long
#define PII	pair<int ,int >
int C,cc,i,S,R,X,N,a,b,w,L;
int main(){
	freopen("ain.txt","r",stdin);
	freopen("aou.txt","w",stdout);
	double t,tt,T;
	scanf("%d",&C);
	F(cc,1,C){
		scanf("%d%d%d%lf%d",&X,&S,&R,&t,&N);vector <PII> p;
		R-=S;a=0;T=0;p.push_back(make_pair(S,X));
		F(i,1,N){
			scanf("%d%d%d",&a,&b,&w);
			w+=S;L=b-a;
            p.push_back(make_pair(w,L));
            p[0].second-=L;
		}
		sort(p.begin(),p.end());
		F(i,0,N){
			tt=double(p[i].second)/(p[i].first+R);
			if(tt<t){
				T+=tt;t-=tt;
			}else{
				T+=t+(p[i].second-t*(p[i].first+R))/p[i].first;t=0;
			}
		}
		printf("Case #%d: %.7lf\n",cc,T);
	}
	return 0;
}
