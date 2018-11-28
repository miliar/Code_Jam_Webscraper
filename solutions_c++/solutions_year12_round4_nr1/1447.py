#include <iostream>
#include <map>
#define MAX 10010
#define x first
#define y second
using namespace std;

typedef long long int entero;
typedef pair<long long int, long long int> Point;

Point p[MAX];
entero D;
int N;
map<entero, bool> dp[MAX];

bool Rec(int i, entero d){
	int j;
	if(dp[i].find(d) == dp[i].end()){
		if((d+p[i].x)>= D)
			return dp[i][d] = true;
		for(j = i+1; j <= N; j++)
			if((d+p[i].x)>=p[j].x){
				if(Rec(j, min(p[j].x-p[i].x, p[j].y)))
					return dp[i][d] = true;
			}
		return dp[i][d] = false;
	}
	return dp[i][d];
}

int main(){
	int  i, j, k, T;
	cin >> T;
	for(k = 1; k<= T; k++){
		cin >> N;
		p[0].x = 0;
		for(i = 1; i <= N; i++)
			cin >> p[i].x >> p[i].y;
		cin >> D;
		if(Rec(1, p[1].x))
			cout << "Case #"<<k<<": YES\n";
		else
			cout << "Case #"<<k<<": NO\n";
		for(i = 1; i <= N; i++)
			dp[i].clear();
	}
	return 0;
}
