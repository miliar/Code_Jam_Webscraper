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

int main(){
	int i,j,k,l;
	//freopen("1.txt","r",stdin);
	//freopen("large-out.txt","w",stdout);
	//freopen("small-out.txt","w",stdout);
	map<string,bool> mp;
	int t,n,m,tot,cas=1,cnt;
	string s,ss;
	scanf("%d",&t);
	while(t--){
		tot=0;
		cnt=0;
		mp.clear();
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++){
			cin>>s;
			s+='/';
			l=s.length();
			ss="";
			for(j=0;j<l;j++){
				if(s[j]=='/'&& j!=0){
					mp[ss]=true;
				}
				ss+=s[j];
			}
		}
		for(i=0;i<m;i++){
			cin>>s;
			s+='/';
			l=s.length();
			ss="";
			for(j=0;j<l;j++){
				if(s[j]=='/' && j!=0){
					if(mp[ss]==false){
						mp[ss]=true;
						tot++;
					}
				}
				ss+=s[j];
			}
		}
		printf("Case #%d: %d\n",cas++,tot);
	}


	return 0;
}