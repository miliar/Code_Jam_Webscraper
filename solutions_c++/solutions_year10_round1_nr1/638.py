#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#define MAX 100
using namespace std;
char in[MAX][MAX];
char r[MAX][MAX];
int n,K;
void Rotate(){
	int i,j,k,l;
		for(i=0,j=0;j<n;i++,j++){
			for(k=0,l=n-1;l>=0;l--,k++){
				r[i][k]=in[l][j];
		//		printf("%c",r[i][k]);
			}

		//	printf("\n");
				
		}

	
}
void Fix(){
	int k;
	char c;
	for(int i=n-1;i>=0;i--){
		for(int j=0;j<n;j++){
			if(r[i][j]=='R' || r[i][j]=='B'){
				k=i;
				k++;
				c=r[i][j];
				while(r[k][j]=='.' && k<n) k++;
				r[i][j]='.';
				r[k-1][j]=c;
				
			}

		}
	}
}


void Show(){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++) printf("%c",r[i][j]);
		printf("\n");
	}
}
void Check(){
	int n1;
	int n2;
	n1=n2=0;
	int ns;
	int k,z;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(r[i][j]=='R'){
				ns=0;
				//horizontal
				k=j;
				while(r[i][k]=='R' && k<n){
					ns++;
					k++;
				}

				if(ns==K) n1=1;

				//vertical
				k=i;
				ns=0;
				while(r[k][j]=='R' && k<n){
					k++;
					ns++;
				}

				if(ns==K) n1=1;

				//right diagonal
				k=i; z=j;
				ns=0;
				while(r[k][z]=='R' && k<n && z<n){
					ns++;
					k++;
					z++;
				}

				if(ns==K) n1=1;

				//left diagonal
				k=i; z=j;
				ns=0;
				while(r[k][z]=='R' && k<n && z>=0 ){
					ns++;
					k++;
					z--;
				}

				if(ns==K) n1=1;


		
			}


			else if(r[i][j]=='B'){
				ns=0;
				//horizontal
				k=j;
				while(r[i][k]=='B' && k<n){
					ns++;
					k++;
					
				}
				
				if(ns==K) n2=1;

				//vertical
				k=i;
				ns=0;
				while(r[k][j]=='B' && k<n){
					k++;
					ns++;
				}

				if(ns==K) n2=1;

				//right diagonal
				k=i; z=j;
				ns=0;
				while(r[k][z]=='B' && k<n && z<n){
					ns++;
					k++;
					z++;
				}

				if(ns==K) n2=1;

				//left diagonal
				k=i; z=j;
				ns=0;
				while(r[k][z]=='B' && k<n && z>=0 ){
					ns++;
					k++;
					z--;
				}

				if(ns==K) n2=1;




			}

			
		
		
		
		}
	}


	if(n1==0 && n2==0) printf("Neither\n");
	else if(n1==1 && n2==0) printf("Red\n");
	else if(n1==0 && n2==1) printf("Blue\n");
	else printf("Both\n");
}
int main(){
//	freopen("A-large.in","r",stdin);
//	freopen("out.txt","w",stdout);
	int tc,i,j;
	cin>>tc;
	for(int z=0;z<tc;z++){
		cin>>n>>K;
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				cin>>in[i][j];
			}
		}

		Rotate();
		Fix();
	//	Show();
		printf("Case #%d: ",z+1);
		Check();

			
		

		
	}
	return 0;
}