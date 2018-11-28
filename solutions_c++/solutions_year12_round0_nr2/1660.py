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
int arr[200];
int main()
{
    int tc;
    cin>>tc;
    int count=1;
    while (tc--)
    {
        int ans=0;
        int n,s,p;
        cin>>n>>s>>p;
        for (int i=0;i<n;i++)
            cin>>arr[i];
        for (int i=0;i<n;i++)
        {
            int bisa=0;
            int notSur=0;
            int sur=0;
            for (int j=0;j<=10;j++)
                for (int k=j;k<=j+2 && k<=10;k++)
                    for (int l=k;l<=j+2 && l<=10;l++)
                    {
                        if (j+k+l==arr[i] && l>=p)
                        {
                            bisa=1;
                            if (l-j<2) notSur=1;
                            else sur=1;
                        }
                    }
            if (notSur==1) ans++;
            else if (notSur==0 && sur==1 && s>0) {ans++;s--;}
        }
        cout<<"Case #"<<count++<<": "<<ans<<endl;
    }
    return 0;
}
