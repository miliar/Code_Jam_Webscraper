#include<iostream>
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out-large.out","w",stdout);
	int casen;
	scanf("%d",&casen);
	int casei;
	for(casei=0;casei<casen;casei++){
		int n,k;
		scanf("%d %d",&n,&k);
		char table[55][55]={0};
		int i,j,l;
		for(i=0;i<n;i++){
			scanf("%s",table[i]);
		}
		for(i=0;i<n;i++){
			int flag=n-1;
			for(j=n-1;j>=0;j--){
				if(table[i][j]!='.'){
					table[i][flag]=table[i][j];
					if(flag!=j)table[i][j]='.';
					flag=flag-1;
				}
			}
			//printf("%s\n",table[i]);
		}
		
		int wina=0;
		int winb=0;
		for(i=0;i<n;i++){

			for(j=0;j<n;j++){

				if(table[i][j]!='.'){
					for(l=1;l<k;l++){
						if(j+l<n && j+l>=0)
						if(table[i][j+l]!=table[i][j]){
							break;
						}
						else{
							if(l==k-1){
								if(table[i][j]=='R')wina=1;
								if(table[i][j]=='B')winb=1;
							}
						}
					}
					
					for(l=1;l<k;l++){
						if(i+l<n && i+l>=0)
						if(table[i+l][j]!=table[i][j]){
							break;
						}
						else{
							if(l==k-1){
								if(table[i][j]=='R')wina=1;
								if(table[i][j]=='B')winb=1;
							}
						}
					}
					
					
					for(l=1;l<k;l++){
						if(j+l<n && i+l<n && j+l>=0&& i+l>=0)
						if(table[i+l][j+l]!=table[i][j]){
							break;
						}
						else{
							if(l==k-1){
								if(table[i][j]=='R')wina=1;
								if(table[i][j]=='B')winb=1;
							}
						}
					}
					
					for(l=1;l<k;l++){
						if(j-l<n && i+l<n && j-l>=0&& i+l>=0)
						if(table[i+l][j-l]!=table[i][j]){
							break;
						}
						else{
							if(l==k-1){
								if(table[i][j]=='R')wina=1;
								if(table[i][j]=='B')winb=1;
							}
						}
					}
	
				}
			}
		}
		printf("Case #%d: ",casei+1);
		if(wina==1 && winb==1)printf("Both\n");
		if(wina==1 && winb==0)printf("Red\n");
		if(wina==0 && winb==1)printf("Blue\n");
		if(wina==0 && winb==0)printf("Neither\n");
		
	}
    //system("pause");
    return 0;
}
