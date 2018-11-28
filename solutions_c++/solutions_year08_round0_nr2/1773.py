#include <iostream>
#include <fstream>

using namespace std;

const int maxn = 101;

class trip {
public:
	int a,d;
};

trip a[maxn], b[maxn];
bool checka[maxn], checkb[maxn];
char s[100];
ofstream fout;
ifstream fin;

#define cin fin

void mysort(trip * a, int l)
{
	int i,j;
	trip tmp;
	for (i = 0;i < l;i ++)
		for (j = i + 1;j < l;j ++)
			if (a[i].d > a[j].d || (a[i].d == a[j].d && a[i].a > a[j].a)) {
				tmp = a[i];
				a[i] = a[j];
				a[j] = tmp;
			}
}

void cango(trip * a, int d, bool * check, int i, int l)
{
	
	while (i < l)
	{
		if (check[i] == 0 && d <= a[i].d) {
			//cout << d << " " << a[i].d << endl;
			check[i] = 1;
			return;
		}
		i ++;
	}
}

int main()
{
	int n, na, nb, t, i, j, ansa, ansb, num = 0;
	
	fout.open("b.out");
	fin.open("b.in");
	cin >> n;
	while (n -- > 0)
	{
		cin >> t;
		cin >> na >> nb;
		for (i = 0;i < na;i ++) {
			while (cin >> s, strlen(s) != 5);
			a[i].d = ((s[0] - '0') * 10 + (s[1] - '0')) * 60 + (s[3] - '0') * 10 + (s[4] - '0');
			while (cin >> s, strlen(s) != 5);
			a[i].a = ((s[0] - '0') * 10 + (s[1] - '0')) * 60 + (s[3] - '0') * 10 + (s[4] - '0');
		}

		for (i = 0;i < nb;i ++) {
			while (cin >> s, strlen(s) != 5);
			b[i].d = ((s[0] - '0') * 10 + (s[1] - '0')) * 60 + (s[3] - '0') * 10 + (s[4] - '0');
			while (cin >> s, strlen(s) != 5);
			b[i].a = ((s[0] - '0') * 10 + (s[1] - '0')) * 60 + (s[3] - '0') * 10 + (s[4] - '0');
		}
		
		mysort(a, na);
		mysort(b, nb);

		i = j = 0;
		ansa = ansb = 0;
		memset(checka, 0, sizeof(checka));
		memset(checkb, 0, sizeof(checkb));
		while (i < na || j < nb)
		{
			if (i < na && (j == nb || a[i].d < b[j].d)) {
				if (checka[i] == 0) ansa ++;
				cango(b, a[i].a + t, checkb, j, nb);
				i ++;
			}
			else {
				if (checkb[j] == 0) ansb ++;
				cango(a, b[j].a + t, checka, i, na);
				j ++;
			}
		}
		num ++;
		fout << "Case #" << num << ": " << ansa << " " << ansb << endl; 
	}
	
	fout.close();
	return 0;
}