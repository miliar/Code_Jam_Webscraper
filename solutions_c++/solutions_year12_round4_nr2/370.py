#include <cstdio>
#include <algorithm>

using namespace std;

struct ele
{
	int x;
	int n;
	bool operator < (const ele a) const
	{
		return x < a.x;
	}
} a[1024];

int b[1024][2];

int main()
{
	FILE *in = fopen("B-large.in", "r");
	FILE *out = fopen("output.txt", "w");

	//in = stdin;
	//out = stdout;

	int tn, ti = 0;
	fscanf(in, "%d", &tn);
	while(tn--)
	{
		int n, W, L;
		fscanf(in, "%d %d %d", &n, &W, &L);
		for(int i =0; i< n;++i) {
			int t;
			fscanf(in, "%d", &t);
			a[i].x = t;
			a[i].n = i;
		}
		sort(a,a+n);
		reverse(a,a+n);
		int w = 0;
		int l = -a[0].x;
		for(int k = 0; k < n;)
		{
			int i = k;
			b[a[i].n][0] = 0;
			b[a[i].n][1] = l + a[i].x;
			if(b[a[i].n][1] > L) printf("!!!!!!!!!\n");
			l += 2 * a[i].x;
			for(i = k+1;i<n;++i)
			{
				if(b[a[i-1].n][0] + a[i-1].x + a[i].x > W) break;
				b[a[i].n][0] = b[a[i-1].n][0] + a[i-1].x + a[i].x;
				b[a[i].n][1] = b[a[i-1].n][1];
			}
			k = i;
		}
		fprintf(out, "Case #%d:", ++ti);
		for(int i = 0; i<n;++i)
			fprintf(out, " %d %d", b[i][0], b[i][1]);
		fprintf(out, "\n");
	}
}

/*
2
2 6 6
1 1
3 320 2
4 3 2
*/