#include <cstdio>
#include <vector>
#include <algorithm>


using namespace std;

vector<pair<long long,long long> > vec;

void init()
{
	vec.clear();
	long long n, A, B, C, D, x0, y0, M;
	scanf("%lld", &n);
	scanf("%lld%lld%lld%lld", &A, &B, &C, &D);
	scanf("%lld%lld", &x0, &y0);
	scanf("%lld", &M);
	long long X = x0;
	long long Y = y0;
	vec.push_back(make_pair(X,Y));
	for (int i = 1; i<=n-1; i++)
	{
		X = (A * X + B) % M;
		Y = (C * Y + D) % M;
		vec.push_back(make_pair(X,Y));
	}
}

long long mas[3][3] = {0};
int index[3][3] = {{0,0,0},{0,1,2},{1,1,1}};

long long calc(int i1, int i2)
{
	if (i1 != 1 && i2 != 1)
	{
		int k1 = index[i1][0];
		int k2 = index[i2][0];
		if (mas[k1][k2] < 2)
			return 0;
		long long res = mas[k1][k2]*(mas[k1][k2]-1)*(mas[k1][k2]-2);
		return res;
	}
	vector<int> v1;
	for (int i=0; i<3; i++)
		v1.push_back(index[i1][i]);
	long long res = 0;
	do
	{
		vector<int> v2;
		for (int i=0; i<3; i++)
			v2.push_back(index[i2][i]);
		do
		{
			long long locres = 1;
			for (int i=0; i<3; i++)
			{
				locres *= mas[v1[i]][v2[i]];
			}
			res += locres;
		}while(next_permutation(v2.begin(), v2.end()));
	}while(next_permutation(v1.begin(), v1.end()));
	if (i1==1 && i2 == 1)
		res /= 6;
	return res;
}


int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int tt=1; tt<=T; tt++)
	{
		init();
		long long res = 0;
		for (int i=0; i<vec.size(); i++)
		{
			for (int j=i+1; j<vec.size(); j++)
			{
				for (int k=j+1; k<vec.size(); k++)
				{
					if (((vec[i].first+vec[j].first+vec[k].first)%3) == 0)
					{
						if (((vec[i].second+vec[j].second+vec[k].second)%3) == 0)
						{
							res++;
						}
					}
				}
			}
		}
		/*
		memset(mas,0,sizeof(mas));
		for (int i=0; i<vec.size(); i++)
		{
			mas[vec[i].first%3][vec[i].second%3]++;
		}
		for (int i=0; i<3; i++)
		{
			for (int j=0; j<3; j++)
			{
				res += calc(i,j);
			}
		}
		*/
		printf("Case #%d: %lld\n", tt, res);
	}
	return 0;
}