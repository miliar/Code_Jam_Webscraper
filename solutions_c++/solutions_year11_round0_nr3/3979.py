#include<vector>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<set>
#include<string.h>
#include<map>
#include<algorithm>
#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<queue>
#include<stack>
#include<ctype.h>
#include<cmath>
#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair
#define fia(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define fib(i,a,b) for(int i=(int)(b);i>(int)(a);i--)
#define ipow(a,b) (int)pow((double)a,(double)b)
#define fill(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;
using namespace std; int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int tc=1;
	while(t--){
		int n;
		int a1=0;
		cin>>n;
		int a[n];
		int temp;
		int max1=0;
		rep(i,n) 
			cin>>a[i];
		a1=1<<n;
		a1--;
			 
	    fia(i,1,a1){
		bool first=true;
		bool sec=true;
		int right,left,sum1=0,sum2=0;
		rep(j,n){
		    if(i&(1<<j)){
				if(first){
					right=a[j];
					sum2+=a[j]; 
					first=false;
				}
				else{
				        right^=a[j];
						sum2+=a[j];
				}
			}
			else{
				if(sec){
					left=a[j];
					sum1+=a[j];
					sec=false;
				}
				else{
				    left^=a[j];
					sum1+=a[j];
				}
			}
		}
		int max2=0;                
		if(left==right){
			max2=max(sum1,sum2); 
			max1=max(max2,max1);
		}
	}
	   		 
	if(max1==0) 
		cout<<"Case #"<<tc<<": "<<"NO"<<endl;
	else 
		cout<<"Case #"<<tc<<": "<<max1<<endl;
	tc++;
	}
	return 0;
}
