#include <iostream>
#include <algorithm>
#include <iomanip>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <set>

using namespace std;

inline int isNumber(const char c) { return (c >= '0' && c <= '9'); }
inline int isAlpha(const char c) { return (c >= 'a' && c <= 'z'); }

struct Albero
{
	Albero() { memset(id, 0, sizeof(id)); }
	Albero(const string& s, double _val) : feature(s), val(_val) { memset(id, 0, sizeof(id)); }
	string feature;
	double val;
	Albero* id[2];
};

void Esplora(Albero* a)
{
	if (a)
	{
		cerr << "(" << a->val << " " << a->feature << " ";
		Esplora(a->id[0]);
		cerr << " ";
		Esplora(a->id[1]);
	   cerr << ")";
	}
}

double getSol(Albero* a, const set<string>& q)
{
	double s = 1;
	while (a)
	{
		#ifdef DEBUG
			cerr << "Feature <" << a->feature << "> ? " << q.count(a->feature) << "\n";
		#endif
		s *= a->val;
		a = a->id[1-q.count(a->feature)];
	}
	return s;
}

void libera(Albero* a)
{
	if (a)
	{
		libera(a->id[0]);
		libera(a->id[1]);
		delete a;
	}
}

void albera(Albero* a, istream& in)
{
	string s;
	char c = 0; 
	int idN = 0;
	while (c != '(') c=in.get();
	while (c != ')')
	{
		c = in.get();
		if (isNumber(c))
		{
			in.putback(c);
			in >> a->val;
		}
		else if (c == '(')
		{
			in.putback(c);			
			albera(a->id[idN++] = new Albero(), in);
		}		
		else if (c == ')') return;
		else if (isAlpha(c))
		{
			in.putback(c);
			in >> a->feature;
		}
	}
}

void run(istream& in, ostream& out)
{
	string buffer;
	int casi;
	char c;
	in >> casi; //getline(in, buffer);

	for (int caso = 1; caso <= casi; caso++)
	{
		Albero* radix = new Albero();
		int l; in >> l; //getline(in, buffer);
		albera(radix, in);

		#ifdef DEBUG
			cerr << "\n\nTest case " << caso << "\n";
			Esplora(radix); 
		#endif
		while (!isNumber(c = in.get())); in.putback(c);
		
		int A, F; in >> A; 
		set<string> q[A];
		for (int a = 0; a < A; a++)
		{
			in >> buffer >> F;
			for (int f = 0; f < F; f++)
			{
				in >> buffer;
				q[a].insert(buffer);
				#ifdef DEBUG
					cerr << "Animal " << a << " feature " << buffer << "\n";
				#endif
			}
		}	

		out << "Case #" << caso << ":\n";
		for (int a = 0; a < A; a++)
			out << fixed << setprecision(7) << getSol(radix, q[a]) << "\n";
		libera(radix);
	}
}

int main()
{
	run(cin, cout);
	return 0;
}

