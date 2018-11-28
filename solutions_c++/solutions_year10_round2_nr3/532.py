#include <vector>
#include <list>
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
using namespace std;
#define dump(x) cerr <<  __LINE__ << " : "<< #x << "  =  " << (x) <<endl;
#define CL(a,x) memset(a,x,sizeof(a))
#define Pb push_back
#define Mp(A,B) make_pair(A,B)
#define SZ(v) ((int)(v).size())
#define LEN(X) ((int)X.length())
//遍历 
#define BEND(v) v.begin(),v.end()
#define FR(i,a,b) for(int i=(a);i<(b);++i)//[a,b)
#define FOR(i,n) FR(i,0,n)//[0,n)
#define FORALL(i,v) FOR(i,(int)v.size())//[0,v.size()) 
#define FORSZ(i,a,v) FR(i,a,SZ(v))//[a,v.size())
#define FRE(i,a,b) for(int i=(a);i<=(b);++i)//[a,b]
#define FORE(i,n) FRE(i,1,n)//[1,n]
#define FOREACH(i,v) for(typeof(v.end())i=v.begin();i!=v.end();++i)
//反向遍历  
#define RF(i,a,b) for(int i=(a)-1;i>=(b);--i)//[b,a)
#define ROF(i,n) RF(i,n,0)//[0,n)
#define RFE(i,a,b) for(int i=(a);i>=(b);--i)//[b,a]
#define ROFE(i,n) RFE(i,1,0)//[1,n]
#define ROFALL(i,v) ROF(i,(int)v.size())//[0,v.size()) 
#define ROFSZ(i,a,v) RF(i,SZ(v),a)//[a,v.size())
#define ROFEACH(i,v) for(typeof(v.rend())i=v.rbegin();i!=v.rend();++i)
const double Pi=acos(-1.0);
const double eps=1e-11;
typedef pair<int,int> pi;
template <class T> void out(T A[],int n){for (int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
template <class T> void out (vector<T> A,int n=-1){if(n==-1) n=A.size();for (int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
int toInt(string s){istringstream sin(s);int t; sin>>t; return t;}
string toString (int v){ostringstream sout;sout<<v; return sout.str();}
#define printg case_number++, printf("Case #%d: ",case_number), printf
#define gout  printf("Case #%d: ",cs), cout
int l[30];
void init(){
l[2]=1;
l[3]=2;
l[4]=3;
l[5]=5;
l[6]=8;
l[7]=14;
l[8]=24;
l[9]=43;
l[10]=77;
l[11]=140;
l[12]=256;
l[13]=472;
l[14]=874;
l[15]=1628;
l[16]=3045;
l[17]=5719;
l[18]=10780;
l[19]=20388;
l[20]=38674;
l[21]=73562;
l[22]=140268;
l[23]=268066;
l[24]=513350;
l[25]=984911;
}
int main() 
{
    init();
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T,n;
    cin>>T;
    for(int cs=1;cs<=T;cs++){
        cin>>n;
        gout<<l[n]%100003<<endl;
    }

	return 0;	
}
