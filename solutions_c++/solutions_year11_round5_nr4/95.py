#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<ctime>
#include<cassert>
using namespace std;
#define y1 fndjifhwdn
#define ws vfsdkofsjd
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pi;
ll tk;
int n;
string s,ss,ans;
void bct(int k){
	if (k==n){
		if (((ll)round(sqrt(tk)))*((ll)round(sqrt(tk)))==tk){
			ans=ss;
		}
		return;
	}
	if (s[k]=='0' || s[k]=='?'){
		tk=tk*2;
		ss[k]='0';
		bct(k+1);
		tk=tk/2;
	}
	if (s[k]=='1' || s[k]=='?'){
		tk=tk*2+1;
		ss[k]='1';
		bct(k+1);
		tk=tk/2;
	}
}
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tt;
	scanf("%d",&tt);
	for (int ti=0;ti<tt;ti++){
		printf("Case #%d: ",ti+1);
		cin>>s;
		n=s.length();
		ss=s;
		tk=0;
		ans="";
		bct(0);
		cout<<ans;
		printf("\n");
	}
    return 0;
}









