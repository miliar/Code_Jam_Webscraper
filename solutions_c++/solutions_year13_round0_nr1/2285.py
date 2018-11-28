/* Author : migdal */
#include <iostream>
#include <cstdio>
#include <vector>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <climits>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
using namespace std;
#define FOR(i,a,b) for(int i= (int )a ; i < (int )b ; ++i)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define INF 1000000000
#define ALL(x) x.begin(),x.end()
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
typedef pair<int,int> PI;
typedef vector<int> VI;
typedef long long LL;
int main()
{
   int test,i,j,coun;
   int fl1,fl2,fl3;
   string str;
   cin>>test;coun=0;
   vector<string>x,o;
   x.PB("XXXX");x.PB("TXXX");x.PB("XTXX");x.PB("XXTX");x.PB("XXXT");
   o.PB("OOOO");o.PB("TOOO");o.PB("OTOO");o.PB("OOTO");o.PB("OOOT");
   while(test--)
   {
      fl1=0;fl2=0;fl3=0;
      coun++;
      vector<string>grid;
      for(i=0;i<4;i++){cin>>str;grid.PB(str);}

      for(i=0;i<4;i++)
      {
	 str="";
	 for(j=0;j<4;j++)str=str+grid[i][j];
	 for(j=0;j<x.size();j++)if(str==x[j])fl2=1;
	 if(fl2)break;
      }
      if(fl2){cout<<"Case #"<<coun<<": "<<"X won"<<endl;continue;}
      for(i=0;i<4;i++)
      {
	 str="";
	 for(j=0;j<4;j++)str=str+grid[j][i];
	 for(j=0;j<x.size();j++)if(str==x[j])fl2=1;
	 if(fl2)break;
      }
      if(fl2){cout<<"Case #"<<coun<<": "<<"X won"<<endl;continue;}
      str="";
      for(i=0;i<4;i++)str=str+grid[i][i];
      for(j=0;j<x.size();j++)if(str==x[j])fl2=1;
      if(fl2){cout<<"Case #"<<coun<<": "<<"X won"<<endl;continue;}
      str="";
      for(i=0;i<4;i++)str=str+grid[3-i][i];
      for(j=0;j<x.size();j++)if(str==x[j])fl2=1;
      if(fl2){cout<<"Case #"<<coun<<": "<<"X won"<<endl;continue;}


      for(i=0;i<4;i++)
      {
	 str="";
	 for(j=0;j<4;j++)str=str+grid[i][j];
	 for(j=0;j<o.size();j++)if(str==o[j])fl3=1;
	 if(fl3)break;
      }
      if(fl3){cout<<"Case #"<<coun<<": "<<"O won"<<endl;continue;}
      for(i=0;i<4;i++)
      {
	 str="";
	 for(j=0;j<4;j++)str=str+grid[j][i];
	 for(j=0;j<o.size();j++)if(str==o[j])fl3=1;
	 if(fl3)break;
      }
      if(fl3){cout<<"Case #"<<coun<<": "<<"O won"<<endl;continue;}
      str="";
      for(i=0;i<4;i++)str=str+grid[i][i];
      for(j=0;j<o.size();j++)if(str==o[j])fl3=1;
      if(fl3){cout<<"Case #"<<coun<<": "<<"O won"<<endl;continue;}
      str="";
      for(i=0;i<4;i++)str=str+grid[3-i][i];
      for(j=0;j<o.size();j++)if(str==o[j])fl3=1;
      if(fl3){cout<<"Case #"<<coun<<": "<<"O won"<<endl;continue;}
       
      for(i=0;i<4;i++)for(j=0;j<4;j++)if(grid[i][j]=='.')fl1=1;
      if(fl1){cout<<"Case #"<<coun<<": "<<"Game has not completed"<<endl;continue;}
      cout<<"Case #"<<coun<<": "<<"Draw"<<endl;

   }
   return 0;
}
