//============================================================================
// Name        : one.cpp
// Author      : Erik Amaru Ortiz <aortiz.erik@gmail.com>
// Version     :
// Copyright   : GPL
// Description : Problem A. Bot Trust
//============================================================================

#include <iostream>
using namespace std;

int main()
{
    int t, n, i, j, is;
    string r, seq[100];

    int posO, posB;
    int time;
    int push;
    int seqO[100], iso, seqB[100], isb;

    cin>>t;
    int casen=0, k;

    while(t-- > 0){
        casen++;
        cin>>n;
        posO = posB = 1;
        iso = isb = is=0;

        for(i=0; i<n; i++){
            cin>>r;
            if(r.compare("O") == 0) {
                seq[is++] = "O";
                cin>>seqO[iso++];
            } else {
                seq[is++] = "B";
                cin>>seqB[isb++];
            }
        }

        time=push=k=i=j=0;

        while(1){
            time++;

            if(posO == seqO[i]){ //try push
                if(seq[k].compare("O")==0){ //can do push
                    //push
                    i++;
                    push=1;
                }
            } else if(i != iso){
                if(posO < seqO[i]) posO++;
                else posO--;
            }

            if(posB == seqB[j]){ //try push
                if(seq[k].compare("B")==0){ //can do push
                    //push
                    j++;
                    push=1;
                }
            } else if(j != isb){
                if(posB < seqB[j]) posB++;
                else posB--;
            }

            if(push){
                k++;
                push=0;
            }

            if(i == iso && j == isb)
               break;
        }
        cout<<"Case #"<<casen<<": "<<time<<endl;
    }

    return 0;
}

