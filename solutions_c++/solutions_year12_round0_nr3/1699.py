# include <cstdio>
# include <cstring>
# include <cstdlib>
# include <iostream>
# include <cmath>
# include <string>
# include <algorithm>
# include <vector>
# define REP(i,n) for(int i=0;i<n;i++)
# define REP1(i,n) for(int i=1;i<=n;i++)
# define CLR(a,b) memset(a,b,sizeof(a))
# define For(i,a,b) for(int i=a;i<=b;i++)
# define Trv(p,a) for(int p=head[a];p;p=next[p])
# define INF 0x7FFFFFFF
# define vi vector<int>
# define it iterator
# define pb push_back
using namespace std;

typedef long long int64;
void setIO(string name){
	string	is=name+".in",
			os=name+".out";
	freopen(is.c_str(),"r",stdin);
	freopen(os.c_str(),"w",stdout);
}

int vis[2000005],que[200],qf,qr,n;
void work(){
	CLR(vis,0);
	int64 ans=0;
	int l,r;scanf("%d %d",&l,&r);
	int w=0,b=l;while(b)	w++,b/=10;
	int lim=1;
	REP1(i,w-1)	lim*=10;
	For(i,l,r)	if(!vis[i]){
		qr=0;
		que[qr++]=i;
		int t=i;
		REP(j,w){
			t=((t%10)*lim)+t/10;
			if(t<l||t>r)	continue;
			que[qr++]=t;
			vis[t]=1;
		}
		sort(que,que+qr);
		int cnt=0,last=-1;
		For(j,0,qr-1){
			if(que[j]!=last){
				cnt++;
				last=que[j];
			}
		}
		ans+=cnt*(cnt-1)/2;
	}
	cout<<ans<<endl;
}
	

int main(){
	setIO("C-large");
	int casen;scanf("%d",&casen);
	REP1(i,casen){
		printf("Case #%d: ",i);
		work();
	}
	return 0;
}
