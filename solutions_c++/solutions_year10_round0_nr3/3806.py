#include<iostream>
using namespace std;
int g[1009];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.in.out","w",stdout);
	int T,R,N,G,k,ca=0,i,j;
	cin>>T;
	while(ca++<T)
	{
		cin>>R>>k>>N;
		for(i=0;i<N;i++)
		{
			cin>>g[i];
		}
		int start = 0;
		int money = 0;
		for(i=0;i<R;i++)
		{
			int cnt=0;
			int timeCnt = 0;
			for(j=start;;j++)
			{
				timeCnt++;
				if(j==N)
					j=0;
				cnt += g[j];
				if(cnt>k)
				{
					cnt -= g[j];
					money += cnt;
					start = j;
					break;
				}
				if(timeCnt>=N)
				{
					start = (j+1)%N;
					money +=cnt;
					break;
				}
			}
		}
		printf("Case #%d: %d\n",ca,money);
	}
}
