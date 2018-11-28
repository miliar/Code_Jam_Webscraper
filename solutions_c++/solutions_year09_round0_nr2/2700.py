#include <iostream>
#include<cstring>
using namespace std;
int arr[105][105];
int dir[105][105];
char ans[105][105];
int n, m;
char paint;
void mark(int j,int k){
	int small=arr[j][k];
	int d = -1;
	if(j-1>=0){
		if(small > arr[j-1][k]){
			small = arr[j-1][k];
			d = 0;
		}
	}
	if(k-1>=0){
		if(small > arr[j][k-1]){
                	small = arr[j][k-1];
			d = 1;
		}
	}
	if(k+1<m){
		if(small > arr[j][k+1]){
			small = arr[j][k+1];
                	d = 2;
		}
	}
	if(j+1<n){
                if(small > arr[j+1][k]){
			small = arr[j+1][k];
			d = 3;
		}
        }
	dir[j][k]=d;
}
char trav(int j, int k){
	switch(dir[j][k]){
		case 0 : ans[j][k] = (ans[j-1][k]!='.') ? ans[j-1][k] : trav(j-1, k); break;
		case 1 : ans[j][k] = (ans[j][k-1]!='.') ? ans[j][k-1] : trav(j, k-1); break;
		case 2 : ans[j][k] = (ans[j][k+1]!='.') ? ans[j][k+1] : trav(j, k+1); break;
		case 3 : ans[j][k] = (ans[j+1][k]!='.') ? ans[j+1][k] : trav(j+1, k); break;
		default: paint++; ans[j][k]=paint; break;
	}
	return ans[j][k];
}
int main(){
	int T;	
	cin >> T;
	for(int i=1; i<=T; i++){
		printf("Case #%d:\n", i);
		scanf("%d %d", &n, &m);
		for(int j=0; j<n; j++)
		for(int k=0; k<m; k++)
			scanf("%d", &arr[j][k]);
		for(int j=0; j<n; j++)
                for(int k=0; k<m; k++){
			mark(j,k);	
		}
		paint = 'a'-1;
		memset(ans, '.', 105*105);
		for(int j=0; j<n; j++)
                for(int k=0; k<m; k++){
			if(ans[j][k]=='.'){
				trav(j,k);
			}
		}
		/*for(int j=0; j<n; j++)
                for(int k=0; k<m; k++){
			balance(j,k);
		}*/
		for(int j=0; j<n; j++){
                for(int k=0; k<m; k++)
                        cout<< ans[j][k]<< " ";
                        cout<<endl;
                }
	}
	return 0;
}
