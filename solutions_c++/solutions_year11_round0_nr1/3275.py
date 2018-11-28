/*
 * BotTrust.cpp
 *
 *  Created on: 2011/05/07
 *      Author: masamichi1222
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class BotTrust
{
public:
	int solve(vector <char> R, vector <int> P, int N)
	{
		int op = 1;
		int bp = 1;
		int od = 0;
		int bd = 0;
		int flag = 0;
		int count = 0;
		int oi = 0;
		int bi = 0;
		int ni = 0;

//		cout << od << bd << flag << count << oi << bi << ni << endl;

		for(int t=0; t<10000; t++){

//			Distination setti
			if(od == 0){
				for(int i=oi; i<N; i++){
					if(R[i]=='O'){
						od = P[i];
						oi = i+1;
						break;
					}
				}
			}
			if(bd == 0){
				for(int i=bi; i<N; i++){
					if(R[i]=='B'){
						bd = P[i];
						bi = i+1;
						break;
					}
				}
			}

//			push button
			if(R[ni]=='O' && P[ni]==op){
				od = 0;
				ni++;
				flag = 1;
			}
			if(R[ni]=='B' && P[ni]==bp && flag == 0){
				bd = 0;
				ni++;
			}
			flag = 0;

//			move
			if(od > op && od != 0) op++;
			if(od < op && od != 0) op--;
			if(bd > bp && bd != 0) bp++;
			if(bd < bp && bd != 0) bp--;

			count++;
//			cout << "time:" <<count << " ni:" << ni << " op:" << op << " bp:" << bp << endl;
			if(ni==N) break;
		}

		return count;
	}
};

int main()
{
	int T, N;
	vector <char> R;
	vector <int> P;
	for(int s=0; s<101; s++){
		P.push_back(0);
		R.push_back(' ');
	}

	BotTrust BT;

	cin >> T;
	for(int i=0; i<T; i++){
		cin >> N;
		for(int j=0; j<N; j++){
			cin >> R[j];
			cin >> P[j];
		}
		for(int j=N; j<101; j++){
			R[j] = ' ';
			P[j] = 0;
		}
		cout << "Case #" << i+1 << ": " << BT.solve(R, P, N) << endl;
	}

	return 0;
}
