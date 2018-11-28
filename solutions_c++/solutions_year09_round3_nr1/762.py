#include <iostream>
using namespace std;

long long v;
int T,t;
char input[100];
int i,ii,iii;
bool alpha[256];
int nletters;
int proc[100];
int cur;
bool hasZero;
int main()
{
  cin>>T;
  hasZero=false;
  nletters = 0;
  cur = 1;
  
  for (t=1;t<=T;t++)
  {
    cin>>input;
	nletters=0;
	hasZero = false;
	for (i=0;i<256;i++)
	{
	  alpha[input[i]]=false;
	}
	
	for (i=0;i<strlen(input);i++)
	{
	  if (!alpha[input[i]])
	  {
	    alpha[input[i]]=true;
		nletters++;
	  }
	  proc[i]=-1;
	}
	
	proc[0]=1;
	for (i=1;i<strlen(input);i++)
	{
	  if (input[i]==input[0])
	  {
	    proc[i]=1;
	  }
	}
	
	cur = 2;
	
	for (i=1;i<strlen(input);i++)
	{
	  if (proc[i]==-1)
	  {
	    if(!hasZero)
		{
		  proc[i]=0;
		  hasZero=true;
		}
		else
		{
		  proc[i]=cur;
		  cur++;
		}
		
		for (ii=i+1;ii<strlen(input);ii++)
		  {
		    if (input[ii]==input[i])
			{
			  proc[ii]=proc[i];
			}
		  }
	  }
	}
	v = 0;
	if (nletters==1)
	{
	  nletters=2;
	}
	for (i=0;i<strlen(input);i++)
	{
	  //cout<<proc[i];
	  v*=nletters;
	  v+=proc[i];
	}
	cout<<"Case #"<<t<<": "<<v<<endl;
  }
  return 0;
}