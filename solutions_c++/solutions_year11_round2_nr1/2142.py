#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("out.txt");

int T,Case = 0,N,i;
string teams[101];
vector<long double>WP,OWP,OOWP;

int count(int team,char ch) {
	int i,cnt = 0;
	for(i = 0;i < teams[team].size();++i) {
		if(teams[team][i] == ch)
			++cnt;
	}
	return cnt;
}
int scount(int team,char ch,int skip) {
	int i,cnt = 0;
	for(i = 0;i < teams[team].size();++i) {
		if(i == skip)continue;
		if(teams[team][i] == ch)
			++cnt;
	}
	return cnt;
}

void Owp() {
	int i,j,k,a,b;
	long double c,d,e;
	for(i = 0;i < N;++i) {//try all teams
		d = 0.0;
		for(j = 0;j < N;++j) {
			if((i == j) || (teams[i][j] == '.') )continue;
			a = scount(j,'0',i);
			b = scount(j,'1',i);
			if(a+b != 0) {
				c = long double(long double(b)/long double(a+b));
			}
			else
				c = 0.0;
			d += c;
		}
		a = count(i,'0');
		b = count(i,'1');
		d = long double(d / long double(a+b));
		//OWP.push_back(d);
		OWP[i] = d;
		//printf("team %d# d = %lf\n",i,d);
	}
}

void OOwp() {
	int i,j,k,a,b;
	long double c,d,e;
	for(i = 0;i < N;++i) {//try all teams
		d = 0.0;
		for(j = 0;j < N;++j) {
			if((i == j) || (teams[i][j] == '.') )continue;
			d += OWP[j];
		}
		a = count(i,'0');
		b = count(i,'1');
		d = long double(d / long double(a+b));
		OOWP[i] = d;
		//OWP.push_back(d);
		//printf("OOWP team %d# d = %lf\n",i,d);
	}
}


int main () {
	fin >> T;
	int a,b,c,d;
	long double e,f,g;
	while(T) {
		--T;
		++Case;
		fin >> N;
		WP.clear();
		OWP.clear();
		OOWP.clear();
		WP.assign(N,0);
		OWP.assign(N,0);
		OOWP.assign(N,0);
		for(i = 0; i < N;++i) {
			fin >> teams[i];
			a = count(i,'0');
			b = count(i,'1');
			if(a+b != 0) {
				e = long double(long double(b)/long double(a+b));
			}
			else
				e = 0.0;
			//printf("%d %d %lf\n",a,b,e);
			//WP.push_back(e);
			WP[i] = e;
		}
		Owp();
		OOwp();
		fout << "Case #" << Case << ":\n";
		for(i = 0; i < N;++i) {
			fout << 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] << endl;
			//printf("%llf\n",0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
		}
	}
	return 0;
}