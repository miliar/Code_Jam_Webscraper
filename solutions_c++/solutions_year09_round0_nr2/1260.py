#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;

int n,m;
int data[200][200];
int diry[5]={-1,0,0,1,};
int dirx[5]={0,-1,1,0,};
int col[200][200];
int go[200][200];

void init(){
	
}

void input(){
	cin >> n >> m;

	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin >> data[i][j];
		}
	}

}

bool outrange(int yy,int xx){
	if (yy<0 || yy>=n) return 1;
	if (xx<0 || xx>=m) return 1;
	return 0;
}

void fil(int y,int x,int c){
	col[y][x]=c;
	for(int k=0;k<4;k++){
		int newy,newx;
		newy=y+diry[k];
		newx=x+dirx[k];

		if (outrange(newy,newx)) continue;

		if (col[newy][newx]!=-1) continue;
		if ( go[newy][newx] == k ) {
			fil(newy,newx,c);
		}
	}	
}

void process(){
	int nb=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			col[i][j]=-1;
		}
	}

	int min;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			min=1000000;
			go[i][j]=-1;
			for(int k=0;k<4;k++){								
				int newx,newy;
				newy=i+diry[k];newx=j+dirx[k];
				if (outrange(newy,newx)) continue;

				if (min>data[newy][newx]) {
					min=data[newy][newx];
					go[i][j]=3-k;
				}
			}
			if (min >= data[i][j] ) go[i][j]=-1;
		}
	}

		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				int ox=0;
				for(int k=0;k<4;k++){
					int newx,newy;
					newy=i+diry[k];newx=j+dirx[k];
					if (outrange(newy,newx)) continue;
					if (data[newy][newx]<data[i][j]) ox=1;
				}
				if (ox==0){
					fil(i,j,nb);

					//it's basin
					nb++;
				}
			}
		}

		char al[100];
		int nal;

		nal=0;

		int check[100];
		for(int i=0;i<100;i++){
			check[i]=0;
		}

		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if (check[col[i][j]]==0){
					check[col[i][j]]=1;
					al[col[i][j]]='a'+nal;
					nal++;
				}
			}
		}

		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cout << al[col[i][j]] <<" ";
			}
			cout << endl;
		}

	}


	int main(){
		int t;
		cin >> t;
		for(int i=0;i<t;i++){
			init();
			input();
			cout << "Case #"<<i+1<<": "<<endl;
			process();

		}
		return 0;
	}
