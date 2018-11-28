#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;
ifstream fcin("a.txt");
ofstream fcout("t.txt");
string standard("welcome to code jam");
string tp;
int Cnt;
void dfs(int C, int pos)
{
	if(C == 19)
	{
		Cnt++;
		return;
	}
	if(C>tp.length())	return;
	for(int i=pos; i<tp.length(); i++)
		if(tp[i] == standard[C])
			dfs(C+1, i+1);
}
int main()
{
	int T, iCas(1);
	fcin >> T;
	fcin.get();
	while(T--)
	{
		Cnt = 0;
		getline(fcin, tp);
		for(int i=0; i<tp.length(); i++)
			if(tp[i] == 'w')
				dfs(1, i+1);
		fcout << "Case #" << iCas++ << ": ";
		fcout << setfill('0') << setw(4) << Cnt << endl;
	}
	return 0;
}
