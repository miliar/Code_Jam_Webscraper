#include <iostream>
#include <string>
#include <list>

using namespace std;

int ilezer(int wynik) {
	int ilezer=0; int i=1000; 
	while( (ilezer < 4) && (wynik / i==0)) {i/=10; ilezer++;}
	if(wynik==0) return ilezer-1;
	return ilezer; 
}

int rekurencyjka(string & str, string & pattern, int str_p, int pat_p ) {	
	if(pat_p >= pattern.size()) return 1; 	
	int possibilities=0; //cout << str.size() << ", "<< pattern.size() << ", " << pat_p << endl;
	int limit=str.size()-(pattern.size()-pat_p)+1; //cout<< limit << endl << endl;
	for(int i=str_p; i< limit; i++) 
	   if(str.at(i)==pattern.at(pat_p)) possibilities+=rekurencyjka(str,pattern,i+1,pat_p+1)%10000; 

	return possibilities % 10000;
}

main()
{   int cases_no; cin >> cases_no; string str; getline(cin,str); 
string pattern="welcome to code jam";
for(int cases=0; cases<cases_no; cases++) {
    getline(cin,str); //cout << str << endl; 
    int wynik=rekurencyjka(str,pattern,0,0);
    cout << "Case #" << cases+1 << ": "; 
    for(int i=0; i<ilezer(wynik); i++) cout << "0"; 
    cout << wynik << endl;
}


}
