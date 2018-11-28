#include<iostream>
#include<map>
#include<math.h>
#include<vector>
#include<string>
#include<string.h>
#include<queue>
#include<algorithm>
#include<sstream>
#define all(X) (X).begin(),(X).end()
#define mem(X) memset(X,0,sizeof(X))
using namespace std;
typedef long long ll;
typedef vector<int>::iterator iv;
typedef map<string,int>::iterator msii;
typedef map<int,int>::iterator miii;
typedef map<int,bool>::iterator mibi;
typedef map<string,bool>::iterator msbi;
typedef map<string,int> msi;
typedef map<int,int> mii;
typedef map<int,bool> mib;
typedef map<string,bool> msb;
typedef vector<int> vi;
typedef vector<string> vs;

int h1,t,a,b,cc=0,pw[100],l,lll;
ll ans;
bool done[2000001];

int call(int fh1)
{
	int ret=0;
	while(fh1)
	{
		fh1/=10;
		ret++;
	}
	return ret;
}

bool check(int fh1,int fh2)
{
	for(;(fh1||fh2)&&(fh1%10==fh2%10);fh1/=10,fh2/=10);
	return fh1%10<fh2%10;
}

void dfs(int nn,int mn,int vv)
{
	if(nn==l)
	{
		int res=0,fh1,fh2,fh3;
		
		for(fh1=vv,fh2=vv%10;fh1/=10;)
			if(fh1%10!=fh2)
				break;
		if(!fh1)return ;
		
		
		//cout<<endl<<vv<<endl;
		
		bool fb=1;
		

		if(fb)
		{
			cout<<vv<<endl;
			
		}
	}
	else
	{
		for(int fh1=mn;fh1<10;fh1++)
			dfs(nn+1,mn,vv+fh1*pw[nn]);
	}
}

int main(){
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	for(pw[0]=h1=1;h1<=11;h1++)pw[h1]=pw[h1-1]*10;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&a,&b);
		mem(done);
		l=call(a);
		
		ans=0;
		int asas=l;
		
		for(lll=1;--l;lll*=10);
		
		l=asas;
		
		for(int vv=a;vv<=b;vv++)
		{
			if(!done[vv])
			{
				int res=0,fh1,fh2;
				for(fh1=0;fh1<l;fh1++)
				{
					if(vv>=lll&&a<=vv&&vv<=b&&!done[vv])
					{
						done[vv]=1;
						res++;
					}
					//cout<<vv<<endl;
					fh2=vv/lll;
					vv=(vv-fh2*lll)*10+fh2;
				}
				ans+=res*(res-1)/2;
			}
		}
		
		printf("Case #%d: %d\n",++cc,ans);
	}
}
