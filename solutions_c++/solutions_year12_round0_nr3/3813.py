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
#include <cassert>
#include <cstring>
#include <queue>
#define vvi vector<vector<int> > 
#define pii pair<int,int>
#define vpii vector<vector<pair<int,int> > > 
#define mp(a,b) make_pair(a,b)
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define sz size()
#define pb push_back
#define all(x) x.begin(),x.end()
using namespace std;
int get(int N, int A, int B)
{
    int ten = 1;
    while(ten <= N) ten *= 10;
    ten /= 10;
    int n = N;
    n = (N%10)*ten + (N/10);
    int ret = 0;
    while(n != N) {
        if (n >= A && n <= B && n > N)
            ret++;
        n = (n%10)*ten + (n/10);
    }
    return ret;
}

int main()
{
    int tc;
    cin>>tc;
    int tot = tc;
    while(tc--) {
        int A, B;
        cin>>A>>B;
        int ans = 0;
        for(int i = A; i <= B; i++) {
            ans += get(i, A, B);
        }
        cout<<"Case #"<<(tot-tc)<<": "<<ans<<endl;
    }
	return 0;
}