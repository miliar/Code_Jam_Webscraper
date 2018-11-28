//Always use ll for safety's sake.
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <bitset>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <ctime>

using namespace std;

#define For(i,a,b) for (int i(a),_b(b); i <_b; ++i)
#define ForR(i,a,b) for (int i(a),_b(b); i > _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define RepR(i,n) for (int i((n)-1); i >= 0; --i)
#define All(v) (v).begin(), (v).end()

typedef long long ll;
typedef vector< ll > vi;
typedef vector<ll>::iterator vi_it;
typedef vector< vector< ll> > vi2d;
typedef vector< vector< ll> >::iterator vi2d_it;
typedef vector<string> vs;
typedef vector<string>::iterator vs_it;
typedef vector<double> vd;
typedef vector<double>::iterator vd_it;



int main()
{
    char clear1;
    string clear2;
    unsigned int n_test;

    ifstream input;
    input.open("A.in");
    input>>n_test;
    
    ofstream output;
    output.open("a-out");
    
    Rep(icase,n_test)
    {
        ll No[1001][1001];
        Rep(ino1,1001)
        Rep(ino2,1001)
            No[ino1][ino2]=0;
        ll n,m,X,Y,Z,count=0;
        vector< ll > A,B;
        input>>n>>m>>X>>Y>>Z;
        Rep(ino3,n)
            No[1][ino3]=1;
        
        Rep(iA,m)
        {   
            ll temp;
            input>>temp;
            A.push_back(temp);
        }
        
        Rep(iB,n)
        {
            B.push_back(A[(iB%m)]);
            A[(iB%m)] = (X * A[(iB%m)] + Y * (iB + 1))%Z;
        }
        for(int i=1;i<=n;i++)
        for(int j=i-1;j<n;j++)
        { 
            for(int k=0;k<j;k++)
            if(B[k]<B[j])
            {
                No[i][j]+=(No[i-1][k]%1000000007);
                No[i][j]%=1000000007;
            }
            count+=No[i][j]; 
            count%=1000000007; 
        } 
          
        
        
        cout<<"Case #"<<icase+1<<": "<<count<<endl; 
        output<<"Case #"<<icase+1<<": "<<count<<endl; 



    }
    input.close();
    output.close();
    return 0;
}
