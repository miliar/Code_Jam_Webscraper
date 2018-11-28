#include <iostream>
#include <queue>
#include <fstream>
using namespace std;

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	long long euro;
	queue<long long> q;
	long T, R, k, N;
	long i, j, tmp;
	cin>>T;
	for (i = 1; i <= T; i++)
		{
		euro = 0;
		//q.clear();
		while (!q.empty())
			{
			q.pop();
			}
		//scanf("%d%d%d", &R, &k, &N);
		cin>>R>>k>>N;
		for (j = 0; j < N; j++)
			{
			//scanf("%d", &tmp);
			cin>>tmp;
			q.push(tmp);
			}
		while (R--)
			{
			tmp = 0;
			j = 0;
			while (true)
				{
				if (tmp + q.front() > k || j >= N)
					{
					break;
					}
				else
					{
					tmp += q.front();
					q.push(q.front());
					q.pop();
					j++;
					}
				}
			euro += tmp;
			}
		//printf("Case #%lld: %lld\n", i, euro);
		cout<<"Case #"<<i<<": "<<euro<<endl;
		}
	system("pause");
	return 0;
}
