#include <iostream>
#include <queue>

using namespace std ;

const int maxn = 105 ;

int dist[maxn][maxn][maxn] ;
int col[maxn] , seq[maxn] ;

int main(){
	int T ;
	cin >> T ;
	for(int it = 1; it <= T ; it ++){
		int N ; 
		cin >> N ;
		for(int i=0;i < N ; i++){
			char c ; int m ;
			cin >> c >> m ;
			if(c == 'O')col[i] = 0; 
			else col[i] = 1 ;
			seq[i] = m ;
		}
		for(int i=0;i <= N ; ++i)
			for(int r1=1; r1 <= 100; r1++)
				for(int r2 = 1;r2 <= 100 ; r2++)
					dist[i][r1][r2] = -1 ;

		queue<pair<int , pair<int,int> > > Q ;
		Q.push(make_pair(0 , make_pair(1 , 1)));
		dist[0][1][1] = 0 ;
		for( ; Q.size() > 0 ; ){
			pair<int , pair<int,int> > state = Q.front();
			Q.pop();
			int sNum = state.first , r1 = state.second.first , r2 = state.second.second ;
			if(sNum >= N) break ;
			for(int n1=r1-1 ; n1 <= r1+1 ; n1++)
				for(int n2=r2-1;n2 <= r2+1 ; n2++)if(n1 >= 1 and n2 >= 1 and n1 <= 100 and n2 <= 100){
					int sNum2 = sNum ;
					if(col[sNum] == 0 and n1 == r1 and seq[sNum] == n1)sNum2 ++ ;
					else if(col[sNum] == 1 and n2 == r2 and seq[sNum] == n2)sNum2 ++ ;
					if(dist[sNum2][n1][n2] < 0){
						dist[sNum2][n1][n2] = 1 + dist[sNum][r1][r2] ;
						Q.push(make_pair(sNum2 , make_pair(n1,n2)));
					}
				}
		}
		int res = -1 ;
		for(int r1 = 1 ; r1 <= 100; r1 ++)
			for(int r2 = 1 ; r2 <= 100;  r2 ++)
				if(dist[N][r1][r2] >= 0){
					if(res < 0 or res > dist[N][r1][r2])
						res = dist[N][r1][r2] ;
				}
		cout << "Case #" << it << ": " << res << endl ;
	}
	return 0 ;
}
