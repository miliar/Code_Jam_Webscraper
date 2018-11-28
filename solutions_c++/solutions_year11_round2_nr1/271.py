#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

char s[110][110];
int win[110];
int ile[110];
double wp[110], owp[110], oowp[110];
double wout[110][110];

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int icas=1; icas<=cases; ++icas)
	{
		int n;
		scanf("%d", &n);
		for(int i=0; i<n; ++i)
		{
			scanf("%s", s[i]);
		}
		printf("Case #%d:\n", icas);
		for(int i=0; i<n; ++i)
		{
			win[i] = ile[i] = 0;
			for(int j=0; j<n; ++j)
			{
				if(s[i][j] == '.') continue;
				ile[i]++;
				if(s[i][j] == '1') win[i]++;
			}
			wp[i] = (double)win[i] / ile[i];
			//printf("%lf\n", wp[i]);
		}
		
		for(int i=0; i<n; ++i)
		{
			for(int j=0; j<n; ++j)
			{
				int il = ile[i] - 1;
				int w = win[i];
				if(s[i][j] == '1') w--;
				wout[i][j] = (double)w / il;
			}
		}
		//for(int i=0; i<n; ++i){for(int j=0; j<n; ++j) printf("%.2lf ", wout[i][j]); printf("\n");}
		
		for(int i=0; i<n; ++i)
		{
			owp[i] = 0.0;
			int il = ile[i];
			for(int j=0; j<n; ++j)
			{
				if(s[i][j] == '.') continue;
				owp[i] += wout[j][i];
			}
			owp[i] /= il;
			//printf("owp: %lf\n", owp[i]);
		}
		
		for(int i=0; i<n; ++i)
		{
			oowp[i] = 0.0;
			for(int j=0; j<n; ++j)
			{
				if(s[i][j] == '.') continue;
				oowp[i] += owp[j];
			}
			oowp[i] /= ile[i];
		}
		
		for(int i=0; i<n; ++i)
		{
			printf("%.12lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}
