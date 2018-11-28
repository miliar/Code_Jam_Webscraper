#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
using namespace std;

double p[200],ans,res;
int l[200],r[200],fa[200],test,L,i,j,k,a,t,cnt,n,bl;
string f[200],bs[200],s1,orz,b;


int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>test;
	for (int tt=1;tt<=test;++tt){
		cin>>L;
		getline(cin,orz);
		s1="";
		for (i=0;i<L;++i){
			getline(cin,orz);
			int sz=orz.size();
			for (j=0;j<sz;++j)
				if (orz[j]=='(')s1+=" 0 ";
				else if (orz[j]==')')s1+=" 1 ";
				else s1+=orz[j];
		};
		istringstream sin(s1);
		memset(l,0,sizeof l);memset(r,0,sizeof r);
		sin>>a;t=1;cnt=1;
		while (t){
			if (l[t] && !r[t]){
				++cnt;fa[cnt]=t;r[t]=cnt;t=cnt;continue;
			};

			sin>>p[t]>>f[t];
			if (f[t]=="1") { 
				while (1){
					sin>>a;
					t=fa[t];
					if (a==0 || t==0)break;
				};
				continue;
			};
			sin>>a;
			if (a==0){
				++cnt;fa[cnt]=t;
				if (!l[t])l[t]=cnt;else r[t]=cnt;
				t=cnt;
			}
			else while (1){
				sin>>a;
				if (a==0 || t==0)break;
				t=fa[t];
			};
		};

		printf("Case #%d:\n",tt);
		cin>>n;
		for (i=1;i<=n;++i){
			cin>>b>>bl;
			for (j=0;j<bl;++j)cin>>bs[j];
			res=1;t=1;
			while (1){
				res*=p[t];
				if (!l[t])break;
				bool flag=false;
				for (j=0;j<bl;++j)if (bs[j]==f[t]) { flag=true;break; };
				if (flag)t=l[t];else t=r[t];
			};
			printf("%.9lf\n",res);
		};
	};
};