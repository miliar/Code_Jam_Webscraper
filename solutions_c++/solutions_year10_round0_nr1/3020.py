#include <stdio.h>
#include <math.h>
#include <string.h>

int m;
int N;
int K;

int main()
{

	char filename[32];
	char infile[32], outfile[32];
	//scanf("%s", filename);
	sprintf(filename,"%s", "A-large");

	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j;
	int cnt;
	fscanf(fp, "%d", &m);
	for(i=1;i<=m;i++) {
		fscanf(fp, "%d %d", &N, &K);
		if ( (K+1)%((int)pow((double)2,N)) == 0) //ON
		//if ( K > ((int)pow((double)2,N)-1) ) //ON
			fprintf(ofp, "Case #%d: %s\n", i, "ON");
		else
			fprintf(ofp, "Case #%d: %s\n", i, "OFF");
	}

	return 0;
	/*
	for(tc=1;tc<=m;tc++)
	{
		fscanf(fp, "%s", &a[1]);
		memset(pos, false, sizeof(pos));
		cnt=0;
		for(i=1;a[i];i++)
		{
			cnt++;
			if(a[i]=='(')
			{
				for(j=i+1;a[j]!=')';j++) pos[cnt][a[j]-'a'+1]=true;
				i=j;
			}
			else pos[cnt][a[i]-'a'+1]=true;
		}
		ans=0;
	for(i=1;i<=m;i++)
		{
			for(j=1;j<=r;j++)
			{
				if(!pos[j][dat[i][j]-'a'+1]) break;
			}
			if(j>r) ans++;
		}*/

}
