#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;

#define maxN 110

char lit[] = "yhesocvxduiglbkrztnwjpfmaq";
char S[maxN];


int main()
{
	ifstream f ("date.in");
	ofstream g ("date.out");
	
	int T;
	f >> T;
	f.get();
	
	for (int t = 1; t <= T; ++ t)
	{
		g << "Case #" << t << ": ";
		
		f.getline (S, maxN);
		int leng = strlen (S);
		
		for (int i = 0; i < leng; ++ i)
			if (S[i] == ' ') g << " ";
			else g << lit[S[i] - 'a'];
		
		g << '\n';
	}
	
	return 0;
}
