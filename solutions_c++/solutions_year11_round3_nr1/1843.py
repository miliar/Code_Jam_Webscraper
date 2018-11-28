/*
 * main.cpp
 *  for GoogleCodeJam 2011 Round1-C _ a
 *  Created on: 2011/05/22
 *      Author: Maloney
 */


//いつものライブラリ様たち
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

//Cのクラス
#include <stdio.h>
#include <math.h>
#include <stdlib.h>



//定数はここで定義しましょう。
#define PROG_SUCCESS true
#define PROG_FAIL false

using namespace std;


int main(void){
	int T=0, tmpT;  //テストケース
	int N=0, tmpN;  //1ケースごとのジョブ数
	int i,j,k;
	int R,C,tmpR,tmpC;
	int count;

	char input[52][52];
	string tmpS;
	bool FailFlag = false;

	cout << "START" << endl;
	cin >> T;

	count = 0;

	while( T > 0 ){
		T--;
		cin >> R >> C;
		tmpN = N;
		FailFlag = false;
		for(int i =0; i<52; i++){
			for(int j =0; j<52; j++)
				input[i][j]='.';
		}
		//入力受付
		tmpR = R;
		while(tmpR>0){
			cin >> tmpS;

			for (int i=1; i <= C; i++){
					input[R+1-tmpR][i]=tmpS[i-1];
			}
			tmpR--;
		}

		for(int i =0; i<=R+1; i++){
			for(int j =0; j<=C+1; j++){
				if (input[i][j]== '#'){
					if (   (input[i+1][j] == '#')
						&& (input[i][j+1] == '#')
						&& (input[i+1][j+1] == '#')){

						input[i][j]='/';
						input[i+1][j+1]='/';
						input[i+1][j]=0x5C;
						input[i][j+1]=0x5C;

						//input[i+1][j] = '\';
						//input[i][j+1] = '\';
					}
					else{
						FailFlag = true;
						break;
					}

				}
			}

			if (FailFlag==true){
				break;
			}
		}

		//
		if (FailFlag==true){
			cout << "Case #" << ++count << ":" << endl;
			cout << "Impossible" << endl;
		}
		else{
			cout << "Case #" << ++count << ":" << endl;
			for(int i =1; i<=R; i++){
				for(int j =1; j<=C; j++){
					cout << input[i][j];
				}
				cout << endl;
			}

		}

	}
}


/*
		//表示
		for(int i =0; i<=R+1; i++){
			cout << i << ", " << j <<": ";
			for(int j =0; j<=C+1; j++){
				cout << input[i][j] << ",";
			}
			cout << endl;
		}*/
		//			cout << "Case #" << ++count << ": Possible" << endl;
