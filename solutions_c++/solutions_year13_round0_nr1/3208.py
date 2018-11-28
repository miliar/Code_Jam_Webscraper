#include <assert.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <time.h>

using namespace std;

/*
int ElapsedTime(const vector<int>& vecButtons, int index) {
	return abs(vecButtons[index] - vecButtons[index - 1]);
}
*/

struct Rec {
    char c1;
    char c2;

    bool operator==(Rec& rec) {
        if (c1 == rec.c1 && c2 == rec.c2)
            return true;
        else
            return false;
    }

    bool operator<(Rec& rec) {
        if (rec.c1 > c1) return true;

        if (c1 == rec.c1 && c2 < rec.c2) 
            return true;

        return false;
    }
};

map<char, char> maps; 
vector<Rec> vec; 
vector<int> vecTry; 

void pushSubStr(vector<Rec> &rec, string& str) {
    for (int i=0; i<(str.length() - 1); i++) {
        Rec rec, rec2; 
        rec.c1 = str[i];
        rec.c2 = str[i+1];
        vec.push_back(rec);

        if (maps[rec.c1] != 0) {
            rec2 = rec; 
            rec2.c1 = maps[rec.c1];
            vec.push_back(rec2);
        }

        if (maps[rec.c2] != 0) {
            rec2 = rec; 
            rec2.c2 = maps[rec.c2];
            vec.push_back(rec2);
        }

        if (maps[rec.c1] != 0 && maps[rec.c2] != 0) {
            rec2 = rec; 
            rec2.c1 = maps[rec.c1];
            rec2.c2 = maps[rec.c2];
            vec.push_back(rec2);
        }
    }
}

int getMinLength(vector<Rec> &vec) {
    int iResult = 2 * vec.size();

    for (int i=0; i<(vec.size()-1); i++) {
        if (vec[i].c2 == vec[i+1].c1)
            iResult--;
    }

    return iResult; 
}

int getResult(int pos, vector<Rec>& resultVec) {
    int min = -1; 
    for (int i=0; i<vec.size(); i++) {
        bool test = false; 
        for (int j=0; j<(pos-1); j++) {
            if (vec[i] == resultVec[j]) {
                test = true;
                break;
            }
        }

        if (!test) {
            resultVec[pos-1] = vec[i];
            vecTry[pos-1] = i; 
        }
        else {
            continue;
        }


        for (int i=0; i<vecTry.size(); i++) {
            cout << vecTry[i] << " ";
        }
        cout << endl; 


        if (pos == (vec.size()))
        {
            return getMinLength(resultVec);
        }
        else {
            int iTemp = getResult(pos+1, resultVec);
            if (min == -1 || min > iTemp) {
                min = iTemp;
            }
        }
    }

    return min; 
}

map<char, int> myMapHead, myMapEnd; 

int getResultInt(vector<Rec> &vec) {
    int result = 0; 

    for (int i=vec.size() - 1; i>=0; i--) {
        for (int j=i-1; j>=0; j--) {
            if (vec[i].c1 == vec[j].c2) {
                result++;
                vec[j].c2 = vec[i].c2;
                break;
            }
        }
    }

    return result; 
}


int main(int argc, char* argv[]) {
    
	if (argc != 2) {
		cerr << "wrong number of parameter" << endl;
		return -1;
	}

	ifstream inf(argv[1]);
	if (!inf) {
		cerr << "cannot open file " << argv[1] << endl;
		return -1;
	}

    // srand(time(NULL));

	string ln;  
    inf >> ln;

    int number = atoi(ln.c_str());
    
	for (int cases=0; cases<number; cases++) 
    {
        vector< string > v; int res = 0; 
        for (int i=0; i<4; i++) {
            {
                inf >> ln; 
                v.push_back(ln);
                if (ln.find('.') != string::npos) {
                    res = 1; 
                }
            }
        }

        char x = 'X', o = 'O', d = '.'; 
        bool bXWin = false, bOWin = false; 

        for (int i=0; i<4; i++) {
            if (v[i].find(x) == string::npos && v[i].find(d) == string::npos) {bOWin = true; break;}
            if (v[i].find(o) == string::npos && v[i].find(d) == string::npos) {bXWin = true; break;}
        }

        if (bOWin) {
            cout << "Case #" << (cases + 1) << ": " << "O won" << endl;
            continue;
        }
        
        if (bXWin) {
            cout << "Case #" << (cases + 1) << ": " << "X won" << endl;
            continue;
        }

        bOWin = true, bXWin = true; 
        for (int i=0; i<4; i++) {
            bOWin = true, bXWin = true; 
            for (int j=0; j<4; j++) {
                if (v[j][i] == x || v[j][i] == d) bOWin = false;
                if (v[j][i] == o || v[j][i] == d) bXWin = false; 
            }

            if (bOWin || bXWin) break;
        }

        if (bOWin) {
            cout << "Case #" << (cases + 1) << ": " << "O won" << endl;
            continue;
        }

        if (bXWin) {
            cout << "Case #" << (cases + 1) << ": " << "X won" << endl;
            continue;
        }

        bOWin = true, bXWin = true; 
        for (int i=0; i<4; i++) {
                if (v[i][i] == x || v[i][i] == d) bOWin = false;
                if (v[i][i] == o || v[i][i] == d) bXWin = false; 
        }

        if (bOWin) {
            cout << "Case #" << (cases + 1) << ": " << "O won" << endl;
            continue;
        }

        if (bXWin) {
            cout << "Case #" << (cases + 1) << ": " << "X won" << endl;
            continue;
        }

        bOWin = true, bXWin = true; 
        for (int i=0; i<4; i++) {
            if (v[i][3 - i] == x || v[i][3-i] == d) bOWin = false;
            if (v[i][3 - i] == o || v[i][3-i] == d) bXWin = false; 
        }

        if (bOWin) {
            cout << "Case #" << (cases + 1) << ": " << "O won" << endl;
            continue;
        }

        if (bXWin) {
            cout << "Case #" << (cases + 1) << ": " << "X won" << endl;
            continue;
        }

        if (res == 1) {
            cout << "Case #" << (cases + 1) << ": " << "Game has not completed" << endl;
            continue;
        }

        // print result
        cout << "Case #" << (cases + 1) << ": " << "Draw" << endl;
	}

	return 0;
}
