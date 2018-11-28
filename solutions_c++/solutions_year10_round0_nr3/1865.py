#include <cstdio>

int a[1024];

int main()
{
	int tn,ti=0;
	FILE *in=fopen("C-large.in","r");
	FILE *out=fopen("output.txt","w");
	fscanf(in,"%d",&tn);
	while(tn--)
	{
		int R,K,N;
		fscanf(in,"%d %d %d",&R,&K,&N);
		for(int i = 0; i < N; ++i)
			fscanf(in,"%d",&a[i]);
		int t=0;
		long long int ans = 0;
		long long int tmp = 0;
		for(int j =0; j < R; ++j)
		{
			long long int r = 0;
			for(int i = 0; i < N; ++i)
			{
				int t2 = (t + i) % N;
				if (r + a[t2] > K) {t = t2; break;}
				else r += (long long int)a[t2];
			}
			tmp += r;
			t %= N;
			if(t == 0) 
			{
				ans += tmp * (R / (j+1));
				j = (R / (j+1)) * (j+1) - 1;
				tmp = 0;
			}
		}
		ans += tmp;
		fprintf(out,"Case #%d: %I64d\n",++ti,ans);
	}
}
/*
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3
*/