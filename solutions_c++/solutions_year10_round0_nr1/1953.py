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
int main()
{
	vector <lint> zyo;zyo.pb(1);
	int n,i;vector <string> out;
	for(i=0;i<40;i++) zyo.pb(zyo[i]*2);
	cin>>n;
	for(i=0;i<n;i++){
		lint a,b;cin>>a>>b;
		b%=zyo[a];if(b==zyo[a]-1) out.pb("ON");else out.pb("OFF");
	}
	for(i=0;i<n;i++){
		cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	}
	return 0;
}
