#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> ivec;
typedef vector<string> svec;
typedef vector<double> dvec;
typedef pair<int,int> ipair;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

ifstream fin;
ofstream fout;

string t;
string s="welcome to code jam";

LL appear[20][500];

int N;

int main(){
	fin.open("C-large.in");
//	fout.open("small-result.txt");
	fout.open("large-result.txt");

	getline(fin,t);
	stringstream ss(t);
	ss>>N;

	Rep(index,N){
		getline(fin,t);
		memset(appear,0,20*500*sizeof(LL));

		int diff = t.size() - s.size();
		if(diff>=0){
			int i,j;
;
			for(j=0;j<=diff+1;j++){
				appear[19][j]=1;
			}
			for(i=18;i>=0;i--){
				for(j=diff;j>=0;j--){
					appear[i][j]=appear[i][j+1];
					if( t[j+i]==s[i] ){
						appear[i][j] += appear[i+1][j];
						appear[i][j] %= 10000;
					}
				}
			}
		}

//		cout<<"Case #"<<index+1<<": "<<setfill('0')<<setw(4)<<appear[0][0]%10000<<endl;
		fout<<"Case #"<<index+1<<": "<<setfill('0')<<setw(4)<<appear[0][0]%10000<<endl;
	}

//	cin>>N;
	fin.close();
	fout.close();

}
