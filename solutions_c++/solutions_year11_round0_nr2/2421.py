#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#define MAX 500
#define cin fin
#define cout fout
using namespace std;

int gr[MAX][MAX];
bool op[MAX][MAX];
vector< int > v;
int C, D, N;
string s;
ofstream fout( "codeJB.txt" );
ifstream fin( "B-large.in" );

int main()
{
	int t;
	cin >> t;
	for( int T = 1; T <= t; T++ ){
		memset( gr, -1, sizeof gr );
		memset( op, false, sizeof op );
		v.clear();
		cin >> C;
		for( int i = 0;i < C; i++ ){
			char a, b, c;
			cin >> a >> b >> c;
			gr[a - 'A'][b - 'A'] = gr[b - 'A'][a - 'A'] = c - 'A';
		}
		cin >> D;
		for( int i = 0;i < D; i++ ){
			char a, b;
			cin >> a >> b;
			op[a - 'A'][b - 'A'] = op[b - 'A'][a - 'A'] = true;
		}
		cin >> N;
		for( int i = 0;i < N; i++ ){
			char c;
			int num;
			cin >> c;
			num = c - 'A';
			v.push_back( num );
			if( v.size() >= 2 && gr[v.back()][v[v.size() - 2]] != -1 ){
				int ch = gr[v.back()][v[v.size() - 2]];
				v.pop_back();
				v.pop_back();
				v.push_back( ch );
			}
			else{ 
				for( int j = 0;j < v.size(); j++ )
					for( int k = 0;k < v.size(); k++ )
						if( op[v[j]][v[k]] )
							v.clear();
			}
		}
		cout << "Case #" << T << ": ";
		cout << '[';
		for( int i = 0;i < v.size(); i++ ){
			if( i )
				cout << ", ";
			cout << char( v[i] + 'A' );
		}
		cout << ']' << endl;
	}
	return 0;
}
