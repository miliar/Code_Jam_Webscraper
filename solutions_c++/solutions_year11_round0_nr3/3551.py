#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <map>

using namespace std;

int nbVal;
int bonbons[1000];
map<int, int> dyn[2][1000];
const int INF = 1<<30;

int dynMaxVal(int pos, int ex, char toutPris)
{
	if(pos == nbVal)return (ex != 0 || toutPris)*-INF;
	if(dyn[toutPris][pos].find(ex) != dyn[toutPris][pos].end())return dyn[toutPris][pos][ex];
	dyn[toutPris][pos][ex]=max(dynMaxVal(pos+1, ex, 0), dynMaxVal(pos+1, ex^bonbons[pos], toutPris)+bonbons[pos]);
	return dyn[toutPris][pos][ex];
}

int main()
{
	int nbTest;
	scanf("%d", &nbTest);
	for(int i = 0; i < nbTest; i++)
	{
		scanf("%d", &nbVal);
		int mini=INF;
		int s = 0;
		
		for(int j = 0; j < nbVal; j++)
		{
			scanf("%d", &bonbons[j]);
			s+=bonbons[j];
			mini = min(bonbons[j], mini);
		}
		printf("Case #%d: ", i+1);
		
		for(int j = 0; j < 20; j++)
		{
			int count = 0;
			for(int k = 0; k < nbVal; k++)
			{
				count += (bonbons[k] & 1);
				bonbons[k]/=2;
			}
			if(count & 1) { printf("NO\n"); goto end; }
		}
		
		printf("%d\n", s-mini);
		end:;
	}

	return 0;
}

