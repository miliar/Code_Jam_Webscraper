#include <iostream>
#include <cstdlib>

using namespace std;

struct Team{
	int *games;
	double *WP;
	double totWP;
	double OWP;
	double OOWP;
	double RPI;
	int gameswon, totalgames;
};

void owp(Team* tourn,int teams);
void oowp(Team* tourn, int teams);
double rpi(double WP, double OWP, double OOWP);

int main()
{
	int tests=0;
	int teams;
	cin >> tests;
	for (int k=0;k<tests;k++){
		cin >> teams;
		Team* tourn=new Team[teams];
		for (int i=0;i<teams;i++){
			tourn[i].games=new int[teams];
			char *t=new char;
			int gameswon=0, totalgames=0;
			for (int j=0;j<teams;j++){
				cin >> *t;
				if (*t=='.') tourn[i].games[j]=3;
				else{
					tourn[i].games[j]=atoi(t);
					totalgames++;
					if (*t=='1') gameswon++;
				}

			}
			tourn[i].totWP=double(gameswon)/double(totalgames);
			tourn[i].WP=new double[teams];
			for (int j=0;j<teams;j++){
				int adjgw=gameswon;
				int adjtotg=totalgames;
				if (tourn[i].games[j] == 0){
					adjtotg--;
				}
				else if (tourn[i].games[j]==1){
					adjgw--;
					adjtotg--;
				}
				if (tourn[i].games[j]< 3) tourn[i].WP[j]=double(adjgw)/double(adjtotg);
			}
			tourn[i].gameswon=gameswon;
			tourn[i].totalgames=totalgames;
		}
		owp(tourn, teams);
		oowp(tourn, teams);

		cout << "Case #" << k+1 << ": \n";
		for (int i=0;i<teams;i++){
			double frpi=rpi(tourn[i].totWP,tourn[i].OWP,tourn[i].OOWP);
			cout << frpi << endl;
		}
	}

	return 0;
}


void owp(Team* tourn,int teams)
{

	for (int i=0;i<teams;i++){
		double avWP=0;
		for (int j=0;j<teams;j++){
			if (tourn[i].games[j] < 3){
				avWP+=tourn[j].WP[i];
			}
		}
		avWP /=(tourn[i].totalgames);
		tourn[i].OWP=avWP;
	}

}
void oowp(Team* tourn, int teams)
{
	for (int i=0;i<teams;i++){
		double avOWP=0;
		for (int j=0;j<teams;j++){
			if (tourn[i].games[j] < 3){
				avOWP+=tourn[j].OWP;
			}
		}
		avOWP /= tourn[i].totalgames;
		tourn[i].OOWP=avOWP;
	//	cout << avOWP << endl;
	}


}

double rpi(double WP, double OWP, double OOWP)
{
	return (.25*WP+.5*OWP+.25*OOWP);
}
