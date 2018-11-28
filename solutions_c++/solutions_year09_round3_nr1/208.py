#include<iostream>
using namespace std;

int arr[36];
int num[100];

int Loc(char ch)
{
	if(ch<='z'&&ch>='a')
		return (ch-'a');
	else
		return (26+ch-'0');
}

void output(char buf[100],int line,FILE* out)
{

	for(int i=0;i<36;i++)
		arr[i]=-1;

	
	arr[Loc(buf[0])]=1;
	num[0]=1;
//	cout<<num[0]<<" ";
    i=1;
	int mark=-1;

	while(buf[i]!='\n'&&buf[i]!='\0')
	{
       if(arr[Loc(buf[i])]!=-1)
	   {
          num[i]=arr[Loc(buf[i])];
		 // cout<<num[i]<<" ";
	   }
	   else
	   {
		   mark++;
		   if(mark==1)
			   mark++;
		   arr[Loc(buf[i])]=mark;
		   num[i]=mark;
		  // cout<<num[i]<<" ";
	   }
	   i++;
	}

	num[i]=-1;

	if(mark<1)
		mark=2;
	else
	    mark++;

	unsigned __int64 result=0;
	i=0;
	while(num[i]!=-1)
	{
        result*=mark;
		result+=num[i];
		i++;
	}

	fprintf(out,"Case #%d: %I64u\n",line,result);
}

int main()
{
	FILE* in=fopen("A-large.in","r");
	FILE* out=fopen("A-large.out","w");

	char buf[100];
	fgets(buf,10,in);
	int T=atoi(buf);

	for(int line=1;line<=T;line++)
	{
		fgets(buf,100,in);
        
		output(buf,line,out);
	}

	fclose(in);
	fclose(out);
	return 0;
}
