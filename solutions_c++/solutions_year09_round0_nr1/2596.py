#include <iostream>
using namespace std;
 int l,d,n;
int find(string str,string temp)
{
  int j=0,flag,find;
  for(int i=0;i<l;i++)
    {
      flag=0;find=0;

      while(!find)
      {
        if( j>=temp.size( ) )
         return 0;
      if(temp[j]=='(')
        {
             j++;
             flag=1;
        }
      else if(temp[j]==str[i])
      {
        find=1;
        if(flag)
        {
            while(temp[j]!=')')
             j++;
            flag=0;
        }
        j++;
      }
      else if(flag==0&&temp[j]!=str[i])
       return 0;
      else if(flag&&temp[j]==')'&&find==0)
      {
          return 0;
      }
      else
      j++;
      }
    }
    if(j==temp.size( ))
    return 1;
    else
    return 0;
}
int main( )
{

    string str[5000];
    int cnt;
    string tmp;
    scanf("%d%d%d",&l,&d,&n);
    for(int i=0;i<d;i++)
    {
      cin>>str[i];
    }
    for(int i=0;i<n;i++)
    {
        cin>>tmp;
        cnt=0;
        for(int j=0;j<d;j++)
         {
          int ans=find(str[j],tmp);

           if(ans)
           {
               cnt++;
           }
         }
         cout<<"Case #"<<i+1<<": "<<cnt<<endl;
    }
    return 0;
}
