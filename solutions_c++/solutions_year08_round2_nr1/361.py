#include<iostream>
using namespace std;
struct Point
{
	long long x , y ;
	Point(){}
	Point(long long x, long long y){}
}point[100001];
int main()
{
	long long n ,N , A , B , C , D , M ;
	long long x0,y0 ;
	long long cases = 0 ;
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	while(1 ==scanf("%lld",&N))
	{
		for(cases=1;cases<=N;cases++)
		{
			scanf("%lld",&n);
			scanf("%lld%lld%lld%lld%lld%lld%lld",&A,&B,&C,&D,&x0,&y0,&M);
			long long i , j , k ,t;
			point[0].x = x0;point[0].y =y0;
			long long temp_x =x0, temp_y=y0;
			for(i=1;i<n;i++)
			{
				temp_x =( A*temp_x +B )%M ;
				temp_y =( C*temp_y +D )%M ;
				point[i].x = temp_x ;
				point[i].y = temp_y ;
			}
			long long ans = 0 ;
			for(i=0;i<n;i++)
			{
				for(j=i+1;j<n;j++)
				{
					for(k=j+1;k<n;k++)
					{
						if((point[i].x+point[j].x+point[k].x)%3==0&&
							(point[i].y+point[j].y+point[k].y)%3==0)
							ans ++;
					}
				}
			}
			cout<<"Case #"<<cases<<": "<<ans<<endl;
		}
	}
	return 0 ;
}