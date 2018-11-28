#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main(int argc , char** argv){

	ifstream ifs;
	if(argc>1){
		ifs.open(argv[1]);
	}else{
		ifs.open("input.txt");
	}
	if(!ifs.good())
		return -1;

	int iSize=0;
	ifs >> iSize;

	ofstream ofs("output.txt");
	for(int isz=0;isz<iSize;isz++){
		int R, C;

		ifs >> R >> C;


		int** tile = new int*[R];
		for(int ir=0;ir<R;ir++){
			tile[ir] = new int[C];
			string str;
			ifs >> str;
			for(int ic=0;ic<C;ic++){
				if(str[ic] == '.'){
					tile[ir][ic] = 0;
				}else{
					tile[ir][ic] = 1;
				}
			}
		}
		bool bpos = true;
		for(int ir=0;ir<R;ir++){
			for(int ic=0;ic<C;ic++){
				if(tile[ir][ic] == 1){
					if(ir == R-1 || ic == C-1){
						bpos = false;
						break;
					}else{
						if(tile[ir][ic+1] == 1 && tile[ir+1][ic] == 1 && tile[ir+1][ic+1] == 1){
							tile[ir][ic] = 2;
							tile[ir][ic+1] = 3;
							tile[ir+1][ic] = 3;
							tile[ir+1][ic+1] = 2;
						}else{
							bpos = false;
							break;
						}
					}
				}
			}
			if(!bpos)
				break;
		}

		if(bpos){
			cout << "Case #" << isz+1 << ":" << endl;
			ofs << "Case #" << isz+1 << ":" << endl;
			for(int ir=0;ir<R;ir++){
				for(int ic=0;ic<C;ic++){
					switch(tile[ir][ic]){
						case 0:
							cout << ".";
							ofs << ".";
							break;
						case 1:
							cout << "#";
							ofs << "#";
							break;
						case 2:
							cout << "/";
							ofs << "/";
							break;
						case 3:
							cout << "\\";
							ofs << "\\";
							break;
					}
				}
				cout << endl;
				ofs << endl;
			}
		}else{
			cout << "Case #" << isz+1 << ":" << endl;
			cout << "Impossible" << endl;
			ofs << "Case #" << isz+1 << ":" << endl;
			ofs << "Impossible" << endl;
		}

		for(int ir=0;ir<R;ir++){
			delete[] tile[ir];
		}
		delete[] tile;
	}

	ifs.close();
	ofs.close();

	return 0;
}
