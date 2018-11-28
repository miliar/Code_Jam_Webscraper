#include <cstdio>
#include <list>

#define INFINITO 1<<30

using namespace std;

class viagem {
	public:
	int saida;
	int chegada;

	bool operator< (const viagem &v) const {
		return saida < v.saida;
	}
};

list<viagem> la, lb;

char pega_menor_lado (void) {
	if (la.empty())
		return 'b';
	else if (lb.empty())
		return 'a';

	if (la.front().saida < lb.front().saida)
		return 'a';
	return 'b';
}

int tem_saida (list<viagem> &l, int tempo) {
	list<viagem>::iterator it;

	for (it=l.begin(); it!=l.end(); ++it) {
		if (it->saida >= tempo) {
			int r = it->chegada;
			l.erase(it);
			return r;
		}
	}
	return 0;
}

int main (void) {

	char lado;	
	int i, k;
	int casos;
	int a, b, c, d;
	int r, t, na, nb;
	viagem v;
	int tempo, trens_a, trens_b;

	scanf("%d", &casos);

	for (k=0; k<casos; ++k) {

		la.clear();
		lb.clear();

		scanf("%d", &t);
		scanf("%d %d", &na, &nb);

		for (i=0; i<na; ++i) {
			scanf("%d:%d %d:%d", &a, &b, &c, &d);

			v.saida = a*60 + b;
			v.chegada = c*60 + d;
			la.push_back(v);
		}

		for (i=0; i<nb; ++i) {
			scanf("%d:%d %d:%d", &a, &b, &c, &d);

			v.saida = a*60 + b;
			v.chegada = c*60 + d;
			lb.push_back(v);
		}

		if (!la.empty()) la.sort();
		if (!lb.empty()) lb.sort();

		tempo=0;
		trens_a=trens_b=0;
		lado=0;
		while (!la.empty() || !lb.empty()) {
			if (lado == 0) {
				lado = pega_menor_lado();
				tempo=0;
				if (lado=='a')
					trens_a++;
				else
					trens_b++;
			}

			if (lado == 'a') {
				r = tem_saida(la, tempo);
				if (r) {
					tempo = r+t;
					lado='b';
				}
				else
					lado=0;
			}
			else {
				r = tem_saida(lb, tempo);
				if (r) {
					tempo = r+t;
					lado='a';
				}
				else
					lado=0;
			}
		}

		printf("Case #%d: %d %d\n", k+1, trens_a, trens_b);
	}

	return 0;
}
