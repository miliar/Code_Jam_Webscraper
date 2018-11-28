#include <fstream.h>
#include <string.h>
#define LMAX 101
#define SMAX 101
ifstream  fi("A-large.in");
ofstream fo("output");

char sName[SMAX][LMAX];
int uz[SMAX];
int n, s, q;

void initUz ()
{
	for (int i=0;i<s;++i) uz[i] = 0;
}

void readSearch ()
{
	int i, j, pos;
	char aux[LMAX];
	fi>>s;
	fi.getline(aux, LMAX, '\n');
	for (i = 0; i < s; ++i)	fi.getline(sName[i], LMAX, '\n');
	//sort the name of search engines
	for (i = 0; i < s; ++i)
	{
		pos = i;
		for (j = i+1; j < s; ++j)
			if (strcmp(sName[pos], sName[j]) > 0) pos = j;
		strcpy(aux, sName[pos]);
		strcpy(sName[pos], sName[i]);
		strcpy(sName[i], aux);
	}
}

int findSearch (char name[LMAX])
{
	int a;
	int f = 0/*first*/, l = s-1/*last*/, m /*middle*/;
	while (f<=l)
	{
		m = (f+l)/2;
		a = strcmp(sName[m], name);
		if (a == 0) return m;
		if (a < 0) f = m + 1;
		else l = m - 1;
	}
	return -1;
}

int main()
{
	int i;
	int pos, res, dif;
	char name[LMAX];
	fi>>n;
	for (i=1;i<=n;++i)
	{
		fo<<"Case #"<<i<<": ";
		readSearch();
		fi>>q;
		fi.getline(name, LMAX, '\n');
		res = dif = 0;
		initUz();
		while (q)
		{
			fi.getline(name, LMAX, '\n');
			pos = findSearch(name);//binary search
			if (!uz[pos])
			{
				if (dif + 1 == s)
				{
					dif = 0;
					res++;
					initUz();
				}
				uz[pos] = 1;
				dif++;
			}
			q--;
		}
		fo<<res<<"\n";
	}
	fi.close();
	fo.close();
	return 0;
}
