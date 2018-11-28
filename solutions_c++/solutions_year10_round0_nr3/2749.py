#include <iostream>
#include <queue>
using namespace std;

void clearQueue(queue<int>& g)
{
	while (!(g.empty()))
	{
		g.pop();
	}
}

int main()
{
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);
	int times; //һ�����ٴ�
	int k; //һ��������������
	int R; //һ�쿪��������
	int N; //һ���ж�����
	int temp; 
	int sum;
	queue<int> g;
	cin>>times;

	for (int i=1;i<=times;i++)
	{
		clearQueue(g);
		sum=0;
		cin>>R>>k>>N;

		for (int j=0;j<N;j++)
		{
			cin>>temp;
			g.push(temp);
		}

		for (int j=0;j<R;j++)
		{
			temp=0;
			for (int m=0;m<N;m++)
			{
				if ((temp+g.front())<=k)
				{
					temp+=g.front();
					g.push(g.front());
					g.pop();
				}
				else break;
			}
			sum+=temp;
		}

		cout<<"Case #"<<i<<": "<<sum<<endl;
	}

	return 0;
}