#include <iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int t = 0; t < T; t++)
	{
		int R,k,N;
		cin>>R>>k>>N;
		int *a = new int[N];
		for(int i = 0; i < N; i++)
		{
			cin>>a[i];
		}

		int *sum = new int[N+1];//sum[0] = 0，sum[n+1]代表从a[0]到a[n]的和，包括两头
		sum[0] = 0;
		for(int i = 0; i < N; i++)
		{
			sum[i+1] = sum[i] + a[i];
		}

		int euro = 0;
		if(sum[N] <= k) //装一船能装下
		{
			cout<<"Case #"<<t+1<<": "<<sum[N]*R<<endl;
		}
		else
		{
			int *end = new int[N]; //end[start]代表从start开始到end[start]，包括头尾的人正好装在一艘船，不能再加。
			for(int start = 0; start < N; start++)
			{
				for(int last = start + 1; last != start; last = (last+1)%N)
				{
					if((last+1)%N > start && sum[(last+1)%N] - sum[start] > k 
					|| (last+1)%N <= start && sum[(last+1)%N] + sum[N] - sum[start] > k)
					{
						end[start] = (last+N-1)%N;
						break;
					}
				}
			}

			int start2 = 0;
			for(int i = 0; i < R; i++)
			{
//				cout<<"start2 = "<<start2<<endl;
				int tmp = sum[(end[start2]+1+N)%N] - sum[(start2+N)%N];
				if(tmp <=0)
				{
					tmp+=sum[N];
				}
				euro += tmp;
				start2 = (end[start2] + 1)%N;
			}
			cout<<"Case #"<<t+1<<": "<<euro<<endl;
			delete[] end;
		}

		delete[] sum;
		delete[] a;
	}
	return 0;
}
