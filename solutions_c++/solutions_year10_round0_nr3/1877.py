#include <iostream>
#include <stdio.h>
#include <set>
#include <vector>
using namespace std;

int r, k, n;
int g[1000];
long long grsum;

int nowpos;
int nowr;
long long income;

long long board() {
	long long people = 0;
	int pspos = nowpos;
	int boardgr = 0;
	while(people <= k) {
		people += g[nowpos];
		nowpos = (nowpos+1)%n;
		boardgr++;
		if( people+g[nowpos] > k || boardgr==n ) break;
	}
	return people;
}

set<pair<int, int>> boardset;
vector<pair<int, int>> boardvector;
vector<long long> accIncome;

void process() {
	nowr = 1;
	nowpos = 0;
	income=0;

	boardset.clear();
	boardvector.clear();
	accIncome.clear();
	accIncome.push_back(0);

	grsum=0;
	for( int i=0; i<n; i++ ) {
		grsum += g[i];
	}


	int st, ed;

	while(true) {
		if( nowr > r ) break;
		st = nowpos;
		long long earn = board();
		ed = (nowpos-1+n)%n;

		pair<int, int> p;
		p.first = st; p.second = ed;
		if( boardset.find(p) == boardset.end() ) {
			boardset.insert(p);
			boardvector.push_back(p);

			income+=earn;
			accIncome.push_back(income);
			nowr++;
		}
		else {
			//주기 1개의 벌이와 롤러코스터 도는 횟수를 구한다
			long long eachearn = 0;
			int eachruns;
			int stpos;
			for( int i=0; i<boardvector.size(); i++ ) {
				if( boardvector[i] == p ) {
					stpos = i;	break;
				}
			}

			int periodr = (int)boardvector.size()-stpos;
			eachearn = accIncome[(int)accIncome.size()-1]-accIncome[stpos];


			//이제 끝날때까지 주기를 돌린다
			int leftr = r-nowr+1;
			long long periodrep = (leftr)/periodr;
			income += (eachearn*periodrep);
			
			int endr = r-(leftr%periodr)+1;
			
			nowr = endr;
			nowpos = boardvector[stpos].first;
			while(true) {
				if( nowr > r ) break;
				long long earn = board();

				income+=earn;
				nowr++;
			}
			break;
		}
	}

	cout<<income<<endl;
	

}

int main() {
	freopen("C-large.in","rt", stdin);
	freopen("out.txt","wt", stdout);

	int t;
	cin>>t;
	for( int i=0; i<t; i++ ) {
		cin>>r>>k>>n;
		for( int j=0; j<n; j++ ) {
			cin>>g[j];
		}

		cout<<"Case #"<<i+1<<": ";
		process();


	}

	return 0;
}