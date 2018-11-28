#include<algorithm>
#include<iostream>
#include<numeric>
#include<cstdlib>
#include<sstream>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<cmath>
#include<set>
#include<map>
using namespace std;

#define EPS 1e-8
#define INF 1<<30
#define PI (2*acos(0.0))
#define flv(vec,val) fill(vec.begin(),vec.end(),val)
#define fl1(arr,beg,end,val) fill(arr+beg,arr+end,val)
#define fl2(arr,beg,end,val) fill(arr[beg],arr[end],val)
#define mems(arr,val) memset(arr,val,sizeof(arr))

typedef vector<int>VI;
typedef vector<string>VS;
typedef map<string,int>MSI;
typedef map<vector<int>,int>MVI;
template<typename T>inline T GCD(T i,T j){if(!j)return i;else return GCD(j,i%j);}
typedef	long long LNG;
//typedef __int64 LNG;
int a[1005][2];

int main(){
	int i,j,l,n,m,t,cas=1,tot=0;
	//freopen("1.txt","r",stdin);
	//freopen("large-out.txt","w",stdout);
	//freopen("small-out.txt","w",stdout);
	
	scanf("%d",&t);
	while(t--){
		tot=0;
		scanf("%d",&l);
		for(i=0;i<l;i++){
			scanf("%d%d",&a[i][0],&a[i][1]);
		}
		for(i=0;i<l;i++){
			for(j=i+1;j<l;j++){
				if(a[i][0]>a[j][0]){
					swap(a[i][0],a[j][0]);
					swap(a[i][1],a[j][1]);
				}
			}
		}
		for(i=0;i<l;i++){
			for(j=i+1;j<l;j++){
				if(a[j][1]<a[i][1])tot++;
			}
		}
		printf("Case #%d: %d\n",cas++,tot);
	}
	
	return 0;
}