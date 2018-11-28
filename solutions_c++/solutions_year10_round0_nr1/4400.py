/* 
 * File:   main.cpp
 * Author: tiago
 *
 * Created on May 8, 2010, 1:37 PM
 */

#include <stdlib.h>
#include <iostream>
#include <vector>

using namespace std;
/*
 *
Input
4
1 0
1 1
4 0
4 47

Output
Case #1: OFF
Case #2: ON
Case #3: OFF
Case #4: ON

 */
class Snapper {
    int toggle;
public:
    Snapper(){
        this->toggle=0;
    }

    int getToggle(){
        return this->toggle;
    }

    bool isOn(){
        if(this->toggle==1)
            return true;
        else
            return false;
    }

    void switchToggle(){
        if(this->toggle == 0)
            this->toggle=1;
        else if(this->toggle == 1)
            this->toggle=0;
    }
};

class Chain {
    vector<Snapper> chain;

public:
    Chain(unsigned int N){
        this->chain = vector<Snapper>(N);
    }

    vector<Snapper>& getChain(){
        return this->chain;
    }

    bool isRecievingPower(unsigned int index){
        if(index==0){
            return true;
        }
        
        for(unsigned int i=index;i>0;i--){
            if(!this->chain[i-1].isOn()){
                return false;
            }
            else if(this->isRecievingPower(i-1)){
                return true;
            }
        }
    }

};

int main(int argc, char** argv) {
    unsigned int T;
    cin >> T;
    for(unsigned int t=1;t<=T;t++){
        unsigned int N;
        unsigned long K;
        cin >> N >> K;
        
        Chain snapchain = Chain(N);
        /*
        cout << endl << "begin ciclo" << endl;
        for(int i = 0; i< snapchain.getChain().size(); ++i){
            cout << snapchain.getChain()[i].getToggle() << endl;
        }
        cout << "endl ciclo" << endl;
        */
        for(unsigned long k=0;k<K;k++){
            long n = N-1;
            while(n>=0){
                if(snapchain.isRecievingPower(n)){
                    snapchain.getChain()[n].switchToggle();
                }
                n--;
            }
        }
        
        bool on=true;
        for(unsigned int l=0; l<N;l++){
            if(!snapchain.getChain()[l].isOn())
                on = false;
        }

        if(on){
            cout << "Case #" << t << ": ON" << endl;
        }
        else {
            cout << "Case #" << t << ": OFF" << endl;
        }

    }
    return (EXIT_SUCCESS);
}

