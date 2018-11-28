#include<iostream>
#include<cstdio>
#include<fstream>
#include<string>
#include<cmath>
#include<map>
#include<set>
#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define REP(i,n) FOR(i,0,n-1)
using namespace std;
int main()
{
 	ifstream instream("/home/condor/GCJ/large.in");
	ofstream outstream("/home/condor/GCJ/large.out");
	int l,d,n;
        char s[10000],inp[5000][50],pattern[100000];
	instream.getline(s,20);
    	s[20]='\n';
	int digit[16][27];
        
	// Get the value of l,d and n
		char lc[21];
	 	int j=0;int k;
         	for(k=0;s[j]!=' '&&s[j]!='\n';j++,k++)	lc[k]=s[j];
  	 	lc[k]='\n'; l=atoi(lc);j++;
	 	for(k=0;s[j]!=' '&&s[j]!='\n';j++,k++)     lc[k]=s[j];              
	 	lc[k]='\n'; d=atoi(lc);j++;
	 	for(k=0;s[j]!=' '&&s[j]!='\n';j++,k++)     lc[k]=s[j];
	 	lc[k]='\n'; n=atoi(lc); 
       
	
	// Read the inpuage
	for(int i=0;i<d;i++)
	{
		instream.getline(s,20);
		strcpy(inp[i],s);
	}

	// Read the pattern and display the answer
	for(int i=0;i<n;i++)
        {
		memset(digit,0,sizeof(digit));
		instream.getline(s,100000);
             	strcpy(pattern,s);
		int open=0;
		for(int j=0,k=0;j<strlen(pattern);j++)
 		{
			if(pattern[j]=='('){open=1; continue;}
			else if(open==1&&pattern[j]==')'){open=0; k++; }
			else { digit[k][pattern[j]-'a']=1; if(open==0) k++;}
		}
		int count1=0;
		for(int j=0;j<d;j++)
		{ 	int flag=0;
			for(int k=0;k<l;k++)
			if(digit[k][inp[j][k]-'a']==0) { flag=1;  break;} 
			if(flag==0) count1++;
		}	   
		outstream<<"Case #"<<i+1<<": "<<count1<<endl;     
        }
	outstream.close();
	instream.close();
	return 0;
}
