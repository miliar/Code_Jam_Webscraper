#include <iostream>
#include <fstream>
#include <cstring>
#include <istream>
#include <string>

using namespace std;

int N,S,Q,Nswitches,q,currs;
char engines[101][101];
char queries[1001][101];

static int findnextswitch(){
    int nextswitch[101];
    for (int s=0;s<S;s++){
        int qq=q;
        while ( strcmp(engines[s],queries[qq])!=0 && qq<Q){
            qq++;
        }
        nextswitch[s]=qq;
    }
    int maxn=0;
    int val=0;
    for (int i=0;i<S;i++){
        if (nextswitch[i]>maxn){
            maxn=nextswitch[i];
            val=i;
        }
    }
    return nextswitch[val];
}



int main()
{
    ifstream fin("..\\temp\\A-large.in");
    ofstream fout("..\\temp\\output.txt");

    string line;
    getline(fin,line);
    N=atoi(line.c_str());
    for(int n=1;n<=N;n++){
        getline(fin,line);
        S=atoi(line.c_str());
        for (int s=0;s<S;s++){
            fin.getline(engines[s],101);
        }
        getline(fin,line);
        Q=atoi(line.c_str());
        for (int q=0;q<Q;q++){
            fin.getline(queries[q],101);
        }
        Nswitches=0;
        q=0;
        q=findnextswitch();
        while (q<Q){
            q=findnextswitch();
            Nswitches++;
        }


        fout << "Case #" << n << ": "<<Nswitches<< endl;
//        delete [] engines;
//        delete [] queries;

    }

    return 0;
}
