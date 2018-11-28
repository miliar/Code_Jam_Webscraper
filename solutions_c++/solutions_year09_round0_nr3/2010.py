#include <iostream>
#include <string>
using namespace std;
char wel[]={'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m','/0'}; //19 caracteres + 1 nulo
int len;
string s;
int calcula(int pos,int index)
{
int r=0;
if(index==19)
return 1;
if(pos==len)
return 0;
if(s[pos]==wel[index])
r+=calcula(pos+1,index+1);

r+=calcula(pos+1,index);
return r;
}

int main()
{freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int n;
cin>>n;
getline(cin,s);
for(int i=1;i<=n;i++)
{
getline(cin,s);
len=s.size();
//if(len<19)
//cout<<"Case #"<<i<<": 0000"<<endl;
//else
 // {
  cout<<"Case #"<<i<<": ";
    int resp=calcula(0,0);
    if(resp>999)
    cout<<resp<<endl;
    else
       if(resp>99)
       cout<<"0"<<resp<<endl;
       else
          if(resp>9)
          cout<<"00"<<resp<<endl;
          else
             if(resp>0)
             cout<<"000"<<resp<<endl;
             else
             cout<<"0000"<<endl;

  //}
}
return 0;    
}
