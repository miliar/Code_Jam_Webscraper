/* 
 * Wczytywanie danych w podstawowej wersji powinno juz dzialac, ale trzeba to wszystko
 * dosyc solidnie zdebugowac. Nie mam pojecia, jak jakos "fajniej" podejsc do tego
 * problemu, chyba bede pisal po prostu brute-force'a => symulacje przebiegu dnia.
 */

#include <stdio.h> 

#include <multimap.h> 
#include <stack.h> 
#include <vector.h> 

using namespace std;

enum structure_sig { ATRAINS, BTRAINS, ADEP, AARR, BDEP, BARR };

typedef struct {
	int dep;
	int arr;
} train_move;

int read_number() {

	char *wzor = "0";
	char *tmp = new char[255];	
	scanf(" %[0123456789]s", tmp);

	fprintf(stderr, "\t\t read_number:: readed: '%s' \n", tmp);

	return (tmp[0] - wzor[0])*10 + (tmp[1] - wzor[0]);
}

int read_hour_min() {
	int hour = read_number();
	char c;
	scanf("%c",&c);
	int min = read_number();		

	fprintf(stderr, "\t hour: %d min: %d \n",hour, min);

	return hour*60+ min;
}

void change_empty( vector <structure_sig> &empty_structs, structure_sig structure) {
	bool found = false;
	for (vector <structure_sig>::iterator i = empty_structs.begin(); (i != empty_structs.end()) && (!found); i++)
		if ((*i) == structure) found = true;
	if (!found) empty_structs.push_back(structure);
}

