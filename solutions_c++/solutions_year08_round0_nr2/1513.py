#include <string>      
#include <stack>      
#include <vector>      
#include <cmath>      
#include <queue>      
#include <set>      
#include <map>      
#include <algorithm>      
#include <iostream>      
#include <cstdio>      
#include <sstream>      
#include <utility>      
#pragma comment (linker, "/STACK:1000000000")      
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)      
#define forv(i, v) for (int i = 0; i < (int)(v.size()); ++i)      
#define fors(i, s) for (int i = 0; i < (int)(s.length()); ++i)      
#define all(a) a.begin(), a.end()      
#define pb push_back      
#define PII pair<int, int>      
#define mp make_pair      
#define VI vector<int>      
#define VS vector<string>      
#define eps 1e-5      
#define inf 1e10      
#define PI 3.1415926535897932384626433832795      
#define cube(a) (a)*(a)*(a)      
#define base 10000;      

using namespace std;      

int j,res1,res2,asd,trya,f,cases,casenum,t,na,nb,i;
string ss;
int a1[1001];
int b1[1001];
int a2[1001];
int b2[1001];


void fff(int a,int b)
{int iii,a5,b5,a4,b4;
int a3[15000+10],b3[15000+10];
memset(a3,0,sizeof(a3));memset(b3,0,sizeof(a3));
a4=a;b4=b;a5=1;b5=1;
forn(iii,1440){
a4+=a3[iii];
b4+=b3[iii];
while (a5<=na&&a1[a5]==iii){
if (a4<=0){f=1;return;}
a4--;b3[a2[a5]+t]++;++a5;
}

while ( (b5<=nb) && (b1[b5]==iii) ){
if (b4<=0){f=1;return;}--b4;++a3[b2[b5]+t];++b5;
}
if (a5>na&&b5>nb)break;
}
}

int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
cin >> cases;
forn (qqq,cases){
cin >> t >> na >> nb;  
for (int i=1;i<=na;++i){
string s1,s2;
cin >> s1 >> s2;
a1[i]=((s1[0]-'0')*10+s1[1]-'0')*60+(s1[3]-'0')*10+s1[4]-'0';
a2[i]=((s2[0]-'0')*10+s2[1]-'0')*60+(s2[3]-'0')*10+s2[4]-'0';
}
for (int i=2;i<=na;++i){
int j=i;
while (j>1&&a1[j]<a1[j-1]){
swap(a1[j],a1[j-1]);swap(a2[j],a2[j-1]);--j;
}}
forn(i,nb){
string s1,s2;
cin >> s1 >> s2;
b1[i]=((s1[0]-'0')*10+s1[1]-'0')*60+(s1[3]-'0')*10+s1[4]-'0';
b2[i]=((s2[0]-'0')*10+s2[1]-'0')*60+(s2[3]-'0')*10+s2[4]-'0';
}
for (int i=2;i<=na;++i){
int j=i;
while (j&&b1[j]<b1[j-1]){
swap(b1[j],b1[j-1]);swap(b2[j],b2[j-1]);--j;
}}
res1=res2=1000;  
forn(asd,na+nb+10){
forn(trya,asd+1){
f=0;fff(trya,asd-trya);
if (f==0){res1=trya;res2=asd-trya;break;}
}if (res1<1000)break;
}cout << "Case #" << qqq << ": " << res1<<" "<<res2 << endl;
}
return 0;
}