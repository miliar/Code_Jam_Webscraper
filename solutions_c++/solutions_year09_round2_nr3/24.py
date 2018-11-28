// Google Code Jam 2009 -- Round 1B
// 12th October 2008
//
// Problem C -  

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <fstream>
#include <cmath>
#include <queue>
#include <set>
#include <algorithm>
#include <list>
#include <cstdio>
using namespace std;


// A few utility I/O functions
vector <string> split(const string &s,const char &separator=' '){vector <string> ret;int p1=0,p2;for (p2 = 0;p2 < s.size();p2++)if (s[p2]==separator){if (p2-p1>0) ret.push_back(s.substr(p1,p2-p1));p1=p2+1;}if (p2-p1 > 0) ret.push_back(s.substr(p1,p2-p1));return ret;}
template <class T> T get(istream &fin){string s;getline(fin,s);stringstream ss(s);T ret;ss >> ret;return ret;}
template <class T> vector <T> getv(istream &fin,const char &separator = ' '){string s;getline(fin,s);vector <string> convert = split(s,separator);vector <T> ret(convert.size());for (int i=0;i<convert.size();i++){stringstream ss(convert[i]);ss>>ret[i];}return ret;}
template <> vector <string> getv <string> (istream &fin,const char &separator){string s;getline(fin,s);return split(s,separator);}

int di[] = {-1,0,1,0};
int dj[] = {0,1,0,-1};
int vis[21][21][5000];
int main(int argc,const char * argv[]){

	// File stuff
	istream *in__;ostream *out__;
	if (argc > 1) in__ = new ifstream(argv[1]);else in__ = &cin;
	if (argc > 2) out__ = new ofstream(argv[2]);else out__ = &cout;
	istream & in = *in__;ostream & out = *out__;

	out.setf(ios::fixed,ios::floatfield);cout.setf(ios::fixed,ios::floatfield);
	out.precision(7);cout.precision(7);

	// Main stuff starts here
	for (int TC = get <int>(in),cas = 1;cas <= TC;cas++){
		vector <int> N = getv <int> (in);
		vector <string> board(N[0]);
		for (int i=0;i<N[0];i++)
			getline(in,board[i]);

		string answers[251];

		memset(vis,0,sizeof(vis));
		priority_queue <
			pair <pair <int,string>, pair <pair <int,int> ,int > >,
			vector <pair <pair <int,string>, pair <pair <int,int> ,int > > >
			,greater <pair <pair <int,string>, pair <pair <int,int> ,int > > > > Q;
		for (int i=0;i<N[0];i++)
			for (int j=0;j<board[i].size();j++)
				if (board[i][j] != '+' && board[i][j] != '-'){
					Q.push(make_pair(make_pair(1,string(1,board[i][j])), make_pair(make_pair(i,j),board[i][j] - '0')));
				}

		memset(vis,0,sizeof(vis));
		cout << "working"  << endl;
		while (!Q.empty()){
			int i = Q.top().second.first.first;
			int j = Q.top().second.first.second;
			string s = Q.top().first.second;
			int val = Q.top().second.second;
			//cout << s << " " << val << endl;
			if (val > 0 && val < 251 && answers[val] == "")
				answers[val] = s;
			Q.pop();
			if (vis[i][j][val+2500]) continue; 
			vis[i][j][val+2500] = true;
			vector <pair <string,pair <int,int> > > next;
			for (int k=0;k<4;k++){
				int ni = i +di[k],nj = j+dj[k];
				if (ni <0 || nj <0 || ni >= board.size() || nj >= board[ni].size()) continue;
				if (board[ni][nj] == '+' || board[ni][nj] == '-'){
					Q.push(make_pair(make_pair(s.size()+1,s+board[ni][nj]),make_pair(make_pair(ni,nj),val)));
				} else {
					int nval = val;
					if (s[s.size()-1] == '+') nval += board[ni][nj] - '0';
					else nval -= board[ni][nj] - '0';
					if (nval >=350 || nval <-350) continue;
					Q.push(make_pair(make_pair(s.size()+1,s+board[ni][nj]),make_pair(make_pair(ni,nj),nval)));
				}
			}
		}
		cout << "done" << endl;
		vector <int> eval = getv <int> (in);
		out << "Case #" << cas << ":" << endl;
		for (int i=0;i<eval.size();i++)
			out << answers[eval[i]] << endl;
				
	}

	if (in__!=&cin) delete in__;if (out__!=&cout) delete out__;
	return 0;
}