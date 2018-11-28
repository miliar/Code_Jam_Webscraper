#ifndef CODEJAM_H
#define CODEJAM_H

#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <stack>
#include <fstream>
#include <math.h>
#include <map>
#include <algorithm>
#include <vector>
#include <crtdbg.h>
using namespace std;

#define FOR0(i,b)	for(int i=0,_b=(int)(b);i<_b;i++)
#define FOR1(i,b)	for(int i=1,_b=(int)(b);i<=_b;i++)
#define LOG(s,ss)	cout<<s<<""<<ss<<endl;
#define FORE(e,c,Ty) vector<Ty*>::iterator e;for(e=(c).begin();e!=(c).end();e++)

// functions declaraion
void su(ifstream &input);
void tt(ifstream &input);
void fs(ifstream &input);

#endif