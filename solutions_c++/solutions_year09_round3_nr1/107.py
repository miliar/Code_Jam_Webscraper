#include<iostream>
#include<vector>
#include<string>
using namespace std;
char arr[100]="";
int dig[10];
int ch[26];
int main()
{ int T;
  cin>>T;
  for(int t=0;t<T;t++)
  { cin>>arr;
    string str=arr;
    int len=str.size();
    for(int i=0;i<10;i++)
    dig[i]=-1;
    for(int i=0;i<26;i++)
    ch[i]=-1;
    if(str[0]>='0'&&str[0]<='9')
    dig[str[0]-'0']=1;
    else
    ch[str[0]-'a']=1;
    int cur=0;
    for(int i=1;i<len;i++)
    if(str[i]>='0'&&str[i]<='9'&&dig[str[i]-'0']==-1)
    { dig[str[i]-'0']=cur;
      cur++;
      if(cur==1)
      cur++;
    }
    else if(str[i]>='a'&&str[i]<='z'&&ch[str[i]-'a']==-1)
    { ch[str[i]-'a']=cur;
      cur++;
      if(cur==1)
      cur++;
    }
    if(cur==0)
    cur=2;
    long long sum=0;
    for(int i=0;i<len;i++)
    if(str[i]>='0'&&str[i]<='9')
    sum=sum*cur+dig[str[i]-'0'];
    else if(str[i]>='a'&&str[i]<='z')
    sum=sum*cur+ch[str[i]-'a'];
    cout<<"Case #"<<t+1<<": "<<sum<<"\n";
  }
}    
    
      
