#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;

struct st
{
	char code;
	int Num;
};

int cari(vector<st> A, char c)
{
	for (int i=0; i<(A.size()); i++)
		if (A[i].code==c)
			return i;
	return -1;
}

int main()
{
	int T;
	cin >> T;
	ofstream fout("a.out");
	
	for (int test=1; test<=T; test++)
	{
		string s;
		cin >> s;
		int Pjg = s.length();
		vector<int> Bil;
		vector<st> Alien;
		int i;
		
		for (i=0; i<10; i++)
			if (i!=1) Bil.push_back(i);
			
		int Ans[Pjg];
		
		Ans[0] = 1;
		st Temp;
		Temp.code = s[0];
		Temp.Num = 1;
		Alien.push_back(Temp);
		for (i=1; i<Pjg; i++)
		{
			int x = cari(Alien, s[i]);
			if (x>=0)
				Ans[i] = Alien[x].Num;
			else
			{
				Temp.code = s[i];
				Temp.Num = Bil[0];
				Ans[i] = Bil[0];
				Alien.push_back(Temp);
				Bil.erase(Bil.begin());
			}
		}
		long long Jawab = 0LL;
		int Base = (Bil.empty()) ? 10 : Bil[0];
		if (Base==0) Base=2;
		long long Kali = 1;
		
		for (i=Pjg-1; i>=0; i--)
		{
			Jawab += (Ans[i]*Kali);
			Kali*=Base;
		}
		fout << "Case #" << test << ": " << Jawab << "\n";
	}
	
	return 0;
}
