#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>  
using namespace std;


#define INF (int)1e9
#define PB push_back
#define SZ(a) ((int)((a).size()))
#define FOR(i,a,b) for(int i = a; i < (b); ++i)
#define FORE(it,x) for(typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define ALL(a) (a).begin(),(a).end()
#define CLR(a,v) memset((a),(v),sizeof(a))
#define FINDA(c,x) ((c).find(x) != (c).end()) 
#define FIND(c,x) (find(ALL(c),x) != (c).end()) 

typedef pair<int,int> II; 
typedef stringstream ss;
typedef long long ll;
typedef long double ld;
typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<II> VII;
typedef vector< VI > VVI;

int value[10005];
bool can[10005];
int gate[10005]; 
int m;
int cal(int cur)
{
    if(cur>(m-1)/2)
        return value[cur];
    int left=cal(cur<<1);
    int right=cal((cur<<1)+1);
    if(gate[cur])
        return value[cur]=left*right;    
    else
        return value[cur]=((left+right)>0)?1:0;
}

int go(int cur,int need)
{
    if(value[cur]==need)return 0;
    int left=cur*2;
    int right=left+1;
    if(left>(m-1)/2) 
    {
        if(need)
        {
            if(value[left]|value[right])
            {
                return can[cur]?1:INF;
            }
            else
            {
                return INF;
            }
        }    
        else
        {
            if(value[left]&value[right])
                return INF;
            else
                return can[cur]?1:INF;
        }
    }
    int ret=INF;
    if(need)
    {
        if(can[cur])
        {
            if(gate[cur])
                ret<?=1+(go(cur*2,1)<?go(cur*2+1,1));
            else
                ret<?=go(cur<<1,1)<?go(cur*2+1,1);            
        }
        else
        {
            if(gate[cur])
                ret<?=go(cur<<1,1)+go(cur*2+1,1);    
            else
                ret<?=go(cur<<1,1)<?go(cur*2+1,1);
        }
    }
    else
    {
        if(can[cur])
        {
            if(gate[cur])
                ret<?=go(cur*2,0)<?go(cur*2+1,0);
            else
                ret<?=1+(go(cur<<1,0)<?go(cur*2+1,0));            
        }
        else
        {
            if(gate[cur])
                ret<?=go(cur<<1,0)<?go(cur*2+1,0);    
            else
                ret<?=go(cur<<1,0)+go(cur*2+1,0);
        }
    }    
    return ret;
}

int main()
{
    ifstream fin;
    fin.open("C:\\data\\A-large.in");//small-attempt1.in");
    ofstream fout;
    fout.open("C:\\data\\al.txt");
    int t;
    fin>>t;
    int cas;
    int v,g,c;
    for(int cas=1;cas<=t;++cas)
    {
        CLR(value,-1);
        CLR(can,false);
        CLR(gate,-1);
        fin>>m>>v;
        for(int i=1;i<=m;++i)
        {
            if(i<=(m-1)/2)
            {
                fin>>gate[i]>>c;
                if(c)can[i]=true;
            }
            else
            {
                fin>>g;
                value[i]=g;    
            }
        }
        int p=cal(1);
        int ret=0;
        if(p==v)
            ret=0;
        else
            ret=go(1,v);
        if(ret!=INF)
            fout<<"Case #"<<cas<<": "<<ret<<endl;    
        else
            fout<<"Case #"<<cas<<": IMPOSSIBLE\n";
    }
    fin.close();
    fout.close();
    return 0;
}

