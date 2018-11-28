#include <iostream>
#include <cstdio>
#include <map>
#include <string>

using namespace std;

#define maxq 1000

int main(){
    freopen("universe.in", "r", stdin);
    int cases;
    cin>>cases;
    string none;
    for (int casenr = 0; casenr < cases; casenr++){
        int engines;
        cin>>engines;
        map<string, int> enginenr;
        string engine;
        getline(cin, none);
        for (int i = 0; i < engines; i++){
            getline(cin, engine);
            enginenr[engine] = i;
        }
        int queries;
        cin>>queries;
        string query[queries];
        getline(cin, none);
        for (int i = 0; i < queries; i++){
            getline(cin, query[i]);
        }

        int table[queries+1][engines+1];
        for (int i = 0; i < engines; i++)
            table[queries][i] = queries;
        for (int querynr = queries-1; querynr >= 0; querynr--){
    	    int number = enginenr[query[querynr]];
            for (int i = 0; i < engines; i++)
                if (i != number)
                    table[querynr][i] = table[querynr+1][i];
                else
                    table[querynr][i] = querynr;
        }
        int switches = 0;
        for (int querynr = 0; querynr < queries;){
            int tmax=0, maxnr;
            for (int j = 0; j < engines; j++)
                if (table[querynr][j] > tmax){
                    tmax = table[querynr][j];
                }
            if (tmax >= queries)
                break;
            else{
                switches++;
                querynr = tmax;
            }
        }
        cout<<"Case #"<<casenr+1<<": "<<switches<<endl;
    }
}
