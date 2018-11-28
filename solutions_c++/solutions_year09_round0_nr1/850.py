#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <map>

using namespace std;

const int ALPHASIZE = 26;
const int MAXL = 15;

class Dictionary
{
	public:
		Dictionary* insert(const int id)
		{
//			int id = c-'a';
			map<int, Dictionary*>::iterator pos = next.find(id);
			if (pos == next.end()) return (next[id] = new Dictionary());
			return pos->second;
		}
		Dictionary* search(const int id)
		{ 
//			int id = c-'a';
			map<int, Dictionary*>::iterator pos = next.find(id);
			if (pos == next.end()) return NULL;
			return pos->second;
		}
	private:
		map<int, Dictionary*> next;		
};

int bucket[ALPHASIZE+1][MAXL];
Dictionary dizionario;
int casi, L;

int dfs(Dictionary* d, int c)
{
	if (d == NULL) return 0;
	if (c == L) return 1;

	int sol = 0;
	for (int i = 1; i <= bucket[0][c]; i++)
	{
		#ifdef DEBUG
			fprintf(stderr, "Livello %d - Scelgo [%c] {Sol = %d}\n", c, static_cast<char>(bucket[i][c]), sol);
		#endif
		sol += dfs(d->search(bucket[i][c]), c+1);
		#ifdef DEBUG
			fprintf(stderr, "Livello %d - Abbandono [%c] {Sol = %d}\n", c, static_cast<char>(bucket[i][c]), sol);
		#endif
	}
	return sol;
}

void solve(int caso, FILE* out)
{
	#ifdef DEBUG
		fprintf(stderr, "Analisi frase: ");
		for (int c = 0; c < L; c++)
		{
			fprintf(stderr, "(");
			for (int i = 1; i <= bucket[0][c]; i++)
				fprintf(stderr, "%c", static_cast<char>(bucket[i][c]));
			fprintf(stderr, ")");
		}
		fprintf(stderr, "\n");
	#endif

	int dfsn = dfs(&dizionario, 0);
	fprintf(out, "Case #%d: %d\n", caso, dfsn);
}

void run(FILE* in, FILE* out)
{
	int letto, par, lopen;
	char c;
	for (int caso = 1; caso <= casi; caso++)
	{
		for (int i = 0; i < L; i++) bucket[0][i] = 0; // Azzera buckets
		
		letto = 0; par = 0; lopen = 0;
		while (true)
		{
			fscanf(in, "%c", &c);
			if (c == '(') { letto = 1; par = 1; }
			else if (c == ')') { letto = 1; par = 0; lopen++; }
			else if (c < 'a' || c > 'z') // Terminatore
			{
				if (letto) // Finito un caso
				{
					solve(caso, out);
					break;
				}
			}
			else 	// Lettera del dizionario
			{
				letto = 1;
				bucket[++bucket[0][lopen]][lopen] = c;
				if (!par) lopen++;
			}
		}		
	}
}

void read(FILE* in)
{
	Dictionary* diz;
	int D; char c;

	fscanf(in, "%d%d%d", &L, &D, &casi);
	for (int d = 0; d < D; d++)
	{
		diz = &dizionario;
		for (int l = 0; l < L; l++)
		{
			fscanf(in, "%c", &c); 
			if (c < 'a' || c > 'z')
			{
				l--; continue;
			}
			#ifdef DEBUG
				fprintf(stderr, "[%c]", c);
			#endif
			diz = diz->insert(c);
		}
		#ifdef DEBUG
			fprintf(stderr, "\n");
		#endif		
	}

	#ifdef DEBUG
		fprintf(stderr, "Fine creazione dizionario!\n");
	#endif
}

int main()
{
	read(stdin);
	run(stdin, stdout);
	return 0;
}

