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

		int *sum = new int[N+1];//sum[0] = 0��sum[n+1]�����a[0]��a[n]�ĺͣ�������ͷ
		sum[0] = 0;
		for(int i = 0; i < N; i++)
		{
			sum[i+1] = sum[i] + a[i];
		}

		int euro = 0;
		if(sum[N] <= k) //װһ����װ��
		{
			cout<<"Case #"<<t+1<<": "<<sum[N]*R<<endl;
		}
		else
		{
			int *end = new int[N]; //end[start]�����start��ʼ��end[start]������ͷβ��������װ��һ�Ҵ��������ټӡ�
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
