#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}
#define gcj_print(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

#define sqr(x) ((x)*(x))

double N;
double X[10],Y[10],R[10];

double func(void){
	if(N == 1) return R[0];
	if(N == 2) return max(R[0],R[1]);
	
	double ans = 1.0E+9;
	ans = min(ans, max(R[0], (R[1] + R[2] + sqrt(sqr(X[1] - X[2]) + sqr(Y[1] - Y[2]))) / 2.0));
	ans = min(ans, max(R[1], (R[0] + R[2] + sqrt(sqr(X[0] - X[2]) + sqr(Y[0] - Y[2]))) / 2.0));
	ans = min(ans, max(R[2], (R[1] + R[0] + sqrt(sqr(X[1] - X[0]) + sqr(Y[1] - Y[0]))) / 2.0));
	
	return ans;
}

int main(void){
	int test,T,i;
	
	cin >> T;
	REP(test,T){
		cin >> N;
		REP(i,N) cin >> X[i] >> Y[i] >> R[i];
		double ans = func();
		printf("Case #%d: %.9f\n",test+1,ans);
	}
	
	return 0;
}
