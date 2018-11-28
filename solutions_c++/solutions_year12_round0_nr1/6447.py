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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

char jum[][200] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
				"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
				"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

char original[][200] = {"our language is impossible to understand",
					"there are twenty six factorial possibilities",
					"so it is okay if you want to just give up"};

char cmap[26];


int main() {
	freopen("c:/gc/data/A-small-attempt6.in", "r", stdin);
	freopen("c:/gc/data/a.out", "w", stdout);

	for(int i=0;i<3;i++) {
		for(int j=0;jum[i][j] != '\0';j++) {
			cmap[jum[i][j]-'a']= original[i][j];
		}
	}
	cmap['z'-'a']='z';
	cmap['q'-'a']='q';

	cmap['z'-'a']='q';
	cmap['q'-'a']='z';
	int t;
	cin>>t;
	char a[202];
	fgets(a,200,stdin);
	for(int i=3;i<t+3;i++) {
		fgets(a,200,stdin);
		cout<<"Case #"<<i-2<<": ";
		for(int i=0; a[i]!= 10;i++){
			if ( a[i] >='a' && a[i] <='z')
			cout<<cmap[a[i]-'a'];
			else cout<<a[i];
		}
		cout<<endl;
	}
}
