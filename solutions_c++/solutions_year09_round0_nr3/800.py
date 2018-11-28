#include<iostream>
#include<vector>
#include<string>
using namespace std;
char arr[1000]="";
string head="welcome to code jam";
int main()
{ int T=0;
  gets(arr);
  string tt=arr;
  for(int i=0;i<tt.size();i++)
  T=T*10+tt[i]-'0';
  for(int t=0;t<T;t++)
  { gets(arr);
    string str=arr;
    vector<int>soln(20);
    int len=str.size();
    int mlen=head.size();
    for(int i=0;i<len;i++)
    for(int j=mlen-1;j>=0;j--)
    if(j==0&&str[i]==head[j])
    soln[j]=(soln[j]+1)%10000;
    else if(j!=0&&head[j]==str[i])
    soln[j]=(soln[j]+soln[j-1])%10000;
    //cout<<str<<":"<<soln[mlen-1]<<"\n";
    cout<<"Case #"<<t+1<<": "<<char((soln[mlen-1]/1000)%10+'0')<<char((soln[mlen-1]/100)%10+'0')<<char((soln[mlen-1]/10)%10+'0')<<char((soln[mlen-1])%10+'0')<<"\n";
  }
}
