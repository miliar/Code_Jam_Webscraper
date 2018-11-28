#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>

const bool OFF = false;
const bool ON = true;

typedef struct Snapper_st
{
	bool state;
	bool power;
	struct Snapper_st *next;
} Snapper;

Snapper *createSnapper()
{
Snapper *s = new Snapper;

	s->state = OFF;
	s->power = OFF;
	s->next = NULL;
	return s;
}

void freeSnapper(Snapper *l)
{
	if (l)
	{
		freeSnapper(l->next);
		delete l;
	}
}

Snapper *connectSnapper(Snapper *list, Snapper *dev)
{
Snapper *aux = list;

	if (!aux)
		return dev;
	else
	{
		while (aux->next != NULL)
			aux = aux->next;
			
		aux->next = dev;
		return list;
	}
}

void snap(Snapper *list)
{
	if (!list) return;
	
	if (list->power)
	{
		if (list->state == ON)
		{
			snap(list->next);
			if (list->next) list->next->power = OFF;
			list->state = OFF;
		}
		else
		{
			list->state = ON;
			if (list->next) list->next->power = ON;
		}
	}			
}

bool isOn(Snapper *list)
{
	if (list)
		return (list->state == ON) && (isOn(list->next));
	else
		return true;
}

void displaySnappers(Snapper *list)
{
	if (list)
	{
		printf(" [p = %d, s = %d] --> ", list->power, list->state);
		displaySnappers(list->next);
	}
	else
		printf(" * \n");
}

void caseNumber(int i, int snappersn, int snapsn)
{
Snapper *s = NULL;
int k;
	
	for (k=1; k<=snappersn; k++)
		s = connectSnapper(s, createSnapper());
		
	s->power = ON;
	
	for (k=1; k<=snapsn; k++)
		snap(s);
		
	if (isOn(s))
		printf("Case #%d: ON\n", i);
	else
		printf("Case #%d: OFF\n", i);
		
	freeSnapper(s);
}

int main()
{
std::ifstream in;
unsigned long int T, N, K, i;

	in.open("snapper_in");
	if (!in.is_open())
	{
		std::cerr << "Error opening file \"snapper_in\"" << std::endl;
		return 1;
	}
	
	in >> T;
	for (i=1; i<=T; i++)
	{
		in >> N;
		in >> K;
		caseNumber(i, N, K);	
	}
	
	in.close();
	return 0;
}



