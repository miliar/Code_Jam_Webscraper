//Always use int64 for safety's sake.
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

typedef long long int64;
typedef vector<int> vi;
typedef vector<int>::iterator vi_it;
typedef vector< vector<int> > vi2d;
typedef vector< vector<int> >::iterator vi2d_it;
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
    output.open("aout");
    
    Rep(icase,n_test)
    {
        int64 n,a,b,c,d,x0,y0,m,count=0;
        input>>n>>a>>b>>c>>d>>x0>>y0>>m;
        vector<int64> X,Y;
        Rep(ip,n)
        {
            X.push_back(x0);
            Y.push_back(y0);
            x0=((a*x0)+b)%m;
            y0=((c*y0)+d)%m;
            
        }

        Rep(i,n)
        cout<<X[i]<<" "<<Y[i]<<endl;
        Rep(i,n)
        For(j,i+1,n)
        For(k,j+1,n)
        {
            if( ( (X[i]+X[j]+X[k])%3==0) && ( (Y[i]+Y[j]+Y[k])%3==0) )
                count++;
        }






        cout<<"Case #"<<icase+1<<": "<<count<<endl; 
        output<<"Case #"<<icase+1<<": "<<count<<endl; 



    }
    return 0;
}
