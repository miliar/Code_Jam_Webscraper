/* 
 * File:   main.cpp
 * Author: sharad
 *
 * Created on 13 February, 2011, 2:47 PM
 */

#include <cstdio>
#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;



//int o_last_press = 0;
//int o_last_position = 1;
//int b_last_press = 0;
//int b_last_position = 1;
//int last_btn_press = 0;

char sq[] = "O 2, B 1, B 2, O 4";
enum Robot {Orange = 'O',Blue = 'B'};

struct inputPair {
    Robot x;
    int buttonPos;
    inputPair(Robot r = Orange, int pos = -1) {
        x = r;
        buttonPos = pos;
    }  
};

int top = -1;
 
//inputPair arr[] = { {Blue,2},{Blue,1}
//                    };
//bool getInput(inputPair& A) {
//    if(top < 1) {
//        top++;
//        A.buttonPos = arr[top].buttonPos;
//        A.x = arr[top].x;
//        return true;
//    } else {
//        return false;
//    }
//}
// 3
//4 O 2 B 1 B 2 O 4
//3 O 5 O 8 B 100
//2 B 2 B 1
int main(int argc, char** argv) {

    int n_testCases = 0;
    cin >> n_testCases;

    for(int i=0; i < n_testCases; i++) {
        int n_moves = 0;
        cin >> n_moves;
        int o_last_press = 0;
        int o_last_position = 1;
        int b_last_press = 0;
        int b_last_position = 1;
        int last_btn_press = 0;
        int moveTime = 0;
        inputPair A;
        
        for(int j=0; j<n_moves; j++) {
            char robot = 'O';
            int position = 0;
            cin >> robot;
            cin >> position;
            A.buttonPos = position;
            A.x = (Robot)robot;
            if(A.x == 'O') {
                moveTime = abs(A.buttonPos - o_last_position) + o_last_press;
                last_btn_press = max(moveTime,last_btn_press) + 1;
                o_last_position = A.buttonPos;
                o_last_press = last_btn_press;
            } else {
                moveTime = abs(A.buttonPos - b_last_position) + b_last_press;
                last_btn_press = max(moveTime,last_btn_press) + 1;
                b_last_position = A.buttonPos;
                b_last_press = last_btn_press;
            }

            
        }
        cout << "Case #"<< i+1 << ": " << last_btn_press << endl;
    }
    

//    inputPair A;
//    int timeStamp = 0;
//    int moveTime = 0;
//    while(getInput(A)) {
//        if(A.x == 'O') {
//            moveTime = abs(A.buttonPos - o_last_position) + o_last_press;
//            last_btn_press = max(moveTime,last_btn_press) + 1;
//            o_last_position = A.buttonPos;
//            o_last_press = last_btn_press;
//        } else {
//            moveTime = abs(A.buttonPos - b_last_position) + b_last_press;
//            last_btn_press = max(moveTime,last_btn_press) + 1;
//            b_last_position = A.buttonPos;
//            b_last_press = last_btn_press;
//        }
//    }

    
    return 0;
}

