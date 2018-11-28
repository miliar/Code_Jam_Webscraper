#include<iostream>
using namespace std;

void output(char* buf,int line,FILE* out)
{
    char str[20]="welcome to code jam";

	char* p=buf;
	while(*p!='\n')
		p++;

	int n=p-buf;

	int* arr=new int[n];
	for(int i=0;i<n;i++)
		arr[i]=1;

	for(i=0;i<19;i++)
	{
		char ch=str[i];
        for(int j=0;j<n;j++)
		{   
			if(j==0)
			{
			   if(buf[j]!=ch)
			    arr[j]=0;
			}
			else
			{
				if(buf[j]==ch)
					arr[j]+=arr[j-1];
				else
					arr[j]=arr[j-1];
			}
						
		}
	}

	int result=arr[n-1]%10000;
	fputs("Case #",out);
	char lineStr[5];
	itoa(line,lineStr,10);
	fputs(lineStr,out);
	fputs(": ",out);

	lineStr[3]=result%10+'0';
	result/=10;
    lineStr[2]=result%10+'0';
	result/=10;
	lineStr[1]=result%10+'0';
	result/=10;
	lineStr[0]=result%10+'0';
	lineStr[4]='\0';

	fputs(lineStr,out);
	fputc('\n',out);

	delete[] arr;
}


int main()
{
	FILE* in=fopen("C-small-attempt0.in","r");
	FILE* out=fopen("C-small-attempt0.out","w");


	char buf[501];
	fgets(buf,501,in);
	int n=atoi(buf);

	for(int line=1;line<=n;line++)
	{
		fgets(buf,501,in);
		output(buf,line,out);
	}

	fclose(in);
	fclose(out);
	return 0;
}