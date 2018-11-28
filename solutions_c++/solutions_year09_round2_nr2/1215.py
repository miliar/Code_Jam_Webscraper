#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
using namespace std;

char v[100];
char aux[100];
int n;

void solve()
{
	ifstream f("test.in");
	ofstream g("test.out");

	f>>n;

	for (int i=1; i<=n; ++i)
	{
		f>>v;
		
		//memcpy(aux, v, sizeof(aux));

		int nr_v=strlen(v);

		if ( next_permutation(v, v+nr_v ) == 0 )
		{
			sort(v, v+nr_v );
			int temp=0;

			while (v[temp]=='0')
				++temp;

			swap(v[0], v[temp]);

			//cout<<i<<"        "<<v[0]<<" "<<v[temp]<<"\n";
			for (int k=nr_v; k!=0 ; --k)
				v[k+1]=v[k];

			v[1]='0';
		}
		g<<"Case #"<<i<<": "<<v<<"\n";
	}
	f.close();
	g.close();
}

int main()
{
	solve();
	return 0;
}