//$CWD$\a.exe input >> output

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
#include <cstring>
#include <cctype>
#include <complex>
#include <cassert>
#include <string>
#include <valarray>
#include <queue>
#include <iterator>
using namespace std;
#define pb push_back
#define B begin()
#define E end()
#define s(a) ((long long)a.size())
#define vs vector<string>
#define vi vector<int>
#define vvi vector<vi>
#define vll vector<long long>
#define vvll vector<vll>
#define vd vector<double>
#define vvd vector<vd>
#define rep(a,b,c) for(long long(a)=(b);(a)<(c);(a)++)
#define repd(a,b,c) for(long long(a)=(b);(a)>=(c);(a)--)
#define ll long long




ll memo[2000001];
//ll A[
void solveTest(int test){
memset(memo,0,sizeof(memo));
//memset(A,0,sizeof(A));
int a,b,ans=0;
scanf("%d\n", &a);
scanf("%d\n", &b);
int ord=1,sz=0;
int x=a,coun;
while(x>0){ord*=10;x/=10;sz++;}
ord/=10;
//string str = scanstr();

rep(e1,a,b+1){
    if(memo[e1]) continue;
    x = e1;
    coun=0;
rep(e2,0,sz){
    if(a<=x&&x<=b) {if(memo[x]!=1)coun++;memo[x]=1;}
    x = x/10 + (x%10)*ord;
}
ans += (coun*(coun-1))/2;
}










printans:;
printf("Case #%d: %d\n",test,ans);
return;
printerr:;
printf("Case #%d: IMPOSSIBLE\n",test);//......................check if different case is not required i.e. Impossible
return;}


int main(int argc, char **argv)
{
    if(argc!=2){printf("usage: %s input_file\n", argv[0]);exit (1);}freopen(argv[1], "r", stdin);
	int T, t;
	scanf("%d\n", &T);
	rep(t, 1, T+1){
		//fprintf(stderr, "Solving %d/%d\n", t, T);
		solveTest(t);}
	return 0;
};
