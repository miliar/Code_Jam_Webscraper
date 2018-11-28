#include <iostream>
#include <fstream>

#define INPUT_F "A-large.in"
#define OUTPUT_F "A-large.out"
using namespace std;
struct List
{
	char sym;
	int n;
	List *next;
};

unsigned long long getres (int dym, int size, int *ress)
{
	long long exp = 1;
	unsigned long long res = 0;
	if (dym == 1) dym = 2;
	for ( int i = size; i >= 0; i--)
	{
		res += ress[i]*exp;
		exp *= dym;
	}
	return res;
}

int main ()
{
	fstream fin, fout;
	fin.open ( INPUT_F, fstream::in);
	fout.open ( OUTPUT_F, fstream::out);
	int T;
	fin >> T;
	char buf [61];
	int ress[61];
	fin.getline ( buf, 1);
	List root;
	for ( int i = 0; i < T; i++)
	{
		fin.getline ( buf, 61);
		int o = 1;
		int dym = 1;
		root.sym = buf[0];
		root.n = 1;
		root.next = NULL;
		ress[0] = 1;
		while ( buf[o] != '\0')
		{
			List *cur = &root;
			for ( int t = 0; t < dym; t++)
			{
				if ( cur->sym == buf[o])
				{
					ress[o] = cur->n;
					goto found;
				}
				if ( cur->next != NULL) cur = cur->next;
			}
			dym ++;
			List *newList = new List;
			cur->next = newList;
			if (dym == 2) 
				newList->n = 0;
			else
				newList->n = dym - 1;
			newList->sym = buf[o];
			newList->next = NULL;
			ress[o] = newList->n;
found:			
			o++;
		}
		unsigned long long res = getres ( dym, o - 1, ress);
		fout << "Case #" << i+1 << ": " << res << endl;
		List *nxt = root.next;
		List *nxt2;
		for (int j = 1; j < dym; j++)
		{
			nxt2 = nxt->next;
			delete nxt;
			nxt = nxt2;
		}
	}

	fin.close ( );
	fout.close ( );
}