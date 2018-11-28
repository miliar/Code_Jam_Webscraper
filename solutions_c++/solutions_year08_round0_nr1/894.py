#include <string.h>
#include <math.h>
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;


void Kevinew(){
#ifndef  ONLINE_JUDGE
	freopen("C:\\TDdownload\\A-large.in","r",stdin);
	freopen("C:\\TDdownload\\A-large.out","w",stdout);
#endif
}





int main(){
	int  i,j,icase,flag[110],nflag;
	int ncase,nS,nQ,ans;
	char S[110][110],temp[110];

	Kevinew();
	scanf("%d\n",&ncase);
	for(icase=0;icase<ncase;icase++) {
		memset(flag,0,sizeof(flag));
		nflag = 0;
		ans = 0;
		scanf("%d\n",&nS);
		for (i=0;i<nS;i++)
		{
			gets(S[i]);
			//puts(S[i]);
		}
		scanf("%d\n",&nQ);
		while (nQ--)
		{
			gets(temp);
			for (i=0;i<nS;i++)
			{
				if (strcmp(temp,S[i]) == 0) 
				{
					if (!flag[i])
					{
						flag[i] = 1;
						nflag++;
						if (nflag == nS)
						{
							ans++;
							memset(flag,0,sizeof(flag));
							flag[i]=1;
							nflag=1;
						}
					}
				}
			}

		}
		printf("Case #%d: %d\n",icase+1,ans);

	}

	return 0;

}


