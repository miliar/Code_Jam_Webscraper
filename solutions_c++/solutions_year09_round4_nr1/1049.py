#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
using namespace std;
const int mn=100;
int n;
int a[mn];


int process(){
	int ans=0;
	for(int i=0,j;i<n;i++){
		if(a[i]>i){
			for(j=i+1;j<n;j++){
				if(a[j]<=i)break;
			}
			for(int k=j;k>i;k--){
				swap(a[k],a[k-1]);
				ans++;
			}
		}
	}
	return ans;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-l-out.txt","w",stdout);
	int Tn;
	scanf("%d",&Tn);
	char s[mn];
	
	for(int Cn=1;Cn<=Tn;Cn++){
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%s",s);
			int max=-1;
			for(int j=0;j<n;j++)
				if(s[j]=='1')max=j;
			a[i]=max;
		}
		printf("Case #%d: ",Cn);
		printf("%d\n",process());
	}
	return 0;
}
