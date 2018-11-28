#include<stdio.h>
#include<string.h>
char tar[20]="welcome to code jam";
int cnt[512][20], mod =10000;
int main()
{
	int n;
	char str[512];
	int i,j,m=0;
	FILE *fin, *fout;
	fin= fopen("C:\\c.txt", "rb");
	fout = fopen("C:\\cout.txt","wb");
	fscanf(fin, "%d", &n);
	fgetc(fin);
	while(++m<=n){
		memset(cnt, 0,sizeof(cnt));
		fgets(str, 512, fin);

		if(str[0]== tar[0]) cnt[0][0] =1;

		for( i=1; str[i]!='\0'; i++ )
			if(str[i] == tar[0]) cnt[i][0]= cnt[i-1][0]+1;
			else cnt[i][0]= cnt[i-1][0];

		for( i=1; str[i]!='\0' ;i++)
			for( j=1; j<=i && j<=18; j++)								
				if(str[i] == tar[j]) cnt[i][j]=(cnt[i-1][j]+cnt[i-1][j-1])% mod;
				else cnt[i][j] = cnt[i-1][j] % mod;
	/*	for( i=0; str[i]!='\0'; i++)
		{
			for(j=0; j<=18; j++)
				fprintf(fout, "%d", cnt[i][j]);
				fprintf(fout,"\n");
		}*/
		fprintf(fout, "Case #%d: %04d\n", m, cnt[i-1][18]);
	}
	fclose(fin);
	fclose(fout);
	return 0;

}