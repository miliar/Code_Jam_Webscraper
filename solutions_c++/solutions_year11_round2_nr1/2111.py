#include <iostream>
#include <sstream>
#include <string>
#include <list>
#include <iomanip>
using namespace std;

enum Cell{
	LOST = 0,
	WIN = 1,
	NO=3
};

Cell transform( char c ){
	if( c == '0'){
		return LOST;
	}else if( c == '1'){
		return WIN;
	}
	return NO;
}

struct Player{
	double jugados;
	double ganados;
	double WP;
	double OWP;
	double OOWP;
	double RPI;
	list<int> oponentes;
	Player(): jugados(0), ganados(0), WP(0), OWP(0), OOWP(0), RPI(0){}
};
Cell sch[100][100];
void process(int test){
	cout<< "Case #"<< test << ":" << endl;

	int teams;
	cin >> teams;
	Player *jugadores = new Player[teams];
	
	Cell cell;
	char c;
	for( int i = 0 ; i < teams ; ++i ){
		for( int j = 0 ; j < teams ; ++j ){
			//jugador i
			cin >>c;
			cell =transform(c);
			sch[i][j]=cell;
			if( cell != NO ){
				jugadores[i].jugados++;
				jugadores[i].oponentes.push_back(j);
				if( cell == WIN ){
					jugadores[i].ganados++;
				}
			}
		}
		
		//calcular WP
		if( jugadores[i].jugados != 0 ){
			jugadores[i].WP = jugadores[i].ganados / jugadores[i].jugados;
		}

	}

	//calcular OWP de todos
	double acum;
	int count;
	for( int i = 0; i < teams; i++ ){
		acum = 0;
		count = 0;
		list<int>::iterator it = jugadores[i].oponentes.begin();
		while( it != jugadores[i].oponentes.end() ){
			//WP del oponente sin mi partido
			Player & oponente = jugadores[*it];
			if( oponente.jugados != 1 ){
				acum += (oponente.ganados - sch[*it][i] ) / (oponente.jugados - 1) ;
			}
			++it;
		}
		if( jugadores[i].jugados != 0 ){

			jugadores[i].OWP = acum / jugadores[i].jugados;
		}

	}

	
	// calcular OOWP, RPI and print RPI
	for( int i = 0; i < teams; i++ ){
		acum = 0;
		list<int>::iterator it = jugadores[i].oponentes.begin();
		while( it != jugadores[i].oponentes.end() ){
			acum += jugadores[*it].OWP;
			++it;
		}
		if( jugadores[i].jugados != 0 ){
			jugadores[i].OOWP = acum / jugadores[i].jugados;
		}
		jugadores[i].RPI =  0.25 * jugadores[i].WP + 0.50 * jugadores[i].OWP + 0.25 * jugadores[i].OOWP;
		cout << setprecision(12) << jugadores[i].RPI << endl;
	}

	
	delete[] jugadores;
}
int main( char * arg, int argc){
	int tests;
	cin >> tests;
	string line;
	getline(cin, line);
	for( int i = 1 ; i <= tests ; i++ ){
		process(i);
	}
	return 0;
}