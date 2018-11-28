/*
 * main.cpp
 *
 *  Created on: 2011/05/07
 *      Author: XXX
 */

//�����̃��C�u�����l����
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

//C�̃N���X
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

//�萔�͂����Œ�`���܂��傤�B
#define PROG_SUCCESS true
#define PROG_FAIL false

#define XX01 0x01

using namespace std;

unsigned int checkSum[20];

//const XX01 = 0x01;


int main(void){
	int T=0;  //�e�X�g�P�[�X
	int N=0;  //1�P�[�X���Ƃ̃W���u��

	multiset<int> piles;
	int cou=1;
	int iTmp1;

	int i;
	long long int sum=0;
	bool cry=false;

//    cout << "START" << endl;
	//�ŏ���T�̒l��ǂݍ���
	cin >> T;

	while( T > 0 ){
		T--;
		cin >> N;  //N�̉񐔂�ǂݍ���

		iTmp1=0;
		piles.clear();
		sum=0;
		cry=false;
		for(i=0;i<20;i++){
			checkSum[i]=0;
		}

		//���͂̃X�g�A�ƁA�r�b�g�̌v�Z�B
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

		//cry�̔���(pile��1�̏ꍇ�������Ńu���b�N)
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
