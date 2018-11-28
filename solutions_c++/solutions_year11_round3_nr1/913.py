#include<cstdio>
#include<iostream>
#include<string>
using namespace std;

string a[55];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("a.ans","w",stdout);
	int t,cs = 1,i,j,n,m;
    cin>>t;
	while(t--){
		cin>>n>>m;
		for(i = 0;i<n;i++){
			cin>>a[i];
			
		}
		
		for(i = 0;i<n-1;i++){
			for(j = 0;j<m-1;j++){
				if(a[i][j]!='#') continue;
				if(a[i][j+1]=='#' && a[i+1][j]=='#' && a[i+1][j+1]=='#'){
					a[i][j] = a[i+1][j+1] = '/';
					a[i+1][j] = a[i][j+1]='\\';
				}
				
			}
		}
		for(i = 0;i<n;i++){
			for(j = 0;j<m;j++){
				if(a[i][j]=='#') break;
				
			}
			if(j<m) break;
		}
		printf("Case #%d:\n",cs++);
		if(i<n) puts("Impossible");
		else{
			for(i = 0;i<n;i++) cout<<a[i]<<endl;
		}
	}
    return 0;
}
