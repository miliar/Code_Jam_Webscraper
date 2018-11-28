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

stringstream ss;
string str;
long long  ans;

bool ugly(long long v)
{
    if  (v % 2 && v %3 && v %5 && v %7)
	return false;
    else
	return true;
}

void deal(long long i ,long long v , long long s , long long f)
{
    long long t = f *(str[i]-'0') + v * 10;
    if (i == (str.size() - 1))
    {
	s += t;
	if (ugly(s))
	    ans ++;
	return ;
    }
    deal(i + 1, 0 ,t + s, 1 );
    deal(i + 1, 0 , t + s , -1);
    deal(i + 1, t , s , f);
}


int main(int argc , char * argv[])
{
    if (argc >1)
    {
	freopen(argv[1], "r", stdin);
    }
    else
	freopen("input.in", "r", stdin);
    /*    freopen("A-small-attempt0.out", "w", stdout);*/
    long long tt, tn;
    cin >> tn;
    for (tt = 0 ; tt < tn ; tt ++)
    {
	ans = 0;
	cin >>str;
	deal(0, 0 , 0, 1);
	cout << "Case #" << tt+1 << ": "<<ans << endl;
    }
    return 0;
}
