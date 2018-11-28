#include<iostream>
#include<string>
#include<cstdio>
#include<map>
#include<algorithm>
#include<cmath>
#include<vector>
#include<sstream>
#include<stack>
#include<queue>
#include<cstring>

#define pb push_back
#define LL long long
#define OUTPUT_TO_FILE 1
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)


using namespace std;
bool check(int n,int m){
	int l = 0;
	int temp = n;
	while(temp > 0){
		l++;
		temp = temp/10;
	}

	if(l==1)
		return false;
	else if(l==2){
		temp = (n%10)*10 + n/10;
		if(temp==m)
			return true;
		else
			return false;
	}
	else if(l==3){
		temp = (n%10)*100 + n/10;
		if(temp==m)
			return true;
		temp = (temp%10)*100 + temp/10;
		if(temp==m)
			return true;

		return false;
	}

}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,t1,A,B,n,m,i,j;
	cin>>t;
	t1 = 1;
	while(t1<=t){
		int ans = 0;
		cin>>A>>B;
		for(i=A;i<=B;i++){
			for(j=i+1;j<=B;j++){
				if(check(i,j))
					ans++;
			}
		}
		cout<<"Case #"<<t1<<": "<<ans<<endl;
		t1++;
	}
}