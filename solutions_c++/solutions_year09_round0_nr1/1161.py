#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

const int MAX_NB_CASE = 500;
const int MAX_NB_MOTS = 5000;
const int TAILLE_MAX = 15;


int nbCases;
int nbMots, taille;

char mots[MAX_NB_MOTS][TAILLE_MAX + 10];
bool is[TAILLE_MAX][26];

bool match(int mot)
{
	for(int t = 0; t < taille; t++)
		if(!is[t][mots[mot][t] - 'a'])
			return false;
	return true;
}
int solve()
{
	memset(is, false, sizeof(is));
	int car = 0;
	bool in = false;
	while(true)
	{
		char c;
		scanf("%c", &c);
		if(c == '\n') break;
		else if(c == '(') in = true;
		else if(c == ')') in = false;
		else is[car][c - 'a'] = true;
		if(!in) car++;
	}
	
	int ret = 0;
	for(int mot = 0; mot < nbMots; mot++)
	{
		if(match(mot))
			ret++;
	}
	return ret;
}

int main()
{
	scanf("%d%d%d\n", &taille, &nbMots, &nbCases);
	for(int mot = 0; mot < nbMots; mot++)
		scanf("%s\n", mots[mot]);
	
	for(int c = 0; c < nbCases; c++)
		printf("Case #%d: %d\n", (c+1), solve());
	return 0;
}
