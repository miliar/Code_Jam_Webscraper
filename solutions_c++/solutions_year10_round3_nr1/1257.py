#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
typedef struct C{ int a,b;} fir;


bool compare( fir a, fir b)
{
return a.a < b.a;
}

int main()
{
FILE * in = fopen("A-large.in", "rt");
FILE * out = fopen("A.out", "wt");

int t,n,j,k, contor,a,b;
vector <fir> v;
fir x;


fscanf(in, "%i", &t);

for (int i = 0; i < t;i++)
{
	v.clear();
		
	fprintf(out, "Case #%i: ", i+1);
	contor = 0;
	fscanf(in, "%i", &n);

	// Bag coordonatele intr-un vector crescator
	for (j = 0; j < n; j++)
	{
		fscanf(in,"%i %i", &a, &b);
		x.a = a;
		x.b = b;
		v.push_back(x);
	}
	
	// sortez dupa a
	make_heap(v.begin(), v.end(), compare);
	sort_heap(v.begin(), v.end(), compare);
	//for (j = 0; j < n; j++) printf ("%i %i\n", v[j].a, v[j].b);
	
	// pentru toate ferestrele de dupa j daca ajung mai jos de j.b => intersectie
	for (j = 0; j < n-1; j++)
	{
		k = j+1;
		while(k < n)
		{
			if (v[j].b > v[k].b) contor++;
			k++;
		}
	}
	
	fprintf(out, "%i\n", contor);
}




fclose(in);
fclose(out);
return 0;
}
