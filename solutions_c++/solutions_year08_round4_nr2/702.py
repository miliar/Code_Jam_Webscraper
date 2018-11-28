#include <iostream>
#include <cmath>
using namespace std;

int N,M,A;

long long llabs(long long a)
{
	if(a<0) return -a;
	return a;
}

void work()
{
	long long y2,A2;
	long long ox1,ox2,ox3,oy1,oy2,oy3;
	A2=A;
	if(A2>N*M)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	for(long long x1=0;x1<=N;++x1)
		for(long long x2=0;x2<=N;++x2)
			for(long long y1=0;y1<=M;++y1)
				for(long long y2=0;y2<=M;++y2)
			{
				/*y2=A+x2*y1;
				if(y2!=0&&x1==0) continue;
				if(y2%x1!=0) continue;
				y2=y2/x1;
				if(llabs(y2-y1)>M) continue;*/
				if(llabs(x1*y2-x2*y1)!=A2) continue;
				ox1=oy1=0;
				ox2=x1;
				oy2=y1;
				ox3=x2;
				oy3=y2;
				/*if(x2<0)
				{
					ox1+=x2;
					ox2+=x2;
					ox3+=x2;
				}
				if(y2<0)
				{
					oy1+=y2;
					oy2+=y2;
					oy3+=y2;
				}*/
				cout<<ox1<<' '<<oy1<<' '<<ox2<<' '<<oy2<<' '<<ox3<<' '<<oy3<<endl;
				return;
			}
}

int main()
{
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;++i)
	{
		scanf("%d%d%d",&N,&M,&A);
		printf("Case #%d: ",i+1);
		work();
	}

	return 0;
}
