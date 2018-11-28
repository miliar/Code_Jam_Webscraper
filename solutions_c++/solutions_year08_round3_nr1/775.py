#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <map>
#include <vector>
#include <math.h>



using namespace std;

#define TAB_SIZE 2000
#define REP(i,b) for (int i=1, _b=(b); i<=_b; i++)
#define REP0(i,b) for (int i=0, _b=(b); i<_b; i++)
#define FORD(i,a,b) for (int _b=(b), i=(a); i>=_b; --i)
#define PB push_back

#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
/*zeby pisac FORE(i, vector) */


class Thing{

	public:
		int id;
		int key1;
		int key2;
		Thing();
		Thing(int);
		Thing(int, int);
		Thing(int, int, int);

};

Thing::Thing(){
	key1 = 0;
	key2 = 0;
}

Thing::Thing(int i){
	id = i;
	key1 = 0;
	key2 = 0;

}

Thing::Thing(int i, int k1, int k2){
	id = i;
	key1 = k1;
	key2 = k2;

}
Thing::Thing(int k1, int k2){
	key1 = k1;
	key2 = k2;
}


bool operator<(const Thing& a, const Thing& b) {
   return (a.key1 < b.key1) || (a.key1 == b.key1 && a.key2 < b.key2);
}


int main(){
ofstream fout("A-small.out");
ifstream f("A-small.in");
//ofstream fout("A-large.out");
//ifstream f("A-large.in");

int i, j, N, big, n1, n2, small, p, k, l, z;
int res = 0, tmp;
vector<int> w1, w2;
vector<Thing> w;
string line;
//int klawisz[LITERY];
Thing t;

	f >> N;
	REP(big, N){
		//w1.PB(rand());
		f >> p;
		f>> k;
		f>>l;
		w1.clear();
		REP0(j, l){
			/*t.id = j;
			f >> t.key1;
			w.PB(t);*/
			f >> tmp;
			w1.PB(tmp);
		}
		REP0(j, l){
			cout << w1.at(j) << " ";

		}
		cout << endl;

		sort(w1.rbegin(), w1.rend());
		REP0(j, l){
			cout << w1.at(j) << " ";

		}
		cout << endl;
		int zakres = l/k;
		cout << zakres << endl;
		if (zakres > p){
			fout << "Case #" << big << ": " << "IMPOSSIBLE" << endl;
		
			cout << "tu" << endl;
		}
		else
		{	res = 0;
			cout << "klawisze " << k << endl;
			int gratis = 0;
			REP0(j, l){
				
				for (z = j; (z < j + k && z < l); z++){
					cout << z << endl;
					res += (gratis + 1) * w1.at(z);
				}
				/*if (j + k >= l){
					res += (gratis + 2) * 

				}*/
				j = j + k - 1;
				gratis++;
			
			}




		//w.PB();
		fout << "Case #" << big << ": " << res << endl; 

		}/* else od impossible */
	}
	/*FORE(thing, w1){
		cout << *thing << endl;
	}*/
	/*FORD(big, N, 1){

		fout << "Case #" << big << ": " << res << endl; 
	}*/
	fout << flush;
	fout.close();
	f.close();

	return 0;


}
