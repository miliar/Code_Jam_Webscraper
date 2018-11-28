#include <iostream>
#include <fstream>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>

double E=1e-9;
using namespace std;

long long mabs(long long x)
{
	if (x>0)
		return x;
	else return -x;
}

int main()
{
	//freopen ("input.txt", "r", stdin);
    //freopen ("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int j=0;j<t;++j)
	{
		string res="", in, x="yhesocvxduiglbkrztnwjpfmaq";
		char a;

		while(1)
		{
			scanf("%c", &a);
			if (a!='\n' && a!='\0')
				break;
		}

		while(1)
		{
			in.push_back(a);
			if (scanf("%c", &a)==EOF)
				break;
			if (a =='\n' || a =='\0')
				break;
		}

		for (int i=0;i<in.size();++i)
			if (in[i]!=' ')
				res.push_back(x[in[i]-'a']);
			else res.push_back(' ');

		printf("Case #%d: ", j+1);
		cout << res << endl;
	}
    return 0;
}