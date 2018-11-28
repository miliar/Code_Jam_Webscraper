#include <stdio.h>
#include <algorithm>
using namespace std;
int getmin(char *t)
{
	int h1=*t-'0';
	int h2=*(t+1)-'0';
	int m1=*(t+3)-'0';
	int m2=*(t+4)-'0';
	return h1*600+h2*60+m1*10+m2;
}
int main()
{
	int T;
	scanf("%d",&T);
	int t,N,M[2];
	int S[2][100];
	int A[2][100];
	int R[2][100];
	int Check[2][100];
	int Index[2][100];
	int q,w,e,Tow;
	char t1[6],t2[6];
	for (t=1;t<=T;t++)
	{
		scanf("%d",&Tow);
		scanf("%d %d",M,M+1);
		for (w=0;w<=1;w++) for (q=0;q<M[w];q++)
		{
			scanf("%s %s",t1,t2);
			S[w][q]=getmin(t1);A[w][q]=getmin(t2);R[w][q]=A[w][q]+Tow;
			Index[w][q]=q;Check[w][q]=0;
		}	
		int ret[2];
		ret[0]=M[0];
		ret[1]=M[1];
		for (w=0;w<=1;w++) for (q=0;q<M[w];q++)
		{
			int par=-1;
			for (e=0;e<M[!w];e++)
				if (S[!w][e]>=R[w][q] && Check[!w][e]==false)
					if (par<0 || S[!w][e] < S[!w][par])
						par=e;
			if (par>=0)
			{
				ret[!w]--;
				Check[!w][par]=true;
			}
		}
		printf("Case #%d: %d %d\n",t,ret[0],ret[1]);
	}
	return 0;
}
