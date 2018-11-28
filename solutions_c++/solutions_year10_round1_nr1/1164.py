#include<iostream>
#include<algorithm>
#include<string>
#include<cstdio>

using namespace std;

#define NN 50

int n;
char AA[NN][NN];
void print(char AA[NN][NN]);

int main()
{
	int t;
	cin>>t;
	int g=0;
	while(t--){
		g++;
		int k;
		scanf("%d",&n);
		scanf("%d",&k);
		for(int i=0;i<n; i++){
			for(int j=0;j<n; j++){
				AA[i][j]='.';
			}
		}

		for (int i = n-1; i>= 0; i--) {
			for (int j = 0; j <n; j++) {
				cin>>AA[j][i];
			}
		}

	      	for(int j=0; j<n; j++){
	      		for(int i=n-1; i>=1; i--){
				int counter=0;
		  		while(AA[i][j]=='.' && counter<=i){
					counter++;
					for(int m=i; m>=1; m--){
						AA[m][j]=AA[m-1][j];
					
					}
					AA[0][j]='.';
				}
			}
		}
//		print(AA);
		int flag1=0;
		int flag2=0;
		for(int x=0; x<n; x++){
			for(int y=0; y<n; y++){
			        char ss=AA[x][y];
				int count=0;
				if(ss=='B' || ss=='R'){
					count=1;		
					for(int z=1; z<k; z++){
						if(y+z<n && AA[x][y+z]==ss){
							count++;
						}else{
							break;
						}
					}
					if(count>=k && ss=='B')	flag1=1;
					if(count>=k && ss=='R')   flag2=1;
					
					count=1;
					for(int z=1; z<k; z++){
						if(x+z<n && AA[x+z][y]==ss){
							count++;
						}else{
						       	break;
						}
					}
					if(count>=k && ss=='B') flag1=1;
					if(count>=k && ss=='R')   flag2=1;
						
					count=1;
					for(int z=1; z<k; z++){
						if(x+z<n && y+z<n && AA[x+z][y+z]==ss){
							count++;
						}else{
							break;
						}
					}
					if(count>=k && ss=='B') flag1=1;
					if(count>=k && ss=='R')   flag2=1;

					count=1;
					for(int z=1;z<k; z++){
						if(x+z<n && y-z >=0 && AA[x+z][y-z]==ss){
							count++;
						}else{
							break;
						}
					}
					
					if(count>=k && ss=='B') flag1=1;
					if(count>=k && ss=='R')   flag2=1;
				}
			
			}
		}
	//	print(AA);
		if(flag1==1 && flag2==1) cout<<"Case #"<<g<<": Both"<<endl;
		else if(flag1==1 && flag2==0) cout<<"Case #"<<g<<": Blue"<<endl; 
		else if(flag1==0 && flag2==1) cout<<"Case #"<<g<<": Red"<<endl; 
		else if(flag1==0 && flag2==0) cout<<"Case #"<<g<<": Neither"<<endl; 		
	}
	return 0;
}

void print(char AA[NN][NN])
{
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			cout<<AA[i][j]<<" ";
		}
		cout<<endl;
	}
}
