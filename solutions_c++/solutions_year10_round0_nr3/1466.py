#include "HH.h"

ifstream input("C:/Users/Yeqi SUN/Desktop/C-large.in");
ofstream output("C:/Users/Yeqi SUN/Desktop/test.out");


int nextj(int j, int N)
{
	int tt = j+1;
	if(tt>=N)
		tt = 0;
	return tt;
}

void main(){
	long long N, k, R,T;
	input >> T;
	FOR(i,T){
		input >> R >> k >> N;
		vector<long long > g(1000,0);
		FOR(j,N)
			input >> g[j];
		vector<long long>  ppl(1000,0);			//#ppl hold if start from group i
		vector<long long>  nexti(1000,0);
		FOR(j,N){
			int ppltotal = g[j];
			int cur = j;
			while( 1 ){
				if( ppltotal + g[nextj(cur,N)] > k ){
					ppl[j] = ppltotal;
					nexti[j] = nextj(cur,N);
					break;
				}		
				cur = nextj(cur,N);
				if( cur == j ){
					ppl[j] = ppltotal;
					nexti[j]=j;
					break;
				}
				ppltotal += g[cur];		
			}
		}
		long long income = 0;
		int start = 0;
		FOR(t, R){
			income += ppl[start];
			start = nexti[start];
		}
		output <<"Case #" << i + 1 << ": "<<income<<endl;	

	}







	system("pause");
}