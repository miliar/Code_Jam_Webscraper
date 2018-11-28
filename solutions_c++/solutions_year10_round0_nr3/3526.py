#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{
	freopen("C-small-attempt3.in","r",stdin);
	freopen("out.txt","w",stdout);

	int R,K,N;
	int T,t=1;

	cin>>T;
	while(T--)
	{
		cin>>R>>K>>N;
		int group[1000];
		int sum=0;
		
		for(int i=0;i<N;i++)
		{
			scanf("%d",&group[i]);
			sum += group[i];
		}

		int T=0;
		long long T_money=0;
		long long sum_money =0;
		if(sum<=K)
		{
			sum_money = sum*R;
			printf("Case #%d: %d\n",t++,sum_money);
			continue;
		}

		bool flag[1000];
		int index;
		memset(flag,0,sizeof(flag));
		int i=0;
		flag[i] = true;
		while(1)
		{
			int money =0;
			while(money+group[i%N]<=K)  //一次运输
			{
				money += group[i%N];
				i++;
			}
			T++;
			T_money += money;
			if(flag[i%N])
			{
				index = i%N;
				int time = 0;
			    int j=0;
			    while(j<index)
			    {
				    int money =0;
			        while(money+group[j%N]<=K)  //一次运输
			        {
				        money += group[j%N];
				    j++;
			        }
				    time++;
					T_money -= money;
			    }
				T = T-time;

				break;
			}
			else
				flag[i%N] = true;

		}

		//cout<<"T="<<T<<endl;
		//cout<<"index="<<index<<endl;
		//cout<<"T_money="<<T_money<<endl;
		
	    int TT = R%T;
		i = 0;
		while(TT--)
		{
			int money =0;
			while(money+group[i%N]<=K)  //一次运输
			{
				money += group[i%N];
				i++;
			}
		    sum_money += money;
		}
		sum_money += R/T*T_money;

		printf("Case #%d: %d\n",t++,sum_money);
		
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}