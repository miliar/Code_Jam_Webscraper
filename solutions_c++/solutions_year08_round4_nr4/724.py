#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ext/hash_map>
#include <ext/hash_set>
#define F(i,a,b) for(int i=(a);i<(b);++i)
#define Fe(it,v)for(__typeof__((v).begin()) it=(v).begin();it!=(v).end();++it)
#define all(x) (x).begin(),(x).end()
using namespace std;
using namespace __gnu_cxx;
int n;
int f(string &s,int x){
	if(x==n)return 0;
	int i=x;
	while(i<n&&s[i]==s[x])i++;
	return 1+f(s,i);
}
int main(){
	int N;
	int test=1;
	cin>>N;
	while(N--){
		int k;
		string s;
		cin>>k>>s;
		int arr[5]={0,1,2,3,4};
		n=s.length();
		int ret=10000;
		do{
			string t="";
			for(int i=0;i<n;i+=k){
				for(int j=0;j<k;++j){
					t+=s[i+arr[j]];
				}
			}
			ret=min(ret,f(t,0));
		}
		while(next_permutation(arr,arr+k));
		cout<<"Case #"<<test++<<": "<<ret<<endl;
	}
}
