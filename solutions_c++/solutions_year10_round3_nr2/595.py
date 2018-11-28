//#include <cstdlib>
//#include <cctype>
//#include <cstring>
//#include <cstdio>
//#include <cmath>
//#include <algorithm>
//#include <vector>
//#include <string>
//#include <iostream>
//#include <sstream>
//#include <map>
//#include <set>
//#include <queue>
//#include <stack>
//#include <fstream>
//#include <numeric>
//#include <iomanip>
//#include <bitset>
//#include <list>
//#include <stdexcept>
//#include <functional>
//#include <utility>
//#include <ctime>
//using namespace std;
//
//int T, CT=1, L, P, C;
//int main() {
//	//freopen("B-small-attempt0.in","r",stdin);
//    //freopen("B-small-attempt0.out","w",stdout);
//	//scanf("%d", &T);
//	cin>>T;
//	while(T--) {
//		scanf("%d %d %d", &L, &P, &C);
//
//		int ans = 0;
//		int TT = C;
//		while(L * C < P) {
//			L *= TT;
//			TT *= C;
//			++ans;
//		}
//		printf("Case #%d: %d\n", CT++, ans);
//
//	}
//	return 0;
//}


#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define maxSize 10003
#define LL long long
long long l,p;
int c;

long long deal(long long a,long long b)
{
	long long ans = 1;
	for(long i=0;i<b;i++)
		ans *= a ;
	return ans;
}
void getAC()
{
    //C^i * l >= p£¬Çólogi
    int i=1;
    while(1)
    {
       long long  tmp = deal(c,i);
        if(tmp*l>=p)
            break;
		i++;
    }
	long res = (long)(ceil(log(i*1.0)/log(2*1.0)));
    cout<<res<<endl;
	return ;
}
int main()
{
	freopen("B-small-attempt3.in","r",stdin);
    freopen("B-small-attempt3.out","w",stdout);
	int t;
	cin >> t;
	for(int cases=1;cases<=t;cases++)
	{
		cin >> l >> p >>c;
		printf("Case #%d: ",cases);
		getAC();
	}
	return 0;
}
