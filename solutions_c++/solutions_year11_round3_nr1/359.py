#include <algorithm> 
#include <bitset> 
#include <cctype> 
#include <cmath> 
#include <cmath> 
#include <cstdio> 
#include <cstdio> 
#include <cstdlib> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <utility> 
#include <vector> 

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define rep(i,s,n) for(int i=s; i<n; i++)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define getint(c) (int)(c - 'a')

using namespace std;

int main()
{
    int T;
    cin>>T;
    char a[55][55];
    for(int t = 0; t < T; t++)
    {
        cout<<"Case #"<<t+1<<":"<<endl;
        int R, C;
        cin>>R>>C;
        rep(i,0,R) rep(j,0,C) cin>>a[i][j];

        rep(i,0,R-1) rep(j,0,C-1)
        {
            if(a[i][j] == '#' && a[i+1][j] == '#' && a[i][j+1] == '#' && a[i+1][j+1] == '#')
            {
                a[i][j] = '/';
                a[i][j+1] = '\\';
                a[i+1][j] = '\\';
                a[i+1][j+1] = '/';
            }
        }
        bool done = true;
        rep(i,0,R) rep(j,0,C) if(a[i][j] == '#') done = false;
        if(!done)
            cout<<"Impossible"<<endl;
        else
        {
            rep(i,0,R)
            {
                rep(j,0,C)
                    cout<<a[i][j];
                cout<<endl;
            }
        }
    }
}

