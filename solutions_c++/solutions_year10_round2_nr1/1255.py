#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#define f(x,y) for(int x=0;x<y;x++)
#define o(x) cout<<x<<endl
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define All(x) x.begin(),x.end()
using namespace std;

typedef long long int LL;
typedef vector<int> vi;
typedef vector<string> vs;

struct Cell
{
    map<string,Cell> self;
};

int main()
{
	int T,N,M;
	ifstream fin("a-large.in");
	ofstream fout("a-large.out");
	string s,prev;
	fin>>T;
	
	
	f(i,T)
	{
        Cell C;
        
        fin>>N>>M;
        f(j,N)
        {
            fin>>s;
            s.erase(s.begin());
            
            stringstream ss(s);
            Cell *pc=&C;
            
            while(getline(ss,s,'/'))
            {
                (*pc).self[s];
                pc=&((*pc).self[s]);
            }
        }
        
        int res=0;
        f(j,M)
        {
            fin>>s;
            
            s.erase(s.begin());
            stringstream ss(s);
            bool NEW=0;
            Cell *pc=&C;
            
            while(getline(ss,s,'/'))
            {
                bool flag=1;
                for(map<string,Cell>::iterator it=(*pc).self.begin();it!=(*pc).self.end();it++)
                {
                    if(s==(*it).st)
                    {
                        flag=0;
                        break;
                    }
                }
                if(flag)
                {
                    (*pc).self[s];
                    res++;
                }
                pc=&((*pc).self[s]);
            }
            
        }
        
        cout<<"Case #"<<i+1<<": "<<res<<endl;
        fout<<"Case #"<<i+1<<": "<<res<<endl;
    }
	return 0;
}
