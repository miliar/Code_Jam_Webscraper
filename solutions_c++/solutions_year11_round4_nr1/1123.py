#include<stdio.h>
#include<iostream>
#include<vector>
#include<math.h>
#include<algorithm>
#include<memory.h>
#include<map>
#include<queue>

using namespace std;

int d,v1,v2,n,f[1111111],x,y,z;
long double ans,k;


int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);	
	int t=0;
	cin >> t;
	cout.precision(6);
	for (int e=1;e<=t;e++){
		cin >> d >> v1 >> v2 >> k >> n;
		for (int i=0;i<d;i++)f[i]=0;
		ans=0;
		for (int i=0;i<n;i++){
			cin >> x >> y >> z;
			for (int j=x;j<y;j++)f[j]+=z;
		}
		sort(f,f+d);
		for (int i=0;i<d;i++){
			long double w=1./(f[i]+v2);
			if (w<k){
				k-=w;
				ans+=w;
			}else{
				ans+=k;
				ans+=(1.-(f[i]+v2)*k)/(f[i]+v1);
				k=0;
			}
		}
		cout << "Case #" << e << ": " << fixed << ans << endl;
	}
	return 0;
}


