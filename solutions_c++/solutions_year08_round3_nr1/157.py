#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

ifstream in("A-large.in");
ofstream out("tmessage2.out");

long N, P, K, L;
long long freq[1002];

void getval();

int main(){
    in >> N;
    for(int i=0; i<N; i++){
        out << "Case #" << i+1 << ": ";
        getval();
    }
}


void getval()
{
    in >> P >> K >> L;
    for(int i=0; i<L; i++)in >> freq[i];
    sort(freq, freq+L);        
    long long multiplier = 1;
    long keycnt = 0;
    long long total=0;
    for(int i=L-1; i>=0; i--){        
        if(keycnt==K){
            keycnt = 0;
            multiplier++;
            if(multiplier>P){
                out << "Impossible" << endl;
                return;
            }
        }
        total+=multiplier*freq[i];
        keycnt++;        
    }
    out << total << endl;
}
