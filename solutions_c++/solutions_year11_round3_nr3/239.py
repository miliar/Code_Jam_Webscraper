#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
 
#define rei(i,a,b) for(int i=a;i<b;i++)
#define red(i,a,b) for(int i=a;i>=b;i--)
#define ree(i,a,b) for(int i=a;i<=b;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define pb(a,x) a.push_back(x)
#define all(a) a.begin(),a.end()
#define srt(a) sort(all(a))
#define rev(a) reverse(all(a))
 
int gcd(int a, int b){
    // Euclidean algorithm
    int t;
    while (b != 0){
        t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int lcm(int a, int b){
    return (a * b / gcd(a, b));
}

int main(){
	int test;
	scanf("%d",&test);
	ree(t,1,test){
		printf("Case #%d: ",t);
		int n,l,h;
		cin>>n>>l>>h;
		vector<int> freq(n,0);
		rei(i,0,n) cin>>freq[i];
		int ans=-1;
		rei(i,l,h+1){
			bool okay=true;
			rei(j,0,n) if((i%freq[j]!=0) && (freq[j]%i)!=0) okay=false;
			if(okay){
				ans=i;
				break;
			}
		}	
		
		if(ans!=-1){
			cout<<ans<<endl;
		}else{
			cout<<"NO\n";
		}
	}
	return 0;
}
