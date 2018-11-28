#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

void Swap(char* a, char* b)
{
	char buf=*b;
	*b=*a;
	*a=buf;
}

bool isRecycled(int n, int m)
{
	char ns[9],ms[9];
	char tm[9];
	sprintf_s(ns,9,"%d",n);
	sprintf_s(ms,9,"%d",m);
	int tries=strlen(ns);

	for(int c=0;c<tries;c++)
	{
		strcpy_s(tm,9,ms);
		for(int i=0;i<c;i++)
		{
			for(int u=0;u<tries;u++)
			{
				Swap(&tm[u],&tm[tries-1]);
			}
		}
		if(!strcmp(ns,tm))
			return true;
	}

	return false;
}

int main(int argc, char* argv[])
{
	FILE* fin,*fout;
	int T;
	int A,B;
	int n,m;
	char buf[256];

	fopen_s(&fin,"C:/input.txt","r");
	fopen_s(&fout,"C:/output.txt","r+");
	if(ferror(fin))
		return 1;
	fgets(buf,256,fin);
	if(!sscanf_s(buf,"%d",&T))
		return 1;

	for(int CT=0;CT<T;CT++)
	{
		int nRecycled=0;
		fgets(buf,256,fin);
		sscanf_s(buf,"%d %d",&A,&B);
		n=A;m=A+1;
		while(true)
		{
			if(isRecycled(n,m))
				nRecycled++;
			if(m<B)
				m++;
			else if(n+1<B)
			{
				n++;
				m=n+1;
			}
			else
				break;
		}
		if(CT==0)
			sprintf_s(buf,256,"Case #%d: %d",CT+1,nRecycled);
		else
			sprintf_s(buf,256,"\nCase #%d: %d",CT+1,nRecycled);
		fputs(buf,fout);
		printf_s("Case #%d: %d\n",CT+1,nRecycled);
	}

	fclose(fin);
	fclose(fout);

	system("PAUSE");
	return 0;
}

