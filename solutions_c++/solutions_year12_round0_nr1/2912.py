#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <queue>
#include <set>
#include <cstring>
#include <sstream>
#include <cassert>
#include <map>
#include <stack>

#define FOR(I,A,B) for(int I=(A);I<(B);I++)
#define REP(I,N) FOR(I,0,N)
#define ALL(A) (A).begin(),(A).end()

#define SQR(x) ((x)*(x))
#define PB(x) push_back(x)

#define PI (acos(-1.0))

using namespace std;

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
char ss[] = "yhesocvxduiglbkrztnwjpfmaq";
int main(){
	int t,k = 1;
	scanf("%d\n",&t);
	while(t--){
		string lh,rh;
		getline(cin,lh);
		printf("Case #%d: ",k++);
		for(int i = 0 ; i < lh.size();i++){
			if( lh[i] == ' '){
				cout<<' ';
				continue;
			}
			cout<<ss[ lh[i] - 'a'];
		}
		cout<<endl;
	}
	return 0;
}
