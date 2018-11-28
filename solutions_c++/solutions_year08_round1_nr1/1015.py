#include <iostream>

using namespace std;
int compare (const void * a, const void * b){
  return ( *(int*)a - *(int*)b );
}
int compare2 (const void * a, const void * b){
  return ( *(int*)b - *(int*)a );
}
int main (){
	int T,n,v1[801],v2[801],X,aux;
	long long Y;
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		scanf("%d",&n);
		for(int j=0;j<n;j++){
			scanf("%d",&aux);
			v1[j]=aux;
		}
		qsort (v1, n, sizeof(int), compare2);
		for(int j=0;j<n;j++){
			scanf("%d",&aux);
			v2[j]=aux;
		}
		qsort (v2, n, sizeof(int), compare);
		Y=0;
		for(int j=0;j<n;j++){
			Y+=v1[j]*v2[j];
			
		}
		printf("Case #%d: %d\n",i,Y);
	}
	return 0;
}
