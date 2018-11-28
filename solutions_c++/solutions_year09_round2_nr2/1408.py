#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <map>
#include <vector>
#include <set>

using namespace std;

#define S(n) scanf("%d",&n)
#define REP(i,n) for(i=0; i<n; i++)
#define REPA(i,a,n) for(i=a; i<n; i++)
#define SOR(x) sort(x.begin(), x.end())
#define REV(x) reverse(x.begin(), x.end())
#define FOREACH(iter,var) for(__typeof((var).begin()) iter=(var).begin(); iter!=(var).end(); iter++)
#define PB push_back
#define VI vector<int>
#define SZ size()
#define VS vector<string>

#define MP make_pair
#define VVI vector< vector<int> >
#define INF 2000000000

long long toNumber( VI digits )
{
    int i;
    long long answer = 0;
    int l = digits.SZ;
    REP( i, l )
    {
        answer += pow( 10, l - 1 - i ) * digits[i];
    }
    return answer;
}

int main()
{
    int i, caseN;
    int N;
    int j;
    freopen( "input.in", "r", stdin );
    freopen( "output.out", "w", stdout );
    cin>>N;
    REP( caseN, N )
    {
        string number;
        //int digits[] = { 0, 0, 0, 0, 0, 0, 0 };
        cin>>number;
        VI digits;
        vector< long long > permutations;
        REP( i, number.length() )
            digits.PB( number[i] - '0' );
        long long input = toNumber( digits );
        //cout<<" input = "<<input;
        digits.PB( 0 );

        SOR( digits );


        permutations.PB( toNumber( digits ) );
        while( next_permutation( digits.begin(), digits.end() ) )
            permutations.PB( toNumber( digits ) );

        SOR( permutations );

        REP(i, permutations.SZ )
        {
            //cout<<" i "<< i << " : "<<permutations[i]<<endl;
            if( input == permutations[i] )
            {
                cout<<"Case #"<<caseN + 1<<": "<<permutations[ i + 1 ]<<endl;
                break;
            }
        }
    }

}
