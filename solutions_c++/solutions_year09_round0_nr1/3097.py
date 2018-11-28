#include<iostream>
using namespace std;
bool  checw(string a,string b)
{int i,j;
bool n=1;
for(i=0,j=0;i<a.length()&&n==1;i++)
{n=0;
  if(b[j]=='(')
  {j++;
  for(;j<b.length()&&n==0&&b[j]!=')';j++)
  {if(a[i]==b[j])
  n=1;
  }
  while(b[j]!=')')
  j++;
  }
  else if(b[j]==a[i])
  n=1;
  j++;
}
return n;
}
int main()
{int  i,j,L,D,N;
bool p;
cin>>L>>D>>N;

string test[N],s,inp[D];

for(i=0;i<D;i++)
{cin>>inp[i];
}
int cnt=0;
for(i=0;i<N;i++)
{cin>>s;
cnt=0;
for(j=0;j<D;j++)
{
p=checw(inp[j],s);
if(p==1)
cnt++;
}
cout<<"Case #"<<i+1<<": "<<cnt<<endl;
}

return 0;
}