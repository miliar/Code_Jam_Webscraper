#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <sstream>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);

    for(int k = 1; k <= t; k++){
    int n;
    scanf("%d", &n);
    int** results = new int*[n];
    for(int i = 0; i < n; i++)
        results[i] = new int[n];
    double** teams = new double*[n];    // 0 - WP, 1 - OWP, 2 - OOWP
    for(int i = 0 ; i < n; i++){
        teams[i] = new double[3];
    }
    for(int i = 0 ; i < n; i++){
        string s;
        cin >> s;
        for(int j = 0; j < n; j++){
            char c = s.at(j);
            if(c == '1') results[i][j] = 1;
            else if (c == '0') results[i][j] = 0;
            else results[i][j] = -1;
        }
    }
    int* matches = new int[n];
    for(int i = 0 ; i < n; i++){
        matches[i] = 0;
    }
    for(int i = 0; i < n; i++){
        int sum = 0;
        for(int j = 0; j < n; j++){
            if(results[i][j] >= 0){
                sum += results[i][j];
                matches[i]++;
            }
        }
        teams[i][0] = (double) sum / (double)matches[i];
    }

    for(int i = 0; i < n; i++){
        double sum = 0;
        for(int j = 0; j < n; j++){
            if(results[i][j] >= 0){
                sum += (teams[j][0] - (double)results[j][i] / matches[j]) * ((double)matches[j] / (matches[j] - 1)) ;
            }
        }
        teams[i][1] = sum / (double)matches[i];
    }
    for(int i = 0; i < n; i++){
        double sum = 0;
        for(int j = 0; j < n; j++){
            if(results[i][j] >= 0){
                sum += teams[j][1];
            }
        }
        teams[i][2] = sum / (double)matches[i];
    }
    /*for(int i = 0; i < n; i++){
        cout <<"graja tak"<<endl;
        cout <<teams[i][0] << " " << teams[i][1] << " " << teams[i][2] << " " <<matches[i]<<endl;
    }*/
    string wynik = "Case #";
    stringstream ss;
    ss << k;
    wynik += ss.str();
    wynik +=":\n";
    for(int i = 0; i < n; i++){
        double sum = teams[i][0]/4 + teams[i][1]/2 + teams[i][2]/4;
        stringstream out;
        out << sum;
        wynik += out.str();
        wynik +="\n";
    }
    cout << wynik;
    for(int i = 0; i < n; i++){
        delete[] results[i];
    }
    for(int i = 0; i < 3; i++){
        delete[] teams[i];
    }
    delete[] results;
    delete[] teams;
    }
    return 0;
}
