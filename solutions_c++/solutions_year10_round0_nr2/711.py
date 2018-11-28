
#include <stdio.h>
#include <string.h>
#include <memory.h>
int T, n;
char dat[1000][55];
char sol[55];
void gop10(char *x){
	int i;
	for(i=1;x[i-1] != '\0';i++);
	for(;i>0;i--) x[i] = x[i-1];
	x[0] = '0';
}
void na10(char *x){
	int i;
	for(i=0;x[i] != '\0';i++) x[i] = x[i+1];
}
void minus(char *A, char *B){ // A -= B;
	int a, b;
	a = strlen(A); b = strlen(B);
	int i, up;
	up = 0;
	for(i=0;i<b;i++){
		A[i] = A[i] - B[i] + '0' + up;
		if(A[i] < '0'){
			A[i] += 10;
			up = -1;
		}
		else up = 0;
	}
	for(;up != 0;i++){
		A[i] = A[i] + up;
		if(A[i] < '0'){
			A[i] += 10;
			up = -1;
		}
		else up = 0;
	}

	a = strlen(A);
	for(a--;A[a] == '0' && a>0;a--){
		A[a] = '\0';
	}
}
bool compare(char *A, char *B){ // <
	int a, b;
	a = strlen(A); b = strlen(B);
	if(b!=a) return b>a;
	int i;
	for(i=a-1;i>=0;i--){
		if(A[i] != B[i]) return A[i] < B[i];
	}
	return false;
}
bool compare2(char *A, char *B){ // <
	int a, b;
	a = strlen(A); b = strlen(B);
	if(b!=a) return b>a;
	int i;
	for(i=a-1;i>=0;i--){
		if(A[i] != B[i]) return A[i] < B[i];
	}
	return true;
}
void nam(char *A, char *B){ //%=
	int n=0;
	while(compare2(B, A)){
		gop10(B);
		n++;
	}
	while(n>0){
		n--;na10(B);
		while(compare2(B, A)){
			minus(A, B);
		}
	}
}

char mn[55];
char a[55], b[55], c[55], tmp[55];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	int t;
	for(t=1;t<=T;t++){
		scanf("%d",&n);
		int i;
		memset(sol, 0, sizeof(sol));
		for(i=0;i<n;i++){
			memset(dat[i], 0, sizeof(dat[i]));
			scanf("%s",dat[i]);
			strrev(dat[i]);
		}
		strcpy(mn, dat[0]);
		for(i=0;i<n;i++){
			if(compare(dat[i], mn)) strcpy(mn, dat[i]);
		}
		for(i=0;i<n;i++){
			minus(dat[i], mn);
		}
		bool go=false;
		for(i=0;i<n;i++){
			if(dat[i][0] != '0' || strlen(dat[i]) > 1){
				if(!go){
					go = true;
					strcpy(sol, dat[i]);
				}
				else{
					memset(a, 0, sizeof(a));
					memset(b, 0, sizeof(b));
					memset(c, 0, sizeof(c));
					memset(tmp, 0, sizeof(tmp));
					strcpy(a, dat[i]);
					strcpy(b, sol);
					while(a[0] != '0' || strlen(a) > 1){
						strcpy(c, a); // c = a
						strcpy(a, b); nam(a, c);//a = b % a
						strcpy(b, c);//b = c;
					}
					strcpy(sol, b);
				}
			}
		}
		strcpy(b, sol);
		nam(mn, sol);
		minus(sol, mn);
		if(!strcmp(sol, b)){
			sol[0] = '0'; sol[1] = '\0';
		}
		strrev(sol);
		printf("Case #%d: %s\n",t, sol);
	}
	return 0;
}
/*
#include <stdio.h>
int dd[1000];
int main(){
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	int n;
	scanf("%d",&T);
	while(T>0){
		scanf("%d",&n);
		int i, mn;
		for(i=0;i<n;i++){
			scanf("%d", &dd[i]);
		}
		mn = dd[0];
		for(i=0;i<n;i++){
			if(mn > dd[i])mn = dd[i];
		}
		for(i=0;i<n;i++){
			dd[i] -= mn;
		}
		int x;
		x = -1;
		for(i=0;i<n;i++){
			if(dd[i] != 0){
				if(x == -1){
					x = dd[i];
				}
				else{
					int a, b, c;
					a = x; b = dd[i];
					while(a != 0){
						c = a;
						a = b % a;
						b = c;
					}
					x = b;
				}
			}
		}
		int ttt = x;
		x = x - mn % x;
		if(x == ttt) x = 0;
		static int t=1;
		printf("Case #%d: %d\n",t++,x);
		T--;
	}
	return 0;
}
*/