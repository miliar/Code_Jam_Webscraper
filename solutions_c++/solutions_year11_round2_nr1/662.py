// roundb-a.cpp : 定¨义?控?制?台?应畖用?程ì序ò的?入?口ú点?。￡
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include<vector>
#include<algorithm>

using namespace std;

int T;
int N;

char team[110][110];

double wp[110][110];
double owp[110];
double oowp[110];
double rpi[110];

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("D:\A-small-attempt0 (2).in");
	ofstream out("D:\A.out");

	in >> T;
	cout << "hello" << T;
	int curtest = 0;
	while(curtest ++ < T){
		int i,j,k;
		in >> N;

		for(i=0;i<N;i++)
			for(j=0;j<N;j++){
				in >> team[i][j];
				//cout << team[i][j];
			}

		for(i=0;i<N;i++){
			for(j=0;j<N;j++){
				if( i!=j && team[i][j] == '.' ) continue;
				double sum = 0 ;
				double win = 0;
				for(k=0;k<N;k++){
					if( k==j ) continue;
					else if( team[i][k] == '.') continue;
					else if( team[i][k] == '0') sum ++;
					else{
						sum ++; win ++;
					}
				}
				wp[i][j] = win/sum;
			}
		}

		for(i=0;i<N;i++){
			owp[i] = 0;
			double sum = 0;
			for(j=0;j<N;j++){
				if( team[i][j] == '.') continue;
				owp[i] += wp[j][i];
				sum ++;
			}
			owp[i] /= sum;
		}

		for(i=0;i<N;i++){
			oowp[i] = 0;
			double sum = 0;
			for(j=0;j<N;j++){
				if( team[i][j] == '.') continue;
				oowp[i] += owp[j];
				sum ++;
			}
			oowp[i] /= sum;
		}

		for(i=0;i<N;i++)
			rpi[i] = 0.25*wp[i][i] + 0.5*owp[i]+0.25*oowp[i];

		out << "Case #"<<curtest<<":"<<endl;
		for(i=0;i<N;i++)
			out << rpi[i] << endl;
	}

	in.close();
	out.close();
	return 0;
}

