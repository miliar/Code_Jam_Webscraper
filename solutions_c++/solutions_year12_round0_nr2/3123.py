#include <fstream>
#include <iostream>

using namespace std;

int main()	{
	ifstream fin("B-large.in");
	ofstream fout("b-large.txt", ios::ate);
	int t, count;
	fin >> t;
	//cin >> t;
	for (count=1; count <= t; count++)	{
		int n, s, p, i, c[100], ans=0;
		fin >> n >> s >> p;
		//cin >> n >> s >> p;
		for (i=0; i<n; i++)	{
			fin >> c[i];
			//cin >> c[i];
		}
		for (i=0; i<n; i++)	{
			if (c[i]>=(p*3-2))	{
				ans++;
			}
			else if ((c[i]>=(p*3-4))&&(p*3-4>0)&&(s>0))	{
				s--;
				ans++;
			}
		}
		fout<<"Case #"<<count<<": "<<ans<<"\n";
	}
	return 0;
}