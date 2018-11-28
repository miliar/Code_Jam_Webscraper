# include <iostream>
# include <string>
using namespace std;
int main(){
int N, liczba;
string cos;
cin>> N;
char n;
getline (cin, cos);
for (int i=0; i<N; i++){
cout<<"Case #"<<i+1<<": ";
        getline (cin, cos);
        char tab [27] = "yhesocvxduiglbkrztnwjpfmaq";        
	for (int j = 0; j<cos.size(); j++){
                n = cos[j];
                if ((int)n >= 97 && (int)n<=122){
		liczba = ((int) n)- 97;
		n = tab[liczba];
		cout << n;
		}
		else
		cout << n;
	}
cout <<"\n";
}
return 0;
}
