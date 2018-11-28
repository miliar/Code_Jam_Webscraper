// problems.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
#include <math.h>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  ifstream input;
  ofstream output;
  string s;
  int  T, Tcur;
  int *stack = new int[100];
  int *orange = new int[100];
  int *blue = new int[100];
  int kol_step = 0, kol_o, kol_b;
  int so, sb;
  int pos_o, pos_b;
  char P;
  int R;
  int push = 0 ;


  
  input.open ("c:\\A-large.in", ios::in);
  //  input.open ("c:\\in.txt", ios::in);
  //input.open ("c:\\A-large-practice.in", ios::in);
  output.open("c:\\out.txt");
  
  input >> T;
  for(int i = 0; i < T; i++) {
	input >> Tcur;
	
	kol_o = 0;
	kol_b = 0;
	so = 0;
	sb = 0;
	kol_step = 0;
	pos_o = 0;
	pos_b = 0;
	push = 0;
	for(int j = 0; j < 100; j++) {
		stack[j] = -1;
		orange[j] = 0;
		blue[j] = 0;
	}
	for(int j = 0; j < Tcur; j++) {
		input >> P;
		input >> R;
		if(P == 'O') {
			stack[j] = 0;
			orange[kol_o] = R - 1;
			kol_o ++;
		}
		if(P == 'B') {
			stack[j] = 1;
			blue[kol_b] = R - 1;
			kol_b ++;
		}
	}
	int j = 0;
		do {
			if (so < kol_o) {
			if(pos_o != orange[so]) {
				if(pos_o < orange[so]) {
					pos_o ++;
				}
				else 
					pos_o --;
			}
			else {
				if(stack[j] == 0) {
					push = 1;
					so ++;
				}
			}
			}

			if(sb < kol_b) {
			if(pos_b != blue[sb]) {
				if(pos_b < blue[sb]) {
					pos_b ++;
				}
				else 
					pos_b --;
			}
			else {
				if(stack[j] == 1) {
					push = 1;
					sb ++;
				}
			}
			}
			kol_step ++;
			if(push == 1) {
				j++; 
				push = 0;
			}
		}while(j != Tcur); 
		output << "Case #"<<i + 1<<": "<<kol_step<<"\n";
  }


  output.close();
  input.close();
	return 0;
}

