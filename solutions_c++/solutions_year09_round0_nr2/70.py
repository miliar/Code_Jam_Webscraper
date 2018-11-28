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
int dx[4] = {0,-1,1,0};
int dy[4] = {-1,0,0,1};

void calc(ifstream &, ofstream &);
main()
{
	stringstream filename, fnamein, fnameout;
	string file("B");
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

void calc(ifstream &fin, ofstream &fout)
	{
	int H, W;
	fin >> H >> W;
	vector<vector<int> > map;
	for(int i=0;i<H;i++)
		{
		vector<int> a;
		for(int j=0;j<W;j++)
			{
			int in;
			fin >> in;
			a.push_back(in);
			}
		map.push_back(a);
		}

	vector<vector<int> > sec(H, vector<int>(W, -1));
	for(int i=0;i<H;i++)
		for(int j=0;j<W;j++)
			{
			int x=j;
			int y=i;
			int xnn=j;
			int ynn=i;
			bool chg=true;
			while(chg)
				{
				chg=false;
				x=xnn;
				y=ynn;
				int lowest=map[y][x];
				int chglowest = lowest;
				for(int d=4;d-->0;)
					{
					int xn=x+dx[d];
					int yn=y+dy[d];
					if(xn<0 || yn < 0 || xn>= W || yn >=H)
						continue;
					if(map[yn][xn] > lowest || map[yn][xn] == chglowest)
						continue;
					chg=true;
					lowest = map[yn][xn];
					xnn=xn;
					ynn=yn;
					}
				}
			sec[i][j] = xnn*101+ynn;
			}
	//cout << sec << endl;

	vector<vector<char> > out(H, vector<char>(W, ' '));
	char nxt='a';
	for(int i=0;i<H;i++)
		for(int j=0;j<W;j++)
			{
			int xbot = sec[i][j]/101;
			int ybot = sec[i][j]%101;
			if(' ' == out[ybot][xbot])
				{
				out[ybot][xbot] = nxt++;
				}
			out[i][j] = out[ybot][xbot];


			}
				


	fout << endl;
	for(int i=0;i<H;i++)
		{
		for(int j=0;j<W;j++)
			{
			fout << out[i][j];
			fout << " ";
			}
		fout << endl;
		}
	return; 
	}
