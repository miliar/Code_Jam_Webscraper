// GCJ11.cpp : Defines the entry point for the console application.
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
#define VD vector<double>
#define VLD vector<long double>
#define VS vector<string>
#define LI list<int>
#define LL list<I>
#define LD list<double>
#define LLD list<long double>
#define LS list<string>
#define SI set<int>
#define SL set<I>
#define SD set<double>
#define SLD set<long double>
#define SS set<string>
#define MII map<int,int>
#define MIL map<int,I>
#define MID map<int,double>
#define MIS map<int,string>
#define MLL map<I,I>
#define MLI map<I, int>
#define MLD map<I,double>
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

/*
int _tmain(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("F:\\Preparation\\GCJ\\A-large.in",ios::in);
	fout.open("F:\\Preparation\\GCJ\\A-large.out",ios::out);
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
	FRE(e,1,casecnt)
	{
		int N,pa=1,pb=1,na=0,nb=0,ret=0;
		fin>>N;
		FR(i,0,N)
		{
			char p;
			int n;
			fin>>p>>n;
			if(p=='O')
			{
				int d = n-pa;
				d = (d<0) ? -d : d;
				if(na>=d)
				{
					ret += 1;
					nb += 1;
				}
				else
				{
					nb += (d+1-na);
					ret += (d+1-na);
				}
				na = 0;
				pa = n;
			}
			else
			{
				int d = n-pb;
				d = (d<0) ? -d : d;
				if(nb>=d)
				{
					ret += 1;
					na += 1;
				}
				else
				{
					na += (d+1-nb);
					ret += (d+1-nb);
				}
				nb=0;
				pb=n;
			}
		}
		fout<<"Case #"<<e<<": "<<ret<<endl;
		cout<<"Case #"<<e<<": "<<ret<<endl;
	}
	return 0;
}
*/
int _tmain(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("F:\\Preparation\\GCJ\\B-large.in",ios::in);
	fout.open("F:\\Preparation\\GCJ\\B-large.out",ios::out);
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
	FRE(e,1,casecnt)
	{
		char C[128][128];
		bool D[128][128];
		MMS(C), MMS(D);
		int c,d,n;
		char x,y,z,ret[500],input[500];
		fin>>c;
		FR(i,0,c)
		{
			fin>>x>>y>>z;
			C[x][y]=z;
			C[y][x]=z;
		}
		fin>>d;
		FR(i,0,d)
		{
			fin>>x>>y;
			D[x][y]=true;
			D[y][x]=true;
		}
		fin>>n>>input;
		FR(i,1,n)
		{	
			int j=0;
			bool cmDone=false;
			bool opDone=false;
			for(j=i-1; j>=0 && input[j]==0; j--);
			if(j>=0)
			{
				if(C[input[i]][input[j]])
				{
					cmDone = true;
					input[i] = C[input[i]][input[j]];
					input[j] = 0;
				}
			}
			if(!cmDone)
			{
				for(j=i-1; j>=0 && !D[input[i]][input[j]]; j--);
				if(j>=0)
				{
					opDone=false;
					for(j=i; j>=0; j--) input[j] = 0;
				}
			}
		}
		fout<<"Case #"<<e<<": ";
		cout<<"Case #"<<e<<": ";
		fout<<"[";
		cout<<"[";
		bool start=false;
		FR(i,0,n)
		{
			if(input[i])
			{
				if(!start)
				{
					fout<<input[i];
					cout<<input[i];
					start = true;
				}
				else
				{
					fout<<", "<<input[i];
					cout<<", "<<input[i];
				}
			}
		}
		fout<<"]"<<endl;
		cout<<"]"<<endl;
	}
	return 0;
}

