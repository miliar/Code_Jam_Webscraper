/*
 * main.cpp
 *
 *  Created on: 2011/05/07
 *      Author: XXX
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
#include <stdio.h>

//定数はここで定義しましょう。
#define PROG_SUCCESS true
#define PROG_FAIL false
#define COL_O 0
#define COL_B 1

int otask[100];
int btask[100];

using namespace std;

struct step{  //前回のステップの記録
	int  type;   //0 orange, 1 blue
	int  move;     //stay状態かどうか？
};


int main(void){
	int T=0;  //テストケース
	int N=0;  //1ケースごとのジョブ数
	int stackStep=0; //連続して同じ色のステップを記録する変数
	char char_tmp=0;
	int result=0;
	int k=1,tmp1;
	step befstep,nowstep;
//	int oPos=0,bPos=0;

	int robot[2];  //0がorange,1がblue
	robot[COL_O] = 1;
	robot[COL_B] = 1;


    cout << "START" << endl;
	//最初のTの値を読み込む
	cin >> T;

	while( T > 0 ){
		T--;
		cin >> N;  //Nの回数を読み込む

//		cout << "#DEBUG T= " << T << endl;
		robot[COL_O] = 1;
		robot[COL_B] = 1;
		result = 0;
		stackStep=0;
		befstep.move=0;
		befstep.type=-1;
		nowstep.move=0;
		nowstep.type=-1;

		//タスクを格納する処理
		while(N > 0)
		{
			befstep.move = nowstep.move;
			befstep.type= nowstep.type;

			N--;
		//	cout << "#DEBUG N= " << N << endl;
			cin >> char_tmp;
			if (char_tmp == 'O'){
				nowstep.type=COL_O;
				cin >> tmp1;
				nowstep.move = abs(robot[COL_O]-tmp1)+1; //前回からの移動距離+ボタンをmoveとしてカウント
			    robot[COL_O] = tmp1;
			}else{
				nowstep.type=COL_B;
				cin >> tmp1;
				nowstep.move = abs(robot[COL_B]-tmp1)+1;//前回からの移動距離+ボタンをmoveとしてカウント
				robot[COL_B] = tmp1;
			}
	//		cout << "DEBUG move = " << nowstep.move << endl;

			//前回と同じ種類の場合は、移動と前回のボタン動作をスタックとして保存。後で計算する。
			if (befstep.type==nowstep.type){
				stackStep += nowstep.move;
			}

			if (befstep.type!=nowstep.type){
				//スタックのほうが大きい場合はstayがある。
				if(stackStep >= nowstep.move){
					result += stackStep;
					stackStep=1;
				}
				//スタックのほうが小さい場合はstayがない。
				else if (stackStep < nowstep.move){
					result += stackStep;
					stackStep = nowstep.move-stackStep;
				}
			}

		}
		result += stackStep;

		cout << "Case #" << k++ << ": " << result << endl;
	}

}
