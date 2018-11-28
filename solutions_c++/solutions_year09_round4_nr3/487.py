#include <cstdio>
#include <list>
using namespace std;
int main(){
  int T;
  scanf("%d",&T);
  for(int nrt=1; nrt<=T; nrt++){
	  int n,k;
	  scanf("%d%d",&n,&k);
	  int data[n][k];
	  for(int i=0; i<n; i++)
	    for(int j=0; j<k; j++)
	      scanf("%d",&data[i][j]);

	  bool res[n][n];
	  for(int i=0; i<n; i++)
	    for(int j=0; j<n; j++){
		int l=0;
		for(l=0; l<k; l++)
		  if(data[i][l]<=data[j][l])
		    break;
		  res[i][j]=(l==k);
	    }
/*
	  for(int i=0; i<n; i++)
	    for(int j=0; j<n; j++)
		printf("%d %d: %d\n",i,j,res[i][j]);
*/	

	  int mini=0;
	  for(int l=0; l<(1<<n); l++){
	    int temp=0;
	    for(int i=0; i<n; i++)
		if(l&(1<<i))
		   temp++;
	    bool flaga=true;
	    for(int i=0; i<n; i++)
	    for(int j=0; j<n; j++){
		if(i==j)continue;
		if(!((l&(1<<i))&&(l&(1<<j))))continue;
		if(res[i][j])flaga=false;	
	    }
	    if(flaga && (temp>mini)){
		mini=temp;
	    }
	  }
	printf("Case #%d: %d\n",nrt,mini);
   }
}

