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
#include <deque>
#include <queue>
#include <stack>

//C�̃N���X
#include <stdio.h>
#include <math.h>

#include <stdlib.h>
#include <stdio.h>

//�萔�͂����Œ�`���܂��傤�B
#define PROG_SUCCESS true
#define PROG_FAIL false
#define COL_O 0
#define COL_B 1

int otask[100];
int btask[100];

using namespace std;

struct step{  //�O��̃X�e�b�v�̋L�^
	int  type;   //0 orange, 1 blue
	int  move;     //stay��Ԃ��ǂ����H
};


int main(void){
	int T=0;  //�e�X�g�P�[�X
	int N=0;  //1�P�[�X���Ƃ̃W���u��
	int stackStep=0; //�A�����ē����F�̃X�e�b�v���L�^����ϐ�
	char char_tmp=0;
	int result=0;
	int k=1,tmp1;
	step befstep,nowstep;
//	int oPos=0,bPos=0;

	int robot[2];  //0��orange,1��blue
	robot[COL_O] = 1;
	robot[COL_B] = 1;


    cout << "START" << endl;
	//�ŏ���T�̒l��ǂݍ���
	cin >> T;

	while( T > 0 ){
		T--;
		cin >> N;  //N�̉񐔂�ǂݍ���

//		cout << "#DEBUG T= " << T << endl;
		robot[COL_O] = 1;
		robot[COL_B] = 1;
		result = 0;
		stackStep=0;
		befstep.move=0;
		befstep.type=-1;
		nowstep.move=0;
		nowstep.type=-1;

		//�^�X�N���i�[���鏈��
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
				nowstep.move = abs(robot[COL_O]-tmp1)+1; //�O�񂩂�̈ړ�����+�{�^����move�Ƃ��ăJ�E���g
			    robot[COL_O] = tmp1;
			}else{
				nowstep.type=COL_B;
				cin >> tmp1;
				nowstep.move = abs(robot[COL_B]-tmp1)+1;//�O�񂩂�̈ړ�����+�{�^����move�Ƃ��ăJ�E���g
				robot[COL_B] = tmp1;
			}
	//		cout << "DEBUG move = " << nowstep.move << endl;

			//�O��Ɠ�����ނ̏ꍇ�́A�ړ��ƑO��̃{�^��������X�^�b�N�Ƃ��ĕۑ��B��Ōv�Z����B
			if (befstep.type==nowstep.type){
				stackStep += nowstep.move;
			}

			if (befstep.type!=nowstep.type){
				//�X�^�b�N�̂ق����傫���ꍇ��stay������B
				if(stackStep >= nowstep.move){
					result += stackStep;
					stackStep=1;
				}
				//�X�^�b�N�̂ق����������ꍇ��stay���Ȃ��B
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
