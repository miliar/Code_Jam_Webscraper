#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
#include <list>
#include <vector>
#include <string>

using namespace std;

int main () {
    int T;
    cin >> T;
    for (int c=0; c<T; ++c)
    {
	bool used[256];
	int d=0;
	string s;
	cin >> s;
	for (int i=0; i<256; ++i) used[i]=0;
	for (string::iterator it=s.begin(); it!=s.end(); ++it)
	{
	    if (!used[*it]) { used[*it]=1; ++d;}
	}

	if (d==1) d=2;

	long sum=0;
	int val[256];
	for (int i=0; i<256; ++i) val[i]=-1;

	string::iterator it=s.begin();
	val[*it]=1;
	sum=1;
	int a=0;
	
	for (++it; it!=s.end(); ++it)
	{
	    sum*=d;
	    if (val[*it]==-1)
	    {
		val[*it]=a;
		a ? ++a : a=2;
	    }
	    sum+=val[*it];
	}

	cout << "Case #" << c+1 << ": " << sum << endl;
    }

    return 0;
}
