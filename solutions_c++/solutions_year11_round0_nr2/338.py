#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<string>
#include<set>
#include<map>
using namespace std;
#define vi vector<int>
#define vvi vector<vi>
#define vp vector< pair<int,int> >
#define vvp vector< vp >
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef long long lli;
int __sign;
int __ch;
inline void S( int &x )
{
			x=0;
			while((__ch<'0' || __ch>'9') && __ch!='-' && __ch!=EOF)	__ch=getchar_unlocked();
			if (__ch=='-')
				__sign=-1 , __ch=getchar_unlocked();
			else
				__sign=1;
			
			do
				x=(x<<3)+(x<<1)+__ch-'0';
			while((__ch=getchar_unlocked())>='0' && __ch<='9');
			x*=__sign;
}
char ele[]={'Q','W','E','R','A','S','D','F'};
int ind[256];
char str[200], ans[200];
int opp[26][26];
char comb[26][26];
int main()
{
	int t,c,d,n,i,l,j,flag,cnt=1;
	for(i=0;i<8;i++)
	ind[ele[i]]=i+1;
	S(t);
	while(t--)
	{
		memset(opp,0,sizeof(opp));
		memset(comb,0,sizeof(comb));
		scanf("%d",&c);
		for(i=0;i<c;i++)
		{
			scanf("%s",str);
			comb[str[0]-'A'][str[1]-'A']=str[2];
			comb[str[1]-'A'][str[0]-'A']=str[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			scanf("%s",str);
			opp[str[0]-'A'][str[1]-'A']=1;
			opp[str[1]-'A'][str[0]-'A']=1;
		}
		scanf("%d",&n);
		scanf("%s",str);
		l=0;
		ans[l++]=str[0];
		for(i=1;i<n;i++)
		{
			if(l>0&&comb[str[i]-'A'][ans[l-1]-'A']!=0)
			ans[l-1]=comb[str[i]-'A'][ans[l-1]-'A'];
			else
			{
				flag=0;
				for(j=l-1;j>=0;j--)
				if(opp[str[i]-'A'][ans[j]-'A']==1)
				{
					ans[0]='\0';
					l=0;
					flag=1;
					break;
				}
				if(flag==0)
				ans[l++]=str[i];
			}
		}
		ans[l]='\0';
		printf("Case #%d: [",cnt++);
		for(i=0;i<l;i++)
		printf("%c%s",ans[i],i==(l-1)?"":", ");
		puts("]");
	}
	return 0;
}
