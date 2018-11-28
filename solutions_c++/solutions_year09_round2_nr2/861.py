#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdio>
using namespace std;
void selectionsort(char a[]){
	int l = strlen(a);
	int small;
	for(int i=0;i<l-1;i++){
		small = i;
		for(int j=i+1;j<l;j++){
			if(a[j]<a[small])
				small = j;
		}
		swap(a[small],a[i]);
	}
}
int main(){
	int testcases;
	cin>>testcases;
	for(int cases=1;cases<=testcases;cases++){
		char num[30];
		scanf("%s",num);
		int l = strlen(num);
		bool flag = true;
		for(int i=0;i<l-1;i++){
			if(num[i]<num[i+1])
				flag = false;
		}
		if(flag){
			num[l]='0';
			num[l+1]='\0';
			l++;
			selectionsort(num);
			int i;
			for(i=0;i<l-1 && num[i]=='0';i++);
			swap(num[0],num[i]);
		}else{
			next_permutation(num,num+l);
		}
// 		cout<<num<<endl;
		printf("Case #%d: %s\n",cases,num);
	}
	return 0;
}