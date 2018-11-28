#include <iostream>
#include <cstdio>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
int main() {
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int T,N,S, p;
	cin >> T; // Leo la cantidad de test cases
	
	for(int i=0; i<T; i++){
		cin >> N >> S >> p; // Leo la cantidad participantes, puntajes sorprendentes y el puntaje
		vector<int> punt; // La lista con los puntajes
		vector<int> cool; // Un puntaje es cool si hay alguna nota mayor a p
		vector<int> uncool; // Un puntaje es uncool si [N/3] < p-2 (siempre la nota va a ser menor a p)
		vector<int> decide; // Y buen, hay que decidir con los otros valores
		punt.resize(N); cool.resize(0); uncool.resize(0); decide.resize(0);
		
		for(int j=0; j<N; j++){
			cin >> punt[j];
		}
		for(int j=0; j<N;j++){
			if((punt[j]+4) < 3*p || (punt[j]==0 && p>0)){
				uncool.push_back(punt[j]);
			}
			else if(punt[j] >3*(p-1) || (punt[j]==0 && p==0)){
				cool.push_back(punt[j]);
			}
			else{
				decide.push_back(punt[j]);
			}
		}
		
		int counter=0;
		/*if(S > decide.size()){
			counter = cool.size()+decide.size();
		}
		else counter = cool.size() + S;*/
		int k=decide.size();
		counter = cool.size() + min(S,k);
		cout << "Case #" << i+1 << ": " << counter << endl;
		cerr << "Case #" << i+1 << ": " << counter << endl;
		counter=0;
	}		
	
	return 0;
}
