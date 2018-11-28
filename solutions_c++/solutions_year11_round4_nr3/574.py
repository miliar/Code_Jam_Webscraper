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
int Prime[120000];
int pos[511001];
#define prime(i) ((Prime[i>>5])&(1<<(i&(31))))
#define set(j) (Prime[j>>5]|=(1<<(j&(31))))
#define LIM 100000
#define SLIM 1001
int main()
{
	int i, j, m, n, t,x,k,l,h;
	set(1);
	pos[0]=2;
	pos[1]=3;
	for(k=2,l=2,i=5; i<=SLIM; k++,i=3*k-(k&1)-1)
		if(prime(k)==0)
		{
			pos[l++]=i;
			for(j=i*i,h=((j+2)/3); j<=LIM; h+=(k&1)?(h&1?((k<<2)-3):((k<<1)-1)):(h&1?((k<<1)-1):((k<<2)-1)), j=3*h-(h&1)-1)
			set(h);
		}
	i=3*k-(k&1)-1;
	for(; i<=LIM; k++,i=3*k-(k&1)-1)
	if(prime(k)==0)
		pos[l++]=i;
	
	
	int ans, N;
	S(t);
	for(j=1;j<=t;j++)
	{
		S(N);
		ans=1;
		if(N==1)
		{
			printf("Case #%d: 0\n",j);
			continue;
		}
		for(i=0;i<l;i++) 
		{
                        if(N>=pos[i])
                        {
                                int lg=log(N)/(log(pos[i]));
                                ans+=(lg-1);
                        }
                }
                printf("Case #%d: %d\n",j,ans);
        }
	return 0;
}