int main() {

	unsigned int n;
	scanf("%d", &n);
	
	for (unsigned int i = 0; i < n; i++) {

		unsigned int t;
		scanf("%d", &t);

		unsigned int na, nb;
		scanf("%d %d", &na, &nb);

		multimap <int, train_move> A_dep, B_arr, A_arr, B_dep;

		fprintf(stderr, "\n\nt: %d na: %d nb: %d \n", t, na, nb);

		for (unsigned int j = 0; j < na; j++) {
			// wykorzystac kontener stl'owy do magazynowania i posortowania tych naszych rzeczy wzgledem godzin odjazdu,
			// a pozniej wzgledem godzin przyjazdu. Puscic 4 iteratory po 4 listach:
			// 	-> przyjazdow na A
			// 	-> odjazdow z A
			// 	-> przyjazdow na B
			// 	-> odjazdow z B
			// i to wszystko powinno w sumie dac potrzebne do udzielenia poprawnej odpowiedzi informacje. 
			//
			fprintf(stderr, "read: %d \n",j);
			train_move tmp;
			tmp.dep = read_hour_min();
			tmp.arr = read_hour_min();

			map <int, train_move>::value_type dep(tmp.dep, tmp), arr(tmp.arr, tmp);
			A_dep.insert(dep);
			B_arr.insert(arr);
		}

		for (unsigned int j = 0; j < nb; j++) {
			train_move tmp;
			tmp.dep = read_hour_min();
			tmp.arr = read_hour_min();
			
			map <int, train_move>:: value_type dep(tmp.dep, tmp), arr(tmp.arr, tmp);
			B_dep.insert(dep);
			A_arr.insert(arr);
		}

		// debugowanie
		for (multimap<int, train_move>::iterator k = A_dep.begin(); k != A_dep.end(); k++)
			fprintf(stderr, "A_dep: dep: %d arr %d \n",(*k).second.dep, (*k).second.arr);
		for (multimap<int, train_move>::iterator k = B_arr.begin(); k != B_arr.end(); k++)
			fprintf(stderr, "B_arr: dep: %d arr %d \n",(*k).second.dep, (*k).second.arr);

		for (multimap<int, train_move>::iterator k = B_dep.begin(); k != B_dep.end(); k++)
			fprintf(stderr, "B_dep: dep: %d arr %d \n",(*k).second.dep, (*k).second.arr);

		for (multimap<int, train_move>::iterator k = A_arr.begin(); k != A_arr.end(); k++)
			fprintf(stderr, "A_arr: dep: %d arr %d \n",(*k).second.dep, (*k).second.arr);


		// powiedzmy, ze jest ok, teraz robimy algorytm symulacji kolei
		multimap <int, train_move>::iterator A_dep_i = A_dep.begin(), A_arr_i = A_arr.begin(), B_dep_i = B_dep.begin(), B_arr_i = B_arr.begin();

		// jeszcze trzeba pamietac wszystkie lokomotywy i o ktorej beda wolne
		unsigned int A_free = 0, B_free = 0; // liczba wolnych lokomotyw i gotowych do uzytku na stacji A i B
		multimap < int, int > A_trains, B_trains; // nawracajace lokomotywy na stosie trzymane, tak naprawde interesuja nas tylko klucze

		bool end = false; 
//		vector<structure_sig> empty_structs; // tam sa wszystkie oproznione juz strutktury
	//		empty_structs.clean();
		 
		unsigned int trains_needed_a = 0, trains_needed_b = 0;
		// przeprowadzamy symulacje
		while (!end) {
			// wybieramy z hash-map (czterech) i stosu nawracajacych rzeczy, wrzucamy do pomocniczej struktury, 
			// z ktorej zdejmujemy najwczesniejsze.
			multimap <int, structure_sig> help_struct;
				help_struct.clear();
			fprintf(stderr, "\n iteracja: A_free: %d B_free: %d trains_needed: %d %d \n", A_free, B_free, trains_needed_a, trains_needed_b);
			if (!B_trains.empty())
			fprintf(stderr, " B_trains top: %d \n",(*B_trains.begin()).first);

			if (!A_trains.empty()) help_struct.insert( pair <int, structure_sig> ((*A_trains.begin()).first*10-1, ATRAINS) );		
//			else change_empty(empty_structs, ATRAINS);

			if (!B_trains.empty()) help_struct.insert( pair <int, structure_sig> ((*B_trains.begin()).first*10-1, BTRAINS) );		
//			else change_empty(empty_structs, BTRAINS);

			if (A_dep_i != A_dep.end()) help_struct.insert( pair <int, structure_sig> ((*A_dep_i).first*10, ADEP) );
//			else change_empty(empty_structs, ADEP);

			if (A_arr_i != A_arr.end()) help_struct.insert( pair <int, structure_sig> ((*A_arr_i).first*10-1, AARR) );
//			else change_empty(empty_structs, AARR);

			if (B_dep_i != B_dep.end()) help_struct.insert( pair <int, structure_sig> ((*B_dep_i).first*10, BDEP) );
//			else change_empty(empty_structs, BDEP);

			if (B_arr_i != B_arr.end()) help_struct.insert( pair <int, structure_sig> ((*B_arr_i).first*10-1, BARR) );
//			else change_empty(empty_structs, BARR);

			if (help_struct.empty()) end = true;
			else {
				// przetwarzamy juz wybrane dane z help_struct
				map <int, structure_sig>::iterator ak = help_struct.begin();
				switch ((*ak).second) {
					case ATRAINS:
						fprintf(stderr, "\t case ATRAINS %d \n", (*ak).first);
						A_free++;
						A_trains.erase(A_trains.begin());
						break;

					case BTRAINS:
						fprintf(stderr, "\t case BTRAINS %d \n", (*ak).first);
						B_free++;
						B_trains.erase(B_trains.begin());
						break;

					case ADEP:
						fprintf(stderr, "\t case ADEP %d \n", (*ak).first);

						if (A_free == 0) trains_needed_a++; else A_free--;
						A_dep_i++;											
						break;

					case BDEP:
						fprintf(stderr, "\t case BDEP %d \n", (*ak).first);

						if (B_free == 0) trains_needed_b++; else B_free--;
						B_dep_i++;
						break;
					case AARR:	
						fprintf(stderr, "\t case AARR %d \n", (*ak).first);
						A_trains.insert(pair <int, int> ( (*A_arr_i).first+t, 0 ) );
//						fprintf(stderr, "\t\t A_trains push: %d \n",A_trains.top());
						A_arr_i++;
						break;

					case BARR:
						fprintf(stderr, "\t case BARR %d \n", (*ak).first);

						B_trains.insert(pair <int, int> ( (*B_arr_i).first+t, 0 ) );
//						fprintf(stderr, "\t\t B_trains push: %d size: %d \n",B_trains.top(), B_trains.size());
						B_arr_i++;
						break;

				}
			}
		}
		
		// ODPOWIEDZ:
		printf("Case #%d: %d %d\n", i+1, trains_needed_a, trains_needed_b);
		// TODO: WARUNKI BRZEGOWE!!
	}	


	return 0;
}
