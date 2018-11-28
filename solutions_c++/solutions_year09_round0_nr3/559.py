#include<cstdio>
#include<queue>

const char w[20]="welcome to code jam";
const int l=19;
int M=10000;
char s[510];
int solve(int no) {
     int a=getchar();
     int len=0;
     while(a!='\n' && a!=-1) {
	  s[len]=a;
	  len++;
	  a=getchar();
     }
	  
     int cur[l];
     for (int j=0; j<l; j++)  cur[j]=0;
     for (int i=0; i<len; i++) {
	  for (int j=l-1; j>0; j--) {
	       if (s[i]==w[j]) cur[j]=(cur[j]+cur[j-1])%M;
	  }
	  if (s[i]==w[0]) cur[0]=(cur[0]+1)%M;
     }
     printf("Case #%d: %.4d\n",no+1,cur[l-1]);
     return 0;
}

int main() {
     int t;
     scanf("%d\n",&t);
     for (int i=0; i<t; i++) solve(i);
     return 0;
  
}