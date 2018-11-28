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
#include <queue>

#include <fstream>
using namespace std;
#define all(x) (x).begin(),(x).end()

#define vs vector <string>
#define vi vector <int>
#define vvi vector < vi >
#define p(X) push_back((X))

#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
#define fire(i,j,n) for(int (i)=(j);(i)<=(n);(i)++)
#define firr(i,j,n) for(int (i)=(j);(i)>(n);(i)--)
#define firre(i,j,n) for(int (i)=(j);(i)>=(n);(i)--)
#define tr(v,it) for(typeof(v.begin()) it=v.begin();it!=v.end();it++)

#define srt(v) sort((v).begin(),(v).end())
#define srtc(v) sort(v.begin(),v.end(),cmp)

#define _bc(i) __builtin_popcount(i)
#define INF 0x3f3f3f3f
#define ipow(a,b) (int)pow((double)a,(double)b)
#define fill(a,b) memset(a,b,sizeof(a))
#define maxr(num,a,b) max_element(num.begin()+a,num.begin()+b);
#define minr(num,a,b) min_element(num.begin()+a,num.begin()++b)
#define maxi(v) max_element(all(v))
#define mini(v) min_element(all(v))


string lower(string s) {for(int i=0;i<s.size();i++) s[i]=tolower(s[i]);return s;}
vector<string> sep(string s,char c) { string temp;vector<string> res;for(int i=0;i<s.size();i++) { if (s[i]==c) {if (temp!="") res.push_back(temp);temp="";continue;}temp=temp+s[i];}if (temp!="") res.push_back(temp);return res;}
int toint(string s) { stringstream s1(s);int n;s1>>n;return n;}
string tostr(int n) {stringstream s;s<<n;return s.str();}
string trim(string s)
{
int p=0;
while(s[p]==' ')
{
p++;
}
s.erase(0,p);
p=s.size()-1;
while(s[p]==' ')
{
p--;
}
s.erase(p+1,s.size()-p-1);
return s;
}
template<class T> void D(T A[],int n) {for(int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
template<class T> void D(vector<T> A,int n=-1) {if (n==-1) n=A.size();for(int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
#define cin fin
#define cout fout
int P[1000];
int rank[1000];
void make_set(int s)
{
P[s]=s;
rank[s]=0;
}
int find_set(int s)
{
if (P[s]!=s)
P[s]=find_set(P[s]);
return P[s];
}
void un_set(int u,int v)
{
int p1=find_set(u);
int p2=find_set(v);
if (p1==p2)
return;
if (rank[p1]<rank[p2])
{
P[p1]=p2;
rank[p2]++;
}
else
{
P[p2]=p1;
rank[p1]++;
}
}
bool prime[100000];
void gen_prime(int n)
{
int m=ceil(sqrt(n));
memset(prime,1,sizeof(prime));
prime[0]=false;
prime[1]=false;
fire(i,2,m)
{
if (prime[i])
for(int k=i*i;k<=n;k+=i)
{
prime[k]=false;
}
}
}
int main() {
ios_base::sync_with_stdio(false);
ofstream fout ("test.out");
ifstream fin ("test.in");
int tc;
cin>>tc;
gen_prime(1001);
vi prim;fir(i,0,1001) if (prime[i]) prim.p(i);
int cas=0;
while(tc--)
{
cas++;
int a,b,sp;
cin>>a>>b>>sp;
vector<vector<int> > pf(b+1);
fire(i,a,b)
{
int t=i;
fir(j,0,prim.size())
{
if (prim[j]>t) break;
if (t%prim[j]==0)
{
if (prim[j]>=sp)
pf[i].p(prim[j]);
while(t%prim[j]==0) t/=prim[j];
}
}
if (t!=1)
if (t>=sp)
pf[i].p(t);
}
fire(i,a,b) make_set(i);
while(1)
{
bool af=false;
fire(i,a,b)
fire(j,i+1,b)
if (find_set(i)!=find_set(j))
{
fir(k,0,pf[i].size())
{
if (find(all(pf[j]),pf[i][k])!=pf[j].end())
{
un_set(i,j);
af=true;
break;
}
}
}
if (!af) break;
}
bool memo[1001];memset(memo,0,sizeof(memo));
fire(i,a,b)
memo[find_set(i)]=1;
int cnt=0;
fire(i,a,b)
{
if (memo[i]) cnt++;
}
cout<<"Case #"<<cas<<": "<<cnt<<endl;
}
return 0;
}
