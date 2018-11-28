/*
C
Author: WANG Yuanjie
*/
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
typedef long long ll;
typedef long double ld;
#define sz(x) ((int)(x).size())


int main()
{
	freopen("C.in","rt",stdin);
	freopen("C.out","wt",stdout);
	int T;
	scanf("%d",&T);
	int m,n;
	char c;

	for (int ii = 0; ii < T; ++ii) {
	    scanf("%d",&m);
        scanf("%d",&n);    
        printf("Case #%d: ",ii+1);
		int count = 0, i=0;
		string strM,strN,strTMP,str,front,rear;
		stringstream ssM,ssN,ssTMP,ss;
		ssM << m;
		ssM >> strM;
		ssN << n;
		ssN >> strN;
		for (int jj = m; jj <= n; ++jj) {
			ssTMP << jj;
			ssTMP >> strTMP;
			int len=strTMP.length();
			int lasti=0;
			for (int kk = 1; kk <len; ++kk) {
			    front=strTMP.substr(0,kk);
			    rear=strTMP.substr(kk,len-kk);
			    rear += front;
                ss << rear;
                ss >> i;
                if (lasti==i) break;
                ss.clear();
			    ss.str();
			    if (i>jj && i<=n) {
                   count++;
                   lasti=i;
                }
		    }
		    ssTMP.clear();
		    ssTMP.str();
		}
		printf("%d\n",count);
	}
	return 0;
}
