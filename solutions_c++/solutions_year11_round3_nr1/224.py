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
#define LEN 10001
int n,m;
char D[LEN][11];
char L[30];
int wordMask[LEN];
int alphaMask[LEN][26];
vector<int> wordLen[11];
pair<int, int> f(int s, vector<int> &v)
{
	if(v.size()==1)
		return pair<int, int>(0,v[0]);

	int mask=0;
	FR(i,0,v.size())
		mask |= wordMask[v[i]];
	while(((1<<(L[s]-'a'))&mask) == 0) s++;
	map<int, vector<int> > group;
	FR(i,0,v.size())
		group[alphaMask[v[i]][L[s]-'a']].push_back(v[i]);

	pair<int, int> ret(-1,-1);
	for(map<int, vector<int> >::iterator it=group.begin(); it != group.end(); ++it)
	{
		pair<int, int> cur = f(s+1, it->second);
		if(it->first==0)
			cur.first++;
		if(cur.first > ret.first || (cur.first==ret.first && cur.second<ret.second))
			ret = cur;
	}
	return ret;
}
int _tmain(int argc, _TCHAR* argv[])
{
	int casecnt;
	int start=1, end=10;
	fin.open("F:\\Preparation\\GCJ\\B-large-practice.in",ios::in);
	fout.open("F:\\Preparation\\GCJ\\B-large-practice-1.out",ios::out);
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
		MMS(wordMask);
		MMS(alphaMask);
		FR(i,0,11)
			wordLen[i].clear();

		fin>>n>>m;
		FR(i,0,n)
		{
			fin>>D[i];
			FR(j,0,strlen(D[i]))
			{
				wordMask[i] |= 1<<(D[i][j]-'a');
				alphaMask[i][D[i][j]-'a'] |= (1<<j);
			}
			wordLen[strlen(D[i])].push_back(i);
		}

		fout<<"Case #"<<e<<": ";
		cout<<"Case #"<<e<<": ";
		FR(i,0,m)
		{
			fin>>L;
			if(e<start || e>end)
				break;
			pair<int, int> best(-1,-1);
			FR(j,1,11)
			{
				if(wordLen[j].size()==0)
					continue;
				pair<int, int> ret = f(0,wordLen[j]);
				if(best.first<ret.first || (best.first==ret.first && best.second>ret.second))
					best = ret;
			}
			fout<<D[best.second]<<" ";
			cout<<D[best.second]<<" ";
		}
		cout<<endl;
		fout<<endl;
	}
	return 0;
}
*/

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
		int N;
		fin>>N;
		int D[101][101];
		MMS(D);
		FR(i,0,N)
		{
			FR(j,0,N)
			{
				char v;
				fin>>v;
				if(v=='0')
					D[i][j]=1;
				else if(v=='1')
					D[i][j]=2;
			}
		}
		double owp[101],wp[101], oowp[101];
		vector<int> dd[101];
		MMS(owp);
		MMS(wp);
		MMS(oowp);
		FR(i,0,N)
		{
			int w=0,t=0;
			FR(j,0,N)
			{
				if(D[i][j])
				{
					t++;
					if(D[i][j]==2)
						w++;
				}
			}
			if(t>0)
				wp[i] = 1.0*w/t;

			int tot=0;
			double sum=0.0;
			FR(j,0,N)
			{
				w=0, t=0;
				if(D[i][j]==0)
					continue;
				FR(k,0,N)
				{
					if(k==i)
						continue;
					if(D[j][k])
					{
						t++;
						if(D[j][k]==2)
							w++;
					}
				}
				if(t>0)
				{
					tot++;
					sum += 1.0*w/t;
					dd[i].push_back(j);
				}
			}
			if(tot>0)
				owp[i] = 1.0*sum/tot;
		}
		fout<<"Case #"<<e<<": "<<endl;
		cout<<"Case #"<<e<<": "<<endl;
		FR(i,0,N)
		{
			int tt=0;
			double val=0.0;
			for(int j=0; j<dd[i].size(); j++)
			{
				tt++;
				val+=owp[dd[i][j]];
			}
			if(tt>0)
				oowp[i]=1.0*val/tt;

			double ret=0.25*wp[i]+0.50*owp[i]+0.25*oowp[i];
			char s[15];
			sprintf(s,"%0.10f", ret);
			fout<<s<<endl;
			cout<<s<<endl;
		}
	}
};
*/

/*
bool f(I t, vector<pair<int,int> > &v, I d)
{
	I end=-1e14;
	FR(i,0,v.size())
	{
		I start = max(v[i].first-t, end+d);
		if(start+(v[i].second-1)*d > v[i].first+t)
			return false;
		end = start+(v[i].second-1)*d;
	}
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("F:\\Preparation\\GCJ\\B-large-practice.in",ios::in);
	fout.open("F:\\Preparation\\GCJ\\B-large-practice.out",ios::out);
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
		int c,d,P[201], V[201];
		vector<pair<int,int> > v;
		fin>>c>>d;
		FR(i,0,c)
		{
			fin>>P[i]>>V[i];
			v.push_back(pair<int,int>(P[i]*2, V[i]));
		}
		sort(v.begin(), v.end());

		I low=0, high=1e14;
		I ret=1e14;
		while(low<=high)
		{
			I mid = (low+high)/2;
			if(f(mid,v,2*d))
			{
				if(ret>mid)
					ret=mid;
				high=mid-1;
			}
			else
				low=mid+1;
		}
		char s[50];
		sprintf(s,"%0.8lf", 1.0*ret/2);
		fout<<"Case #"<<e<<": "<<s<<endl;
		cout<<"Case #"<<e<<": "<<s<<endl;
	}
};
*/

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
		int r,c;
		char S[100][100];
		fin>>r>>c;
		FR(i,0,r)
		{
			FR(j,0,c)
				fin>>S[i][j];
		}
		bool pos = true;
		FR(i,0,r)
		{
			FR(j,0,c)
			{
				if(S[i][j]=='#')
				{
					if(i+1>=r || j+1>=c)
					{
						pos=false;
						break;
					}
					if(S[i][j+1]=='#' && S[i+1][j]=='#' && S[i+1][j+1]=='#')
					{
						S[i][j]='/';
						S[i+1][j+1]='/';
						S[i+1][j]='\\';
						S[i][j+1]='\\';
					}
					else
					{
						pos=false;
						break;
					}
				}
			}
			if(!pos)
				break;
		}
		fout<<"Case #"<<e<<": "<<endl;
		cout<<"Case #"<<e<<": "<<endl;
		if(!pos)
		{
			fout<<"Impossible"<<endl;
			cout<<"Impossible"<<endl;
		}
		else
		{
			FR(i,0,r)
			{
				FR(j,0,c)
				{
					fout<<S[i][j];
					cout<<S[i][j];
				}
				cout<<endl;
				fout<<endl;
			}
		}
	}
}