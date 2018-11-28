//#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
ifstream cin("B-Large.in");
ofstream cout ("B.out");

int getlabel(int nl[105][105],int parents[105][105][3],int r,int c){
	if(nl[r][c]!=0) return nl[r][c];
	if(parents[r][c][2]>0){
		nl[r][c] = parents[r][c][2];
		return nl[r][c];
	}
	nl[r][c] = getlabel(nl,parents,parents[r][c][0],parents[r][c][1]);

	return nl[r][c];
}

int main(){
	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		int H,W;
		int EM[105][105]={0};
		int parents[105][105][3]={0};
		int nl[105][105]={0};		
		cin >> H >> W;
		for(int j=0;j<H;j++){
			for(int k=0;k<W;k++){
				cin >> EM[j][k];				
			}
		}//North West East South
		int z = 0;
		for(int j=0;j<H;j++){
			for(int k=0;k<W;k++){
				int row[]={j-1,j,j,j+1};
				int col[]={k,k-1,k+1,k};
				int lowr, lowc, lowval = 100000;
				for(int m=0;m<4;m++){
					if((0<=row[m])&&(row[m]<H)&&(0<=col[m])&&(col[m]<W)){
						if(EM[row[m]][col[m]]<lowval){
							lowval = EM[row[m]][col[m]];
							lowr = row[m];
							lowc = col[m];
						}
					}
				}
				if(lowval<EM[j][k]){
					//cout << j << " " << k << " " << lowr << " "  << lowc << endl;
					parents[j][k][0]=lowr;
					parents[j][k][1]=lowc;
					parents[j][k][2]=0;
				}
				else{
					z++;
					parents[j][k][0]=j;
					parents[j][k][1]=k;
					parents[j][k][2]=z;					
				}
			}
		}
		for(int j=0;j<H;j++)
			for(int k=0;k<W;k++)
				getlabel(nl,parents,j,k);
		int IDS[30]={0};
		char lb = 'a';
		for(int j=0;j<H;j++)
			for(int k=0;k<W;k++)
				if(IDS[nl[j][k]]==0) IDS[nl[j][k]]=lb++;
		cout <<"Case #"<<i+1<<":"<<endl;
		for(int j=0;j<H;j++){
			cout << char(IDS[nl[j][0]]) ;
			for(int k=1;k<W;k++)
				cout << " " << char(IDS[nl[j][k]]) ;
			cout << endl;
		}
				
	}
	return 0;
};