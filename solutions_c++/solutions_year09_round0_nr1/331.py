#include <iostream>
#include <string>
#include <map>

using namespace std;

map<string, bool> mapa;
int possib(string &pal, int pos, string sf = "")
{
	int soma = 0, prox;
	if(!mapa[sf]) return 0;
	if(pos == pal.size())
		return mapa[sf];
	if(pal[pos] != '(')
		return possib(pal, pos+1, sf+pal[pos]);
	for(prox = pos+1; pal[prox] != ')'; prox++);
	for(int i = pos+1; pal[i] != ')'; i++)
		soma += possib(pal, prox+1, sf+pal[i]);
	return soma;
}

int main()
{
	int L, D, N;
	cin >> L >> D >> N;
	for(int i = 0; i < D; i++)
	{
		string pal;
		cin >> pal;
		for(int j = 0; j <= pal.size(); j++)
			mapa[pal.substr(0, j)] = true;
	}
	for(int i = 0; i < N; i++)
	{
		string pal;
		cin >> pal;
		cout << "Case #" << i+1 << ": " << possib(pal, 0) << endl;
	}
	return 0;
}
