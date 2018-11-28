// roundb-b.cpp : 定¨义?控?制?台?应畖用?程ì序ò的?入?口ú点?。￡
//


#include "stdafx.h"
#include <fstream>
#include <iostream>
#include<vector>
#include<algorithm>

using namespace std;

int T;
int C;
int D;

int vendor[201][2];

int MIN(int a, int b){
	if(a>b) return b;
	else return a;
}

int MAX(int a, int b){
	if(a<b) return b;
	else return a;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("D:\B-small-attempt0 (2).in");
	ofstream out("D:\B-small.out");

	in >> T;

	int cur = 0;
	while(cur++ < T){
		in >> C;
		in >> D;
		int i,j;

		for(i=0;i<C;i++){
			in >> vendor[i][0];
			in >> vendor[i][1];
		}

		int begin = vendor[0][0];
		double max = 0;
		int end ;
		for(i=0;i<C;i++){
			end = MAX(begin,vendor[i][0])+vendor[i][1]*D-D;
			int len = end - vendor[i][0];
			if( len > max) max = len;
			begin = end+D;
		}

		out << "Case #" << cur <<": " << max/2.0<<endl;
	}

	in.close();
	out.close();
	return 0;
}

