#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
using namespace std;

int main(){
    int cases;
    ifstream fin("1l.in");
    ofstream fout("1l.txt");
    fin >> cases;
    string temp;
    for (int i = 0; i < cases; i++){
        map <string, int> se;
        int s;
        fin >> s;
    	getline (fin, temp, '\n');
	for (int j = 0; j < s; j++){
            string curr;
            getline (fin, curr, '\n');
            se[curr] = j;
        };
        int q;
        fin >> q;
        int sc = 0;
        int csc = 0;
        string cse,dse;
        vector <int> v(s);
        for (int m = 0; m < s; m++){
            v[m] = 0;
        };
	if (q != 0){
	   getline (fin, temp, '\n');
	   getline (fin, cse, '\n');
	};
        v[se[cse]] = 1;
        for (int k = 0; k < q-1 ; k++){
            getline (fin, dse, '\n');
            if (v[se[dse]] == 0){
                           v[se[dse]] = 1;
                           csc++;
                           if (csc == s-1){
				   //cout << k << dse << endl;
                                   csc = 0;
                                   for (int m = 0; m < s; m++){
                                       v[m] = 0;
                                   };
                                   sc++;
                                   cse = dse;
                                   v[se[dse]] = 1;
                           };
            };
        };
        fout << "Case #" << i+1 <<": "<<sc <<endl;
    };
    fout << endl;
    return 0;
}
