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
int num[1009];
int main()
{
	int t,n,mini,i,sum,cnt=1,x;
	S(t);
	while(t--)
	{
		S(n);
		sum=x=0;
		mini=(1<<30);
		for(i=0;i<n;i++)
		{
			S(num[i]);
			mini=min(mini,num[i]);
			sum+=num[i];
			x^=num[i];
		}
		sum-=mini;
		if(x!=0)
		printf("Case #%d: NO\n",cnt++);
		else
		printf("Case #%d: %d\n",cnt++,sum);
	}
	return 0;
}
