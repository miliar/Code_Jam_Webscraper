//Welcome to Code Jam
#include<iostream>
#include<string>
#include<cstring>
using namespace std;
#define si 10000
string str,s;
int arr[501][21];
int match(int i,int j)
{
 
 if((i==s.size() && j<str.size()) || ((s.size()-i)<(str.size()-j)))
 return 0;
else if(arr[i][j]==-1)
{
 if(j==str.size())
 arr[i][j]=1;
 else 
 arr[i][j]=match(i+1,j)+(s[i]==str[j]?match(i+1,j+1):0);
}
 arr[i][j]%=si;
 return arr[i][j]%si;
}
int main()
{
 str="welcome to code jam";s="";

 int t;
 cin>>t;
 getline(cin,s);
 for(int i=1;i<=t;i++)
 {
  getline(cin,s);
  memset(arr,-1,sizeof(arr));
  printf("Case #%d: %04d\n",i,(match(0,0))%si);
 }
 return 0;
}
