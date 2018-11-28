#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>
#include <numeric>
#include <bitset>
#include <stack>
#include <queue>
#include <set>
#include <fstream>
#include <string>
#include <string.h>
using namespace std;

#define zmax(a,b) (((a)>(b))?(a):(b))
#define zmin(a,b) (((a)>(b))?(b):(a))
#define zabs(a) (((a)>=0)?(a):(-(a)))

typedef vector<int> VI;
typedef vector< vector<int> > VII;
typedef vector<string> VS;
#define MOD 1000000007

int M[26] = {24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
int main()
{
    int t;
    int i,j;
    string s1;
    cin >> t;
    getline(cin, s1);

    for (i = 0; i<t; i++) {
        getline(cin,s1);

        for (j = 0; j<s1.size(); j++) {
            if (s1[j]>='a' && s1[j]<='z') {
                s1[j] = M[s1[j]-'a']+'a';
            }
         }
         cout << "Case #" << i+1<<": " << s1 << endl;
    }
    return 0;
}

