#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <set>
#include <numeric>

using namespace std;

/*Defines*/
#define SZ(A) (A).size()
#define ALL(A) (A).begin(), (A).end()
#define SORT(A) sort(ALL(A))
#define REP(I,N) for(int I=0 ; I<N ; I++)
#define PB push_back
#define sqr(A) ((A)*(A))

#define ISS istringstream
#define OSS ostringstream
#define INT_INF (0x7fffffff)
#define LL_INF (0x7fffffffffffffffLL)
#define MSG(A) cout << #A << " = " << (A) << endl

/*Types*/
typedef long long un64;
typedef unsigned long long s64;
typedef vector<int> vi;
typedef vector<vi> vii;


int main(){

	int T;
	cin >> T;

	for(int t=1 ; t<=T ; t++){
		int N;
		cin >> N;

		vii mat(N, vi(N,0));

		for(int i=0 ; i<N ; i++){
			string aux;
			cin >> aux;
			for(int j=0 ; j<SZ(aux) ; j++)
				mat[i][j] = aux[j]-'0';
		}
		
/*		cout << "matrix" << endl;
		REP(i,N){
			REP(j,N) cout << mat[i][j] << " ";
			cout << endl;
		}	
*/
		vector<int> zeros;
		for(int i=0 ; i<N ; i++){
			int cnt = 0;
			bool found = false;
			for(int j=N-1 ; j>=0 && !found ; j--){
				if( mat[i][j] == 1) found = true;
				else cnt++;
			}
			zeros.PB(cnt);
		}

		long long count = 0;

		for(int k=N-1 ; k>= 0 ; k--){
			int i=0;
			int found = false;
			for(i=N-1-k ; i<N && !found; i++)
				if( zeros[i] >= k){
					found = true;
					break;
				}
			if(found){
//				cout << "found " << i << endl;
				int j=i;
				while( j-1>=N-1-k && zeros[j]>zeros[j-1]){
					swap(zeros[j], zeros[j-1]);
					count++;
					j--;
				}
			}

			
			bool ready = true;
			for(int l=0 ; l<N && ready ; l++)
				if( zeros[l] < N-1-l) ready = false; 
			if(ready) break;
		}

		cout <<"Case #"<< t << ": " << count << endl;
	}

	return 0;
}
