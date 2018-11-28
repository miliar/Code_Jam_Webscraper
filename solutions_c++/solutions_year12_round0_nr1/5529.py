#include <fstream>
using namespace std;

int main(){
	string const eng="abcdefghijklmnopqrstuvwxyz ";
	string const ggl="ynficwlbkuomxsevzpdrjgthaq ";
	string linea;
	bool found=false;
	char c;
	
	ifstream fin("gcj1.in");
	ofstream fout("gcj1.out");
	
	int ncases;
	fin >> ncases;
	int i=0;
	while(i<ncases && getline(fin,linea)){
		if(linea!=""){
			fout << "Case #" << i+1 << ": ";
			for(unsigned int j=0;j<linea.size();j++){
				found=false;
				for(int k=0;k<27 && found==false;k++){
					if(linea.at(j) == ggl.at(k)){
						c=eng.at(k);
						found=true;
					}
				}
				if(!found){
					c='_';
				}
				fout << c;
			}
			fout << endl;
			i++;
		}
	}
	
	return 0;
}
