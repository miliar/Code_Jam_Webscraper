#include<iostream>
#include<fstream>
using namespace std;

int main(){
    fstream fin, fout;
    fin.open( "A-small-attempt0.in", ios::in);
    fout.open( "a.out", ios::out);
    int T;
    string input;
    char table[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    fin >> T;
    fin.ignore();
    for( int i = 0; i < T; i++){
        getline( fin, input);
        fout << "Case #" << i + 1 <<": ";
        for( int j = 0; j < input.length(); j++){
            if( input[j] >= 97 && input[j] <= 122){
                fout << table[input[j]-'a'];
            }
            else{
                fout << input[j];
            }
        }
        fout << endl;
    } 
    system("pause");
    return 0;
}
