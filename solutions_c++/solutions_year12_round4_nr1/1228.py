/*
 * File:   main.cpp
 * Author: herman
 *
 * Created on April 27, 2012, 8:31 PM
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <climits>

using namespace std;

ifstream infile;
ofstream outfile;

/*
 *  swinging wild
 */
int main(int argc, char** argv) {
    infile.open("input.txt");
    outfile.open("output.txt");

    int trials;
    infile >> trials;
    for (int i = 0; i < trials; i++){
        int N;
        infile >> N;
        int dist[N];
        int length[N];
        for (int j = 0; j < N; j++){
            infile >> dist[j];
            infile >> length[j];
        }
        int D;
        infile >> D;
        int dneeded[N];
        for(int j = 0; j < N;j++){
            dneeded[j] = D - dist[j];
        }
        for(int j = N-1; j >= 0; j--){
                // try using other vine
                int next = j+1;
                bool outofreach;
                if (next < N)
                    outofreach = (dist[next] - dist[j] > length[j]);
                else
                    outofreach = true;
                bool found = false;
                while (next < N && !outofreach && !found){
                    int dnext = dist[next] - dist[j];
                    int slength = min(dnext,length[next]);
                    if (slength >= dneeded[next]){
                        // cout << slength;
                        // found possibility
                        dneeded[j] = dnext;
                        found = true;
                    }
                    next++;
                    if (next < N)
                        outofreach = (dist[next] - dist[j] > length[j]);
                }
            }
        

        cout << "Case #" << (i+1) << ": ";
        outfile << "Case #" << (i+1) << ": ";
        if (dneeded[0] <= dist[0]){
            // it is possible
            cout << "YES" << endl;
            outfile << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
            outfile << "NO" << endl;
        }
        
    }

    infile.close();
    outfile.close();

    return (EXIT_SUCCESS);
}

