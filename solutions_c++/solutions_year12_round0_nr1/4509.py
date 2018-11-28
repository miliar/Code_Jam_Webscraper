#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <queue>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()

typedef long long ll;

int main (){
	//freopen ("A.in" , "rt" , stdin);
	//freopen("A.out" , "wt" , stdout);
	string a = "abcdefghijklmnopqrstuvwxyz";
	string b = "ynficwlbkuomxsevzpdrjgthaq";
	int tests , c=1;
	cin>>tests;
	string inp;
	getline(cin,inp);
	while(tests--)
	{
		string out = "";
		getline(cin,inp);
		for(int i=0 ; i<inp.size();i++)
		{
			int x = b.find(inp[i]);
			if(x!=-1)
				out+=a[x];
			else
				out+=" ";
		}
		cout<<"Case #"<<c<<": "<<out<<endl;
		c++;
	}
	return 0;
}
