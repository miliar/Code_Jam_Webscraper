#include <iostream>
#include <vector>
#include <fstream>

using namespace std;


void read_matrix(ifstream &f, vector<vector<char> > &m, int r, int c){
m.resize(r);
for(int i=0;i<r;i++)
m[i].resize(c);

for(int i=0;i<r;i++){
	for(int j=0;j<c;j++){
		f >> m[i][j];
	}
}
}

bool check(vector<vector<char> > &m, int r, int c, int pos_x, int pos_y){
		if(pos_x+1<r && pos_y+1<c && m[pos_x+1][pos_y]=='#' && m[pos_x][pos_y+1]=='#' && m[pos_x+1][pos_y+1]=='#')
			return true;
		else
			return false;
}

bool scan(vector<vector<char> > &m, int r, int c){

	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){

			if(m[i][j]!='.' && m[i][j]!='\\' && m[i][j]!='/' ){

				if ( check(m,r,c,i,j) ){
				
					m[i][j] ='/';
					m[i][j+1] = '\\';
					m[i+1][j] = '\\';
					m[i+1][j+1] = '/';
				}
				else{
					return false;
				}
			}	
		}
	}
	return true;	
}

int main(int argc, char ** argv){

	ifstream f;
	int test_cases;
	int r,c;
	vector<vector< char> > m;

	f.open(argv[1]);
	f>> test_cases;
	
		

for(int k=0;k<test_cases;k++){
	f>>r >> c;
	read_matrix(f,m,r,c);

	
	if(scan(m,r,c)){
		cout << "Case #" << k+1 << ":\n" ;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout <<  m[i][j];
			}
			cout << endl;
		}
	}
	else{
		cout << "Case #" << k+1 << ":\n" ;
		cout << "Impossible" << endl;	
	}
}

	f.close();
}


