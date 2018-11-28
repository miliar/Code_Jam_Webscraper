#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}
#define gcj_print(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

int N;
int a[50][50];
bool graph[50][50];
bool used[50];

int func(void){
	int i,j,k,ans=0;
	
	REP(i,N){
		int tmp = 0;
		REP(j,N) if(a[i][j] == 1) tmp = max(tmp,j);
		REP(j,N) graph[i][j] = (j >= tmp);
	}
	
	REP(i,N) used[i] = false;
	REP(i,N){
		REP(j,N) if(!used[j] && graph[i][j]) break;
		used[j] = true;
		REP(k,j) if(!used[k]) ans++;
	}
	
	return ans;
}

int main(void){
	int test,T,i,j;
	
	cin >> T;
	REP(test,T){
		cin >> N;
		REP(i,N) {
			string s;
			cin >> s;
			REP(j,N) a[i][j] = s[j] - '0';
		}
		int ans = func();
		gcj_print(ans);
	}
	
	return 0;
}
