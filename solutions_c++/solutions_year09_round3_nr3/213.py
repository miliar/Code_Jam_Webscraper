#include<iostream>
using namespace std;

int loc[102];
long opt[102][102];

void output(int P,int Q,int line,FILE* out)
{

	for(int i=0;i<=Q;i++)
		opt[i][i+1]=0;
	for(int l=2;l<=Q+1;l++)
	{
		for(int i=0;i<=Q-l+1;i++)
		{
            opt[i][i+l]=10000000;
			int result=loc[i+l]-loc[i]-2;
			for(int j=i+1;j<i+l;j++)
			{
				if(result+opt[i][j]+opt[j][i+l]<opt[i][i+l])
                   opt[i][i+l]=result+opt[i][j]+opt[j][i+l];
			}
		}
	}

	fprintf(out,"Case #%d: %ld\n",line,opt[0][Q+1]);
}

int main()
{
	FILE* in=fopen("C-large.in","r");
	FILE* out=fopen("C-large.out","w");

	char buf[1000];
	fgets(buf,10,in);
	int T=atoi(buf);
    loc[0]=0;
	for(int line=1;line<=T;line++)
	{
		fgets(buf,20,in);
		int P=atoi(buf);

		char* p=buf;
		while(*p!=' ')
			p++;

		int Q=atoi(++p);
        
		fgets(buf,1000,in);
		char* mark=buf;
		p=buf;
		for(int i=1;i<=Q;i++)
		{
			loc[i]=atoi(mark);

			while(*p!=' '&&*p!='\n')
				p++;
			mark=++p;
		}

		loc[Q+1]=P+1;
		output(P,Q,line,out);
	}

	fclose(in);
	fclose(out);
	return 0;
}
