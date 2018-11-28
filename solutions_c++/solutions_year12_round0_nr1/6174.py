#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int encoded[26];
void init()
{
	encoded[0]='y';
	encoded[1]='h';
	encoded[2]='e';
	encoded[3]='s';
	encoded[4]='o';
	encoded[5]='c';
	encoded[6]='v';
	encoded[7]='x';
	encoded[8]='d';
	encoded[9]='u';
	encoded[10]='i';
	encoded[11]='g';
	encoded[12]='l';
	encoded[13]='b';
	encoded[14]='k';
	encoded[15]='r';
	encoded[16]='z';
	encoded[17]='t';
	encoded[18]='n';
	encoded[19]='w';
	encoded[20]='j';
	encoded[21]='p';
	encoded[22]='f';
	encoded[23]='m';
	encoded[24]='a';
	encoded[25]='q';
}
char* convert (char* str,int bound)
{
	
	for(int i = 0; i<100;i++)
	{
		int c;
		if(i<bound)
		{
		    c=str[i];
		    if(c>=97 && c<=122)
		    {
			    c=encoded[c-97];
	    	}
		    str[i]=c;
		}
		if(i>bound)
		{
			c=0;
			str[i]=c;
		}
	}
	str[bound]='\n';
	
	return str;
}

int main()
{
    init();
    int T,i=0;
    cin>>T;
    for(i=0;i<=T;i++)
    {
        char G[100];
        for(int j=0;j<100;j++)
        {
        	G[i]='\n';
       	}
        int j=0;
        char c;
        for(j=0,c=getchar();c!='\n';j++,c=getchar())
        {
           G[j]=c;
        }
        G[j]='\n';
        if(i!=0)
        {
        	cout<<"Case #"<<i<<": "<<convert(G,j);
       	
       	}
    }
    return 0;
}
