#include <cstdio>
#include <cstring>

using namespace std;

int a[10000][2];
int b[10000];

int main()
{
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("output.txt", "w");

	//in = stdin;
	//out = stdout;
	int tn, ti = 0;
	fscanf(in, "%d", &tn);
	while(tn--)
	{
		int n, m;
		fscanf(in, "%d", &n);
		for(int i = 0; i < n; ++i)
			fscanf(in, "%d %d",&a[i][0],&a[i][1]);
		fscanf(in, "%d",&m);
		memset(b,0,sizeof(b));
		b[0] = (a[0][0] < a[0][1]) ? a[0][0] : a[0][1];
		bool ans = false;
		for(int i = 0; i < n; ++i)
		{
			if(b[i] == 0) break;
			if(a[i][0] + b[i] >= m) {ans=true; break;}
			for(int j = i+1;j<n;++j)
			{
				if(b[i] >= a[j][0] - a[i][0])
				{
					int t = (a[j][0]-a[i][0] <= a[j][1]) ? a[j][0]-a[i][0] : a[j][1];
					if(b[j] < t) b[j] = t;
				}
				else break;
			}
		}
		if(ans) fprintf(out, "Case #%d: YES\n", ++ti);
		else fprintf(out, "Case #%d: NO\n", ++ti);
	}
}

/*
4
3
3 4
4 10
6 10
9
3
3 4
4 10
7 10
9
2
6 6
10 3
13
2
6 6
10 3
14
*/