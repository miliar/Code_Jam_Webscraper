#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;
main()
{
int L,N,D,i,j,k,a,b[20][26],cnt;
vector<string> c;
string s;

scanf("%d %d %d",&L,&D,&N);
//cout<<"here"<<endl;
memset(b,0,sizeof(b));
for(i=0;i<D;i++)
{
 cin>>s;
 c.push_back(s);
}
//cout<<"here"<<endl;
for(i=0;i<N;i++)
{
  cin>>s;
  int flag=0;
cnt=0;
  j=0;
  k=0;
  while(j<s.size())
     {   
         if(s[j]=='(')
          { 
             flag=1;j++;continue;
          }
          if(s[j]==')')
          {
             flag=0;k++;j++;continue;
          }

           b[k][s[j]-'a']=i+1;
         if(flag==0)
          k++;
                  
      j++;
     }  
 
for(j=0;j<D;j++)
 {  
    flag=0;
    for(k=0;k<L;k++)
     {
          if( b[k][c[j][k]-'a']==i+1)
             continue;
          else
           {flag=1;break;}

     
     }
      if(flag==0)
       cnt++;     
 
 }
  cout<<"Case #"<<i+1<<": "<<cnt<<endl;
 
}

}
