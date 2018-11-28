#include<cstdio>
#include<algorithm>

int main() {
     int l,d,n;
     scanf("%d%d%d\n",&l,&d,&n);
     int **W=new int*[d];
     char a;
     for (int i=0; i<d; i++) {
	  W[i]=new int[l];
	  a=getchar();
	  while(a<'a' || a>'z') a=getchar();
	  for (int j=0; j<l; j++) {
	       a-='a';
	       W[i][j]=(1<<a);
	       a=getchar();
	//       printf("%d ",W[i][j]);
	  }
//	  printf("\n");
     }
     int *pos=new int[d];
     int pat;
     int ans;
     int cur;
     for (int i=0; i<n; i++) {
	  ans=d;
	  for (int j=0; j<d; j++) pos[j]=j;
	  for (int j=0; j<l; j++) {
	       a=getchar();
	       while ((a<'a' || a>'z') && a!='(') a=getchar();
	       pat=0;
	       if (a=='(') {
		    a=getchar();
		    while(a!=')') {
			 pat+=(1<<(a-'a'));
			 a=getchar();
		    }
	       }
	       else pat=(1<<(a-'a'));
	 //      printf("%d ",pat);
	       cur=0;
	       for (int t=0; t<ans; t++) {
		    if ((W[pos[t]][j]&pat)==W[pos[t]][j]) {
			 pos[cur]=pos[t];
			 cur++;
		    }
	       }
	  //     printf("(%d) ",cur);
	       ans=cur;
	  }
//	  printf("\n");
	  printf("Case #%d: %d\n",i+1,ans);
     }
     return 0;
  
}