#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <utility>
#include <sstream>
#include <fstream>
#include <cmath>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef long long ll;
typedef pair<int, int> pii;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(), (a).end()
#define SORT(a) sort(ALL(a))
#define pb push_back


int main(int argc, char** argv)
{
    ifstream in(argv[1]);
    int testnum;
    in >> testnum;
    string eof;
    getline(in, eof);

    for (int h=0; h<testnum; ++h)
    {
        int dim = 0;
        int temp = 0;
        in >> dim;
        vector<int> first;
        vector<int> second;
        REP(i, dim)
        {
            in >> temp;
            first.pb(temp);
        }
        REP(i, dim)
        {
            in >> temp;
            second.pb(temp);
        }

        SORT(first);
        SORT(second);
        int min = 0;
        int sum = 0;
        REP(i, dim)
            sum += first[i] * second[i];
        min = sum;

        while (next_permutation(ALL(first)))
        {
                sum = 0;
                REP(i, dim)
                    sum += first[i] * second[i];
                if (sum < min)
                    min = sum;
        }

        cout << "Case #" << h+1 << ": " << min; 

        cout << endl;
    }    
}
