#include<iostream>
#include<string>
using namespace std;

int main(){
	int N;
	cin>>N;
	char wc[32]="welcome to code jam";
	int lwc=strlen(wc);
	char st[1024];
	cin.getline(st, 1024);
	for(int t=1; t<=N; t++){
		cin.getline(st, 1024);
		int lst=strlen(st);
		int ans[lwc+1][lst+1];
		for(int i=0; i<=lst; i++) ans[0][i]=1;
		for(int i=1; i<=lwc; i++) ans[i][0]=0;
		for(int i=1; i<=lwc; i++){
			for(int j=1; j<=lst; j++){
				ans[i][j]=0;
				if(wc[i-1]==st[j-1]){
					ans[i][j]=(ans[i][j]+ans[i-1][j-1])%10000;
				}
				ans[i][j]=(ans[i][j]+ans[i][j-1])%10000;
			}
		}
		printf("Case #%d: %04d\n", t, ans[lwc][lst]);
	}
	return 0;
}
