#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char* argv[]){

	ifstream fp;
	fp.open(argv[1]);

	if(fp.is_open()){
		int tc;
		fp>>tc;
		for(int i =1; i <= tc;i++){
			cout<<"Case #"<<i<<":"<<endl;
			int r,c;
			fp>>r>>c;
			vector<string> m;
			m.clear();
			for(int j = 0 ; j < r;j++){
				string tmp;
				fp>>tmp;
				m.push_back(tmp);
				//cout<<tmp<<endl;
			}
			for(int j = 0 ; j < r-1;j++){
				for(int k = 0 ; k < c-1; k++){
					if(m[j][k] == '#'
							&& m[j+1][k] == '#' 
							&& m[j][k+1] == '#'
							&& m[j+1][k+1] == '#'){
						m[j][k] ='/';
						m[j+1][k] ='\\';
						m[j][k+1] ='\\';
						m[j+1][k+1] ='/';

					}
				}
			}
			bool is_sol = true;
			for(int j = 0 ; j < r;j++){
				for(int k = 0 ; k < c; k++){
					if(m[j][k] == '#'){
						is_sol = false;
					}
				}
			}
			if(is_sol){

				for(int j = 0 ; j < r;j++){
					cout<<m[j]<<"\n";
				}
			}
			else
				cout<<"Impossible\n";

		}
	
	}


	return 0;
}
