#include <iostream>

using namespace std;

long long tmp[10];


void push(long long x, long long y)
{
	tmp[x%3 + (y%3)*3]++;
}


long long good(int a, int b, int c)
{
	if( (a%3 + b%3 + c%3)%3 == 0 && (a/3 + b/3 + c/3)%3 == 0 )
	{
		if(a==c)
			return tmp[a]*(tmp[a]-1)*(tmp[a]-2)/6;
		if(a==b)
			return tmp[a]*(tmp[a]-1)*tmp[b]/2;
		return tmp[a]*tmp[b]*tmp[c];
	}
	return 0;
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int N;
	scanf("%d",&N);
	for(int I=0; I<N; I++)
	{
		long long x0,y0,A,B,C,D,M;
		int n;
		scanf("%d %lld %lld %lld %lld %lld %lld %lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
		long long X = x0, Y = y0;	
		memset(tmp,0,sizeof(tmp));
		push(X,Y);
		for(int i=1; i<n; i++)
		{
			X = ((A * X)%M + B) % M;
			Y = ((C * Y)%M + D) % M;
			push(X,Y);
		}
		long long res = 0;
		n=9;
		for(int i=0; i<n; i++)
			for(int j=i; j<n; j++)
				for(int k=j; k<n; k++)
					res+=good(i,j,k);
		printf("Case #%d: %lld\n",I+1,res);
	}
	return 0;
}