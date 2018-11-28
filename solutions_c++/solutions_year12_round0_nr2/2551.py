#include <iostream>
#include <map>
#include <set>
#include <cstdio>
using namespace std;

/*
Google CodeJam 2012 - Problem B
Guillermo Croppi (Argentina)

I did all the combinations in paper, used set cause the order of the points doesnt matter

*/

void Adding(int key, int a, int b, int c, map< int,set<int> > & m){
	int init[] = {a,b,c};
	set<int> s (init,init+3);
	pair <int,set<int> > p;
	p = make_pair (key, s);
	m.insert( p );
}

int main(int argc, char *argv[]) {
	
	map< int,set<int> > notSurprise;
	map< int,set<int> > Surprise;
	set<int>::iterator it;
	int cases;
	int casesCount = 1;
	int googlers;
	int surprisingTriplets;
	int p;
	int aux;
	int points;
	int cont_notSur;
	int cont_sur;
	int cont_both;
	int cont_impossible;
	int sum;
	int flag_notSur = 0; // Marca que se encontro un puntaje >= a p en notSurprise;
	int flag_Sur = 0; // Marca que se encontro un puntaje >= a p en notSurprise;
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	Adding(0,0,0,0,notSurprise);
	Adding(1,1,0,0,notSurprise);
	Adding(2,1,1,0,notSurprise);
	Adding(3,1,1,1,notSurprise);
	Adding(4,2,1,1,notSurprise);
	Adding(5,2,2,1,notSurprise);
	Adding(6,2,2,2,notSurprise);
	Adding(7,3,2,2,notSurprise);
	Adding(8,3,3,2,notSurprise);
	Adding(9,3,3,3,notSurprise);
	Adding(10,4,3,3,notSurprise);
	Adding(11,4,4,3,notSurprise);
	Adding(12,4,4,4,notSurprise);
	Adding(13,5,4,4,notSurprise);
	Adding(14,5,5,4,notSurprise);
	Adding(15,5,5,5,notSurprise);
	Adding(16,6,5,5,notSurprise);
	Adding(17,6,6,5,notSurprise);
	Adding(18,6,6,6,notSurprise);
	Adding(19,7,6,6,notSurprise);
	Adding(20,7,7,6,notSurprise);
	Adding(21,7,7,7,notSurprise);
	Adding(22,8,7,7,notSurprise);
	Adding(23,8,8,7,notSurprise);
	Adding(24,8,8,8,notSurprise);
	Adding(25,9,8,8,notSurprise);
	Adding(26,9,9,8,notSurprise);
	Adding(27,9,9,9,notSurprise);
	Adding(28,10,9,9,notSurprise);
	Adding(29,10,10,9,notSurprise);
	Adding(30,10,10,10,notSurprise);
	
	Adding(2,2,0,0,Surprise);
	Adding(3,2,1,0,Surprise);
	Adding(4,2,2,0,Surprise);
	Adding(5,3,1,1,Surprise);
	Adding(6,3,2,1,Surprise);
	Adding(7,3,3,1,Surprise);
	Adding(8,4,2,2,Surprise);
	Adding(9,4,3,2,Surprise);
	Adding(10,4,4,2,Surprise);
	Adding(11,5,3,3,Surprise);
	Adding(12,5,4,3,Surprise);
	Adding(13,5,5,3,Surprise);
	Adding(14,6,4,4,Surprise);
	Adding(15,6,5,4,Surprise);
	Adding(16,6,6,4,Surprise);
	Adding(17,7,5,5,Surprise);
	Adding(18,7,6,5,Surprise);
	Adding(19,7,7,5,Surprise);
	Adding(20,8,6,6,Surprise);
	Adding(21,8,7,6,Surprise);
	Adding(22,8,8,6,Surprise);
	Adding(23,9,7,7,Surprise);
	Adding(24,9,8,7,Surprise);
	Adding(25,9,9,7,Surprise);
	Adding(26,10,8,8,Surprise);
	Adding(27,10,9,9,Surprise);
	Adding(28,10,10,8,Surprise);

	scanf("%d",&cases);
	while(cases--){
		cont_sur = cont_notSur = cont_both = cont_impossible = sum = 0;
		scanf("%d %d %d", &googlers, &surprisingTriplets, &p);
		aux = googlers;
		while(aux--){
			scanf("%d", &points);
			flag_notSur = flag_Sur = 0;
			for (it=notSurprise[points].begin(); it!=notSurprise[points].end(); it++) if(*it >= p) flag_notSur = 1;
			for (it=Surprise[points].begin(); it!=Surprise[points].end(); it++) if(*it >= p) flag_Sur = 1;
			if(flag_Sur && flag_notSur) cont_both++;
			if(!flag_Sur && flag_notSur) cont_notSur++;
			if(flag_Sur && !flag_notSur) cont_sur++;
			if(!flag_Sur && !flag_notSur) cont_impossible++;
		}
		if(surprisingTriplets == 0) sum = cont_notSur + cont_both;
		else if(surprisingTriplets > 0 && cont_sur <= surprisingTriplets){
			sum = cont_notSur + cont_both + cont_sur;
		}
		else if(surprisingTriplets > 0 && cont_sur > surprisingTriplets){
			sum = cont_notSur + cont_both + surprisingTriplets;
		}
		//cout << "This case: " << cont_notSur << " " << cont_sur << " " << cont_both << " " << cont_impossible << endl;
		cout << "Case #" << casesCount++ << ": " << sum << endl;
	}
	
	return 0;
}

