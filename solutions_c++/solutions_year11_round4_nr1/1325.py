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







class part{
      public:
             int a1;
             int a2;
             

bool operator<(part b)const{
if((*this).a2<b.a2)return 1;
if((*this).a2>b.a2) return 0;
return (*this).a1<b.a1;}
};








double tim=0;
double trem;
int s,r;


void func(double d, int a){
double req=d/(a+r);
if(req>trem){
tim+=d/(a+r);
trem-=d/(a+r);}
else{
tim+=trem+(d-trem*(a+r))/(a+s);
trem=0;}
}









//ll memo[
//ll A[
void solveTest(int test){
//memset(memo,0,sizeof(memo));
//memset(A,0,sizeof(A));
tim=0;
int n,x,tr;
scanf("%d %d %d %d %d\n", &x,&s,&r,&tr,&n);
trem=tr;
//double u=1;u=u/1000;u=u/1000;u=u/1000;u=u/1000;
//printf("%.14lf\n",u);

int last=0;
int b,e,w;
part temp;
vector<part> data;



rep(e1,0,n){
scanf("%d %d %d\n",&b,&e,&w);
if(last<b){
temp.a1=b-last;
temp.a2=0;
data.pb(temp);}
temp.a1=e-b;
temp.a2=w;
data.pb(temp);
last=e;}
if(last<x){
temp.a1=x-last;
temp.a2=0;
data.pb(temp);}
sort(data.B,data.E);

//cout<<trem<<endl;


rep(e1,0,s(data)){
temp=data[e1];
double d=temp.a1;
int a=temp.a2;
double req=d/(a+r);
//cout<<"req     "<<req<<endl;
if(req<trem){
tim+=d/(a+r);
trem-=d/(a+r);}
else{
tim+=trem+(d-trem*(a+r))/(a+s);
trem=0;}
//cout<<tim<<endl;
//cout<<trem<<endl;
}










//int ans=recur(0,v);

//if(ans==lim)goto printerr;

printans:;
printf("Case #%d: %lf\n",test,tim);
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
