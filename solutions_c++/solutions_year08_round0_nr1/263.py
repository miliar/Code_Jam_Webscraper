#include <stdio.h>
#include <string.h>

#define INF 10000000

int main(){
  char s[10001],names[101][201];
  int l,u,i,j,k,e,n,count[2001][101];
  gets(s);
  sscanf(s,"%d",&l);
  for (u=0; u<l; u++){
    gets(s);
    sscanf(s,"%d",&e);
    //printf("e=%d\n",e);
    for (i=0; i<e; i++)
      gets(names[i]);
    gets(s);
    sscanf(s,"%d",&n);
    //printf("%d=n\n",n);
    int min=0;
    if (n>0){
      
      
      gets(s);
      //printf(">>>%s\n",s);
      for (j=0; j<e; j++){
	if (strcmp(s,names[j])==0) break;
      }
      for (k=0; k<e; k++){
	count[0][k]=0;
	if (k==j) count[0][k]=INF;
      }
  
      for (i=1; i<n; i++){
	gets(s);
	//printf(">>%s\n",s);
	for (j=0; j<e; j++){
	  if (strcmp(s,names[j])==0) break;
	}
	int eng=j;
	for (k=0; k<e; k++){
	  if (k==eng) count[i][k]=INF;
	  else{
	    count[i][k]=count[i-1][k];
	    for (j=0; j<e; j++)
	      if (count[i][k]>count[i-1][j]+1)
		count[i][k]=count[i-1][j]+1;
	  }
	}
      }
      min=count[n-1][0];
      for (i=1; i<e; i++){
	if (count[n-1][i]<min)
	  min=count[n-1][i];
      }
    }
    printf("Case #%d: %d\n",u+1,min);
  }
  return 0;
}
