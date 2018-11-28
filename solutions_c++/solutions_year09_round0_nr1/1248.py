#include <string>
#include <iostream>
using namespace std;

int main()
{
  int L,D,N,i,j,k,ctr,flag;
  string s;
  cin>>L>>D>>N;
  string word[5000];
  int a[15][26];
  for(i=0;i<D;i++)
    cin>>word[i];
  for(i=0;i<N;i++)
    {
      cin>>s;
      for(j=0;j<L;j++)
	for(k=0;k<26;k++)
	  a[j][k]=0;
      for(j=0,k=0,flag=0;j<s.length();j++)
	{
	  switch (s[j])
	    {
	    case '(': flag=1;
	      break;
	    case ')': flag=0;
	      break;
	    default: a[k][s[j]-'a']=1;
	    }
	  if(!flag)
	    k++;
	}
      for(j=0,ctr=0;j<D;j++)
	{
	  for(k=0;k<L;k++)
	    if(!a[k][word[j][k]-'a'])
	      break;
	  if(k==L)
	    ctr++;
	}
      cout<<"Case #"<<i+1<<": "<<ctr<<"\n";
    } 
}
