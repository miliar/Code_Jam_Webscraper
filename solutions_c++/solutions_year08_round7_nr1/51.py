/* Brian's GCJ entries */
#include <vector>
#include <iterator>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
using namespace std;
int bitct(long long r) {return r == 0 ? 0 : (bitct(r>>1) + (r&1));}
long long gcd(long long x, long long y) {return x ? gcd(y%x,x) : y;}
template<typename T> ostream& operator << (ostream &o,vector<T> v)
 {o<<"{";int i=0;for(;i<v.size()-1;i++)o<<v[i]<<", ";o<<v[i]<<"}";return o;}
long long choose(long long n, long long q)
{ if(n==0 || q==0) return 1;
	if (q==1) return n; else return ( choose(n, q-1) * (n-q+1 ) /q); }
#define foreach(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define FOR(i,a,b) for(typeof(a) i=(a); i < (b); ++i)
//int dx[8] = {0,  1,  1,  1,  0, -1, -1, -1}
//int dy[8] = {1,  1,  0, -1, -1, -1,  0,  1}
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

void calc(ifstream &, ofstream &);
main()
{
	stringstream filename, fnamein, fnameout;
	string file("A");
	filename << file << "-large.";
	fnamein << filename.str() << "in";
	fnameout << filename.str() << "out";

	ifstream fin(fnamein.str().c_str());
	ofstream fout(fnameout.str().c_str());
	int count;
	fin >> count;
	for(int i=0;i<count;i++)
		{
		fout << "Case #" << (i+1) << ": ";
		calc(fin, fout);
		fout.flush();
		}

	fin.close();
	fout.close();
}
int recurse(vector<vector<int> > tree, int node);

void calc(ifstream &fin, ofstream &fout)
	{
	int N;
	fin >> N;
	map<string, int> mixs;
	vector<vector<int> > tree;
	vector<vector<string> > data;
	for(int i=0;i<N;i++)
		{
		string my;
		int ing;
		fin >> my;
		fin >> ing;
		vector<string> mine;
		mixs[my] = i;
		for(int j=0;j<ing;j++)
			{
			string my1;
			fin >> my1;
			if(my1[0] <= 'z' && my1[0] >= 'a')
				continue;
			mine.push_back(my1);
			}
		data.push_back(mine);
		}
	for(int i=0;i<data.size();i++)
		{
		vector<int> mine;
		for(int j=0;j<data[i].size();j++)
			{
			mine.push_back(mixs[data[i][j]]);
			}
		tree.push_back(mine);
		}

	fout << recurse(tree, 0) << endl;


	return; 
	}

int recurse(vector<vector<int> > tree, int node)
	{
	if(tree[node].size() == 0)
		return 1;
	
	vector<int> anss;
	for(int i=0;i<tree[node].size();i++)
		{
		anss.push_back(recurse(tree, tree[node][i]));
		}

	int max=-1;
	int min=1000000;

	for(int i=0;i<anss.size();i++)
		{
		if(anss[i] < min)
			min=anss[i];
		if(anss[i] > max)
			max=anss[i];
		}
	
	int out=max;
	if(1+anss.size() > out)
		out = 1+anss.size();
	if(anss.size() -1 + min > out)
		out = anss.size() -1 + min;
	return out;

	}
