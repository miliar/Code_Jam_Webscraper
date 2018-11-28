using namespace std;

#include <iostream>
#include <queue>

struct Button {
	unsigned char who;
	unsigned int  but;
};

//#define TEST
//#define SMALL
#define LARGE
int main(void) {
#ifdef TEST
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif

#ifdef SMALL
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
#endif

#ifdef LARGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif

	int T;
	int R, C;

	unsigned char *tab;
	unsigned char tmp;

	cin >> T;
	bool poss;

	for(int i=0; i<T; i++){
		cin >> R;
		cin >> C;
		poss = true;

		tab = (unsigned char *) malloc(sizeof(unsigned char) * R * C);

		for(int j=0; j<R; j++)
		{
			for(int k=0; k<C; k++)
			{
				cin >> tab[j*C+k];
			}
		}


		for(int j=0; j<R && (poss==true); j++)
		{
			for(int k=0; k<C && (poss==true); k++)
			{
				if(tab[j*C+k] == '#')
				{
					tab[j*C+k]='/';
					if(((j+1)<R) && tab[(j+1)*C+k]=='#')
					{
						tab[(j+1)*C+k]='\\';
					}
					else
					{
						poss = false;
						continue;
					}

					if(((k+1)<C) && tab[j*C+k+1]=='#')
					{
						tab[j*C+k+1]='\\';
					}
					else
					{
						poss = false;
						continue;
					}
					if(tab[(j+1)*C+k+1]=='#')
					{
						tab[(j+1)*C+k+1]='/';
					}
					else
					{
						poss = false;
						continue;
					}
				}
			}
		}
		
		cout << "Case #" << (i+1) << ":" << endl;

		if(poss)
		{
			for(int j=0; j<R; j++)
			{
				for(int k=0; k<C; k++)
				{
					cout << tab[j*C+k];
				}
				cout << endl;
			}
		}
		else
		{
			cout << "Impossible" << endl;
		}

		free(tab);
		
	}
	return 0;
}
