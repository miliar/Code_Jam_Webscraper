#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
using namespace std;
#define pb push_back
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
double ou;
lint calc(int a,int b){
	if(a==0 || b==0) return 0;
	lint ret=0;int i;
	for(i=1;i<=a;i++){
		int t=(int)(ou*i);
		ret+=max(0,b-t);
	}
	for(i=1;i<=b;i++){
		int t=(int)(ou*i);
		ret+=max(0,a-t);
	}
	return ret;
}
int main()
{
	ou=(sqrt(5.0)+1.0)*0.5;
	vector <lint> out;int n,i,a1,a2,b1,b2;
	cin>>n;
	for(i=0;i<n;i++){
		cin>>a1>>a2>>b1>>b2;
		out.pb(calc(a2,b2)-calc(a2,b1-1)-calc(a1-1,b2)+calc(a1-1,b1-1));
	}
	for(i=0;i<n;i++) cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	return 0;
}
