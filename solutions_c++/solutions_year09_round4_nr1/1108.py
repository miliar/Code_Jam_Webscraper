#include <iostream>
using namespace std;
int last[50], t, n;
char x[50];
int main(){
	scanf("%d",&t);
	for (int c=1 ;c<=t; c++){
		memset(last, 0, sizeof last);
		scanf("%d",&n);
		for (int i=0;i<n;i++){
			scanf("%s",x);
			for (int j=0;j<n;j++)
				if (x[j]=='1') last[i] = j;
		}
		int cnt = 0;
		for (int i=0;i<n;i++){
			if (last[i]>i){
				int j;
				for (j=i+1;j<n;j++) if (last[j]<=i) break;
				for (;j>i;j--){
					int t=last[j]; last[j]=last[j-1]; last[j-1]=t;
					cnt++;
				}
			}
		}
		cout<<"Case #"<<c<<": "<<cnt<<endl;
	}
} 
