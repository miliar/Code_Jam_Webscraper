#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int run(int,int,int,vector<long> &);
int main(char **argv,int argc)
{
   int lineNum;
   cin >> lineNum;
   for (int i=0;i<lineNum;++i)
   {
       long r,k,n;
	   cin >> r >> k >> n;
       vector<long> group;
       group.reserve(1050);
       long g;
       for (int j=0;j<n;++j)
       {
           cin >> g;
           group.push_back(g);
       }
	   int rlt=run(r,k,n,group);
	   cout <<     "Case #" << i+1 << ": " << rlt << endl;
	   
   }
   return 0;
}
int run(int r,int k,int n,vector<long> &group)
{
    int earning=0;
    int flag=0;
    for (int i=0;i<r;++i)
    {
       int people=0;
       int startFlag=flag;
       while (people+group.at(flag)<=k)
       {
             people+=group.at(flag);
             ++flag;
             if (flag>=n) flag=0;
             if (flag==startFlag) break;
       }
       earning +=people;
    }
    return earning;
}
