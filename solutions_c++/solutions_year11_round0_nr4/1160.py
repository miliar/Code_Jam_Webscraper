#include<iostream>
#include<stdio.h>
#include<queue>
using namespace std;


int main()
{
	
	FILE *fp = fopen("D-large.in","r");
	FILE *fpw = fopen("D-large.out","w");
	int T,N;

	fscanf(fp, "%d", &T);
	for(int i = 1; i <= T; i ++)
	{
		fscanf(fp, "%d", &N);
		int temp;
		int ans = 0;
		for(int j = 1; j <= N; j ++)
		{
			fscanf(fp, "%d", &temp);
			if(temp != j)
			{
				ans ++;
			}
		}
		fprintf(fpw, "Case #%d: %d.000000", i, ans);
		cout<<ans<<endl;
	}
	
	return 0;

}

