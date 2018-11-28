#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <sstream>

#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)


int main(int argc , char * argv[])
{
    if (argc >1)
    {
	freopen(argv[1], "r", stdin);
    }
    else
	freopen("input.in", "r", stdin);
    /*    freopen("A-small-attempt0.out", "w", stdout);*/
    int tt, tn;
    cin >> tn;
    
    for (tt = 0 ; tt < tn ; tt ++)
    {
	int p , k , l;
	cin >>p ;
	cin >> k;
	cin >> l;
	vector<int> lt;
	int time = 1;
	int k1 =0;
	long  ans = 0;
	bool flag = true;
	
	for (int i = 0 ; i < l ; i ++)
	{
	    int lttemp;
	    cin >> lttemp;
// 	    cout << i << " :" << lttemp << endl ;
	    lt.push_back(lttemp);
	}
	sort(lt.begin(), lt.end(), greater<int>() );
	time = 1;
	k1 =0;
	ans = 0;
	flag = true;
	for (int i = 0 ; i < l;i ++)
	{
	    k1 ++;
// 	    cout << lt[i] << "*"<<time <<endl;
	    ans = ans + lt[i] * time;
	    if (k1 == k)
	    {
		k1 = 0;
		time ++;
/*		if (time > p)
		{
		    flag = false;
		    break;
		}*/
	    }
	}
	if (flag)
	    cout << "Case #" << tt+1 << ": "<<ans << endl;
	else
	    cout << "Impossible" << endl;
    }
    return 0;
}
