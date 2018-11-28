#include<iostream>
#include<string>
#include<vector>
#include<cstring>
#include<algorithm>
#include <iomanip>
#include<cmath>
#include<map>
#include <sstream>
using namespace std;

#define PB push_back
#define F0(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FORE(i,x) for( auto i=(x).begin();i != (x).end();++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,w) memset((x),w,sizeof (x))
#define X first
#define Y second
//////////////////////////////////////////////////
string str[4];

void display()
{
 cout<<"--------------------"<<endl;
 F0(i,4)
 {
   cout<<str[i]<<endl;
 }
 cout<<"--------------------"<<endl;
}

int check(char ch)
{
  int a,b,c,d;
  a=b=c=d=0;
  F0(i,4)
  {
    a=b=0;
    F0(j,4)
	{
	  if(str[i][j]==ch || str[i][j]=='T')
	   a++;
	  if(str[j][i]==ch || str[j][i]=='T')
	   b++;
	}
	if(a==4)
   return a;
    if(b==4)
   return b;
  }
  
   c=0;
   F0(i,4)
   {
    if(str[i][i]==ch || str[i][i]=='T')
	 c++;
   }
   if(c==4)
   return c;
   d=0;
   int i,j;
   i=0,j=3;
   for(;i<4 && j>=0 ;i++,j--)
   {
    if(str[i][j]==ch || str[i][j]=='T')
	 d++;
   }
   if(d==4)
     return d;
  return 0;
}
int checkg()
{
 F0(j,4)
{
  string::size_type found = str[j].find('.');
   if (found!=string::npos)
  {
	return 1;
  }
}
 return 0;
}

int main()
{

  int T;
  cin>>T;
  cin.get();
  FOR(i,1,T)
  {
    int x,o,d;
    F0(j,4)
	getline(cin,str[j],'\n');
	//display();
	cin.get();
	x=check('X');
	o=check('O');
	if(x==0 && o==0)
	{
	  if(checkg())
	  {
	   cout<<"Case #"<<i<<": Game has not completed"<<endl;
	  }
	  else
	  {
	   cout<<"Case #"<<i<<": Draw"<<endl;
	  }
	}
	else if(x>0 && o==0)
    cout<<"Case #"<<i<<": X won"<<endl;
	else if(x==0 && o>0)
	 cout<<"Case #"<<i<<": O won"<<endl;
	else
	{
	  if(checkg())
	  {
	   cout<<"Case #"<<i<<": Game has not completed"<<endl;
	  }
	   
	}
  }

return 0;
}