// codejam-C.cpp : 定¨义?控?制?台?应畖用?程ì序ò的?入?口ú点?。￡
//

#include "stdafx.h"
#include <fstream>
#include <iostream>

using namespace std;

int testnum;
int curnum = 1;

int len;
unsigned int a[1010];

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("D:\C.txt");
	ofstream out("D:\Cr.txt");

	in >> testnum;

	int i;
	while(testnum-->0){
		//input
		in >> len;
		for(i=0;i<len;i++)
			in >> a[i];
		//process:init
		unsigned long sum = 0;
		unsigned long min = a[0];
		unsigned long xosum = 0;
		//compute
		for(i=0;i<len;i++){
			sum += a[i];
			xosum ^= a[i];
			if(min>a[i]) min = a[i];
		}

		//output
		out<<"Case #"<<curnum++<<": ";
		if(xosum == 0){
			//cout <<"Yes"<<sum-min<<endl;
			out<<sum-min<<endl;
		}
		else{
			//cout <<"No"<<endl;
			out<<"NO"<<endl;
		}
	}

	in.close();
	out.close();

	return 0;
}


