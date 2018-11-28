
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cctype>
#include<iostream>
#include<stack>
#include<set>
#include<list>
#include<map>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
//-------------------------------------------------------
typedef pair<int,int> ii;
typedef vector<int> vi;
#define pb push_back
#define sz(c) (c).size()
#define all(c) (c).begin(),(c).end()
#define vtr(c,i) for(vi::iterator i=c.begin();i!=c.end();i++)
#define INF  (1<<30)
#define EPS  1e-8
#define SET(NAME)   (memset(NAME,-1,sizeof(NAME)))
#define CLR(NAME)   (memset(NAME,0,sizeof(NAME)))
#define max(a,b) ((a)>(b)?(a):(b))

//--------------------------------------------------------
char str[70];
int mp[200];
void reset(){}
int minBase(){

	int st[200];
	CLR(st);
	int res=0,i;
	for(i=strlen(str)-1;i>=0;i--)
		st[str[i]]=1;
	for(i=30;i<150;i++)
		res+=st[i];
	return res;
}
void mapvalue(){

	SET(mp);
	int l=strlen(str),i,as=2;
	mp[str[0]]=1;
	for(i=1;i<l;i++)
		if(mp[str[i]]==-1)
		{
			mp[str[i]]=0;
			break;
		}

	for(i=1;i<l;i++)
		if(mp[str[i]]==-1)
		{
			mp[str[i]]=as;
			as++;			
		}

}
void process(){

	int b=minBase(),i;
	if(b==1) 
		b=2;
	mapvalue();

	 unsigned long long res=0;
	int l=strlen(str);
	for(i=0;i<l;i++)
		res=res*b+mp[str[i]];

	cout<<res<<endl;
}
int main()
{
	freopen("contest/A-large.in","rt",stdin);
	freopen("contest/out.txt","w",stdout);
	int t,cas=1;
		
		scanf("%d",&t);
		while(t--){

			scanf("%s",str);
			printf("Case #%d: ",cas++);
			process();
		
		}
		return 0;
}
