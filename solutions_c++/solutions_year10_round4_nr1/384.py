#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;

class Dia{
public:
	int value[100][100];
	int insize;
	int size;
	int px;
	int py;
	Dia(int s){
		insize = s;
	}
	void clear(){
		memset(value,0,sizeof(int) * 100 * 100);
	}
	int get(int i, int j){
		if( i >= px && i < insize + px && j >= py && j < insize + py)
			return value[i-px][j-py];
		else return -1;
	}
	bool check(){
		for(int i = 0; i < size - 1; i++){
			for(int j = 0; j < size - i; j++){
				int v1 = get(i,j);
				int v2 = get(size - j - 1,size - i - 1);

				if(v1 == -1 || v2 == -1) continue;
				else if(v1 != v2) return false;
			}
			for(int j = i + 1; j < size; j++){
				int v1 = get(i,j);
				int v2 = get(j,i);
				if(v1 == -1 || v2 == -1) continue;
				else if(v1 != v2) return false;
			}
		}

		return true;
	}
	bool search(){
		int space = size - insize;
		//if(space == 0) return check();
		for(int i = 0 ; i <= space; i++)
			for(int j = 0; j <= space;j++)
			{
				px = i;
				py = j;
				if(check()) return true;
			}
		return false;
	}

};

int main(){
	ifstream in("input");
	ofstream out("output1");
	int cases;
	in >> cases;

	Dia dia(1);
	int size;
	for(int casenum = 1; casenum <= cases; casenum++){
		out << "Case #" << casenum << ": ";
		cout << "Case " << casenum << endl;

		dia.clear();
		in >> size;
		dia.insize = size;
		int temp;
		for(int i = 0; i < 2 * size - 1; i++){
			if(i < size){
				for(int j = 0; j <= i; j++){
					in >> temp;
					dia.value[i-j][j] = temp;
				}
			}
			else{
				for(int j = 0; j < 2 * size - i - 1; j++){
					in >> temp;
					dia.value[size - j - 1][i - size + j + 1] = temp;
				}
			}
		}
		/*
		for(int i = 0; i < size; i++){

			for(int j = 0 ; j < size; j++){
				cout << dia.value[i][j] << " ";
			}
			cout << endl;
		}*/
		dia.size = dia.insize;
		while(!dia.search()){
			dia.size++;
		}
		out << dia.size * dia.size - dia.insize * dia.insize << endl;



	}
	return 0;
}
