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
#define vi vector<long long>
#define rep(a,b,c) for(long long(a)=(b);(a)<(c);(a)++)
#define repd(a,b,c) for(long long(a)=(b);(a)>=(c);(a)--)
#define ll long long
#define ld long double




vector<string> token(string start,char a)
{
        vector<string> splitted;
        while(s(start)!=0)
        {
             size_t k= start.find(a,0);
             if(k==string :: npos)
               {  
                   splitted.push_back(start);
                   start="";
                   break;
               }               
             string temp(start.begin(),start.begin()+k); 
             if(s(temp)>0)      
               splitted.push_back(temp);
             start.erase(0,k+1);       
       }
       return splitted;
}

long long atoll(string k){                          
long long ans=0;                              
for(int i=0;i<s(k);i++){
ans=ans*10+k[i]-'0';
}
return ans;
}




ll data[2000009];//....................................................clean data
ll d,n;



/*
ll move(ll moved,ll last,ll tim,ll d){//........................................tc of -ve and +ve
if(moved==0)return data[moved]-tim;
if(last+d>data[moved]+tim)return 0;//..............................tc of this
return max(last+d,data[moved]-tim);}

*/

bool check(ll tim){
ll last=data[0]-tim;
rep(e1,1,n){
if(last+d>data[e1]+tim)return 0;//..............................tc of this
last=max(last+d,data[e1]-tim);}
return 1;}

#define TYP1 long long 

//returns last zero if one is absent
//make sure low<=high
TYP1 find_first_one(TYP1 low,TYP1 high){
while(low < high) {
  TYP1 m = (low>>1)+(high>>1)+((low&1)&&(high&1));
  if(check(m)) high = m; else low = m+1;
  }
return low;
}








//long long
//clean global data
//convert to array
//case of floating points
//0 case check












//ll memo[
//ll A[
void solveTest(int t){
//memset(memo,0,sizeof(memo));
//memset(A,0,sizeof(A));
ll c,p,v;
n=0;
ll ans;
	scanf("%lld %lld\n",&c,&d);
	rep(e1,0,c){
	scanf("%lld %lld\n",&p,&v);
	rep(e2,0,v){
	data[n+e2]=p*2;}
	n+=v;}
d*=2;
ans=find_first_one(0,1000000000000000ll);
	










printf("Case #%d: %lld",t,ans/2);
if(ans%2==0){
printf(".0\n");}
else{
printf(".5\n");}


}

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
