/* 
 * File:   main.cpp
 * Author: lukas
 *
 * Created on 17 lipiec 2008, 15:14
 */

#include <ios>


#include <vector>


#include <stdlib.h>
#include <vector>
#include <string>
#include <iostream>
#include <string>
#include <string>
#include <cstdio>
#include <vector>
#include <fstream>

using namespace std;
/*
 * 
 */
int searchResult(vector <string> &engines, vector <string> &queries);
int main(int argc, char** argv) {
    string inputFile = "";
    string outputFile = "";
    if (argc==2) {
        inputFile = string(argv[1]);
        //outputFile = argv[1];
        outputFile = inputFile.substr(0, inputFile.length()-3);
        outputFile+=(".out");
    }
    else {
        cout << "You must give input file as argument" <<endl;
        return 0;
    }

    //reading data
    
    ifstream infile ( inputFile.c_str() , ifstream::in );
    ofstream outfile ( outputFile.c_str(), ofstream::out);
    if (infile.is_open() && outfile.is_open()) {
        int N;
        //fscanf(fp, "%d", &N);
        infile >> N;
        for (int i=0; i<N; i++) {
            int S;
            infile >> S;
          //  fscanf(fp, "%d", &S);
            vector <string> engines(0);
            for (int j=0; j<S; j++) {
                char tmp[101];
                infile.getline(tmp, 101);
                if (strlen(tmp)>0) {
                    engines.push_back(string(tmp));
                } else j--;
            }
            int Q;
            infile >> Q;
            vector <string> queries(0);
            for (int j=0; j<Q; j++) {
                char tmp[101];
                infile.getline(tmp, 101);
                if (strlen(tmp)>0) {
                    queries.push_back(string(tmp));
                } else j--;
            }
//            cout << engines.size()<<endl;
//            cout << queries.size()<<endl;
//            cout << "Result "<< searchResult(engines, queries) <<endl;
            outfile << "Case #" << (i+1) << ": " <<searchResult(engines, queries) << endl;
            cout << "-------------------"<<endl;
        }
        infile.close();
        outfile.close();
    
    }
    return (EXIT_SUCCESS);
}

int searchResult(vector <string> &engines, vector <string> &queries) {
    int ret =0;
    int E = engines.size();
    int Q = queries.size();
    int pos=0;
    while (true) {
        vector <int> max(E, INT_MAX);
        int max_id = 0;
        for (int i = 0; i<E; i++) {
            for (int j=pos; j<Q; j++) {
                if (queries[j]==engines[i]) {
                    max[i]=j;

                    break;
                }
            }
            if (max_id!=i && max[max_id]<max[i])
                max_id=i;
        }
        for (int i = 0; i<E; i++) { 
            cout << engines[i] << " " << max[i] << endl;
        }
        cout << "max_id " << max_id << "val: " << max[max_id] <<endl;
        if (max[max_id]==INT_MAX)
            return ret;
        ret++;
        pos=max[max_id];
    }
    return ret;
}
