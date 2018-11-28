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
 
using namespace std;
 
typedef long long LL;
#define PB push_back
#define all(v) (v).begin(),(v).end()
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define pii pair<int,int>
#define INF 200000000
LL gcd(LL m,LL n){LL tmp;while(n!=0){tmp=m%n;m=n;n=tmp;}return m;}   
LL lcm(LL m,LL n){return (m*n)/gcd(m,n);}
string i2s(LL n){stringstream ss;ss<<n;return ss.str();}
LL s2i(string s){stringstream ss;ss<<s;LL n;ss>>n;return n;}

vi get(int n){
	vi ret(10,0);
	while(n){
		int x=n%10;
		if(x) ret[x]++;
		n/=10;
	}
	return ret;
}
bool spl(int n){
	bool ret=1;
	int last=-1;
	while(n){
		int x=n%10;
		if(last==-1)
			last=x;
		else{	
			if(x!=last) ret=0;
		}	
		n/=10;
	}
	return ret;
}
int getspl(int n){
	vi a;
	while(n){
		a.PB(n%10);
		n/=10;
	}
	reverse(all(a));
	
	int ret;
	ret=a[0]*10;
	for(int i=1;i<a.size();i++)
		ret=(ret*10)+a[i];
	return ret;	
}
int main()
{
	int T;
	cin>>T;
	int n;
	for(int t=1;t<=T;t++){
		cin>>n;
		vi a=get(n);
		if(spl(n)){
			printf("Case #%d: %d\n",t,getspl(n));
			continue;
		}
		
		
		for(int x=n+1;;x++){
			if(get(x) == a){
				printf("Case #%d: %d\n",t,x);
				break;
			}
		}
	}
}