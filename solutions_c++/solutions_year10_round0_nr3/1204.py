#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <queue>
using namespace std;
int T;
int R,k,N;
queue<int> queue_w;
int numpeo[2000];
int numFirst[2000];
map<int, int> record;
int main()
{
	freopen("..\\C-large.in","r",stdin);
	freopen("..\\C-large.out","w",stdout);
	scanf("%d",&T);
	for(int t = 1;t <= T;t++)
	{
		scanf("%d %d %d", &R, &k, &N);
		memset(numFirst, 0, sizeof(numFirst));
		while(!queue_w.empty())
			queue_w.pop();
		record.clear();
		for(int i = 1;i <= N;i++)
		{
			scanf("%d" ,&numpeo[i]);
			queue_w.push(i);
		}
		long long res = 0;
		int index = 1;
		while(R--)
		{
			if(record.find(queue_w.front()) == record.end())
			{
				record[queue_w.front()] = index;
				int t_tmp = 0;
				int t_num = 0;
				while(t_num < N && (t_tmp + numpeo[queue_w.front()]) <= k )
				{
					t_num++;
					int t_t = queue_w.front();
					t_tmp += numpeo[t_t];
					queue_w.pop();
					queue_w.push(t_t);
				}
				numFirst[index++] = t_tmp;
				res += (long long)t_tmp;
			}
			else
			{
				R++;
				int start = record[queue_w.front()];
				int end = index;
				int c = R / (end - start);
				long long sum = 0;
				for(int q = start;q <= end;q++)
					sum += (long long)numFirst[q];
				res += (long long)sum * (long long)c;
				R -= c * (end - start);
				for(int q = 0;q < R;q++)
					res += (long long)numFirst[q + start];
				break;
			}
		}
		if(res < 0)
		{
			int x = 3;
			x++;
		}
		printf("Case #%d: %lld\n", t, res);
	}
	return 0;
}