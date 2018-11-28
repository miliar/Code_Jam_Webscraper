#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("A-large.in");
    ofstream out("A-large.txt");
    
    int N,cas=0;
    in>>N;
    
    while(N--)
    {
        int P,K,L;
        in>>P>>K>>L;
        
        vector<long long> f;
        int x;
        
        for(int i=0;i<L;i++)
        {
            in>>x;f.push_back(x);
        }
        
        sort(f.begin(),f.end());
        reverse(f.begin(),f.end());
        
        long long ret=0,a=1;
        
        for(int i=0;i<f.size();i++){
            if(i && (i)%K == 0) a+=1;
                ret+=((long long)a*f[i]);
            
        }
        
        out<<"Case #"<<++cas<<": "<<ret<<'\n';
    
    }
    
 return 0;
}
