#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

ofstream output("a.txt");
char flag = 'a';
char sink = -1;
int count = 1;
int move(vector<vector<int> >& m, vector<vector<int> >& m1 , int x, int y ){
	if(m[y][x] < 0){
		return m[y][x];
	}

	if(m1[y][x]<=m1[y][x-1]
			&& m1[y][x]<=m1[y-1][x]
			&& m1[y][x]<=m1[y+1][x]
			&& m1[y][x]<=m1[y][x+1]
	  ){
		m[y][x] = sink--;
	}
	else{
		int c,n,w,e,s;
		c = m1[y][x];
		n = m1[y-1][x];
		w = m1[y][x-1];
		e = m1[y][x+1];
		s = m1[y+1][x];
		if(n <= w && n <=e && n <=s){
			m[y][x] = move(m,m1,x,y-1);
		}
		else if(w <=n && w <=e && w <=s){
			m[y][x] = move(m,m1,x-1,y);
		}
		else if(e <=n && e <=w && e <=s){
			m[y][x] = move(m,m1,x+1,y);
		}
		else if(s <=n && s <=e && s <= w){
			m[y][x] = move(m,m1,x,y+1);
		}
	}
	return m[y][x];
}

void detect(vector<vector<int> > m){
	vector<vector<int> > m1, m2;

	vector<vector<int> >n1;
	vector<int> tmpx;

	flag = 'a'-1;
	sink = -1;

	for(int i = 0; i<m[0].size()+2; i++){
		tmpx.push_back(100000);
	}
	n1.push_back(tmpx);

	for(int i = 0; i<m.size(); i++){

		vector<int> tmpxx;
		tmpxx.push_back(100000);
		for(int j = 0; j<m[i].size(); j++){
			tmpxx.push_back(m[i][j]);
		}
		tmpxx.push_back(100000);
		n1.push_back(tmpxx);
	}
	n1.push_back(tmpx);

	m = m1 = n1;
	
	/*for(int i = 0; i< m.size(); i++){
		for(int j = 0; j < m[i].size(); j++){
			cout<<m[i][j]<<'\t';
		}
		cout<<endl;
	}*/

	for(int i = 1; i< m.size()-1; i++){
		for(int j = 1; j < m[i].size()-1; j++){
			move(m,m1,j,i);
		}
	}

	output<<"Case #"<<count++<<":"<<endl;
	for(int i = 1; i< m.size()-1; i++){
		for(int j = 1; j < m[i].size()-1; j++){
			output<<(char)(flag - m[i][j])<<' ';
		}
		output<<endl;
	}
}


int main(){

	int a,b,c,d;
	ifstream input("B-small-attempt0.in");
	
	input>>a;
	//cout<<a<<endl;
	for(int x=0; x<a; x++){
		input>>b>>c;
		vector<vector<int> > s;
		for(int i = 0; i<b; i++){
			vector<int> ss;
			for(int j = 0; j<c; j++){
				input>>d;
				ss.push_back(d);
			}
			s.push_back(ss);
		}
		detect(s);
	}
	
}

