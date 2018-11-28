// GCJ10.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

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

/* Utilities */
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
void parseString(VS &v)
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

int _tmain(int argc, _TCHAR* argv[])
{
	fin.open("F:\\Preparation\\GCJ\\C-large.in",ios::in);
	fout.open("F:\\Preparation\\GCJ\\C-large.out",ios::out);
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
	int input[1001],order[1001],groups[1001];
	I amount[1001];
	int casecnt;
	fin>>casecnt;
	FRE(e,1,casecnt)
	{
		MMS(order);MMS(groups);MMS(amount);MMS(input);
		int r,k,n,g,cap;
		I ret=0;
		fin>>r>>k>>n;
		
		FR(i,0,n)
			fin>>input[i];

		int curStart=0;
		int next=0;
		int r1=0;
		int num=0;
		bool done=false;
		while(r1<r)
		{
			order[curStart]=++num;
			cap = k;
			int cnt=0;
			I a=0;
			int i=0;
			for(i=0;i<n;i++)
			{
				int in=(curStart+i)%n;
				if(input[in]>k)
				{
					done = true;
					break;
				}
				if(input[in]>cap)
					break;
				a += input[in];
				cap -= input[in];
				cnt++;
			}
			groups[curStart]=cnt;
			amount[curStart]=a;
			ret += a;
			r1++;
			if(order[(curStart+i)%n]>0)
			{
				next=(curStart+i)%n;
				break;
			}
			curStart=(curStart+i)%n;
		}
		if(done || (r1==r))
		{
			fout<<"Case #"<<e<<": "<<ret<<endl;
			cout<<"Case #"<<e<<": "<<ret<<endl;
			continue;
		}
		I cyclicnum=amount[curStart];
		int cyclicgroups=1;
		for(int j=next;j!=curStart;j=(j+groups[j])%n)
		{
			cyclicgroups++;
			cyclicnum += amount[j];
		}
		ret += (r-r1)/cyclicgroups*cyclicnum;
		r1 = (r-r1)%cyclicgroups;

		int l=next;
		while(r1)
		{
			ret += amount[l];
			l=(l+groups[l])%n;
			r1--;
		}

		fout<<"Case #"<<e<<": "<<ret<<endl;
		cout<<"Case #"<<e<<": "<<ret<<endl;
	}
	return 0;
}


/*int _tmain(int argc, _TCHAR* argv[])
{
	fin.open("F:\\Preparation\\GCJ\\C-small-attempt3.in",ios::in);
	fout.open("F:\\Preparation\\GCJ\\C-small-attempt3.out",ios::out);
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
	int casecnt;
	fin>>casecnt;
	FRE(e,1,casecnt)
	{
		int r,k,n,g,cap;
		I ret=0;
		fin>>r>>k>>n;
		list<int> l;
		cap = k;
		int i=0;
		bool done=false;
		I result[1001];
		MMS(result);
		int r1=0;
		int cnt=0;
		FRD(i,0,n)
		{
			fin>>g;
			if(!done)
			{
				if(g>k)
					done = true;
					
				if(g>cap)
				{
					result[r1]=ret;
					r1++;
					cnt=0;
					cap=k;
					if(r1==r)
						done=true;
				}
				if(!done)
				{
					ret += g;
					l.push_back(g);
					cap -= g;
					cnt++;
				}
			}
		}
		if(!done)
		{
			while(!l.empty())
			{
				if(cnt==n)
				{
					result[r1]=ret;
					r1++;
					cnt=0;
					cap=k;
					if(r1==r)
						break;
				}
				g=l.front();
				l.pop_front();
				if(g>cap)
				{
					result[r1]=ret;
					r1++;
					cnt=0;
					cap=k;
					if(r1==r)
						break;
				}
				ret += g;
				l.push_back(g);
				cap -= g;
				cnt++;
			}
		}
		
		fout<<"Case #"<<e<<": "<<ret<<endl;
		cout<<"Case #"<<e<<": "<<ret<<endl;
	}
	return 0;
}*/

/*int _tmain(int argc, _TCHAR* argv[])
{
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
	int casecnt;
	fin>>casecnt;
	FRE(e,1,casecnt)
	{
		I n,k;
		fin>>n>>k;
		int val=(1<<n)-1;
		if(k<val)
		{
			fout<<"Case #"<<e<<": OFF"<<endl;
			cout<<"Case #"<<e<<": OFF"<<endl;
		}
		else
		{
			if(!((k-val)%(val+1)))
			{
				fout<<"Case #"<<e<<": ON"<<endl;
				cout<<"Case #"<<e<<": ON"<<endl;
			}
			else
			{
				fout<<"Case #"<<e<<": OFF"<<endl;
				cout<<"Case #"<<e<<": OFF"<<endl;
			}
		}
	}
	return 0;
}*/

