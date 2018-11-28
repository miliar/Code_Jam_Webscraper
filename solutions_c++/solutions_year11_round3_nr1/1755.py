#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <fstream>
#include <string>
#include <vector>
#include <conio.h>
#include <Windows.h>

/* ==================
    Here are comments
================== */

using namespace std;



void mainFunction(){
	freopen( "input.txt", "r", stdin );
	freopen( "response.txt", "w", stdout );

    int test_cases;
    cin >> test_cases;

    int i, j, k;
    int rows, cols;

    vector <string> map;

    string temp_str;

    bool imposible, diez;

    for(i = 0; i < test_cases; i++){
    	cin >> rows >> cols;
    	map.clear();
    	for(j=0;j<rows;j++){
    		cin >> temp_str;
    		map.push_back(temp_str);
    	}

    	imposible = false;

    	// test
    	diez = true;
    	while(true){
    		diez = false;
    		for(j=0;j<rows;j++){
				for(k=0;k<cols;k++){
					if(map[j][k] == '#'){
						diez = true;
						if(j < rows-1 && k < cols-1 && map[j+1][k] == '#' && map[j][k+1] == '#' && map[j+1][k+1] == '#'){
							map[j][k] = '/';
							map[j+1][k] = '\\';
							map[j][k+1] = '\\';
							map[j+1][k+1] = '/';
						}else{
							// imposible
							imposible = true;
							diez = false;
						}
					}
					if(imposible)
						break;
				}
				if(imposible)
					break;
    		}
    		if(!diez)
				break;
    	}

    	cout << "Case #" << i+1 << ":" << endl;
    	if(imposible)
			cout << "Impossible" << endl;
		else
			for(j=0;j<rows;j++){
				cout << map[j] << endl;
			}
    }
}

int main(){
    int begin, end;
    begin = clock();
    mainFunction();
    end = clock();
//    cout << "Time: " << ((double)( end - begin )/CLOCKS_PER_SEC ) << endl;
    return 0;
}
