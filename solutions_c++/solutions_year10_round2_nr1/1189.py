/* 
 * File:   main.cpp
 * Author: danyel_dumitriu
 *
 * Created on May 22, 2010, 8:54 AM
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
ofstream fout("big.out");

int main(){

    int t;
    fin >> t;
    for (int i = 0; i < t; i++){

        int n,m;
        fin >> n>> m;
        set<string> have;
        string created[n];
        string need[m];
        for (int j = 0; j< n;j++) {

            fin>> created[j];
            string aux = created[j];
            have.insert(created[j]);
            string temp="/";
            vector<int> pos;
            for (int c =0;c<aux.size();c++ ){
                if (char(aux[c]) == '/'){
                    pos.push_back(c);
                }
            }
            for(int c= 1; c< pos.size(); c++){
                have.insert(aux.substr(0,pos[c]));
               cout << "sub :a "<< aux.substr(0,pos[c]) << endl;
            }
            string str = aux.substr(0,aux.size());
            have.insert(str);
           cout <<"sub:b "<< str <<endl;
        }
        set<string> create;
        int count = 0;
        for (int j = 0; j<m; j++) {
            fin >> need[j];
            string aux = need[j];
            vector<int> pos;
            for (int c =0;c<aux.size();c++ ){
                if (char(aux[c]) == '/'){
                    pos.push_back(c);
                }
            }
            for(int c= 1; c< pos.size(); c++){
                string str = aux.substr(0,pos[c]);
                
                if (have.find(str)==have.end() ){
                    count++;
                    have.insert(str);
                    cout << "str:1 " << str <<endl;
                }
                create.insert(str);
            }
            string str = aux.substr(0,aux.size());
            create.insert(str);
            if(have.find(str) == have.end()){
                count++;
                have.insert(str);
                cout << "str:2 "<<str <<endl;
            }
        }
        cout << "case # " <<i+1 <<endl;
        fout << "Case #" << i+1 <<": " << count <<endl;

        

    }
    return 0;
}