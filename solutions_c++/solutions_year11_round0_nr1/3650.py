// codejam1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;
	for(int t = 0; t < T; t++){
		int N, steps = 0, aim = 0, Opos = 1, Bpos = 1;
		int desPosNum[100];
		char desPosRobot[100];
		bool OcanMove = true, BcanMove = true;
		in >> N;
		for(int n = 0; n < N; n++){
			in >> desPosRobot[n] >> desPosNum[n];
		}
		while(aim < N){
			steps++;
			OcanMove = true;
			BcanMove = true;
			if(desPosRobot[aim] == 'O'){ // robot O press the button
				if(desPosNum[aim] == Opos){
					aim++;
					OcanMove = false;
				}
			} else { // 'B'
				if(desPosNum[aim] == Bpos){
					aim++;
					BcanMove = false;
				}
			}
			int oAim = aim, bAim = aim;
			// find the nearest task for robot O
			while(desPosRobot[oAim] != 'O' && oAim < N)oAim++;
			// find the nearest task for robot B
			while(desPosRobot[bAim] != 'B' && bAim < N)bAim++;
			if(oAim != N && OcanMove){
				if(Opos < desPosNum[oAim])Opos++;
				if(Opos > desPosNum[oAim])Opos--;
			}
			if(bAim != N && BcanMove){
				if(Bpos < desPosNum[bAim])Bpos++;
				if(Bpos > desPosNum[bAim])Bpos--;
			}
		}
		out << "Case #" << t + 1 << ": " << steps << endl;
	}
	return 0;
}

