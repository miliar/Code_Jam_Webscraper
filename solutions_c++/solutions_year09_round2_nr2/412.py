#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
int cnt [10];
int cnt2 [10];
int n;
void solve()
{
	scanf ("%d", &n);
	int p = n;
	int i;
	while (n){ cnt[n%10] ++; n/=10;} 
	
	for (p = p+1; ; ++p)
	{
		n = p;
		memset (cnt2, 0, sizeof (cnt2));
		while (n){ cnt2[n%10] ++; n/=10;} 
	
		for (i = 1; i < 10; i++) if (cnt[i]!= cnt2[i]) break; 
		
		if ( i == 10) {printf ("%d\n", n);break;}
	}
	
}
string eee;
int main ()
{
	
	int o, i;
	scanf ("%d", &o);
	for (i = 1 ; i <= o; i++)
	{
		printf ("Case #%d: ", i);
		cin >> eee;
		string st = eee;
	
		next_permutation (eee.begin (), eee.end ());
		//if (eee[0] == '0') eee = st.substr (0, 1) + "0" + st.substr (1);
		//else
		if (eee == st) eee = st.substr (0, 1) + "0" + st.substr (1);
		else
		if (eee < st)
		{
			sort (st.begin (), st.end ());
			int j; for (j = 0; j < st.size (); j++) if (st[j] != '0') {swap(st[j], st[0]);break;}
			eee = st.substr (0, 1) + "0" + st.substr (1);
		}
		cout << eee << endl;	
		//solve ();
	}
	
	
	return 0;
}