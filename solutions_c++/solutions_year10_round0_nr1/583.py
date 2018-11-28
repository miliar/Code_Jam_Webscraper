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
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

#define ME(s) memset((s), 0, sizeof((s)))
#define MM(s,a) memset((s),(a),sizeof((s)))
#define MCP(s,a) memcpy((s), (a), sizeof(s))
#define LL long long
#define LD long double
#define PII pair<int, int>
#define PDD pair<double, double>
#define mkp(a,b) make_pair((a),(b))
#define y first
#define x second
#define sqr(a) ((a)*(a))
#define lowbit ((x)&(-(x)))
#define two(x) (1<<(x))
#define contain(mask,x) ((mask&two(x))!=0) 


int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int Test;
	cin >> Test ;
	int c=0,N,K;
	while(Test--){
		printf("Case #%d: ",++c);
		cin >> K >> N;
		int flag=1;
		for(int i=0;i<K;i++){
			flag&=N&1;
			N>>=1;
		}
		if(flag)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
	return 0;
}



