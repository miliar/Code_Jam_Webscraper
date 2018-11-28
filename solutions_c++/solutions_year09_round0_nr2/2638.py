#include<iostream>
using namespace std;
enum dir{North,West,East,South,I};
void markbasin(char basin[][100],dir adj[][100], int H,int W){
	char curr ='a'; 
	for(int i=0;i<H;i++)
		for(int j=0;j<W;j++){
			if(basin[i][j]=='0'){
				int ti=i,tj=j;
				while(adj[ti][tj]!=I){
					switch(adj[ti][tj]){
						case North:	ti--;
									break;
						case West:	tj--;
									break;
						case East: 	tj++;
									break;	
						case South: ti++;
									break;
					}
				}
				if(basin[ti][tj]=='0'){
					basin[ti][tj]=curr;
					curr++;
				}
				char label=basin[ti][tj];
				ti=i;tj=j;
				while(adj[ti][tj]!=I){
					basin[ti][tj]=label;
					switch(adj[ti][tj]){
						case North:	ti--;
									break;
						case West:	tj--;
									break;
						case East: 	tj++;
									break;	
						case South: ti++;
									break;
					}
				}
			}
		}
}
int main(){
	/*freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);*/
	int totalcases;
	cin>>totalcases;
	for(int cases=1;cases<=totalcases;cases++){
	int H,W;
	cin>>H>>W;
	int alt[100][100];
	char basin[100][100];
	dir adj[100][100];	
	
	for(int i=0;i<H;i++)
		for(int j=0;j<W;j++){
			cin>>alt[i][j];
			basin[i][j]='0';
			adj[i][j]=I;
		}
	for(int i=0;i<H;i++)
		for(int j=0;j<W;j++){
			int min = alt[i][j];			
			if(i!=0 && alt[i-1][j]<min){
				min=alt[i-1][j];
				adj[i][j] = North;
			}
			if(j!=0 && alt[i][j-1]<min){
				min=alt[i][j-1];
				adj[i][j] = West;
			}
			if(j!=W-1 && alt[i][j+1]<min){
				min=alt[i][j+1];
				adj[i][j] = East;
			}
			if(i!=H-1 && alt[i+1][j]<min){
				min=alt[i+1][j];
				adj[i][j] = South;
			}
		}
	/*cout<<"altitude"<<endl;
	for(int i=0;i<H;i++){
		for(int j=0;j<W;j++){
			cout<<alt[i][j]<<" ";		
		}
		cout<<endl;
	}
	cout<<"adjacency"<<endl;
	for(int i=0;i<H;i++){
		for(int j=0;j<W;j++){
			cout<<adj[i][j]<<" ";		
		}
		cout<<endl;
	}
	cout<<"before"<<endl;*/
	markbasin(basin,adj,H,W);
	//cout<<"after"<<endl;
	printf("Case #%d:\n",cases);
	for(int i=0;i<H;i++){
		for(int j=0;j<W-1;j++){
			cout<<basin[i][j]<<" ";		
		}
		cout<<basin[i][W-1]<<endl;
	}
	}
	return 0;
}
