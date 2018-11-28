#include<iostream>
using namespace std;
int t,n,k,i,r,c;
bool duan=0;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("out","w",stdout);
	cin>>t;
	c=0;
	while(t--){
		c++;
		cin>>n>>k;
		r=0;
		duan=0;
		while(n>0&&k>0){
			r=k%2;
			k=k/2;
			n--;
			if (r==0) duan=1;
		}
		if (n==0){
			if (r==1&&duan==0)
				printf("Case #%d: ON\n",c);
			else
				printf("Case #%d: OFF\n",c);
		}
		else
			printf("Case #%d: OFF\n",c);
	}
//	system("pause");
	return 0;
}
