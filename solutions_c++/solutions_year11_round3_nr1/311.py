#include <fstream>

using namespace std;

const int NMAX=50;

int main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t,ti;
	char mas[NMAX][NMAX],in[NMAX][NMAX];
	fin>>t;
	for(ti=1;ti<=t;++ti){
		memset(mas,'.',sizeof(char)*NMAX*NMAX);
		memset(in,0,sizeof(char)*NMAX*NMAX);
		char ch;
		int r,c;
		int i,j;

		fin>>r>>c;
		for(i=0;i<r;++i){
			for(j=0;j<c;++j){
				fin>>in[i][j];
			}
		}

		for(i=0;i<r;++i){
			for(j=0;j<c;++j){

				if(in[i][j]=='#'){
					if(i<r-1&&j<c-1&&in[i+1][j]=='#'&&in[i+1][j+1]=='#'&&in[i][j+1]=='#'&&in[i+1][j]=='#'){
						mas[i][j]='/';
						in[i][j]='.';

						mas[i+1][j]='\\';
						in[i+1][j]='.';

						mas[i][j+1]='\\';
						in[i][j+1]='.';

						mas[i+1][j+1]='/';
						in[i+1][j+1]='.';
					}
					else{
						fout<<"Case #"<<ti<<":"<<endl<<"Impossible"<<endl;
						break;
					}
				}

			}
			if(j<c){
				break;
			}
		}
		if(i<r){
			continue;
		}
		
		fout<<"Case #"<<ti<<":"<<endl;
		for(i=0;i<r;++i){
			for(j=0;j<c;++j){
				fout<<mas[i][j];
			}
			fout<<endl;
		}
	}

	return 0;
}