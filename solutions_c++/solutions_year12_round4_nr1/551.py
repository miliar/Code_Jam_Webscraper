// Template By Fendy Kosnatha (Seraph)
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
#include <cstring>
#include <string.h>

#define fs first
#define sc second
#define mp make_pair
#define pii pair<int, int>

using namespace std;
pii arr[10002];
int aa[10002];
int main()
{
    int tc;
    cin>>tc;
    int count=1;
    while (tc--)
    {
        memset(aa,0,sizeof(aa));
        int n,d;
        cin>>n;
        for (int i=0;i<n;i++)
            cin>>arr[i].fs>>arr[i].sc;
        cin>>d;
        sort(arr,arr+n);
        aa[0] = min(arr[0].fs, arr[0].sc);
        int bisa=0;
        for (int i=0;i<n;i++)
        {
            for (int j=i+1;j<n;j++)
            {
                if (arr[i].fs <= arr[j].fs && arr[i].fs+aa[i] >= arr[j].fs)
                {
                    aa[j] = max(aa[j], min(arr[j].sc, arr[j].fs-arr[i].fs));
                    
                }
            }
            if (aa[i]+arr[i].fs >= d){bisa=1;break;}
        }
        cout<<"Case #"<<count++<<": ";
        if (bisa==1) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
