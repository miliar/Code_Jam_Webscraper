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
#include <cstring>
#include <cstdlib>
#include <ctime>
 
#define SZ(a) (int)(a).size()
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define INF (int)1e9
 
#define ll long long
#define vi vector<int>
#define vs vector<string>
 
using namespace std;

int main()
{
    int T;
    cin >> T;
    
    for(int cas = 1; cas <= T; cas++)
    {
            int N;
            cin >> N;
            
            vector <int> A(N), B(N);
            
            for(int i = 0; i < N; i++)
                    cin >> A[i] >> B[i];
                    
            int cnt = 0;
            for(int i = 0; i < N; i++)
                    for(int j = i + 1; j < N; j++)
                    {
                            if((A[i] < A[j] && B[i] > B[j]) || (A[i] > A[j] && B[i] < B[j]))
                                     cnt++;
                    }
            
            cout << "Case #" << cas << ": " << cnt << endl;
    }
    return 0;
}
