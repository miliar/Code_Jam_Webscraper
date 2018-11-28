#include"tmp_bign.h"
#include<conio.h>
bign a[1001],b[1001];

bign gcd(bign x,bign y){
	return y!=0?gcd(y,x%y):x;
}

int main(){
	int C,n;
	bign max,y;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>C;
	for(int i=1;i<=C;i++){
		cin>>n;
		for(int j=0;j<n;j++) cin>>a[j];
		sort(a,a+n);
		for(int j=0;j<n-1;j++) b[j]=a[j+1]-a[j];
		n--;
		max=b[0];
		if(n>1) max=gcd(b[0],b[1]);
		for(int j=2;j<n;j++) max=gcd(max,b[j]);
		//for(int j=0;j<n;j++) cout<<b[j]<<endl;
		//cout<<max<<endl;
		if(a[0]%max!=0) y=max-a[0]%max;
		else y=0;
		cout<<"Case #"<<i<<": "<<y<<endl;
	}
	getch();
	return 0;
}
