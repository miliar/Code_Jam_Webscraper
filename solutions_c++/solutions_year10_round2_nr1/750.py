#include <cstdio>
#include <map>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

struct nod
{
	map <string, nod *> n;
};

nod *T;
int n, m;
char a[100001];
int len;

vector <string> x;

void init ()
{
	T = new nod;
}

int insert (nod *T)
{
	int n =x.size ();

	int i;
	int nr = 0;
	for (i = 0; i < n; ++i)
	{
		if (T->n[x[i]] == 0)
		{
			++nr;
			T->n[x[i]] = new nod;
		}
	
		T = T->n[x[i]];
	}

	return nr;

}

int main ()
{
	init ();

	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);
	int nT;
	scanf ("%d\n", &nT);


	
	for (int caz = 1; caz <= nT; ++caz)
	{
		init ();
		scanf ("%d %d\n", &n, &m);

		//printf ("%d %d\n", n, m);
		int i, j;
		for (i = 1; i <= n; ++i)
		{
			scanf ("%s\n", &a);
			len = strlen (a);

//			printf ("%s\n", a);
			int p = 0;		
			x.clear ();
			string aux = "";
			for (p = 1; p < len; ++p)
			{
				if (a[p] == '/')
				{
					x.push_back (aux);
					
					aux = "";
				}
				else
					aux += a[p];

//				printf ("%c", a[p]);

			}
			//printf ("\n");
			if (aux.size ())
				x.push_back (aux);

		//	for (j = 0; j < x.size (); ++j)
		//		printf ("%s ", x[j].c_str());
		//	printf ("\n");
		
			insert (T);
			//printf ("(%d)\n", insert (T));	
			for (j = 0; j < len; ++j)
				a[j] = 0;
		}


		int sum = 0;
		for (i = 1; i <= m; ++i)
		{
			scanf ("%s\n", &a);
			len = strlen (a);

			int p = 0;
			x.clear ();
			string aux = "";

			for (p = 1; p < len; ++p)
				if (a[p] == '/')
				{
					x.push_back (aux);
					aux = "";
				}
				else
					aux += a[p];

			if (aux.size ())
				x.push_back (aux);

		//	for (j = 0; j < x.size (); ++j)
		//		printf ("%s ", x[j].c_str ());

		//	printf ("\n");

			sum += insert (T);
			for (j = 0; j < len; ++j)
				a[j] = 0;

		}

		printf ("Case #%d: %d\n", caz,sum);



	}


	return 0;
}
