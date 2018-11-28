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

#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define RepR(i,n) for (int i((n)-1); i >= 0; --i)
#define All(v) (v).begin(), (v).end()

const int max_m=10000;

typedef long long ll;
typedef vector< ll > vi;
typedef vector< ll >::iterator vi_it;
typedef vector< vector< ll > > vi2d;
typedef vector< vector< ll > >::iterator vi2d_it;
typedef vector< string > vs;
typedef vector< string >::iterator vs_it;
typedef vector< double > vd;
typedef vector< double >::iterator vd_it;

inline ll minimum(ll a,ll b)
{
    if(a<b)
        return a;
    else
        return b;
}


int main()
{
    char clear1;
    string clear2;
    unsigned int n_test;

    ifstream input;
    input.open("in");
    input>>n_test;
    
    ofstream output;
    output.open("out");

    
    Rep(icase,n_test)
    {
        ll m,vroot;
        input>>m>>vroot;
        ll minval[max_m][2],value[max_m],gate[max_m],changeable[max_m];

        Rep(irow,10000)
            Rep(icol,2)
            {
                minval[irow][icol]=0;
            }
        
        Rep(irow,10000)
        {
            value[irow]=-1;
            gate[irow]=-1;
            changeable[irow]=-1;
        }

        Rep(iintnode,((m-1)/2))
        {
            input>>gate[iintnode]>>changeable[iintnode];
        }

        for(int ileaf=((m-1)/2);ileaf<m;++ileaf)
        {
            input>>value[ileaf]; 
            minval[ileaf][value[ileaf]]=0;
            minval[ileaf][((value[ileaf]+1)%2)]=max_m+1;

        }
        /*

        Rep(ix,((m-1)/2))
        {
            cout<<ix<<" "<<gate[ix]<<" "<<changeable[ix]<<endl;
        }
        for(int ileaf=((m-1)/2);ileaf<m;++ileaf)
        {
            cout<<ileaf<<" "<<minval[ileaf][0]<<" "<<minval[ileaf][1]<<endl;
        }
        cout<<endl;
        */


        

        RepR(i,((m-1)/2))
        {
            if(changeable[i])
            {
                if(gate[i]==1)
                {
                    minval[i][0]=minimum(minval[2*i+1][0],minval[2*i+2][0]);
                    minval[i][1]=minimum(minimum(minval[2*i+1][1],minval[2*i+2][1])+1,minval[2*i+1][1]+minval[2*i+2][1]);
                }
                else
                {
                    minval[i][1]=minimum(minval[2*i+1][1],minval[2*i+2][1]);
                    minval[i][0]=minimum(minimum(minval[2*i+1][0],minval[2*i+2][0])+1,minval[2*i+1][0]+minval[2*i+2][0]);
                }

            }
            else
            {
                if(gate[i]==1)
                {
                    minval[i][0]=minimum(minval[2*i+1][0],minval[2*i+2][0]);
                    minval[i][1]=minval[2*i+1][1]+minval[2*i+2][1];
                }
                else
                {
                    minval[i][1]=minimum(minval[2*i+1][1],minval[2*i+2][1]);
                    minval[i][0]=minval[2*i+1][0]+minval[2*i+2][0];
                }
            }
        }

        if(minval[0][vroot]>=max_m+1)
        {
            output<<"Case #"<<icase+1<<": "<<"IMPOSSIBLE"<<endl; 
            cout<<"Case #"<<icase+1<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
        else
        {
            cout<<"Case #"<<icase+1<<": "<<minval[0][vroot]<<endl; 
            output<<"Case #"<<icase+1<<": "<<minval[0][vroot]<<endl;
        }
        



    }

    input.close();
    output.close();
    return 0;
}
