#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <complex>

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef long long LL;
typedef complex<double> Point;

template<typename T> inline int size(const T &a) { return a.size(); }
template<typename T> inline bool operator<(const int &a,const vector<T> &b) { return a<b.size(); }

int D,I,M,N;
VI dyna,nex;

bool process(void)
{
	scanf("%d %d %d %d",&D,&I,&M,&N);

	dyna.resize(257,9999);
	dyna[256] = 0;
	for(int i=0;i<N;i++)
	{
		int num;		
		scanf("%d", &num);

		nex = VI(257,0);
		nex[256] = dyna[256] + D;

		for(int j=0;j<256;j++)
		{
			nex[j] = dyna[256] + D + I;
			nex[j] = min(nex[j], dyna[j] + D);
		}

		for(int j=0;j<256;j++)
		{
			int basecost = abs(j - num);
			nex[j] = min(nex[j], dyna[256] + basecost);

			for(int k=0;k<256;k++)
			{
				int diff = abs(j-k) - 1;
				if(M > 0)
				{
					if(diff < 0) diff=0;
					nex[j] = min(nex[j], basecost + dyna[k] + I * (diff / M));
				}
				else
				{
					if(j == k)
					{
						nex[j] = min(nex[j], basecost + dyna[k]);
					}
				}
			}
		}

		dyna.swap(nex);
	}

	int ret = dyna[0];
	for(int i=0;i<257;i++)
	{
		if(ret > dyna[i]) ret = dyna[i];
	}

	cout << ret << endl;

	return true;
}

int main(void)
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		process();
	}
	return 0;
}

