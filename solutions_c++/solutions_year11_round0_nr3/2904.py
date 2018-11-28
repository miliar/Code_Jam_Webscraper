#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include<cmath>
#include <map>
using namespace std;
int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int cas,n,k=1;
	scanf("%d",&cas);
	while(cas--){
		scanf("%d",&n);
		int x;
		scanf("%d",&x);
		int temp=x;
		int min=x;
		int sum=x;
		for(int i=1;i<n;i++){
		scanf("%d",&x);
		if(min>x)
			min=x;
		sum+=x;
		temp=temp^x;
		}
		printf("Case #%d: ",k++);
		if(temp!=0)
			cout<<"NO\n"<<endl;
		else
			cout<<sum-min<<endl;
	}
	fclose(stdin);
    fclose(stdout);
	return 0;
}


