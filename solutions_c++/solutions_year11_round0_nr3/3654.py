#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,n,a,x,min,sum;
	scanf("%d",&t);
	x=0;
	for(int i=1;i<=t;i++){
		scanf("%d",&n);scanf("%d",&a);
		x=a;min=a;sum=a;
		for(int j=1;j<n;j++){
			scanf("%d",&a);
			x^=a;
			sum+=a;
			if(min>a)min=a;
		}
		if(x)
			cout<<"Case #"<<i<<": NO"<<endl;
		else 
			cout<<"Case #"<<i<<": "<<sum-min<<endl;
	}
	return 0;
}
		
