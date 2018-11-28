#include <stdio.h>
#include <queue>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;


#define TRACE(x) 
#define DEBUG(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)


int N, T, NA, NB;
priority_queue< pair<int, int> > trensA, trensB;
priority_queue<int> dispA, dispB;

int main() {
	scanf(" %d", &N);
	for (int _42=1; _42 <= N; _42++) {
		int needA=0, needB=0;
		while (!dispA.empty()) dispA.pop();
		while (!dispB.empty()) dispB.pop();

		scanf(" %d", &T);
		scanf(" %d %d", &NA, &NB);
		for (int i=0; i < NA; i++) {
			int hh1, mm1, hh2, mm2;
			scanf(" %d:%d %d:%d", &hh1, &mm1, &hh2, &mm2);
			trensA.push( make_pair( -1*(hh1*60+mm1), -1*(hh2*60+mm2) ) );
		}
		for (int i=0; i < NB; i++) {
			int hh1, mm1, hh2, mm2;
			scanf(" %d:%d %d:%d", &hh1, &mm1, &hh2, &mm2);
			trensB.push( make_pair( -1*(hh1*60+mm1), -1*(hh2*60+mm2) ) );
		}

		while (!trensA.empty() || !trensB.empty()) {
			if (!trensA.empty()) DEBUG("A: <%d, %d>\n", trensA.top().first, trensA.top().second);
			if (!trensB.empty()) DEBUG("B: <%d, %d>\n", trensB.top().first, trensB.top().second);

			if (trensA.empty()) {
				DEBUG("soh temos viagens de B pra A\n");
				// vamos esvaziar a lista de B
				pair<int,int> p = trensB.top();
				trensB.pop();

				if (!dispB.empty() && dispB.top() >= p.first) {
					// tem trem disponivel
					DEBUG("peguei trem disponivel em B (%d)\n", dispB.top());
					dispB.pop();
				}
				else {
					// preciso de um trem
					needB++;
				}
			}
			else if (trensB.empty()) {
				DEBUG("soh temos viagens de A pra B\n");
				// vamos esvaziar a lista de A
				pair<int,int> p = trensA.top();
				trensA.pop();

				if (!dispA.empty() && dispA.top() >= p.first) {
					// tem trem disponivel
					DEBUG("peguei trem disponivel em A (%d)\n", dispA.top());
					dispA.pop();
				}
				else {
					// preciso de um trem
					needA++;
				}
			}
			else {
				// pega o trem q deve sair mais cedo
				pair<int,int> p;
				if (trensA.top().first >= trensB.top().first) {
					DEBUG("escolhi o trem de A\n");
					p = trensA.top();
					trensA.pop();

					if (!dispA.empty() && dispA.top() >= p.first) {
						// tem trem disponivel
						DEBUG("peguei trem disponivel em A (%d)\n", dispA.top());
						dispA.pop();
					}
					else {
						// preciso de um trem
						needA++;
					}

					// poe trem disponivel em B
					dispB.push( p.second - T );
				}
				else {
					DEBUG("escolhi o trem de B\n");
					p = trensB.top();
					trensB.pop();

					if (!dispB.empty() && dispB.top() >= p.first) {
						// tem trem disponivel
						DEBUG("peguei trem disponivel em B (%d)\n", dispB.top());
						dispB.pop();
					}
					else {
						// preciso de um trem
						needB++;
					}

					// poe trem disponivel em A
					dispA.push( p.second - T );
				}
			}
		}

		printf("Case #%d: %d %d\n", _42, needA, needB);
	}


	return 0;
}
