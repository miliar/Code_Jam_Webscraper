#include <stdio.h>
int on[30];
int main()
{
	int T,n,k;
	scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		scanf("%d %d",&n,&k);
		//initially all off..
		for (int q=0;q<n;++q) on[q]=0;
		for (int ref=1;;++ref)
		{
			for (int q=0;q<n;++q)
			{
				on[q] ^= 1;
				if (on[q]) break;
			}
			int bad=0;
			for (int q=0;q<n;++q)
				if (!on[q])
					bad=1;
			if (!bad)
			{
				printf("Case #%d: %s\n",kase,(const char*)( k%(ref+1) == ref )?"ON":"OFF");
				break;
			}
		}
	}
	return 0;
}