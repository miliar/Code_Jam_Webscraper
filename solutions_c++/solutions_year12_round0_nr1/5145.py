#include<iostream>
#include<string>

using namespace std;

string S[200],G[200],s;
char ch1;
int temp1,temp2,A[30];

int main()
{
  for(int i=0;i<26;i++)
    A[i]=-1;
  
  temp1=1;
  
  while(cin>>s)
  {
    if(s=="stop")
    {
      G[temp1]=s;
      break;
    }
    G[temp1]=s;
    temp1++;
  }
  
  cout<<G[1]<<endl;
  
  temp1=1;
  
  while(cin>>s)
  {
    S[temp1]=s;
    temp1++;
  }
  
  for(int i=1;i;i++)
  {
    if(G[i]=="stop")
      break;
    for(int j=0;j<G[i].size();j++)
    {
      temp1=G[i][j]-'a';
      temp2=S[i][j]-'a';
      A[temp1]=temp2;
    }
  }
  
  for(int i=0;i<26;i++)
    cout<<A[i]<<",";
}