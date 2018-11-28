//saving universe
#include<fstream>
#include<iostream>
#include<string>
#include<vector>
#include<map>
using namespace std;

map<string,int> m;//mapa do spr czy wykluczylismy juz dana wyszukiwarke
map<string,bool> jest;//mapa do spr czy to wyszukiwarka

int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");

	int tests,n,q,i,j;
	string pom;
	vector<string>name;
	in>>tests;
	for(int c = 0; c < tests; c++)
	{		
		in>>n;//ile wyszukiwarek
		getline(in,pom);//wczytaj koniec wiersza
		i = 0; j = n;//ile potrzeba przelaczen, ile jest aktualnie dostepnych wyszukiwarek
		for(int c = 0; c < n; c++)//wczytaj wyszukiwarki		
		{
			getline(in,pom);
			jest[pom] = 1;
			name.push_back(pom);
		}
		in>>q;//ile pytan 
		getline(in,pom);//wczytaj koniec wiersza
		for(int c = 0; c < q; c++)
		{
			getline(in,pom);		
			if(jest[pom] && m[pom] != i+1)//spr czy to wyszukiwarka i czy jest juz odrzucona
			{
				if(j == 1)//jesli zostala tylko ta wyszukiwarka
				{
					i++;//musisz przelaczyc
					j=n;//po przelaczeniu wszystkie wyszukiwarki dostepne
				}
				m[pom]= i+1;//odznacz, ze w tym przelaczeniu juz nie mozesz z niej skorzystac
				j--;//zmniejsz ilosc dostepnych				
			}
		}		
		for(int c = 0; c < n; c++)//wyczysc mapy
		{
			m[name[c]] = 0;
			jest[name[c]] = 0;
		}
		name.clear();//wyczysc vector
		out <<"Case #"<<c+1<<": "<< i << '\n';
	}
	in.close();
	out.close();
	return 0;
}