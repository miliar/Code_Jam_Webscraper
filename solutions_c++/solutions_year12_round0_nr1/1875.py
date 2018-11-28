#include <iostream>
#include <string>

using namespace std;


string translate(string word){
    string result;
    char achar;
    for (int i=0;i<word.size();i++){

        achar = word.at(i);


        if (achar == ' ') achar = ' ';
        else if (achar=='a') achar = 'y';//
        else if (achar=='b') achar = 'h';//
        else if (achar=='c') achar = 'e';//
        else if (achar=='d') achar = 's';//
        else if (achar=='e') achar = 'o';//
        else if (achar=='f') achar = 'c';//
        else if (achar=='g') achar = 'v';//
        else if (achar=='h') achar = 'x';//
        else if (achar=='i') achar = 'd';//
        else if (achar=='j') achar = 'u';//
        else if (achar=='k') achar = 'i';//
        else if (achar=='l') achar = 'g';//
        else if (achar=='m') achar = 'l';//
        else if (achar=='n') achar = 'b';//
        else if (achar=='o') achar = 'k';//
        else if (achar=='p') achar = 'r';//


        else if (achar=='q') achar = 'z';//

        else if (achar=='r') achar = 't';//
        else if (achar=='s') achar = 'n';//
        else if (achar=='t') achar = 'w';//
        else if (achar=='u') achar = 'j';//
        else if (achar=='v') achar = 'p';//
        else if (achar=='w') achar = 'f';//
        else if (achar=='x') achar = 'm';
        else if (achar=='y') achar = 'a';
        else if (achar=='z') achar = 'q';

        result.push_back(achar);
    }
    return result;
}

int main(){

    int num;
    cin >> num;

    string w;
	getline(cin,w,'\n');
    for (int j = 1;j<=num;j++){

	getline(cin, w,'\n');
        cout << "Case #" << j<<": "<< translate(w)<<endl;
    }

    return 0;

}


