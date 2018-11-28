#include <cstdio>

int a[10000];
int b[10000];
int c[10000];

int main()
{
	int tn, ti = 0;
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("output.txt", "w");
	fscanf(in,"%d",&tn);
	while(tn--)
	{
		int n, n1 = 0, n2 = 0;
		fscanf(in,"%d",&n);
		for(int i=0;i<n;i++)
		{
			char ch;
			int k;
			fscanf(in," %c %d", &ch, &k);
			if(ch == 'B') a[n1++] = k, c[i] = 0;
			else b[n2++] = k, c[i] = 1;
		}
		int ans = 0;
		int x = 1, y = 1;
		int t = 0, t1 = 0, t2 = 0;
		while(t < n)
		{
			int r = 0;
			ans++;
			if(c[t] == 0 && a[t1] == x) r = 1, t1++, t++;
			else if(c[t] == 1 && b[t2] == y) r = 2, t2++, t++;

			if(r != 1 && t1 < n1)
			{
				if(a[t1] < x) x--;
				else if(a[t1] > x) x++;
			}

			
			if(r != 2 && t2 < n2)
			{
				if(b[t2] < y) y--;
				else if(b[t2] > y) y++;
			}
		}
		fprintf(out, "Case #%d: %d\n", ++ti, ans);
	}
}