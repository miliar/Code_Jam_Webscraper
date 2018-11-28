#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;


int main()
{
	
	//freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\gcj\\A-small-attempt0.in","r",stdin);
	//freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\gcj\\A-small-attempt0.out","w",stdout);

	int cas;
	cin>>cas;
	int n,k;
	for(int cs=1;cs<=cas;cs++)
	{
		cin>>n>>k;
		cout<<"Case #"<<cs<<": "<<(k==(k|((1<<n)-1))?"ON":"OFF")<<"\n";
	}
}