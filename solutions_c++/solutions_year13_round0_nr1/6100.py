#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    int n;
    fin >> n;
    string s;
    vector< vector<char> > arr(4, vector<char>(4));
    vector< unsigned > res(n);
    for (int i = 0; i < n; i++) {
        bool dotExist = 0;
        int dSum = 0;
        int j = 0;
        for(j; j < 4; j++) {
            getline(fin, s);
            if(!s[0]) {
                j--;
                continue;
            }
            int sum = 0;
            for(int k = 0; k < 4; k++) {
                arr[j][k] = s[k];
                if(s[k] == '.') {
                    dotExist = 1;
                    continue;
                }
                sum += (int)arr[j][k];
            }
            dSum += (int)arr[j][j];
            if(sum == 352 or sum == 348) {
                res[i] = 1;
                while(j<4) {
                    getline(fin, s);
                    j++;
                }
                continue;
            }
            else if(sum == 316 or sum == 321) {
                res[i] = 2;
                while(j<4) {
                    getline(fin, s);
                    j++;
                }
                continue;
            }

        }
        if(dSum == 352 or dSum == 348) {
            res[i] = 1;
            while(j<4) {
                getline(fin, s);
                j++;
            }
            continue;
        }
        else if(dSum == 316 or dSum == 321) {
            res[i] = 2;
            while(j<4) {
                getline(fin, s);
                j++;
            }
            continue;
        }
        dSum = 0;
        for(int m = 0; m < 4; m++) {
            int sum = 0;
            for(int n = 0; n < 4; n++) {
                if(arr[n][m] == '.') {
                    continue;
                }
                sum += arr[n][m];
            }
            if(sum == 352 or sum == 348) {
                res[i] = 1;
                while(j<4) {
                    getline(fin, s);
                    j++;
                }
                continue;
            }
            else if(sum == 316 or sum == 321) {
                res[i] = 2;
                while(j<4) {
                    getline(fin, s);
                    j++;
                }
                continue;;
            }
            dSum += arr[m][3-m];
        }

        if(dSum == 352 or dSum == 348) {
            res[i] = 1;
            while(j<4) {
                getline(fin, s);
                j++;
            }
            continue;;
        }
        else if(dSum == 316 or dSum == 321) {
            res[i] = 2;

            while(j<4) {
                getline(fin, s);
                j++;
            }
            continue;;
        }
        stop:
            if(!res[i] and dotExist) res[i] = 4;
            else if(!res[i]) res[i] = 3;
    }

    for(int i = 0; i < n; i++) {
        cout << "Case #" << i+1 << ": ";
        switch(res[i]) {
            case 1: cout << "X won"; break;
            case 2: cout << "O won"; break;
            case 3: cout << "Draw"; break;
            case 4: cout << "Game has not completed"; break;
            default: cout << "Game has not completed"; break;
        }
        cout << endl;
    }
}
