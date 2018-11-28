#include <iostream>
#include <fstream>
#define MAX 200
#define cout fout
#define cin fin
using namespace std;

int turn[MAX], pos[MAX];
int ptr = 0, n;
ofstream fout( "codeJA.txt" );
ifstream fin( "A-large.in" );

int nextTT( int idx ){
	for( int i = ptr + 1; i < n; i++ )
		if( turn[i] == idx )
			return pos[i];
	return -1;
}

int main()
{
	int t;
	cin >> t;
	for( int T = 1; T <= t; T++ ){
		ptr = -1;
		cin >> n;
		for( int i = 0;i < n; i++ ){
			char ch;
			int num;
			cin >> ch >> pos[i];
			turn[i] = ( ch == 'O' ) ? 1 : 0;
		}
		int p[2] = {1, 1}, ptr = -1, cur = 0;
		while( true ){
			int next[2];
			for( int i = 0;i < 2; i++ ){
				next[i] = -1;
				for( int j = ptr + 1; j < n; j++ )
					if( turn[j] == i ){
						next[i] = pos[j];
						break;
					}
			}
	
			//cout << ptr << ' ' << p[0] << ' ' << p[1] << ' ' << next[0] << ' ' << next[1] << endl;
			
			if( next[0] == -1 && next[1] == -1 )
				break;
			int ss = false;
			for( int i = 0;i < 2; i++ ){
				if( next[i] == -1 )
					continue;
				if( next[i] > p[i] )
					p[i]++;
				else if( next[i] < p[i] )
					p[i]--;
				else
					if( turn[ptr + 1] == i && !ss){
						ptr++;
						ss = true;
					}
			}
			cur++;
		}
		cout << "Case #" << T << ": " << cur << endl;
	}
	return 0;
}