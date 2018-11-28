#include<iostream>
using namespace std;

char arr[25];

void output(int N,int line,FILE* out)
{

	for(int i=N-1;i>0;i--)
	{
		if(arr[i]>arr[i-1])
		{
			for(int j=N-1;j>=i;j--)
			{
				if(arr[j]>arr[i-1])
				{
					char temp=arr[i-1];
					arr[i-1]=arr[j];
					arr[j]=temp;
					for(int k=i,l=N-1;k<l;k++,l--)
					{
						temp=arr[k];
						arr[k]=arr[l];
						arr[l]=temp;
					}
					arr[N]='\0';
					break;
				}
				else
					continue;
			}
			break;
		}

	}

	if(i==0)
	{
		for(int k=0,l=N-1;k<l;k++,l--)
		{
			char temp=arr[k];
			arr[k]=arr[l];
			arr[l]=temp;
		}

		for(int i=0;i<=N-1;i++)
		{
			if(arr[i]>'0')
			{
				char temp=arr[0];
			    arr[0]=arr[i];
			    arr[i]=temp;
				break;
			}
		}

		for(i=N;i>=2;i--)
			arr[i]=arr[i-1];
		arr[1]='0';


		arr[N+1]='\0';
	}

	fprintf(out,"Case #%d: %s\n",line,arr);
}

int main()
{
	FILE* in=fopen("B-large.in","r");
	FILE* out=fopen("B-large.out","w");

	char buf[50];
	fgets(buf,10,in);
	int T=atoi(buf);

	for(int line=1;line<=T;line++)
	{
		fgets(buf,50,in);
		
		char* p=buf;
		int loc=0;
		while(*p!='\n')
		{
            arr[loc++]=*p;
			p++;
		}
 
		output(loc,line,out);
	}

	fclose(in);
	fclose(out);
	return 0;
}
