#include<iostream>
using namespace std;

void output(int** word,int D,int L,int line,FILE* out,bool** arr)
{
	int result=0;

	for(int i=0;i<D;i++)
	{
		for(int j=0;j<L;j++)
		{
			if(!arr[j][word[i][j]])
				break;
		}
		if(j==L)
			result++;
	}

	fputs("Case #",out);
	char str[5];
	itoa(line,str,10);
	fputs(str,out);
	fputs(": ",out);

	itoa(result,str,10);
	fputs(str,out);
	fputc('\n',out);
}

int main()
{
	FILE* in=fopen("A-large.in","r");
	FILE* out=fopen("A-large.out","w");


	char buf[500];
	fgets(buf,500,in);
	char* p=buf;
	char* mark=buf;
	while(*p!=' ')
		p++;
	*p='\0';
	int L=atoi(mark);
    mark=++p;

	while(*p!=' ')
		p++;
	*p='\0';
	int D=atoi(mark);
    mark=++p;

	while(*p!='\n')
		p++;
	*p='\0';
	int N=atoi(mark);
    

//	cout<<L<<" "<<D<<" "<<N<<endl;
    int** word=new int*[D];
	for(int i=0;i<D;i++)
	{
		word[i]=new int[L];
		fgets(buf,500,in);
	//	cout<<buf<<endl;
		for(int j=0;j<L;j++)
          word[i][j]=buf[j]-'a';
	}

	bool** arr=new bool*[L];
	for(i=0;i<L;i++)
	{
		arr[i]=new bool[26];
		for(int j=0;j<26;j++)
			arr[i][j]=false;
	}


	for(int line=1;line<=N;line++)
	{
		//cout<<line<<endl;
		fgets(buf,500,in);
		int j=0;
		p=buf;
		int flag=0;
		while(*p!='\n')
		{
			if(*p=='(')
				flag=1;
			else if(*p==')')
			{
				j++;
				flag=0;
			}
			else if(flag==0)
				arr[j++][*p-'a']=true;
			else
				arr[j][*p-'a']=true;

			p++;

		}
		output(word,D,L,line,out,arr);

	   for(int i=0;i<L;i++)
	   for(int j=0;j<26;j++)
		  arr[i][j]=false;
	  

	}

	for(i=0;i<D;i++)
	{
	    delete[] word[i];	
	}
	delete[] word;


	for(i=0;i<L;i++)
	{
		delete[] arr[i];
	}
	delete[] arr;

	fclose(out);
	fclose(in);
	return 0;

}