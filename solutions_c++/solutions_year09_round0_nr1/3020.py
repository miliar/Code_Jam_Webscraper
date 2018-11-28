
#include<fstream>
#include<iostream>
#include<vector>
#include<string>


using namespace std;

int main(){
    ofstream fout("alien.out");

    vector< vector <bool> > ok(17, vector<bool>(30, false));
    vector<string> words;
    string s = "";
//    bool inList = false;
    bool alt = false;


    int L, D, N;        //length, words, number of tests
    int pos = 0;        //possible words



    cin >> L >> D >> N;


    //Legg inn alle ordene
    for(int i = 0; i < D; ++i){
        cin >> s;
        words.push_back(s);
    }

    //Test cases
    for(int i = 0; i < N; ++i){
        cin >> s;
        
        int j = 0; //first coordinate in ok

        for(int k = 0; k < s.size(); ++k){
            if(s[k] == '('){
                alt = true;
                continue;
            }
            if(s[k] == ')'){
                alt = false;
                ++j;
                continue;
            }
            
            ok[j][(int) (s[k] - 'a')] = true;

            if(!alt){
                ++j;
            }

        }


        int num = 0;
        int ltr;
        //Check each word
        for(int k = 0; k < D; ++k){
            for(int j = 0; j < L; ++j){
                ltr = (int) (words[k][j] - 'a');
                
                if(!ok[j][ltr]) break;
                if(j+1 == L) ++num;
            }
        }
        
        fout << "Case #" << i+1 << ": " << num << endl;
        

        for(int k = 0; k < 17; ++k){
            for(int j = 0; j < 30; ++j){
                ok[k][j] = false;
            }
        }

    }
    
    return 0;

}

