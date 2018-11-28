#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#define sz size()
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define fu(i,n) for(int i=0; i<(n); i++)
#define ALL(a) (a).begin(),(a).end()
#define cl(a,co) memset(a,co,sizeof a)
#define un(a) sort(ALL(a)),a.erase( unique(ALL(a)), a.end() )
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

int ileTestow;

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
		
		int n;
		int last[] = {1,1};
		int score[] = {0,0};

		scanf("%d", &n);

		fu(a,n){
			char c;
			int where;
			int index;

			cin >> c >> where;

			if( c == 'O' ){
				index = 0;
			} else {
				index = 1;
			}

			score[index] = score[index] + abs(last[index]-where) + 1;
			if( score[index] <= score[1-index] ){
				score[index] = score[1-index] + 1;		
			} 
			last[index] = where;

		}

		printf("%d\n", score[0]>score[1]?score[0]:score[1]);
	}

	return 0;
}
