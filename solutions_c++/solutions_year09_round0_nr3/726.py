#include <iostream>
#include <string>
#include <cstdio>
#include <cassert>
using namespace std;
string x, y = "welcome to code jam";
int table[500][2];
int count()
{
    assert(y.size() == 19);
    for (size_t i=0; i<x.size(); ++i)
	table[i][0] = 1;
    for (int i=0; i<19; ++i) {
	for (size_t j=0; j<x.size(); ++j) {
	    table[j][(i+1)%2] = j ? table[j-1][(i+1)%2] : 0;
	    if (y[i] == x[j])
		table[j][(i+1)%2] += table[j][i%2];
	    table[j][(i+1)%2] %= 10000;
	}
    }
    return table[x.size()-1][y.size()%2];
}
int main()
{    
    int N;
    cin >> N; getline(cin, x);
    for (int t = 0; t<N; ++t) {
	getline(cin, x);
	printf("Case #%d: %04d\n", t+1, count());
    }
}

