// GCJ13.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

#define SWAP(a,b,t) (t)=(a);(a)=(b);(b)=(t);
#define MAX(a,b)	((a)>(b))?(a):(b)
#define MIN(a,b)	((a)<(b))?(a):(b)
#define FR(i,a,b)	for(int ( i)=(a); ( i)<(b); ++( i))
#define FRE(i,a,b)	for(int ( i)=(a); ( i)<=(b); ++( i))
#define FRD(i,a,b)	for(( i)=(a); ( i)<(b); ++( i))
#define FRI(i,a)	for(( i)=(a).begin(); ( i)!=(a).end(); ++( i))
#define SWAP(a,b,t) (t)=(a);(a)=(b);(b)=(t);

#define I __int64
#define VI vector<int>
#define VL vector<I>
#define VD vector<long double>
#define VLD vector<long long double>
#define VS vector<string>
#define LI list<int>
#define LL list<I>
#define LD list<long double>
#define LLD list<long long double>
#define LS list<string>
#define SI set<int>
#define SL set<I>
#define SD set<long double>
#define SLD set<long long double>
#define SS set<string>
#define MII map<int,int>
#define MIL map<int,I>
#define MID map<int,long double>
#define MIS map<int,string>
#define MLL map<I,I>
#define MLI map<I, int>
#define MLD map<I,long double>
#define IT iterator

#define MMS(a) memset(a,0,sizeof(a))

fstream fin, fout;

void parseInt(VI &v)
{
	char s[500];
	fin.getline(s,500);
	memset(s,0,sizeof(char)*500);
	fin.getline(s,500);
	string str(s);
	for(int i=0; i != string::npos;)
	{
		string sub;
		int pos = str.find_first_of(' ',i);
		if(pos!=string::npos)
		{
			sub = str.substr(i, pos-i);
			i = pos+1;
			int val;
			sscanf(sub.c_str(),"%d ",&val);
			v.push_back(val);
		}
		else
		{
			sub = str.substr(i, str.length()-i);
			i = string::npos;
			int val;
			sscanf(sub.c_str(),"%d ",&val);
			v.push_back(val);
		}
	}
}
void parseString(VS &v,string str)
{
	for(int i=0; i != string::npos;)
	{
		string sub;
		int pos = str.find_first_of('/',i);
		if(pos!=string::npos)
		{
			sub = str.substr(i, pos-i);
			i = pos+1;
			v.push_back(sub);
		}
		else
		{
			sub = str.substr(i, str.length()-i);
			i = string::npos;
			v.push_back(sub);
		}
	}
}

I gcd(I a, I b)
{
	if(a<2 || b<2)
		return 1;
	if(a>b)
	{
		I t=a;
		a=b;
		b=t;
	}
	while(b%a)
	{
		I t=a;
		a=b%a;
		b=t;
	}
	return a;
}

class Counting
{
	I arr[67][67];
public:
	Counting()
	{
		memset(arr,0,sizeof(I)*67*67);
		FR(i,0,67)
		{
			arr[i][0]=1;
			arr[i][i]=1;
		}
		FRE(i,1,66)
			FRE(j,1,i-1)
				arr[i][j] = arr[i-1][j]+arr[i-1][j-1];
	}
	I ncr(int n, int r)
	{
		return arr[n][r];
	}
};

/* Tic-Tac-Toe-Tomek */

int main(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\A-large.in",ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\A-large.out",ios::out);
	if(!fin.good())
	{
		cout<<"Input file not opened"<<endl;
		exit(-1);
	}
	if(!fout.good())
	{
		cout<<"Output file not opened"<<endl;
		exit(-1);
	}
	fin>>casecnt;
	char b[4][416];
	FRE(e,1,casecnt)
	{
		MMS(b);
		FR(i,0,4) {
			FR(j,0,4) {
				fin>>b[i][j];
			}
		}
		bool xwins[4]={true, true, true, true};
		bool owins[4]={true, true, true, true};
		bool complete=true;
		FR(i,0,4) {
			xwins[0]=xwins[1]=true;
			owins[0]=owins[1]=true;

			if(b[i][i]!='X' && b[i][i]!='T') xwins[2] = false;
			if(b[i][i]!='O' && b[i][i]!='T') owins[2] = false;

			if(b[i][3-i]!='X' && b[i][3-i]!='T') xwins[3] = false;
			if(b[i][3-i]!='O' && b[i][3-i]!='T') owins[3] = false;

			FR(j,0,4) {

				if(b[i][j]!='X' && b[i][j]!='T') xwins[0] = false;
				if(b[i][j]!='O' && b[i][j]!='T') owins[0] = false;

				if(b[j][i]!='X' && b[j][i]!='T') xwins[1] = false;
				if(b[j][i]!='O' && b[j][i]!='T') owins[1] = false;

				if(b[i][j] == '.') complete = false;
			}
			if(xwins[0] || xwins[1] || owins[0] || owins[1]) {
				xwins[2]=xwins[3]=false;
				owins[2]=owins[3]=false;
				break;
			}
		}
		string result;
		if(xwins[0] || xwins[1] || xwins[2] || xwins[3])
			result = "X won";
		else if(owins[0] || owins[1] || owins[2] || owins[3])
			result = "O won";
		else if(!complete) 
			result = "Game has not completed";
		else 
			result = "Draw";
		fout<<"Case #"<<e<<": "<<result;
		cout<<"Case #"<<e<<": "<<result;
		fout<<endl;
		cout<<endl;
	}
	return 0;
}

