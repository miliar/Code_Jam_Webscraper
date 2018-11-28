#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <stdlib.h>
#include <list>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream inFile(argv[1], ifstream::in);
    ofstream outFile(argv[2], ofstream::out);
    string sLine; int T;
    if(getline(inFile, sLine)) //!! global "getline()"
    {
        //Do here whatever you need to do
        istringstream buffer(sLine, istringstream::in);
        buffer >> T;
    }
    else{
        cout << "ERROR in file format!" << endl;
        return -1;
    }

    for(int i0 = 0; i0 < T; i0 ++){
        int L, N, C; long t;
        if(getline(inFile, sLine))
        {
            istringstream buffer(sLine, istringstream::in);
            buffer >> L; 
            buffer >> t; 
            buffer >> N; 
            buffer >> C; 
            int a[C];
            for(int i1 = 0; i1 < C; i1 ++) buffer >> a[i1]; 
            int d[N];
            for(int i1 = 0; i1 < N/C; i1 ++){ //!!
                for(int i2 = 0; i2 < C; i2 ++){
                    d[i1*C+i2] = a[i2]; //!!
                }
            }
            for(int i1 = 0; i1 < N%C; i1 ++) d[(N/C)*C+i1] = a[i1]; //!!
            
            outFile << "Case #" << i0+1 << ": "; 
            //for(int i1 = 0; i1 < N; i1 ++) cout << d[i1] << " ";
            //cout << endl;
            
            if(L == 0){
                long sum = 0;
                for(int i1 = 0; i1 < N; i1 ++) sum += d[i1];
                sum *= 2;
                outFile << sum << endl;
            }
            else{
                if(t == 0){
                    sort(d, d+N, greater<int>()); //????????????????????????????????????????????????????
                    long sum = 0;
                    assert(L <= N);
                    for(int i1 = 0; i1 < L; i1 ++) sum += d[i1];
                    for(int i1 = L; i1 < N; i1 ++) sum += 2 * d[i1];
                    outFile << sum << endl;
                }
                else{
                    long dist = t; //in t we can walk dist
                    long sum = 0; int i1;
                    for(i1 = 0; i1 < N; i1 ++){
                        sum += 2 * d[i1];
                        if(sum >= dist)
                            break;
                    }
                    
                    if(i1 == N-1)
                    {
                        sum -= (sum-dist)/2;
                        outFile << sum << endl;
                        continue;
                    }
                    
                    //cout << "Here 1" << endl;  
                    //cout << N << " " << i1 << " " << sum << " " << t << endl;  
                    int d2[N-1-(i1+1)+1];
                    for(int i2 = i1 + 1; i2 < N; i2 ++) d2[i2-i1-1] = d[i2];
                    sort(d2, d2+N-1-(i1+1)+1, greater<int>());
                    //cout << "Here 2" << endl;    
                    if(sum == dist){                       
                        int LL = L < N-1-(i1+1)+1 ? L : N-1-(i1+1)+1;
                        for(int i2 = 0; i2 < LL; i2 ++) sum += d2[i2];
                        for(int i2 = LL; i2 < N-1-(i1+1)+1; i2 ++) sum += 2 * d2[i2];
                        outFile << sum << endl;
                    }
                    else{ //sum > dist
                        int delta = (sum-dist)/2; sum = dist;
                        //cout << delta << " " << sum  << endl;  
                        int LL = L < N-1-(i1+1)+1 ? L : N-1-(i1+1)+1;
                        bool isAdded = false; int k = 0;
                        for(int i2 = 0; i2 < LL; i2 ++) {
                            if(isAdded == false && d2[k] < delta) { isAdded = true; sum += delta; }
                            else { sum += d2[k]; k ++; }
                        }
                        //cout << LL << " " << sum  << endl;  
                        if(isAdded == false) sum += 2 * delta;
                        //cout << LL << " " << sum  << endl;  
                        for(int i2 = k; i2 < N-1-(i1+1)+1; i2 ++) sum += 2 * d2[i2];
                        //cout << LL << " " << sum  << endl;  
                        //cout << k << " " << N-1-(i1+1)+1  << " " << i1 << " " << N << endl;  
                        outFile << sum << endl;
                    }//else
                }//else
            }//else
            
        }//if(getline(inFile, sLine))
     }//for(int i0 = 0; i0 < T; i0 ++) 
}

