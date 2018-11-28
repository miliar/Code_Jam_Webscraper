#include "LongInt.h"
#include <QtCore/QCoreApplication>
#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <algorithm>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <cassert>
#include <cmath>
using namespace std;
ifstream fin; 
ofstream fout;

void preWork();
void work();

int main(int argc, char *argv[])
{
	preWork();
	QCoreApplication a(argc, argv);

//	char * inputName="A-large.in";
//	fin.open(inputName);
//	fin.open ( "A-small-practice.in");
	//fin.open ( "A-large-practice.in");
	fin.open ( "NO1_input.txt");

	fout.open("output.txt");
	int n;
	fin >>n;
	for (int i=0; i<n; i++)
	{
		fout<<"Case #"<<i+1<<": ";
		work();
		fout<<endl;
	}


	fin.close();

	fout.close();



//	return a.exec();
}



void preWork()
{
	//  test longInt;

	LongInt a="123456789";
	LongInt b="987654321";
	LongInt c,d;
	c= b.modDivide(a,&d);
	
	cout<<c<<endl;
	cout<<d<<endl;
}
bool check(char z[4]) {
	bool a,b,c;
	a= false;
	b= false;
	c= false;
	for (int j=0; j<4; j++) {
		if (z[j]=='.') c=true;
		if (z[j] == 'X') a = true;
		if (z[j] == 'O') b = true;
	}
	if (c) return false;
	if (a && !b) {
		fout<<"X won"<<endl;
		return true;
	}
	if (!a && b) {
		fout<<"O won"<<endl;
		return true;
	}
	return false;
}
void work()
{
	bool ic = false;
	char z[4][4];
	for (int i=0; i<4; i++) {
		for (int j=0; j<4; j++) {
			fin>>z[i][j];
			if (z[i][j]=='.') ic = true;
		}
	}
	for (int i=0; i<4; i++) {
		if (check(z[i])) return;
	}
	for (int i=0; i<4; i++) {
		char x[4];
		for (int j=0; j<4; j++) {
			x[j] = z[j][i];
		}
		if (check(x)) return;
	}
	char a[4], b[4];
	for (int i=0; i<4; i++) {
		a[i] = z[i][i];
		b[i] = z[i][3-i];
	}
	if (check(a)) return;
	if (check(b)) return;
	if (ic) fout<<"Game has not completed"<<endl;
	else fout<<"Draw"<<endl;
}