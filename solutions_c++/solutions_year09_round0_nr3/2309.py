#include <iostream>
#include <cstdio>
#include <cstdlib>


using namespace std;

char dp[501][20];

long long res;

string str;
string wlc = "welcome to code jam";

void construct(int last, int k, int n, int c[],int *nc){
	int i;
	*nc = 0;
	for ( i = last + 1 ; i < str.size() ; i++ )
		if ( dp[i][k] ){
			c[*nc] = i;
			(*nc)++;
		}
}


void go(int last , int k , int n ){
	int c[501];
	int nc;
	int i;

	if ( k == n ){
		res++;
	} else {
		construct(last,k,n,c,&nc);
//cout << "last: " << last << " k: " << k << endl;
//for ( i = 0 ; i < nc ; i++ )
//	cout << c[i] << endl;

		k++;
		for ( i = 0 ; i < nc ; i++ ){
			go(c[i],k,n);
		}
	}
}


int main(){
	int N , n;
	int i, j;

	cin >> N;
	getline ( cin , str );
	for ( n = 1 ; n <= N ; n++ ){
		getline ( cin , str );
		
		for ( i = 0 ; i < str.size() ; i++ ){
			for ( j = 0 ; j < wlc.size() ; j++ ){
				if ( str[i] == wlc[j] )
					dp[i][j] = 1;
				else
					dp[i][j] = 0;
			}
		}

		res = 0;
		go(-1,0,wlc.size());
		
		printf("Case #%d: %04d\n", n, res % 10000);
	}

	return 0;
}

