#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <algorithm>
#include <iomanip>


using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out_a.txt","w",stdout);
    long long a[33];
    a[1] = 1;
    for (int i = 2 ;i <= 32 ;i++){
        a[i] = 2 * a[i-1] + 1;
      //  cout << a[i] << endl;
    }
    int ca;
    cin >> ca ;
    long long k;
    for (int t = 0 ;t < ca ;t++){
        int n,k;
        cin >> n >> k;
        bool xx = ((k % (a[n]+1)) == a[n]);
        cout << "Case #" << t+1 <<": " << (xx?"ON":"OFF") << endl;
    }
   // while (1);
}


