//Marcin Baran

#include<iostream>
#include<sstream>
#include<vector>
#include<cmath>
#include<list>
#include<algorithm>

using namespace std;
typedef long long int lli;
lli z,ile_razy,ile_miejsca,ile_ludzi;
lli a,b;

struct ladunek{
	lli wagon;
	lli nastepny;
	ladunek():wagon(0),nastepny(0) {}
	ladunek(lli a,lli b):wagon(a),nastepny(b) {}
	void wypisz(){
		cout<<"wagon: "<<wagon<<endl<<"nastepny: "<<nastepny<<endl<<endl;
	}
};

int main(){
	cin>>z;
	for(lli ii=1;ii<=z;++ii){
		vector<lli> kolejka;
		cin>>ile_razy>>ile_miejsca>>ile_ludzi;
		for(lli i=0;i<ile_ludzi;++i){
			cin>>a;
			kolejka.push_back(a);
		}
		vector<ladunek> lad(kolejka.size());
		lli suma = 0,pozycja = 0,start = 0;
		while(suma + kolejka[pozycja] <= ile_miejsca){
			suma += kolejka[pozycja];
			++pozycja;
			if(pozycja == ile_ludzi) break;
		}
		if(pozycja == ile_ludzi){
			cout<<"Case #"<<ii<<": "<<suma*ile_razy<<endl;
			continue;
		}
		while(start != kolejka.size()){
			lad[start] = ladunek(suma,pozycja);
			suma -= kolejka[start];
			while(suma + kolejka[pozycja] <= ile_miejsca){
				suma += kolejka[pozycja];
				++pozycja;
				pozycja %= ile_ludzi;
			}
			++start;
		}
//		for(lli i = 0 ;i<kolejka.size();++i){cout<<i<<": "<<kolejka[i]<<endl;lad[i].wypisz();}
		suma = 0,pozycja = 0;
		for(lli i=0;i<ile_razy;++i){
			suma += lad[pozycja].wagon;
			pozycja = lad[pozycja].nastepny;
		}
		cout<<"Case #"<<ii<<": "<<suma<<endl;
	}
	return 0;
}
