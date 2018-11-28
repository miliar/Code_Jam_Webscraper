#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <sstream>
#include <assert.h>
#include <set>
#include <map>
#include <queue>
#include <utility>
#include <time.h>
#include <limits.h>
#include <string.h>
using namespace std;

int main(void)
{
	int N;
	cin >> N;

	vector< vector< pair<int,int> > > ws;
	for( int i = 0; i < 4; i ++ ){
		vector< pair<int,int> > w1, w2;
		for( int j = 0; j < 4; j ++ ){
			w1.push_back(pair<int,int>(i, j));
			w2.push_back(pair<int,int>(j, i));
		}
		ws.push_back(w1);
		ws.push_back(w2);
	}
	{
		vector< pair<int,int> > w1, w2;
		for( int j = 0; j < 4; j ++ ){
			w1.push_back(pair<int,int>(j, j));
			w2.push_back(pair<int,int>(j, 3-j));
		}
		ws.push_back(w1);
		ws.push_back(w2);
	}
	cerr << "vectors:" << endl;
	for( int i = 0; i < ws.size(); i ++ ){
		for( int j = 0; j < ws[i].size(); j ++ )
			cerr << ws[i][j].first << "," << ws[i][j].second << " ";
		cerr << endl;
	}

	for( int C = 1; C <= N; C ++ ){
		string B[4];
		cin >> B[0];
		cin >> B[1];
		cin >> B[2];
		cin >> B[3];
		bool Xwon = false;
		bool Owon = false;
		bool emptyExists = false;
		for( int y = 0; y < 4; y ++ )
			assert( B[y].size() == 4 );

		for( int wi = 0; wi < ws.size(); wi ++ ){
			int Xnum = 0;
			int Onum = 0;
			for( int j = 0; j < ws[wi].size(); j ++ ){
				int x = ws[wi][j].first;
				int y = ws[wi][j].second;
				if( B[y][x] == 'X' ) Xnum ++;
				else if( B[y][x] == 'O' ) Onum ++;
				else if( B[y][x] == 'T' ) Xnum ++, Onum ++;
				else if( B[y][x] == '.' ) emptyExists = true;
				else assert(false);
			}
			if( Xnum == ws[wi].size() ) Xwon = true;
			if( Onum == ws[wi].size() ) Owon = true;
		}

		cout << "Case #" << C << ": ";
		if( Xwon ){
			assert( !Owon );
			cout << "X won" << endl;
		}
		else if( Owon ){
			cout << "O won" << endl;
		}
		else if( emptyExists ){
			cout << "Game has not completed" << endl;
		}
		else{
			cout << "Draw" << endl;
		}
	}
	return 0;
}
