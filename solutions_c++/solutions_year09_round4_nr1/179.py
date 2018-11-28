#include <stdio.h>
#include <algorithm>
using namespace std;
int N;
int Val[50];
int Goal[50];
int Cnt[50];
int main()
{
		int T;
		scanf("%d",&T);
		for (int kase=1;kase<=T;++kase)
		{
				scanf("%d",&N);
				for (int q=0;q<N;++q) Cnt[q]=0;
				for (int q=0;q<N;++q)
				{
						char tmp[50];
						scanf("%s",tmp);
						for (int w=N-1;w>=0;w--)
								if (w==0 || tmp[w]=='1')
								{
										Val[q]=w;
										Cnt[w]++;
										break;
								}
				}
				int ret=0;
				for (int q=0;q<N;++q)		
				{
						for (int w=q;w<N;++w)
								if (Val[w]<=q)
								{
										for (int e=w;e-1>=q;--e) 
										{
												swap(Val[e],Val[e-1]);
												ret++;
										}
										break;
								}
				}
				printf("Case #%d: %d\n",kase,ret);
		}
		return 0;
}
