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

bool done[101][11];
int dp[101][11],h1,h2,h3,p,s,n,t,ans,cc=0;

bool chk(int ff)
{
	for(int fh1=0;fh1<=10;fh1++)
		for(int fh2=max(fh1-2,0);fh2<=min(10,fh1+2);fh2++)
			for(int fh3=max(fh1-2,0);fh3<=min(10,fh1+2);fh3++)
				if(fh1+fh2+fh3==ff&&(abs(fh1-fh2)==2||abs(fh2-fh3)==2||abs(fh1-fh3)==2))
					return 1;
	return 0;
}

bool cal(int ff)
{
	for(int fh1=p;fh1<=min(ff,10);fh1++)
		for(int fh2=max(fh1-2,0);fh2<=min(10,fh1+2);fh2++)
			for(int fh3=max(fh1-2,0);fh3<=min(10,fh1+2);fh3++)
				if(fh1+fh2+fh3==ff&&(abs(fh1-fh2)==2||abs(fh2-fh3)==2||abs(fh1-fh3)==2))
					return 1;
	return 0;
}

void upt(int fh1,int fh2,int fw)
{
	if(fh1==n&&fh2==s)
		ans=max(ans,fw);
	else if(!done[fh1][fh2]||dp[fh1][fh2]<fw)
	{
		done[fh1][fh2]=1;dp[fh1][fh2]=fw;
	}
}

int main(){
	freopen("B-small-attempt1 (1).in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&n,&s,&p);
		mem(done);
		ans=0;
		upt(0,0,0);
		for(h1=0;h1<n;h1++)
		{
			scanf("%d",&h3);
			
			for(h2=0;h2<=s;h2++)
				if(done[h1][h2])
				{
					upt(h1+1,h2,dp[h1][h2]+((h3+2)/3>=p));
					if(h2<s&&chk(h3))
						upt(h1+1,h2+1,dp[h1][h2]+cal(h3));
				}
		}
		printf("Case #%d: %d\n",++cc,ans);
	}
}
