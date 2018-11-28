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
	int i,t,n,j,p;string r;cin>>t;
	for(i=0;i<t;i++){
		int b1=1,b2=0,o1=1,o2=0,now=0;scanf("%d",&n);
		for(j=0;j<n;j++){
			cin>>r>>p;
			if(r=="O"){now=max(abs(p-o1)+o2,now)+1;o1=p;o2=now;}
			else{now=max(abs(p-b1)+b2,now)+1;b1=p;b2=now;}
		}
		printf("Case #%d: %d\n",i+1,now);
	}
	return 0;
}
