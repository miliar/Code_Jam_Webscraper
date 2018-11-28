#include <iostream>
#include <fstream>
using namespace std;
int main(){
	int n;
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	fin>>n;
	char input;
	int O[4][4];
	int X[4][4];
	int line;
	int sum;
	for(int k=0;k<n;k++){
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				fin>>input;
				if(input=='O') {
					O[i][j]=2;
					X[i][j]=0;
				}
				if(input=='X') {
					O[i][j]=0;
					X[i][j]=2;
				}
				if(input=='T') {
					O[i][j]=2;
					X[i][j]=2;
				}
				if(input=='.') {
					O[i][j]=1;
					X[i][j]=1;					
				}
			}
		}
		sum=0;
		line=1;
		for(int i=0;i<4;i++){
			line=1;
			for(int j=0;j<4;j++){
				line=line*O[i][j];
			}
			
			if(line==16){
				fout<<"Case #"<<k+1<<": O won"<<endl;
				break;
			};
			sum=sum+line;
			line=1;
			for(int j=0;j<4;j++){
				line=line*X[i][j];
			}		
			if(line==16){
				fout<<"Case #"<<k+1<<": X won"<<endl;
				break;
			};
			sum=sum+line;		
		}
		if(line==16)continue;
		for(int j=0;j<4;j++){
			line=1;
			for(int i=0;i<4;i++){
				line=line*O[i][j];
			}
			if(line==16){
				fout<<"Case #"<<k+1<<": O won"<<endl;
				break;
			};			
			sum=sum+line;
			line=1;
			for(int i=0;i<4;i++){
				line=line*X[i][j];
			}
			if(line==16){
				fout<<"Case #"<<k+1<<": X won"<<endl;
				break;
			};
			sum=sum+line;			
		}
		if(line==16)continue;
		line=1;
		for(int i=0;i<4;i++){
				line=line*O[i][i];
		}
		if(line==16){
				fout<<"Case #"<<k+1<<": O won"<<endl;
				continue;
		};
		sum=sum+line;
		line=1;
		for(int i=0;i<4;i++){
				line=line*O[i][3-i];
		}
		if(line==16){
				fout<<"Case #"<<k+1<<": O won"<<endl;
				continue;
		};
		sum=sum+line;
		line=1;
		for(int i=0;i<4;i++){
				line=line*X[i][i];
		}
		if(line==16){
				fout<<"Case #"<<k+1<<": X won"<<endl;
				continue;
		};
		sum=sum+line;
		line=1;
		for(int i=0;i<4;i++){
				line=line*X[i][3-i];
		}
		if(line==16){
				fout<<"Case #"<<k+1<<": X won"<<endl;
				continue;
		};
		sum=sum+line;
		if(sum==0)fout<<"Case #"<<k+1<<": Draw"<<endl;
		else fout<<"Case #"<<k+1<<": Game has not completed"<<endl;
	}
	return 0;
}
