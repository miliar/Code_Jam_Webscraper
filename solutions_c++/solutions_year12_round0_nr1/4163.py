#include<cstdio>
#include<cstring>
FILE *fin,*fout;
char table[]="yhesocvxduiglbkrztnwjpfmaq";
char src[200],ans[200];
int main()
{
	int n;
	fin=fopen("a.in","r");
	fout=fopen("a.out","w");
	fscanf(fin,"%d\n",&n);
	for (int cnt=1;cnt<=n;++cnt)
	{
		memset(ans,0,sizeof(ans));
		int p=0;
		char c;
		while (1)
		{
			fscanf(fin,"%c",&c);
			if (c=='\n') break;
			if (c==' ') ans[p++]=' ';
			else ans[p++]=table[c-'a'];
		}
		fprintf(fout,"Case #%d: %s\n",cnt,ans);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}

