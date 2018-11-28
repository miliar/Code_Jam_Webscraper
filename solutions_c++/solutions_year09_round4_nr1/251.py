#include <cstdio>
#include <algorithm>
using namespace std;

#define M 500
//int tab[M][M];
char s[M][M+1];
int ok[M],can[M];//,rowcount[M];

int main(){
	int t,u,n,i,j,k,x[M];//,p,tmp[M];
	pair<int,int> d[M];
	
	scanf("%d",&t);
	for (u=0; u<t; u++){
		scanf("%d",&n);
//		for (i=0; i<n; i++) for (j=0; j<n; j++) tab[i][j]=0;
//		for (i=0; i<n; i++){ 
//			rowcount[i]=0; 
//			ok[i]=0; 
//		}
		for (i=0; i<n; i++){
			scanf("%s",s[i]);
			for (j=n-1; j>0 && s[i][j]=='0'; j--);
			//d[i]=make_pair(j,i);
//			tab[j][i]=1;
			can[i]=j;
			ok[i]=0;
//			rowcount[j]++;
		}
		for (i=0; i<n; i++){
			for (j=0; j<n; j++){
				if (ok[j]==0 && can[j]<=i) break;
			}
			ok[j]=1;
			x[i]=j;
		}
				
		//sort(d,d+n);
	//	for (i=0; i<n; i++) printf("%d,%d ",d[i].second,d[i].first);
		//printf("\n");

//		for (i=n-1; i>=0; i--){
//			for (j=n-1; j>0; j--){
//				if (d[j].first<=j-1 && d[j].second<d[j-1].second){
//					swap(d[j],d[j-1]);
//				}
//			}
//		}

//		for (i=j=n-1; i>=0; i--){
//			int count=0;
//			for (k=n-1; k>=0; k--){
//				if (tab[i][k]){
//					tmp[count++]=k;
//					ok[k]=1;
//				}
//			}
//			for (k=n-1; k>=0 && count<j-i+1; k++
//			for (k=n-1; k>=0; k--){
//				if (tab[i][k]){
//					for (p=n-1; p>k; p--){
//					x[j--]=k;
//					
//				}
//			}
//		}
//		for (i=0; i<n; i++) printf("%d,%d ",d[i].second,d[i].first);
	//	for (i=0; i<n; i++) printf("%d ",x[i]);
	//	printf("\n");
		for (i=k=0; i<n; i++){
			for (j=i+1; j<n; j++){
				k+=(x[j]<x[i]); //( d[j].second<d[i].second); //(x[j]<x[i]);
			}
		}
		printf("Case #%d: %d\n",u+1,k);
	}
	return 0;
}
