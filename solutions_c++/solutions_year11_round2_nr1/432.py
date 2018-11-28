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



























#define lim 200
char buff[lim];
string scanstr(){
cin.getline(buff,lim);
//fprintf(stderr,"%s\n",buff);
return string(buff);
}


double memo[105][105];//wp of a wrt b
double wp[105],owp[105],oowp[105];

void solveTest(int t){
memset(memo,0,sizeof(memo));
memset(wp,0,sizeof(wp));
memset(owp,0,sizeof(owp));
memset(oowp,0,sizeof(oowp));
//memset(A,0,sizeof(A));
int n;
scanf("%d\n",&n);
string str;
vector<string> data;
rep(e1,0,n){
str=scanstr();
data.pb(str);}

double won,tot;

rep(e1,0,n){
rep(e2,0,n){
if(e2==e1)continue;//........................tc
tot=0;won=0;
rep(e3,0,n){
if(e3==e1||e3==e2)continue;
if(data[e2][e3]=='1'){//owpt[e2]++;owpw[e2]++;
tot++;won++;
}
else if(data[e2][e3]=='0'){//owpt[e2]++;
tot++;
}
}
memo[e1][e2]=won/tot;
}}


rep(e1,0,n){
tot=0;won=0;
rep(e2,0,n){
if(data[e1][e2]=='1'){//owpt[e2]++;owpw[e2]++;
tot++;won++;
}
else if(data[e1][e2]=='0'){//owpt[e2]++;
tot++;
}
}
wp[e1]=won/tot;
}


rep(e1,0,n){
tot=0;won=0;
rep(e2,0,n){
if(e2==e1)continue;
if(data[e1][e2]!='.'){
won+=memo[e1][e2];
tot++;
}}
owp[e1]=won/tot;
}

rep(e1,0,n){
tot=0;won=0;
rep(e2,0,n){
if(e2==e1)continue;
if(data[e1][e2]!='.'){
won+=owp[e2];
tot++;
}}
oowp[e1]=won/tot;
}






double ans;




printf("Case #%d:\n",t);
rep(e1,0,n){
ans=wp[e1]/4+owp[e1]/2+oowp[e1]/4;
printf("%lf\n",ans);
}
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
