#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <list>
#include <bitset>
#include <complex>
#include <list>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define pb push_back
#define SIZE(x) ((int)(x.size()))
#define LENGTH(x) ((int)(x.length()))
#define PI 3.14159265358979323846264338327950288

typedef long long ll;
typedef unsigned long long ull;

int digit[40];
int T,smallest;

int main(){
	cin>>T;
	for (int testcase=1; testcase<=T; ++testcase) {
		smallest=1000010;
		ull res=0;
		memset(digit,0,sizeof(digit));
		int N;
		cin>>N;
		for (int i=0; i<N; ++i) {
			int tmp;
			cin>>tmp;
			res+=tmp;
			if (tmp<smallest)smallest=tmp;
			int j=0;
			while (tmp) {
				digit[j]+=(tmp&1);
				tmp>>=1;
				j++;
			}
		}
		
		bool odd=false;
		for (int j=0; j<40; ++j) {
			if ( digit[j]%2 ){
				odd=true;
				break;
			}
		}
		
		cout<<"Case #"<<testcase<<": ";
		if (odd) cout<<"NO"<<endl;
		else cout<<res-smallest<<endl;
	}
	return 0;
}
