#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
char STR[50005];
int K;
int Cost[16][16];
int Link[16][16];
int D[16][16][65536];
int main()
{
	int t,T,q,w,e,r;
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		scanf("%d",&K);
		scanf("%s",&STR);
		for (q=0;q<K;q++) for (w=0;w<K;w++) Cost[q][w]=Link[q][w]=0;
		int N;for (N=0;STR[N];N++);
		for (q=0;q<N;q+=K)
		{
			for (w=0;w<K;w++) for (e=0;e<K;e++) Cost[w][e]+=int(STR[q+w]!=STR[q+e]);
			if (q+K<N) for (w=0;w<K;w++) for (e=0;e<K;e++) Link[w][e]+=int(STR[q+w]!=STR[q+e+K]);
		}
		int s,full=(1<<K);
		for (q=0;q<K;q++) for (w=0;w<K;w++) for (e=0;e<full;e++) D[q][w][e]=-1;
		for (s=0;s<K;s++) 
		{
			D[s][s][1<<s]=1; //intro cost
			for (w=0;w<full;w++) for (e=0;e<K;e++)
				if (D[s][e][w]>=0)
				{
					for (r=0;r<K;r++)
					{
						if ( (w>>r)&1 ) continue;
						int c=D[s][e][w]+Cost[e][r]; //to D[s][r][w|(1<<r)]
						int &ref=D[s][r][w|(1<<r)];
						if (ref<0 || c<ref) ref=c;
					}
				}			
		}
		int ret=-1;
		for (q=0;q<K;q++) for (w=0;w<K;w++)
			if (D[q][w][full-1]>=0)
				if (ret<0 || D[q][w][full-1]+Link[w][q]<ret)
					ret=D[q][w][full-1]+Link[w][q];
		printf("Case #%d: %d\n",t,ret);
	}
	return 0;
}
