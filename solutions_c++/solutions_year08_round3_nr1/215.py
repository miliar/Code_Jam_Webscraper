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
#include <utility>
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
#define AllR(v) (v).rbegin(), (v).rend()

typedef long long ll;
typedef vector<ll> vi;
typedef vector<ll>::iterator vi_it;
typedef vector< vector<ll> > vi2d;
typedef vector< vector< ll > >::iterator vi2d_it;
typedef vector<string> vs;
typedef vector<string>::iterator vs_it;
typedef vector<double> vd;
typedef vector<double>::iterator vd_it;
typedef pair< ll, ll> alph;

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
        ll p,k,l,char_count=0;
        input>>p>>k>>l;
        vi freq;
        
        Rep(ifreq,l)
        {
            ll frequency;
            input>>frequency;
            freq.push_back(frequency);
            if(frequency!=0)
                char_count++;
            
        }
        
        if(k*p<char_count)
        {
            cout<<"Case #"<<icase+1<<": Impossible"<<endl;
            continue;
        }
        
        
        sort(AllR(freq));
        
        ll key_press=0,iter=0,numpress=1;
        while(char_count)
        {
            if(iter<(numpress*k))
            {
                key_press+=freq[iter]*numpress;
            }
            else
            {
                ++numpress;
                key_press+=freq[iter]*numpress;
            }
            if(freq[iter]>0)
                char_count--;
            iter++;
            
        }        
        
        
        

        




        cout<<"Case #"<<icase+1<<": "<<key_press<<endl; 
        output<<"Case #"<<icase+1<<": "<<key_press<<endl; 



    }
    input.close();
    output.close();
    return 0;
}



















