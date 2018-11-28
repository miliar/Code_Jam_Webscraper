#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <cctype>
#include <assert.h>
#include <list>
#include <ext/hash_set>
#include <ext/hash_map>

using namespace __gnu_cxx;
using namespace std;

#define MP(a,b) make_pair(a,b)
#define i64 long long
#define pb push_back
#define For(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define Rev(i,a,b) for(typeof(a) i=(a);i>=(b);i--)
#define FOREACH(V,it) for(typeof(V.begin()) it=V.begin();it!=V.end();it++)
#define CLR(a,x) memset(a,x,sizeof(a))
#define ALL(x) x.begin(),x.end()

/**********************************************************************************/

int t;
int main(){
	scanf("%d",&t);
	int n,orig,best,num;
	int cas=1;
	char buf[100];
	while (t--){
		scanf("%s",buf);
		n=strlen(buf);
	
		vector<int> a;
		For(i,0,n)
			a.pb(buf[i]-'0');
		bool test= next_permutation(ALL(a));
		//cout << test << ' ';
		//For(i,0,a.size()) cout << a[i] << ' '; 
		if (test){
		}
		else{
			a.pb(0);
			sort(ALL(a));
			For(i,0,a.size())
				if (a[i]!=0) {
					swap(a[0],a[i]);
					break;
				}

		}
		printf("Case #%d: ",cas);
		For(i,0,a.size()) printf("%c",a[i]+'0');
		putchar(10);
		cas++;
	}
	return 0;
}
