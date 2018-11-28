#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
//---------- macros ----------
#define fp(i,a,b) for(long i=a; i<b; i++)
#define fm(i,a,b) for(long i=a; i>b; i--)

using namespace std;

int t, n;  long D; int _case;
vector <long> d,l; 
bool isreachable( long x, int ind, long cl)
{
    //cout << x <<" "<< ind <<" " << x+cl  << endl; 
    if(x+cl >= D) return true;
    if(ind>=n) return false;
    int i=ind+1; long temp;
    while(i <n && d[i] <= x+cl)
    {
        temp = min(d[i]-d[ind], l[i]);
        if(isreachable(d[i], i, temp  )) return true;
        i++;
    }
    return false;
}

int main()
{
    _case=1;
	
    cin >> t;
    while(_case<=t)
    {
        cin >> n;
        d.resize(n); l.resize(n);
        fp(i,0,n) cin >> d[i] >> l[i];
        cin>> D;
        
        
        cout <<"Case #"<< _case <<": ";
        if(isreachable(d[0], 0, d[0]))
           cout << "YES" << endl;
        else
           cout << "NO" << endl;
        _case++;
    }
	return 0;
}
