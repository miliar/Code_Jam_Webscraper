#include<cstdio>
#include<algorithm>
#include<vector>
#include<list>
#include<queue>
#include<stack>
#include<string>

using namespace std;


int solve(int cas) {
     int no[10];
     printf("Case #%d: ",cas+1);
     for (int i=0; i<10; i++) no[i]=0;
     int c[21];
     char a=getchar();
     while(a<'0' || a>'9') a=getchar();
     int l=0;
     while(a>='0' && a<='9') {
	  c[l]=a-'0';
	  l++;
	  a=getchar();
     }
     int i;
     bool OK=false;
     for (i=l-1; i>=0; i--) {
	  no[c[i]]++;
	  if (i<l-1 && c[i]<c[i+1]) {
	       OK=true;
	       break;
	  
	  }
     }
    
     if (OK) {
	  for (int j=0; j<i; j++) printf("%d",c[j]);
	  for (int j=c[i]+1; j<10; j++) {
	       if (no[j]>0) {
		    no[j]--;
		    printf("%d",j);
		    break;
	       }
	  }
	  for (int j=0; j<10; j++) {
	       while (no[j]>0) {
		    no[j]--;
		    printf("%d",j);
	       }
	  }
     }
     else {
	  for (int j=1; j<10; j++) {
	       if (no[j]>0) {
		    no[j]--;
		    printf("%d",j);
		    break;
	       }
	       
	  }
	  printf("0");
	  for (int j=0; j<10; j++) {
	       while (no[j]>0) {
		    no[j]--;
		    printf("%d",j);
	       }
	  }
	  
     }
     printf("\n");
     return 0;
}

int main() {
     int n;
     scanf("%d",&n);
     for (int i=0; i<n; i++) solve(i);
     return 0;
}