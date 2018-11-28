/*
 * Watersheds.cpp
 *
 *  Created on: 2009/09/03
 *      Author: hiroki
 */
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	string file = "B-large";
	string in = file + ".in";
	string out = file + ".out";
	ifstream ifs(in.c_str());
	ofstream ofs(out.c_str());

	int T;
	ifs >> T;

	char ch;
	vector<int> p;
	vector<int> q;
	int i, j;
	int mini, minj;

	for(int t=0; t<T; t++)
	{
		// 入力
		int H, W;
		ifs >> H >> W;
		// 端判定が面倒なので、山で囲ってしまう
		vector<vector<int> > alt(H+2, vector<int>(W+2));
		vector<vector<char> > map(H+2, vector<char>(W+2));
		for(int r=1; r<H+1; r++) for(int c=1; c<W+1; c++) { ifs >> alt[r][c]; map[r][c] = '0'; }
		for(int r=0; r<H+2; r++) { alt[r][0] = alt[r][W+1] = 20000; map[r][0] = map[r][W+1] = '1'; }
		for(int c=0; c<W+2; c++) { alt[0][c] = alt[H+1][c] = 20000; map[0][c] = map[H+1][c] = '1'; }

		// 計算
		ch = 'a';
		for(int r=1; r<H+1; r++) for(int c=1; c<W+1; c++)
		{
			// そのマスが既にラベルついていたらパス
			if(map[r][c] != '0') continue;

			// 経路探索のための初期化
			i = r; j = c;
			p.clear(); q.clear();
			// sinkまでの経路を保存しながら探索
			while(true)
			{
				p.push_back(i); q.push_back(j);
				// ラベルのついているセルに合流した場合そこまでの経路をすべてそのラベルに更新
				if(map[i][j] != '0')
				{
					for(int n=0; n<(int)p.size(); n++) map[p[n]][q[n]] = map[i][j];
					break;
				}
				// (ラベルのついてない)sinkに到達した場合、
				// そこまでの経路に新しいラベル(ch)をつけてchをインクリメント
				else if(alt[i][j] <= alt[i-1][j] && alt[i][j] <= alt[i+1][j] &&
					alt[i][j] <= alt[i][j-1] && alt[i][j] <= alt[i][j+1])
				{
					for(int n=0; n<(int)p.size(); n++) map[p[n]][q[n]] = ch;
					ch++;
					break;
				}
				// (ラベルのついていない)経路の途中ならば、もっとも低い方向へ進む
				else
				{
					mini = i-1; minj = j;
					if(alt[i][j-1] < alt[mini][minj]) { mini = i; minj = j-1; }
					if(alt[i][j+1] < alt[mini][minj]) { mini = i; minj = j+1; }
					if(alt[i+1][j] < alt[mini][minj]) { mini = i+1; minj = j; }
					i = mini; j = minj;
				}
			}
		}

		// 出力
		ofs << "Case #" << t+1 << ":" << endl;
		for(int i=1; i<H+1; i++) for(j=1; j<W+1; j++)
		{
			ofs << map[i][j];
			if(j < W) ofs << ' ';
			else ofs << endl;
		}
	}

	return 0;
}


