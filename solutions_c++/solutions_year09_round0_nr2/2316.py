#include<iostream>
#include<cstring>
using namespace std;

int arr[101][101];
char label[101][101];
char ch;
int m,n;

char fun(int i,int j){
	//cerr<<i<<" "<<j<<"\n";
	int mini=i,minj=j,value=arr[i][j];
	
	if(i>0 && value>arr[i-1][j]){
		mini=i-1; minj=j; value=arr[i-1][j];
	}
	if(j>0 && value>arr[i][j-1]){
		minj=j-1; mini=i; value=arr[i][j-1];
	}
	if(j<n-1 && value>arr[i][j+1]){
		minj=j+1; mini=i; value=arr[i][j+1];
	}
	if(i<m-1 && value>arr[i+1][j]){
		mini=i+1; minj=j; value=arr[i+1][j];
	}
	
	
	if(mini==i&&minj==j){
		if(!label[i][j]){
			label[i][j]=++ch;
			return ch;
		}
		else{
			return label[i][j];
		}
	}
	else{
		label[i][j]=fun(mini,minj);
		return label[i][j];
	}
}

int main(){
	int tc;
	scanf("%d",&tc);
	int ii=1;
	while(tc--){
	printf("Case #%d:\n",ii++);
		ch='a'-1;
		scanf("%d%d",&m,&n);
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++)
				scanf("%d",&arr[i][j]);
			
		memset(label,0,sizeof label);
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++){
				if(!label[i][j])
				{
					fun(i,j);
				}
				
				printf("%c%c",label[i][j],(j==n-1)?'\n':' ');
			}
	}	
}
