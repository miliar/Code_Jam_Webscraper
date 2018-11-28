#include<stdio.h>
#include<algorithm>
#include<string>
#include<iostream>


using namespace std;

int n;
int i,j;
string num;
int ar[100];
int ln;

int main(){
	freopen("nn2.in","r",stdin);
	freopen("nn2.out","w",stdout);

	scanf("%d\n",&n);
	for(i=1;i<=n;i++){
		getline(cin,num);
		num = "0"+num;
		ln= num.length();
		//printf("%s %d\n",num.c_str(),ln);
		for(j=0;j<ln;j++){
			ar[j]=num[j]-48;
		}
		next_permutation(ar,ar+ln);
		int st=0;
		if(ar[st]==0) st=1;
		printf("Case #%d: ",i);
		for(j=st;j<ln;j++){
			printf("%d",ar[j]);
		}
		printf("\n");
	}
	return 0;
}