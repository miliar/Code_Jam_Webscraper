#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
#include <cmath>
#include <map>
#include <set>
#include <cstring>
#include <sstream>
#include <cctype>

#define FIN for(i=0;i<N;i++)
#define FIM for(i=0;i<M;i++)
#define FJN for(j=0;j<N;j++)
#define FJM for(j=0;j<M;j++)
#define FOR(i,N) for(i=0;i<N;i++)
#define FAB(i,A,B) for(i=A;i<=B;i++)
using namespace std;

__int64 R,K,N; 
__int64 A[5555];
__int64 SUMS[5555];
__int64 NEXT[5555];
__int64 SCORE[5555];

int prev[5555];
__int64 prevS[5555];
__int64 ans,bonus;

__int64 suma(int i,int l)
{
	__int64 ret=0;
	if(i>0) ret=-SUMS[i-1];
	if(i+l<N) return SUMS[i+l]+ret;

	return SUMS[N-1]+ret+SUMS[(i+l)%N];
}
void test()
{
	cin>>R>>K>>N;
	int i,j;
	FIN cin>>A[i];
	FIN SUMS[i]=0;
	SUMS[0]=A[0];
	for(i=1;i<N;i++) SUMS[i]=SUMS[i-1]+A[i];
	FIN NEXT[i]=0;
	FIN SCORE[i]=0;

	__int64 k=K;

	ans=0;

	int a=0,b=N-1,c=0,x;

	if(SUMS[N-1]<K)
	{
		ans=SUMS[N-1]*R;
	}
	else
	{
		for(i=0;i<N;i++)
		{
			
			a=0; b=N-1;
			
			while(b>a+1)
			{
				
				c=(a+b)/2;
				if(suma(i,c)<=k) a=c;
				else b=c;
			}
			if(suma(i,b)<=k) a=b;
			SCORE[i]=suma(i,a);
			NEXT[i]=(a+1+i)%N;
		}

		FIN prev[i]=-1;

		x=0;
		c=0;
		ans=0;

		while(prev[x]==-1&&c<R)
		{
			//cout<<"STEP"<<x<<" "<<c<<" "<<ans<<endl;
			prev[x]=c;
			prevS[x]=ans;
			c++;
			ans+=SCORE[x];
			x=NEXT[x];
		}

		if(c<R)
		{
			//cout<<x<<" "<<ans<<" "<<prevS[x]<<" "<<c<<" "<<prev[x]<<" "<<R<<endl;
			ans+=(ans-prevS[x])*(((R-c)/(c-prev[x])));
			c+=(((R-c)/(c-prev[x]))*(c-prev[x]));
		}
		//cout<<x<<" "<<ans<<" "<<prevS[x]<<" "<<c<<" "<<prev[x]<<" "<<R<<endl;

		while(c<R)
		{
			c++;
			ans+=SCORE[x];
			x=NEXT[x];
		}

		
	}

	cout<<ans<<endl;

	//cout<<ans<<endl;
	/*bonus=(K/SUMS[N-1])*SUMS[N-1];;
	K-=bonus;
	ans=bonus*
	SCORE[0]=(K/SUMS[N-1])*SUMS[N-1];
	k=K-SCORE[0];

	if(k)
	{
		int a=0,b=N-1,c;

		while(b>a+1)
		{
			c=(a+b)/2;
			if(SUMS[c]<=k) a=c;
			else b=c;
		}
		if(SUMS[b]<=k) a=b;
		SCORE[0]+=SUMS[a];
		NEXT[0]=(a+1)%N;
	}
	cout<<SCORE[0]<<" "<<NEXT[0]<<endl;*/
	

		
}
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

	int t=0,T;

	scanf("%d",&T);

	for(t=0;t<T;t++)
	{
		printf("Case #%d: ",t+1);
		test();
	}
}