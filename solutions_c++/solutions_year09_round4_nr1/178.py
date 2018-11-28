#include<stdio.h>
#include<algorithm>
#include<string>
using namespace std;

typedef string str;
#define MAX 105

int n;
str mat[MAX];
int x[MAX];//,taken[MAX];

int main(){

	char buf[105];
	int i,j,k;

	int T,N;

	scanf("%d",&T);
	for(N=1;N<=T;N++){
		
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%s",buf);
			mat[i] = str(buf);
//			taken[i] = 0;
			
			for(j=n-1;j>0;j--){
				if(mat[i][j]=='1')
					break;
			}
			x[i] = j;
//			printf(">>>> %s %d\n",mat[i].c_str(),x[i]);
		}

		k = 0;
		for(i=0;i<n;i++){
			for(j=i;j<n;j++){
				if(x[j]<=i)
					break;
			}
			if(j!=i){
				while(j!=i){
					k++;
					swap(mat[j-1],mat[j]);
					swap(x[j-1],x[j]);
					j--;
				}
			}
		}

		printf("Case #%d: %d\n",N,k);

		
	}
	return 0;
}