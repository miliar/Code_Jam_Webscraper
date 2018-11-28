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
//#include <multiset>
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

#define XX01 0x01

using namespace std;

unsigned int checkSum[20];

//const XX01 = 0x01;


int main(void){
	int T=0;  //テストケース
	int N=0;  //1ケースごとのジョブ数

	multiset<int> piles;
	int cou=1;
	int iTmp1;

	int i;
	long long int sum=0;
	bool cry=false;

//    cout << "START" << endl;
	//最初のTの値を読み込む
	cin >> T;

	while( T > 0 ){
		T--;
		cin >> N;  //Nの回数を読み込む

		iTmp1=0;
		piles.clear();
		sum=0;
		cry=false;
		for(i=0;i<20;i++){
			checkSum[i]=0;
		}

		//入力のストアと、ビットの計算。
		while(N > 0)
		{
			N--;
			cin >> iTmp1;
			piles.insert(iTmp1);
			sum += iTmp1;
			for(i=0;i<20;i++){
				checkSum[i] += ((1 << i) & iTmp1) >> i;
			}
		}

		//cryの判定(pileが1個の場合もここでブロック)
		i=0;
		while( i<20){
//			cout << i << ": " << checkSum[i] << endl;
			if ( 1==(checkSum[i++] % 2)){
				cry=true;
			}
		}
		if (cry){
			cout << "Case #" << cou++ << ": NO" << endl;
		}
		else{
			multiset<int>::iterator it = piles.begin();
			sum = sum - *it;

			cout << "Case #" << cou++ << ": " << sum << endl;
		}

	}
}

/*do
{
	cout << *it << endl;
}while( it-- != piles.begin() );
*/
/*			i=piles.size();
while( i>=0 ){
    cout << piles[i-1] << endl;
//				cout <<  i << ": " << iTmp1 << endl;
	i++;
}*/

/*
		multiset<int>::iterator it = piles.begin();
		while( it != piles.end() )
			{
				cout << (*it).first << ":" << (*it).second << endl;
				it++;
			}
*/
