#include <iostream>
#include <stdio.h>

using namespace std;


void printResult(int numCase, int numTeam);
double countWP(int j, int numTeam);
double countOWP(int j, int numTeam);
double countOOWP(int j, int numTeam);
char a[105][105];
double numOne[105], numZero[105];
double wp[105], owp[105], oowp[105];

int main()
{
    freopen("large.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int numCase, numTeam;

    cin >> numCase;

    for (int i = 1; i <= numCase; ++i){
        cin >> numTeam;

        //count WP
        for (int j = 0; j < numTeam; ++j){
            for (int k = 0; k < numTeam; ++k){
                cin >> a[j][k];
            }
            wp[j] = countWP(j, numTeam);
        }
        //count OWP
        for (int j = 0; j < numTeam; ++j){
            owp[j] = countOWP(j, numTeam);
        }
        //count OOWP
        for (int j = 0; j < numTeam; ++j){
            oowp[j] = countOOWP(j, numTeam);
        }

        printResult(i, numTeam);
    }

    return 0;
}

void printResult(int numCase, int numTeam){
    cout << "Case #" << numCase << ":" << endl;
    //print RPI
    for (int i = 1; i <= numTeam; i++){
        cout << 0.25 * wp[i-1] + 0.5 * owp[i-1] + 0.25 * oowp[i-1] << endl;
    }
}

double countWP(int j, int numTeam){
    double countOne = 0, countZero = 0;
    for (int k = 0; k < numTeam; ++k){
        if(a[j][k] == '1'){
            countOne++;
        }else if(a[j][k] == '0'){
            countZero++;
        }
    }
    numOne[j] = countOne;
    numZero[j] = countZero;
    return countOne / (countOne + countZero);
}

double countOWP(int j, int numTeam){
    double counter = 0, sum = 0;
    for (int k = 0; k < numTeam; ++k){
        if(a[j][k] == '1' || a[j][k] == '0'){
            counter++;
            if (a[k][j] == '0'){
                sum += numOne[k] / (numOne[k] + numZero[k] - 1);
            }else if (a[k][j] == '1'){
                sum += (numOne[k] - 1) / (numOne[k] + numZero[k] - 1);
            }
        }
    }
    return (sum / counter);
}

double countOOWP(int j, int numTeam){
    double counter = 0, sum = 0;
    for (int k = 0; k < numTeam; ++k){
        if(a[j][k] == '1' || a[j][k] == '0'){
            counter++;
            sum += owp[k];
        }
    }
    return (sum / counter);
}
