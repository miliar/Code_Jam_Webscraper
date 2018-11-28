/* 
 * File:   main.cpp
 * Author: danyel_dumitriu
 *
 * Created on May 23, 2010, 1:50 AM
 */
#include<fstream>
#include<queue>
#include <iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include <set>
#include<string>
using namespace std;
//read from file
ifstream fin("small.in");
//output to file
ofstream fout("small.out");

int main() {

    int t;
    fin >> t;
    for (int i = 1; i <= t; i++){

        int n;
        fin >>n;
        int a[n][2];
        int found[n][n];
        for (int j= 0; j<n;j++){
            for (int c= 0; c<n;c++){
                found[j][c] =0;
            }
        }
        int count = 0;
        for (int j= 0; j <n; j++){
            fin >>a[j][0] >>a[j][1];
            for (int k = 0; k<j;k++){
                if ((a[k][0]<a[j][0]&& a[k][1]>a[j][1]) ||
                        (a[k][0]>a[j][0]&&a[k][1]<a[j][1])){

                    if(found[k][j]==0){
                    found[k][j]=1;
                    found[j][k]=1;
                    count++;
                    }
                }
            }
        }
        cout << count <<endl;


        fout <<"Case #" <<i<<": " <<count <<endl;
    }
    return 0;
}