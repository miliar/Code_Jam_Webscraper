#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

int main(){
	int tc;
	scanf("%d",&tc);
	int j=0;
	while(j++<tc){
		char arr[100];
		cin>>(arr+1);
		arr[0]='0';
		next_permutation(arr,arr+strlen(arr));
		int i = (arr[0]=='0')?1:0;
		cout<<"Case #"<<j<<": ";
		cout<<(arr+i)<<"\n";
	}
}
