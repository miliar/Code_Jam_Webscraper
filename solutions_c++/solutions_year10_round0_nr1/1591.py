#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int nCasos;
	cin>>nCasos;

	for(int caso=1; caso<=nCasos; caso++)
	{
		int n, k;
		cin>>n>>k;

		cout<<"Case #"<<caso<<": ";
		if((k%(1<<n)) == (1<<n)-1) cout<<"ON"<<endl;
		else cout<<"OFF"<<endl;
	}
	
	return 0;
}
