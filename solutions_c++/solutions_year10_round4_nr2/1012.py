#include<iostream>
#include<fstream>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<stack>
#include<utility>
#include<string>
#include<sstream>

#define f(i,a,b) for(int (i)=(a);(i)<(b);(i)++)
#define pb push_back

using namespace std;

typedef pair<int,int> pii;
typedef pair<pair<int,int> ,int> tri;
typedef vector<int> vi;
typedef vector<double> vd;

ifstream fin;
ofstream fout;

int main()
{
    fin.open("B-small-attempt0.in");
    fout.open("B-small-attempt0.out");
    int cases;
    fin>>cases;
    int p,n,temp,currx,curry,cost;
    f(cas,1,cases+1)
    {
                    fout<<"Case #"<<cas<<": ";
                    fin>>p;
                    cost=0;
                    n=int(pow(2.0,p)+0.1);
                    int m[n];
                    f(i,0,n)
                    {
                            fin>>m[i];
                            m[i]=p-m[i];
                    }
                    f(i,0,n-1)
                    {
                              fin>>temp;
                    }
                    vector<bool> attend[p];
                    f(i,0,p)
                    {
                            f(j,0,int(pow(2.0,i)+0.1))
                            {
                                                      attend[i].pb(false);
                            }
                    }
                    f(i,0,n)
                    {
                            currx=0;
                            curry=0;
                            while(m[i]>0)
                            {
                                         
                                         if(!attend[curry][currx])
                                         {
                                                                  attend[curry][currx]=true;
                                                                  cost++;
                                                                  f(j,currx*int(pow(2.0,p-curry)+0.1),(currx+1)*int(pow(2.0,p-curry)+0.1))
                                                                  {
                                                                                                                                          m[j]--;
                                                                  }                                                                 
                                         }
                                         else
                                         {
                                             if((i/int(pow(2.0,p-curry-1)+0.1))%2==0)
                                             {
                                                                                 currx*=2;
                                             }
                                             else currx=currx*2+1;
                                             curry++;
                                         }
                            }
                    }
                    fout<<cost<<"\n";
    }
    
    fin.close();
    fout.close();
    return 0;
}
