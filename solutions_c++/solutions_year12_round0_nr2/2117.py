#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

const int never = 0;
const int sometimes = 1;
const int always = 2;

int check_triple(int sum, int p)
{
    if(sum%3 == 1) {
	if((sum-1)/3 + 1 >= p)
	    return always;
	if((sum-4)/3 + 2 >= p && (sum-4)/3 >= 0)
	    return sometimes;
    }

    if(sum%3 == 2) {
	if((sum-2)/3 + 1 >= p)
	    return always;
	if((sum-2)/3 + 2 >= p && (sum-2)/3 >= 0)
	    return sometimes;
    }

    if(sum%3 == 0) {
	if((sum/3) >= p)
	    return always;
	if((sum-3)/3 + 2 >= p && (sum-3)/3 >= 0)
	    return sometimes;
    }

    return never;
}

int main()
{
    int t; cin >> t;

    for(int i=0;i<t;i++) {
	int n, s, p;
	int c_always = 0;
	int c_sometimes = 0;
	cin >> n >> s >> p;
	for(int j=0;j<n;j++) {
	    int sum; cin >> sum;
	    int res = check_triple(sum, p);
	    if(res == always)
		c_always++;
	    if(res == sometimes)
		c_sometimes++;
	}
	if(s < c_sometimes)
	    cout << "Case #" << i+1 << ": " << c_always + s << endl;
	else
	    cout << "Case #" << i+1 << ": " << c_always + c_sometimes << endl;
    }

    return 0;
}
