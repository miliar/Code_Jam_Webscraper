#include <cstdio>
#include <cstdlib>
#include <cstring>

const char hint1[]="zeyejp q mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
const char ans1[] ="qoaour z language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
char map[26]="";

int main(int argc, char** argv)
{
	bool openans[26];
	int iclosedans=-1;

	int len=strlen(hint1);
	for(int i=0;i<len;i++)
	{
		if(hint1[i]!=' ')
		{
			map[hint1[i]-'a']=ans1[i];
			openans[ans1[i]-'a']=true;
		}
	}

	char buf[1024];
	FILE *fin, *fout;
	fopen_s(&fin,"C:/input.in","r");
	fopen_s(&fout,"C:/output.txt","r+");

	int T;
	fgets(buf,1024,fin);
	sscanf(buf,"%d",&T);

	for(int i=1;i<=T;i++)
	{
		fgets(buf,1024,fin);
		int buflen=strlen(buf);
		for(int l=0;l<buflen;l++)
		{
			if(buf[l]==' ')
				continue;
			char newchar=map[buf[l]-'a'];
			buf[l]=newchar;
		}
		char out[1024]="\n";
		char tmp[1024];
		sprintf_s(tmp,256,"Case #%d: %s",i, buf);
		if(i==1)
			out[0]=0;
		strcat(out,tmp);
		fputs(out,fout);
	}

	fclose(fin);
	fclose(fout);
	system("PAUSE");
}