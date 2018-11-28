#include<cstdio>
#include<iostream>
using namespace std;
int test;
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	cin>>test;
	for (int t=1;t<=test;t++){
		int A,B;
		cin>>A>>B;
		int j=1;
		int ans=0;
		for (int i=A;i<B;i++){
			while (j*10<=A)
				j=j*10;
			int k=i;
			k=k/10+k%10*j;
			while (k!=i){
				if (i<k && k<=B)
					ans++;
				k=k/10+k%10*j;
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
