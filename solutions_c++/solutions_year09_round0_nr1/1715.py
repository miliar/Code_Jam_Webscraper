#include<iostream>
#include<algorithm>

using namespace std;
int main()
{
 int i,j,N,L,D,k,c=0,cnt;
 cin>>L>>D>>N;
 string words[D];
 for(i=0;i<D;i++)
  cin>>words[i];
 while(c++<N)
 {
  string S;
  cin>>S;cnt=0;
  char Arr[L][26];
  int l=S.length();
  i=0;k=0;
  while(i<l)
  {
   j=0;
   if(S[i]!='(')
   {
    Arr[k][j]=S[i++];
   }
   else
   {i++;
    while(S[i]!=')')
    { 
      Arr[k][j++]=S[i++];
    }
    i++;
   }
   k++;
  }
  /*for(i=0;i<l;i++) 
   for(j=0;j<l;j++)
    cout<<Arr[i][j]<<" ";*/
  bool flag[L],flag1;
  for(i=0;i<D;i++)
  { 
    for(j=0;j<L;j++) flag[j]=false;
    
    for(j=0;j<L;j++)
    {
     for(k=0;k<26;k++)
     if(words[i][j]==Arr[j][k])
     { flag[j]=true;
       break;
     }
     if(!flag[j]) break;
    }
    flag1=true;
    for(j=0;j<L;j++)
     {if(!flag[j])
       {flag1=false;break;}
     }
    if(flag1) cnt++;
    
   }
   cout<<"Case #"<<c<<": "<<cnt<<endl;
 }
 return 0;
 }
   
   
