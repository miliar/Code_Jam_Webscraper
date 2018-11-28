#include <stdio.h>
#include <iostream>
using namespace std;
int Data[1000];
int Next[1000];
int Sum[1000];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		int R,K,N;
		scanf("%d %d %d",&R,&K,&N);
		for (int q=0;q<N;++q)
		{
			scanf("%d",Data+q);
			Sum[q]=Data[q];
			Next[q]=(q+1)%N;
		}
		for (int q=0;q<N;++q)
		{
			while (Next[q]!=q && Sum[q]+Data[Next[q]]<=K)
			{
				Sum[q]+=Data[Next[q]];
				Next[q]=(Next[q]+1)%N;
			}
		}
		long long ret = 0;
		int cursor = 0;
		for (int q=0;q<R;++q)
		{
			ret += Sum[cursor];
			cursor = Next[cursor];
		}
		cout << "Case #" << kase << ": " << ret << endl;
	}
	return 0;
}