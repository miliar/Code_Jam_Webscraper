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

#define sz size()
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define S(x) sort(x.begin(),x.end())
#define pb push_back

#define vi vector<int>
#define vs vector<string>

long long x[100002]={0},y[100002]={0},n;

int main()
{
    
    ifstream in("A-small-attempt1.in");
    ofstream out("A-small.txt");
    
    int N,cas=0;
    in>>N;
    
    while(N--)
    {
        int A,B,C,D,x0,y0,M;
              
        in>>n>>A>>B>>C>>D>>x0>>y0>>M;
        
        x[0]=x0,y[0]=y0;
        for(int i=1;i<=n-1;i++)
        {
            x[i]=((A*x[i-1])+B)%M;
            y[i]=((C*y[i-1])+D)%M;
            
//            out<<x[i]<<" "<<y[i]<<'\n';
        }
            
        int c=0;
        for(int i=0;i<n;i++)
        for(int j=i+1;j<n;j++)
        for(int k=j+1;k<n;k++)
            if((long long)((long long)x[i]+x[j]+x[k])%3 == 0 && (long long)((long long)y[i]+y[j]+y[k])%3 ==0 )
                c++;
                
        out<<"Case #"<<++cas<<": "<<c<<'\n'; 
    }
    
    
    return 0;
}
