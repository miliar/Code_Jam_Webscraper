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

//create large input self

#define lim 55
char buff[lim];
string scanstr(){
cin.getline(buff,lim);
//fprintf(stderr,"%s\n",buff);
return string(buff);
}
int N,D;
int points[10000],dist[10000],length[10000];

//ll memo[
//ll A[
void solveTest(int test){
//memset(memo,0,sizeof(memo));
//memset(A,0,sizeof(A));
//fill levels

rep(e1,0,10000){
points[e1]=0;}
scanf("%d\n", &N);
rep(e1,0,N){
scanf("%d %d\n", &dist[e1], &length[e1]);}
scanf("%d",&D);
points[0]=dist[0];
rep(e1,0,N){
rep(e2,e1+1,N){
if(dist[e2]-dist[e1]<=points[e1]) {points[e2]=max(points[e2],min(length[e2],dist[e2]-dist[e1]));}
else break;}}



bool reached=0;
rep(e1,0,N){
if(points[e1]+dist[e1]>=D) {reached=1;break;}}



printans:;
if (reached)
printf("Case #%d: YES\n",test);
else
printf("Case #%d: NO\n",test);
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
