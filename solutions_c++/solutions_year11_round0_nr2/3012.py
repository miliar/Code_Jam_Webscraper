#include <iostream>
#define MAX 100
#define DESTROYED '*'

using namespace std;

typedef struct tag_fusion
{
	char element1, element2, result;
	int match(char e1, char e2)
	{
		return ((e1 == element1 && e2 == element2)||(e1 == element2 && e2 == element1));
	}
} fusion;

typedef struct tag_oposite
{
	char element1, element2;
	int match(char e1, char e2)
	{
		return ((e1 == element1 && e2 == element2)||(e1 == element2 && e2 == element1));
	}
} oposite;

int main()
{
	int ncases, ccase = 0;
	cin >> ncases;
	while (ccase++ < ncases)
	{
		int nfusions; cin >> nfusions;
		fusion fusions[MAX];
		for (int i=0; i<nfusions; i++)
			cin >> fusions[i].element1 >> fusions[i].element2 >> fusions[i].result;
		
		int noposites; cin >> noposites;
		oposite oposites[MAX];
		for (int i=0; i<noposites; i++)
			cin >> oposites[i].element1 >> oposites[i].element2;
			
		int nelements; cin >> nelements;
		char elements[MAX];
		int currElementI = -1;
		for (int i=0; i<nelements; i++)
		{
			char element;
			cin >> element;
			//cout << "pegou " << element << " " << i << "/" << nelements << endl;
			if (currElementI >= 0)
			{
				int fused = 0;
				for (int j=0; j<nfusions; j++)
				{
					fused = fusions[j].match(element, elements[currElementI]);
					if (fused)
					{
						//cout << "fundiu " << elements[currElementI] << " a " << element << ", originando " << fusions[j].result << endl;
						elements[currElementI] = fusions[j].result;
						break;
					}
				}
				if (fused) continue;
				
				int oposed = 0;
				for (int j=0; j<=currElementI; j++)
				{
					for (int k=0; k<noposites; k++)
					{
						oposed = oposites[k].match(elements[j], element);
						if (oposed)
						{
							//cout << "destruir " << elements[j] << " e " << element << ", e lista toda" << endl;
							elements[j] = DESTROYED;
							currElementI = -1;
							break;
						}
					}
					if (oposed) break;
				}
				if (oposed) continue;
				//cout << "adicionou " << element << " apos " << elements[currElementI] << endl;
				elements[++currElementI] = element;
			}
			else
			{
				//cout << "adicionou " << element <<endl;
				elements[++currElementI] = element;
			}
		}
		
		cout << "Case #" << ccase << ": [";
		for (int i=0; i<=currElementI; i++)
		{
			if (elements[i] == DESTROYED)
				continue;
			cout << elements[i];
			if (i < currElementI)
				cout << ", ";
		}
		cout << "]" << endl;
	}
}
