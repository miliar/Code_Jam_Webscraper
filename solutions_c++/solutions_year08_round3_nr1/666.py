#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;

bool cmp(int i, int j)
{
	return i > j;
}

int main()
{
	fstream f;
	f.open("out.out");
	int t;
	scanf("%d", &t);
	for(int cc = 1; cc <= t; cc++)
	{
		int P, K, L;
		scanf("%d%d%d", &P, &K, &L);
		printf("Case #%d: ", cc);
		f << "Case #" << cc <<": ";
		vector<int> v;
		for(int i = 0; i < L; i++)
		{
			int tmp;
			scanf("%d", &tmp);
			v.push_back(tmp);
		}
		sort(v.begin(), v.end(), cmp);
		int len = v.size();
		int w = 1, sum = 0;
		for(int i = 0; i < len; i++)
		{
			sum += v[i]*w;
			if((i+1)%K == 0)
			{
				w++;
			}
		}
		printf("%d\n", sum);
		f << sum << endl;
	}
	f.close();
	return 0; 
}