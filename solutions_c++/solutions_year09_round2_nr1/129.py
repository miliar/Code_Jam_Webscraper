#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <sstream>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;
typedef set<string> SS;

SS car;

double prob (string arb)
{
	string lec;
	stringstream ss(arb);
	ss >> lec; //must be a (
	double p;
	ss >> p;
	ss >> lec;
	if (lec==")")
		return p;
	int nab=0;
	int ct=0;
	while (nab<2)
	{
		if (arb[ct++]=='(')
			nab++;
	}
	int ct2=arb.size()-1;
	while (arb[ct2--]!=')');
	arb=arb.substr(ct-1,ct2-ct+1);
	int pm=0;
	ct=0;
	do
	{
		if (arb[pm]=='(')
			ct++;
		if (arb[pm]==')')
			ct--;
		pm++;
	}while (ct!=0);
	double p1=prob(arb.substr(0,pm));
	double p2=prob(arb.substr(pm));
	if (car.find(lec)==car.end())
		return p*p2;
	return p*p1;
}

int main()
{
	cout.setf(ios::fixed);
	cout.precision(10);
	int N;
	cin >> N;
	for (int caso=1;caso<=N;caso++)
	{
		cout << "Case #" << caso << ":" << endl;
		int L;
		cin >> L;
		cin.ignore();
		string arb="";
		fi (L)
		{
			string aux;
			getline (cin,aux);
			if (i<L-1)
				aux+=' ';
			string aux2;
			fj (aux.size())
			{
				if (aux[j]=='(' or aux[j]==')')
					aux2+=' ';
				aux2+=aux[j];
				if (aux[j]=='(' or aux[j]==')')
					aux2+=' ';
			}
			arb+=aux2;
		}
		int A;
		cin >> A;
		fi (A)
		{
			car.clear();
			string s;
			cin >> s;
			int nc;
			cin >> nc;
			fi(nc)
			{
				cin >> s;
				car.insert(s);
			}
			cout << prob(arb) << endl;
		}
	}
}
