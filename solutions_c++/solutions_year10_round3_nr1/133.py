#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <gmpxx.h>	/* GNU MP, http://gmplib.org/, link with -lgmp -lgmpxx */



using namespace std;

typedef struct {
	int a;
	int b;
} wire;

bool mysort(wire w1, wire w2)
{
	return (w1.a < w2.a);
}



int main (int argc, char *argv[])
{
	int T, t;
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		int N;
		cin >> N;
		vector<wire> wires;
		for (int n = 0; n < N; n++)
		{
			wire w;
			cin >> w.a >> w.b;
			wires.push_back(w);
		}
		sort(wires.begin(), wires.end(), mysort);
		/*for (int n = 0; n < N; n++)
		{
			cout << "Wire " << n << endl;
			cout << wires[n].a << " " << wires[n].b << endl;
		}*/
		long long ints = 0;
		for (int n = 0; n < N; n++)
		{
			for (int j = n+1; j < N; j++)
			{
				if (wires[j].b < wires[n].b)
					ints++;
			}
		}
		cout << "Case #" << t << ": " << ints << endl;
		
	}
	
	return 0;
}


