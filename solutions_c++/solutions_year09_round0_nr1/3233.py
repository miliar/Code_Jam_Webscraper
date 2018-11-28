#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
int l, d, n;
string dic[30], tp;
ifstream fin("a.txt");
ofstream fout("t.txt");
int main()
{
	fin >> l >> d >> n;
	for(int i=0; i<d; i++)
		fin >> dic[i];
	string ex, fl;
	vector<string> gb;
	int iCas(1);
	while(fin >> tp)
	{
		gb.clear();
		for(int i=0, j=0; i<tp.length(); i++)
		{
			if(tp[i] == '('){
				ex.clear();
				for(i++; ; i++){
					if(tp[i] == ')')	break;
					ex += tp[i];
				}
			}
			else	ex = tp[i];
			gb.push_back(ex);
		}
		int Cnt(0);
		for(int c=0; c<d; c++)
		{
			fl = dic[c];
			int S(0);
			for(int i=0; i<fl.length(); i++)
				for(int j=0; j<gb[i].length(); j++)
					if(gb[i][j] == fl[i]){
						S++;
						break;
					}
			if(S == fl.length())	Cnt++;
		}
		fout << "Case #" << iCas++ << ": " << Cnt << endl;
		//printf("Case #%d: %d\n", iCas++, Cnt);
	}
	return 0;
}
