// codejam-D.cpp : 定¨义?控?制?台?应畖用?程ì序ò的?入?口ú点?。￡
//

#include "stdafx.h"
#include <fstream>
#include <iostream>

using namespace std;

int testnum;
int N;
int a[1010];

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("D:\D-small-attempt0.in");
	ofstream out("D:\Dr-small.txt");
	
	in >> testnum;
	int curnum = 1;
	int i;
	while( testnum-->0){
		in >> N;
		int sum = N;
		for(i=0;i<N;i++){
			in >> a[i];
			if( a[i] == i+1 )
				sum --;
		}
		cout << sum << endl;
		out << "Case #"<<curnum++<<": ";
		out << sum <<".000000"<<endl;
	}

	in.close();
	out.close();

	return 0;
}




