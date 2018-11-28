#include<iostream>
#include<fstream>
using namespace std;
double RPI[105],WP[105],OWP[105],OOWP[105];
char opponent[105][105],nopp[105],wins[105];
char a[105][105];
int n;
void wp(int i)
{
	if(WP[i] != 0)
		return;
	WP[i] = double(wins[i])/nopp[i];
	return;
}
void owp(int i)
{	
	if(OWP[i] != 0)
		return;
	int j;
	double s = 0;
	for(j = 1; j <= nopp[i]; j++) {
		//wp(opponent[i][j]);
		//s += WP[opponent[i][j]];
		s += (double(wins[opponent[i][j]] - a[opponent[i][j]][i])/ (nopp[opponent[i][j]] - 1));
	}
	/*for(j = 1; j < i ; j++) {
		wp(j);
		s += WP[j];
	}
	for(j = i + 1; j <= n; j++) {
		wp(j);
		s += WP[j];
	}*/
	OWP[i] = s / nopp[i];
	//OWP[i] = s / (n - 1);
	return;
}
void oowp(int i)
{
	if(OOWP[i] != 0)
		return;
	int j;
	double s = 0;
	for(j = 1; j <= nopp[i]; j++) {
		owp(opponent[i][j]);
		s += OWP[opponent[i][j]];
	}
	/*for(j = 1; j < i ; j++) {
		wp(j);
		s += OWP[j];
	}
	for(j = i + 1; j <= n; j++) {
		wp(j);
		s += OWP[j];
	}*/
	OOWP[i] = s / nopp[i];
	//OOWP[i] = s / (n - 1);
	return;
}
void rpi(int i)
{
	if(RPI[i] != 0)
		return;
	wp(i);
	owp(i);
	oowp(i);
	RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
	return;
}
int main()
{
	char aux;
	ifstream fin("date.txt");
	ofstream fout("output.out");
	int i,j,t,test;
	fin>>t;
	for(test = 1; test <= t; test++) {
		fin>>n;
		memset(RPI ,0,sizeof(double[104]));
		memset(WP  ,0,sizeof(double[104]));
		memset(OWP ,0,sizeof(double[104]));
		memset(OOWP,0,sizeof(double[104]));
		memset(nopp,0,sizeof(char[104]));
		memset(wins,0,sizeof(char[104]));
		for(i = 1; i <= n; i++) {
			for(j = 1; j <= n; j++) {
				fin>>aux;
				if(aux == '.') {
					a[i][j] = 2;
				} else {
					nopp[i]++;
					opponent[i][int(nopp[i])] = j;
					if(aux == '0') {
						a[i][j] = 0;
					} else {
						wins[i]++;
						a[i][j] = 1;
					}
				}
			}
		}
		fout<<"Case #"<<test<<":\n";
		for(i = 1; i <= n; i++) {
			rpi(i);
			fout<<RPI[i]<<'\n';
		}
	}
}
