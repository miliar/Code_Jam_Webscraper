#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int INF = numeric_limits<int>::max();

const int nmax = 105, wmax = 15;
char d[nmax][wmax];
char l[30];
bool p[nmax];

int n, m;

int sim(char* w)
{
	int c[30];
	memset(c, 0, sizeof(c));
	memset(p, false, sizeof(p));
	int wl = strlen(w);
	for(int i=0;i<n;i++)
		if(strlen(d[i]) == wl)
		{
			p[i] = true;
			for(int j=0;d[i][j];j++)
				c[d[i][j]-'a']++;
		}
	
	int score=0;
	char b[wmax];
	memset(b, 0, sizeof(b));
	int lc = 0;
	for(int i=0;lc < wl;i++)
	{
		assert(i < 26);
		if(c[l[i]-'a']==0)
			continue;
		//for(int j=0;j<n;j++)			if(p[j])				printf("%s ", d[j]);		printf("\n");
		//printf("%c %d\n", l[i], c[l[i]-'a']);
		if(strchr(w, l[i])==NULL)
		{
			score++;
			for(int j=0;j<n;j++)
				if(p[j])
					for(int k=0;k<wl;k++)
						if(d[j][k] == l[i])
						{
							p[j]=false;
							for(int h=0;h<wl;h++)
								c[d[j][h]-'a']--;
							break;
						}
			continue;
		}
		
		for(int k=0;k<wl;k++)
			if(w[k]==l[i])
			{
				lc++;
				for(int j=0;j<n;j++)
					if(p[j])
						if(l[i] != d[j][k])
						{
							p[j] = false;
							for(int h=0;h<wl;h++)
								c[d[j][h]-'a']--;
						}
			}
			else
			{
				for(int j=0;j<n;j++)
					if(p[j])
						if(l[i] == d[j][k])
						{
							p[j] = false;
							for(int h=0;h<wl;h++)
								c[d[j][h]-'a']--;
						}
			}
	}
	return score;
}		

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
		scanf("%d%d", &n, &m);
		for(int i=0;i<n;i++)
			scanf("%s", d+i);
		printf("Case #%d:",test_case);
		for(int i=0;i<m;i++)
		{
			scanf("%s", l);
			int pmax = 0, wbest = 0;
			for(int j=0;j<n;j++)
			{
				//printf("\n");
				int p = sim(d[j]);
				//printf("%s %d\n", d[j], p);
				if(p > pmax)
				{
					pmax = p;
					wbest = j;
				}
			}
			printf(" %s", d[wbest]);
		}
		printf("\n");
    }
    return 0;
}
