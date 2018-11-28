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
string ma[15];
bool cal(int a,int b,int c){
	int i,j;
	double ta=0.0,yo=0.0,x=a+0.5*(c-1),y=b+0.5*(c-1);
	for(i=a;i<a+c;i++) for(j=b;j<b+c;j++){
		if((i==a || i==a+c-1) && (j==b || j==b+c-1)) continue;
		ta+=(ma[i][j]-'0')*(i-x);yo+=(ma[i][j]-'0')*(j-y);
	}
//	if(a==1 && b==1 && c==5) cout<<ta<<' '<<yo<<endl;
	if(fabs(ta)<1e-10 && fabs(yo)<1e-10) return true;return false;
}
int main()
{
	int i,j,k,l,r,c,d,n;cin>>n;
	for(i=0;i<n;i++){
		cin>>r>>c>>d;int ret=0;
		for(j=0;j<r;j++) cin>>ma[j];
		for(j=0;j<r-2;j++) for(k=0;k<c-2;k++) for(l=3;j+l<=r && k+l<=c;l++){
			if(cal(j,k,l)) ret>?=l;
		}
		printf("Case #%d: ",i+1);
		if(ret<3) printf("IMPOSSIBLE\n");
		else printf("%d\n",ret);
	}
	return 0;
}
