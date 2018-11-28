#include <iostream>
#include <string>
#include <vector>


using namespace std;

int main() {

    string in;

    int L, D, N;
    cin >> L >> D >> N;

    //cout << "L" << L << "  D" << D << "  N" << N << endl;

    vector<string> words;
    for (int i = 0; i < D; i++) {
        cin >> in;
        words.push_back(in);
    }

    vector <vector<string> > tab;
    for (int i = 0; i < N; i++)
    {
        cin >> in;
        //parsons
        bool parenthese = false;
        vector<string> test;
        for (unsigned j = 0; j < in.size(); j++) {
            if (in[j] == '(')
            {
                j++;
                string ensemble;
                while (in[j] != ')') {
                    ensemble += in[j];
                    //tab[i][letter] += in[j];
                    j++;
                }

                test.push_back(ensemble);
            }
            else
            {
                string ensemble;
                ensemble += (in[j]);
                test.push_back(ensemble);
            }


        }
        tab.push_back(test);
    }

//    cout << "\nAffichage\n";
//    for (int numtest = 0; numtest < N; numtest++) {
//        cout << "test" << numtest << endl;
//        for (int j = 0; j < L; j++)
//            cout << tab.at(numtest).at(j) << endl;
//    }

//    cout << "\nCalcul\n";
    for (int numtest = 0; numtest < N; numtest++)
    {
        int resultat = 0;
        for (int mot = 0; mot < D; mot++) 
        {
            bool match = true;
            for (int lettre = 0; lettre < L; lettre++) {
                size_t pos;

                pos = tab.at(numtest).at(lettre).find(words[mot][lettre]);
                //cout << "test" << numtest << " mot" << mot << " lettre" << lettre << "  pos :" << pos << endl;
                   // if not found,
                if (pos == string::npos) match = false;

            }
            if (match) resultat++;
        }
        cout << "Case #" << numtest+1 << ": " << resultat << endl;
    }

}