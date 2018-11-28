#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <set>
#include <numeric>
#include <string.h>

using namespace std;

#define SZ(A) A.size()
#define ALL(A) A.begin(), A.end()
#define SORT(A) sort(ALL(A))
#define REP(I,N) for(int I=0, I<N ; I++)
#define INF INT_MAX
#define PB push_back

int main(){

	vector<string> dic;
	int L, D, N;
	char a[30];

	cin >> L >> D >> N;

	for(int i=0 ; i<D ; i++){
		string aux;
		cin >> aux;
		dic.PB(aux);
	}

	for(int i=0; i<N ; i++){
		unsigned long long cnt = 0;
		vector<string> pos;		
		for(int j=0 ; j<L ; j++){
			memset(a, 0, 30);
			if( scanf(" ( %[a-z] ) ", a) <= 0)
				scanf("%c", a);
//			cout << "tomo : "<< a << endl;
			pos.PB(string(a));
		}
		
		for(int j=0 ; j<D ; j++){
			bool sepuede = true;
			for(int k=0 ; k<SZ(dic[j]) && sepuede; k++)
				if(pos[k].find(dic[j][k]) == string::npos ) sepuede = false;
			cnt += sepuede;
		}
		
		cout << "Case #" << i+1 << ": " << cnt << endl;
		pos.clear();
	}

	return 0;
}
