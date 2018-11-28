#include<cstdio>
#include<string>
using namespace std;

int n;
char board[60][60];

void print(){
	for(int i=0; i<n; i++){
		printf("%s\n",board[i]);
	}
}

bool check(string s, char c, int k){
	int tmp=0;
	for(int i=0; i<s.size(); i++){
		if(s[i]==c) tmp++;
		else tmp=0;
		if(tmp==k) return true;
	}
	return false;
}

bool win(char c, int k){
	string s;
	for(int i=0; i<n; i++) if(check(board[i],c,k)) return true;
	for(int j=0; j<n; j++){
		s="";
		for(int i=0; i<n; i++) s+=board[i][j];
		if(check(s,c,k)) return true;
	}
	for(int nr=0; nr<2*n-1; nr++){
		s="";
		for(int i=0; i<n; i++) {
			int k = nr-i;
			if(k<n && k>=0) s+=board[i][k];
		}
		if(check(s,c,k)) return true;
	}
	for(int nr=-n; nr<=n; nr++){
		s="";
		for(int i=0; i<n; i++) {
			int k = nr+i;
			if(k<n && k>=0) s+=board[i][k];
		}
		if(check(s,c,k)) return true;
	}
	return false;
}

main(){
	int t,k;
	scanf("%d",&t);
	for(int C=1; C<=t; C++){
		scanf("%d %d",&n,&k);
		for(int i=0; i<n; i++)  scanf("%s",board[i]);
		for(int i=0; i<n; i++){
			int pos = n-1;
			for(int j=n-1; j>=0; j--)
				if(board[i][j]!='.') board[i][pos--]=board[i][j];
			while(pos>=0) board[i][pos--]='.';
		}
		printf("Case #%d: ",C);
		if(win('B',k) && win('R',k)) printf("Both\n");
		else if(win('B',k)) printf("Blue\n");
		else if(win('R',k)) printf("Red\n");
		else printf("Neither\n");
	}
	return 0;
}
