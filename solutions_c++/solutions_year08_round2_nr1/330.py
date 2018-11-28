#include <iostream>
using namespace std;

int N;
int n,A,B,Cc,D,x0,y0,M;

int p[3][3];

long long C(long long a,int c)
{
	if(a<c) return 0ll;
	if(c==1) return a;
	if(c==2)
		return a*(a-1)/2ll;
	return a*(a-1)*(a-2)/6ll;
}

void work()
{
	long long res=0ll;
	long long xx,yy;
	memset(p,0,sizeof(p));
	xx=x0;
	yy=y0;
	p[xx%3][yy%3]++;
	for(int i=1;i<n;++i)
	{
		xx=((long long)A*xx+(long long)B)%M;
		yy=((long long)Cc*yy+(long long)D)%M;
		p[xx%3][yy%3]++;
	}
	res+=C(p[0][0],3);
	res+=C(p[0][0],1)*C(p[0][1],1)*C(p[0][2],1);
	res+=C(p[0][1],3);
	res+=C(p[0][2],3);

	res+=C(p[0][0],1)*C(p[1][1],1)*C(p[2][2],1);
	res+=C(p[0][0],1)*C(p[1][2],1)*C(p[2][1],1);
	res+=C(p[0][1],1)*C(p[1][0],1)*C(p[2][2],1);
	res+=C(p[0][1],1)*C(p[1][2],1)*C(p[2][0],1);
	res+=C(p[0][2],1)*C(p[1][0],1)*C(p[2][1],1);
	res+=C(p[0][2],1)*C(p[1][1],1)*C(p[2][0],1);

	res+=C(p[0][0],1)*C(p[1][0],1)*C(p[2][0],1);
	res+=C(p[0][1],1)*C(p[1][1],1)*C(p[2][1],1);
	res+=C(p[0][2],1)*C(p[1][2],1)*C(p[2][2],1);

	res+=C(p[1][0],3);
	res+=C(p[1][0],1)*C(p[1][1],1)*C(p[1][2],1);
	res+=C(p[1][1],3);
	res+=C(p[1][2],3);

	res+=C(p[2][0],3);
	res+=C(p[2][0],1)*C(p[2][1],1)*C(p[2][2],1);
	res+=C(p[2][1],3);
	res+=C(p[2][2],3);
	cout<<res<<endl;
}

int main()
{
	scanf("%d",&N);
	for(int i=0;i<N;++i)
	{
		printf("Case #%d: ",i+1);
		scanf("%d%d%d%d%d%d%d%d",&n,&A,&B,&Cc,&D,&x0,&y0,&M);
		work();
	}
	return 0;
}
