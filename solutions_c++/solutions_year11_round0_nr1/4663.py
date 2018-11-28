#include <cstdlib>
#include <iostream>
#include <string>
#include <math.h>

using namespace std;

/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
*/
int main(int argc, char *argv[]) {
    int cases,ret,aktualO,aktualB,inRow,move_to,timeO,timeB,time,lastCH;
    string moveAk = "O";
    string charTest = "O";
    cin >> cases;
    for(int cases_i=1;cases_i<=cases;cases_i++){
        ret = timeO = timeB = 0;
        aktualO = 1;
        aktualB = 1;
        lastCH = 0;
        cin >> inRow;
        for(int move_i=0;move_i<inRow;move_i++){
            cin >> moveAk;
            cin >> move_to;
            if(moveAk==charTest){
                 //cout << " is O: " << move_to << " ";
                 timeO = timeO+abs(move_to-aktualO); aktualO = move_to;
                 //cout << timeB << " " << timeO << endl;
                 if(lastCH==1){
                      timeO = timeO+1;
                 }else if(timeB<timeO){
                      timeO = timeO+1;
                 }else{
                      timeO = timeB+1; 
                 }
                 //cout << timeB << " " << timeO;
                 //cout << endl << endl;
                 lastCH = 1;
            }else{
                 //cout << " is B: " << move_to << " ";
                 timeB = timeB + abs(move_to-aktualB); aktualB = move_to;
                 //cout << timeB << " " << timeO << endl;
                 if(lastCH==2){
                      timeB = timeB+1;
                 }else if(timeO<timeB){
                      timeB = timeB+1;
                 }else{
                      timeB = timeO+1; 
                 }
                 //cout << timeB << " " << timeO;
                 //cout << endl << endl;
                 lastCH = 2;
            }
        }
        if(timeB<timeO){
             ret = timeO;
        }else{
             ret = timeB; 
        }
        cout << "Case #" << cases_i << ": " << ret << endl; 
    }
    //system("PAUSE");
    return EXIT_SUCCESS;
}
