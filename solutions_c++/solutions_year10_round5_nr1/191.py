#include <stdio.h>

int IsPrime[1000005];

int main()
{
	for (int q=2;q<=1000000;++q)
		IsPrime[q] = 1;
	for (long long q=2;q<=1000000;++q)
		if (IsPrime[q])
			for (long long w=q*q;w<=1000000;w+=q)
				IsPrime[w] = 0;
	int T;
	scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		fprintf(stderr,"%d\n",kase);
		int D,N;
		int Seq[10];
		scanf("%d %d",&D,&N);
		for (int q=0;q<N;++q) scanf("%d",&Seq[q]);
		int maxP = 1;
		int candi = -1;
		int mul = 0;
		int maxV = Seq[0];
		for (int q=1;q<N;++q)
			if (Seq[q]>maxV)
				maxV = Seq[q];
		for (int q=0;q<D;++q) maxP *= 10;
		for (int q=0;q<maxP;++q)
		{
			if (IsPrime[q] && q > maxV)
			{
				if (N>1 && !mul) for (int a=0;a<q;++a)
				{
					int tb = Seq[1] - (Seq[0] * a) % q;
					int b = (tb+q)%q;
					//°ËÁõ.
					int good = 1;
					for (int w=0;w+1<N;++w)
						if ( ( Seq[w] * a + b ) % q != Seq[w+1])
						{
							good = 0;
							break;
						}
					if (good)
					{
						int rec = (Seq[N-1] * a + b)  % q;
						if (candi<0)
							candi = rec;
						else if (candi != rec)
						{
							mul = 1;
							break;
						}
					}
				}
			}
		}
		if (mul || candi<0) printf("Case #%d: I don't know.\n",kase);
		else printf("Case #%d: %d\n",kase,candi);
	}
	return 0;
}
