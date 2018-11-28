
#include<cmath>
#include<cstdio>
#include<fstream>
#include<iostream>
#include<vector>
#include<list>
#include<algorithm>
#include<utility>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<string>
#include<cstdlib>
#include<bitset>
#include<cassert>

#define f(i,a,b) for(int (i)=(a);(i)<(b);(i)++)
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define inp(x) scanf("%d",&(x))

using namespace std;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef pair<int,bool> pib;
ifstream fin;
ofstream fout;


int main()
{
    fin.open("B-small-attempt0.in");
    fout.open("B.out");
    fout.precision(10);
    int numcases;
    fin>>numcases;
    int c,d,t3,t2,v;
    double t1;
    vector<int> vendors;
    f(cas,1,numcases+1)
    {
        fout<<"Case #"<<cas<<": ";
        fin>>c>>d;
        vendors.clear();
        f(i,0,c)
        {
                fin>>t3>>t2;
                f(i,0,t2)
                {
                         vendors.pb(t3);
                }
        }
        v=vendors.size();
        sort(vendors.begin(),vendors.end());
        double time[v],loc[v];
        time[0]=0;
        
        loc[0]=vendors[0];
        f(i,1,v)
        {
                t1=vendors[i]+time[i-1];
                if(t1>=loc[i-1]+d)
                {
                                          //cerr<<'a';
                                          time[i]=time[i-1];
                                          loc[i]=max(loc[i-1]+d,vendors[i]-time[i]);
                }
                else
                {
                    
                    time[i]=time[i-1]+(d-(t1-loc[i-1]))/2;
                    loc[i]=t1+(d-(t1-loc[i-1]))/2;
                }
               // cerr<<time[i]<<" "<<loc[i]<<"\n";
        }
        fout<<time[v-1]<<"\n";
        
    }
    fin.close();
    fout.close();
    return 0;
}
