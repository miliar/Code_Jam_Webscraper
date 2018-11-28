#include<iostream>
#include<cmath>
using namespace std;
int t,cl,c,l,p,ans,temp;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("out","w",stdout);
	cin>>t;cl=0;
	while(t--){
		cl++;
		cin>>l>>p>>c;
		temp=ceil(log((double)p/l)/log(c));
		//printf("%lf\n",log((double)p/l));
		//printf("%d\n",temp);
		//if ((double)(log(p/l)/log(c)-floor(log(p/l)/log(c)))<0.00000001) temp++;
		ans=ceil(log(temp)/log(2));
		//printf("%lf\n",log(temp)/log(2));
		//if ((double)(log(temp)/log(2)-floor(log(temp)/log(2)))<0.00000001) ans++;
		printf("Case #%d: %d\n",cl,ans);
	}
	//system("pause");
	return 0;
}
