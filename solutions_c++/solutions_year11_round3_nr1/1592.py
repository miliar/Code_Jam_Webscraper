// A.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <map>
#include <math.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* in = freopen("input.txt", "r", stdin);
	FILE* out = freopen("output.txt", "w", stdout);

	int T;
	cin>>T;
	for(int t=0; t<T; t++){
		int r, c;
		cin>>r>>c;
		char** mas = new char*[r];
		for(int i=0; i<r; i++){
			mas[i] = new char[c+1];
			cin>>mas[i];
		}

		cout<<"Case #"<<t+1<<":\n";

		bool pos = true;

		for(int i=0; (i<r) && pos ; i++)
			for(int j=0; (j<c) && pos; j++)
				if(mas[i][j] == '#'){
					if( (j== c-1) || (i==r-1) || (mas[i][j+1]!='#') || (mas[i+1][j]!='#') || (mas[i+1][j+1]!='#') ){
						cout<<"Impossible\n";
						pos = false;
					}else{
						mas[i][j] = '/';
						mas[i][j+1] = '\\';
						mas[i+1][j] = '\\';
						mas[i+1][j+1] = '/';
					}
				};
		
		if(pos){
			for(int i=0; i<r; i++){
				for(int j=0; j<c; j++)
					cout<<mas[i][j];
				cout<<endl;
			}
		}

		for(int i=0; i<r; i++){
			delete[] mas[i];
		}
		delete[] mas;

	}

	fclose(in);
	fclose(out);
	return 0;
}

