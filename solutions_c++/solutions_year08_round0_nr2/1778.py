#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

typedef struct {
	int hour;
	int min;
}tempo_t;

typedef struct {
	tempo_t dep;
	tempo_t arr;
}trem_t;

void leHorario(vector< trem_t > *A, int t){
	string departure,arrival;
	tempo_t horario;
	trem_t trem;
	cin >> departure;
	string hora = departure.substr(0,2);
	string minutos = departure.substr(3,2); 			
	horario.hour = atoi(hora.c_str());
	horario.min = atoi(minutos.c_str());			
	trem.dep = horario;			
	
	cin >> arrival;			
	hora = arrival.substr(0,2);	
	minutos = arrival.substr(3,2);	
	horario.hour = atoi(hora.c_str());
	horario.min = atoi(minutos.c_str());
	horario.min += t;
	trem.arr = horario;
	(*A).push_back(trem);
}

bool arrivalComp(trem_t a, trem_t b){
	if (a.arr.hour < b.arr.hour)
		return true;
	if (a.arr.hour > b.arr.hour)
		return false;
	if (a.arr.min < b.arr.min)
		return true;
	return false;
}
bool departureComp(trem_t a, trem_t b){
	if (a.dep.hour < b.dep.hour)
		return true;
	if (a.dep.hour > b.dep.hour)
		return false;
	if (a.dep.min < b.dep.min)
		return true;
	return false;
}

int main(){
	int ncases,cont = 0;
	cin >> ncases;
	while (ncases != 0){
		cont++;
		vector< trem_t > A, B;
		int turnaround, na, nb, nTrensA, nTrensB;
		cin >> turnaround;
		cin >> na >> nb;
		nTrensA = na;
		nTrensB = nb;
		for (int i = 0 ; i < na; i++){
			leHorario(&A,turnaround);
		}
		for (int i = 0 ; i < nb; i++){
			leHorario(&B,turnaround);
		}		
		
		set<int> listaTabu;
		listaTabu.clear();
		sort(A.begin(),A.end(), departureComp);
		sort(B.begin(),B.end(), arrivalComp);
		/*
		cout << "A" << endl;
		for (int i = 0 ; i < A.size(); i++){
			cout << A[i].dep.hour << ":" << A[i].dep.min << " ";
			cout << A[i].arr.hour << ":" << A[i].arr.min << endl;
		}
		cout << "B" << endl;
		for (int i = 0 ; i < B.size(); i++){
			cout << B[i].dep.hour << ":" << B[i].dep.min << " ";
			cout << B[i].arr.hour << ":" << B[i].arr.min << endl;
		}
		cout << endl;
		*/
		for ( int i = 0 ; i < B.size(); i++){
			trem_t tremB = B[i];			
			for (int k = 0; k < A.size(); k++){
				/*
				cout << "lista = ";
				set<int>::iterator it;
				for (it = listaTabu.begin(); it != listaTabu.end(); it++)
					cout << *it << " ";
				cout << endl;
				*/
				trem_t tremA = A[k];
				/*
				cout << "trem B chega ";
				cout << tremB.arr.hour << ":" << tremB.arr.min << endl;				
				cout << "trem A sai ";
				cout << tremA.dep.hour << ":" << tremA.dep.min << endl;
				*/
				if (tremA.dep.hour > tremB.arr.hour){
					//A.erase(A.begin()+k);
					if (listaTabu.insert(k).second){
						nTrensA--;					
						break;
					}
					else continue;
				}
				if (tremA.dep.hour < tremB.arr.hour){					
					continue;
				}
				if (tremA.dep.min >= tremB.arr.min){
					//A.erase(A.begin()+k);
					if (listaTabu.insert(k).second){
						nTrensA--;					
						break;
					}else continue;
				}else{					
					continue;
				}
			}
		}
		
		listaTabu.clear();
		sort(A.begin(),A.end(), arrivalComp);
		sort(B.begin(),B.end(), departureComp);
		
		for ( int i = 0 ; i < A.size(); i++){
			trem_t tremA = A[i];			
			for (int k = 0 ; k < B.size(); k++){
				//~ cout << "B.size = " << B.size() << endl;
				//~ cout << "k = " << k <<  endl;
				trem_t tremB = B[k];
				if (tremB.dep.hour > tremA.arr.hour){
					//B.erase(B.begin()+k);
					if (listaTabu.insert(k).second){
						nTrensB--;
						break;
					}else continue;
				}
				if (tremB.dep.hour < tremA.arr.hour)					
					continue;
				
				if (tremB.dep.min >= tremA.arr.min){
					//B.erase(B.begin()+k);
					if (listaTabu.insert(k).second){
						nTrensB--;
						break;
					}else continue;
				}else continue;
				
			}
		}
		
		cout << "Case #" << cont << ": " << nTrensA << " " << nTrensB << endl;
		ncases--;
	}
	
	return 0;
}
