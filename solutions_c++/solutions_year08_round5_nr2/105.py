// Google Code Jam -- Online Round 3
// 9th August 2008
//
// Problem B - Large Solution

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

int di [] = {-1,0,1,0};
int dj [] = {0,1,0,-1};

bool empty(int i,int j,const vector <string> &mp){
	if (i<0 || i>= mp.size() || j < 0 || j >= mp[i].size() || mp[i][j] == '#') return false;
	return true;
}

int main(int argc,const char * argv[]){

	// File stuff
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	fout.setf(ios::fixed,ios::floatfield);
	fout.precision(7);

	// Main stuff starts here
	for (int TC = get <int>(fin),cas = 1;cas <= TC;cas++){
		vector <int> v = getv<int>(fin);
		int R = v[0], C = v[1];
		vector <string> mp(R);
		for (int i=0;i<R;i++)
			mp[i] = get <string> (fin);
		int N=0,M=0,si;

		map <pair <int,int> ,int> fr;
		map < pair <pair <int,int>,int >,int > wallm; 

		for (int i=0;i<R;i++){
			wallm[make_pair(make_pair(i,-1),1)] = N++;
			wallm[make_pair(make_pair(i,C),3)] = N++;
		}

		for (int i=0;i<C;i++){
			wallm[make_pair(make_pair(-1,i),2)] = N++;
			wallm[make_pair(make_pair(R,i),0)] = N++;
		}


		vector <vector <int> > hit(3000,vector <int> (4)),go1(3000),go(3000);

		for (int i = 0;i < R;i++)
			for (int j=0;j<C;j++)	{
				if (mp[i][j] != '#'){
					if (fr.find(make_pair(i,j)) == fr.end()) fr[make_pair(i,j)] = M++;
					
					int index = fr[make_pair(i,j)];
					
					if (mp[i][j] == 'O') si = index;
					for (int k=0;k<4;k++){
						if (empty(i+di[k],j+dj[k],mp)){
							if (fr.find(make_pair(i+di[k],j+dj[k])) == fr.end()) fr[make_pair(i+di[k],j+dj[k])] = M++;
							int index1 = fr[make_pair(i+di[k],j+dj[k])];
							go[index].push_back(index1);
						} else {
							pair <pair <int,int> , int> w = make_pair(make_pair(i+di[k],j+dj[k]),k);
							if (wallm.find(w) == wallm.end()) wallm[w] = N++;
							go1[index].push_back(wallm[w]);
						}
						int ni=i,nj=j;
						while (empty(ni,nj,mp)){
							ni+=di[k];nj+=dj[k];
						}

						pair <pair <int,int> , int> w = make_pair(make_pair(ni,nj),k);
						if (wallm.find(w) == wallm.end()) wallm[w] = N++;
						hit[index][k] = wallm[w];
					}
				}
			}


		vector <pair <pair <int,int>,int > > walls(N);
		vector <pair <int,int> >  free(M);
		for (map < pair <pair <int,int>,int >,int >::iterator it = wallm.begin();it != wallm.end();it++)
			walls[(*it).second] = (*it).first;
		for (map <pair <int,int> , int> :: iterator it = fr.begin();it!=fr.end();it++)
			free[(*it).second] = (*it).first;
/*
*/		int ans = -1;
		int * mem = new int[(N+1)*(N+1)*M];
		memset(mem,0,sizeof (mem));
		priority_queue <pair <int,pair <int,pair <int,int> > > > Q;
		Q.push(make_pair(0,make_pair(si,make_pair(N,N))));
		while (!Q.empty()){
			int i = Q.top().second.first;
			int T = -Q.top().first;
			int blue = Q.top().second.second.first;
			int yellow = Q.top().second.second.second;
			Q.pop();
			if (mp[free[i].first][free[i].second] == 'X'){
				ans = T;
				break;
			}
			int state = i;
			state = state * (N+1) + yellow;
			state = state * (N+1) + blue;

			if (mem[state]) continue;
			mem[state] = true;
			for (int j=0;j<go[i].size();j++)
				Q.push(make_pair(-T-1,make_pair(go[i][j],make_pair(blue,yellow))));
			if (yellow != N && blue != N){
				for (int j=0;j<go1[i].size();j++){
					if (go1[i][j] == blue) {
						int ni = walls[yellow].first.first + di[(walls[yellow].second + 2)%4];
						int nj = walls[yellow].first.second + dj[(walls[yellow].second + 2)%4];
						int nindex = fr[make_pair(ni,nj)];
						Q.push(make_pair(-T-1,make_pair(nindex,make_pair(blue,yellow))));
					}
					if (go1[i][j] == yellow) {
						int ni = walls[blue].first.first + di[(walls[blue].second + 2)%4];
						int nj = walls[blue].first.second + dj[(walls[blue].second + 2)%4];
						int nindex = fr[make_pair(ni,nj)];
						Q.push(make_pair(-T-1,make_pair(nindex,make_pair(blue,yellow))));
					}
				}
			}
			for (int j=0;j<4;j++)
				Q.push(make_pair(-T,make_pair(i,make_pair(hit[i][j],yellow))));

			for (int j=0;j<4;j++)
				Q.push(make_pair(-T,make_pair(i,make_pair(blue,hit[i][j]))));
		}
		delete [] mem;

		if (ans != -1){
		fout << "Case #" << cas << ": " << ans << endl;
		if (argc == 4) cout  << "Case #" << cas << ": " << ans << endl;
		} else {

		fout << "Case #" << cas << ": " << "THE CAKE IS A LIE" << endl;
		if (argc == 4) cout  << "Case #" << cas << ": " <<  "THE CAKE IS A LIE" << endl;
		}
	}
	return 0;
}