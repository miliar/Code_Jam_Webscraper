#include<iostream>
#include <fstream>
#include<math.h>
using namespace std;

int main(void) {
    fstream input, output;
    long tests, snapers, snap_times, snaps_need;
    int i, flag, case_=0;

    input.open("A-large.in", ios::in);
    output.open("A-large.out", ios::out);
    if (!input.is_open() || !output.is_open()) {
        cout << "Error opening files....\n\n";
        getchar();
        return 1;
    }
    input >> tests;

    for (i = 0; i < tests; i++) {
        input >> snapers;
        input >> snap_times;

        snaps_need = pow(2, snapers)-1;
        flag=0;
        while(flag==0){
            snap_times-=snaps_need;
            if(snap_times==0){
                flag=1;
            }else if(snap_times>0){
                snap_times--;
            }else{
                break;
            }
        }
        if (flag==1) {
            cout<<"ON"<<endl;
            output << "Case #" << ++case_ << ": " << "ON" << "\n";
        }else{
            cout<<"OFF"<<endl;
            output << "Case #" << ++case_ << ": " << "OFF" << "\n";
        }
    }
    input.close();
    output.close();
    return 0;
}

