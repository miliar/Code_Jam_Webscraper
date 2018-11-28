#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <cctype>
using namespace std;

#define MAXNA 100
#define MAXNB 100
#define MAXT 60

struct Hora {
	int hora, min;
	int hora2, min2;
	bool operator<(const Hora &h) const
	{
		if (hora != h.hora) {
			return hora < h.hora;
		}
		return min < h.min;
	}
	bool somar(int T) 
	{
		if (T == 60) {
			++hora;
		}
		min += T;
		
		if (min >= 60) {
			++hora;
			min = min - 60;
		}
		
		return ! (hora >= 24);
	}
};

int N, T, NA, NB;
int partiuA, partiuB;
int answerA, answerB;
Hora horA[MAXNA];
Hora horB[MAXNB];
list<Hora> comboiosA;
list<Hora> comboiosB;

void
processaA()
{
	//e' preciso usar um comboio
	if (comboiosA.size() == 0 ||  horA[partiuA] < *(comboiosA.begin())) {
		++answerA; 
	}
	else {
		comboiosA.erase(comboiosA.begin());
	}
	Hora novoC;
	novoC.hora = horA[partiuA].hora2;
	novoC.min = horA[partiuA].min2;
	novoC.somar(T);
	comboiosB.push_back(novoC);
	comboiosB.sort();
	
	//cout << "partiu de A: " << horA[partiuA].hora << " " << horA[partiuA].min << " " << answerA << endl; 
	++partiuA;
}

void
processaB()
{
	//e' preciso usar um comboio
	if (comboiosB.size() == 0 ||  horB[partiuB] < *(comboiosB.begin())) {
		++answerB; 
	}
	else {
		comboiosB.erase(comboiosB.begin());
	}
	Hora novoC;
	novoC.hora = horB[partiuB].hora2;
	novoC.min = horB[partiuB].min2;
	novoC.somar(T);
	comboiosA.push_back(novoC);
	comboiosA.sort();
	
	//cout << "partiu de B: " << horB[partiuB].hora << " " << horB[partiuB].min << " " << answerB << endl; 
	++partiuB;
}

bool
escolhe_seguinte()
{
	if (partiuA == NA && partiuB == NB) {
		return false;
	}
	if ((partiuA == NA || horB[partiuB] < horA[partiuA]) && partiuB != NB) {
		processaB();
		return true;
	}
	if ((partiuB == NB || horA[partiuA] < horB[partiuB]) && partiuA != NA) {
		//cout << "dois" << endl;
		processaA();
		return true;
	}
	else {
		//cout << "tres" << endl;
		processaA();
		processaB();
		return true;
	}
	
}

int
main()
{
	cin >> N;

	for (int n = 1; n <= N; n++) {
		partiuA = 0, partiuB = 0;
		answerA = 0, answerB = 0;
		comboiosA.clear(); comboiosB.clear();
		cin >> T;
		cin >> NA >> NB;
		
		//ler horarios e fazer sort deles!
		for (int i = 0; i < NA; i++) {
			scanf("%d:%d", &horA[i].hora, &horA[i].min);
			scanf("%d:%d", &horA[i].hora2, &horA[i].min2);
			//cout << horA[i].hora << " " << horA[i].min << " " << horA[i].hora2 << " " << horA[i].min2 << endl;
		}
		for (int i = 0; i < NB; i++) {
			scanf("%d:%d", &horB[i].hora, &horB[i].min);
			scanf("%d:%d", &horB[i].hora2, &horB[i].min2);
			//cout << horB[i].hora << " " << horB[i].min << " " << horB[i].hora2 << " " << horB[i].min2 << endl;
		}
		sort(horA, horA + NA);
		sort(horB, horB + NB);
		
		while (escolhe_seguinte());
	
		cout << "Case #" << n << ": " << answerA << " " << answerB << endl; 
	}


	return 0;
}
