#ifndef GJ_H
#define GJ_H

#include <fstream>
using namespace std;

ofstream outf;
void tic_tac(){
    int num_cases;
    char board[17];
    cin >> num_cases;
    for(int cases = 0; cases < num_cases; cases++){
       for(int j = 0; j < 4; j++){
           cin >> (board + 4 * j);
       }

       int X_win = 0;
       int O_win = 0;
       int not_complete = 0;
       //check hor
       for(int i = 0; i < 4; i++){
           char* start = board + i * 4;

           char* tmp_ptr = start;
           int has_dot = 0;
           for(int j = 0; j < 4; j++){
               if(*tmp_ptr == '.'){
                   not_complete = 1;
                   has_dot = 1;
                   break;
               }
               tmp_ptr++;
           }
           if(has_dot){
               continue;
           }

           char val = *start;
           int same = 1;
           for(int j = 0; j < 4; j++){
               if(val == 'T'){
                   val = *start;
               }
               if(val != 'T' && *start != val && *start != 'T'){
                   same = 0;
               }
               start++;
           }
           if(same){
               if(val == 'X'){
                   X_win = 1;
               }else{
                   O_win = 1;
               }
               break;
           }
       }
       if(X_win){
           outf << "Case #" << cases + 1 << ": X won" << endl;
           continue;
       }else if(O_win){
           outf << "Case #" << cases << ": O won" << endl;
           continue;
       }

       //check veh
       for(int i = 0; i < 4; i++){
           char* start = board + i;
           char val = *start;

           char* tmp_ptr = start;
           int has_dot = 0;
           for(int j = 0; j < 4; j++){
               if(*tmp_ptr == '.'){
                   not_complete = 1;
                   has_dot = 1;
                   break;
               }
               tmp_ptr += 4;
           }
           if(has_dot){
               continue;
           }

           int same = 1;
           for(int j = 0; j < 4; j++){
               if(val == 'T'){
                   val = *start;
               }
               if(val != 'T' && *start != val && *start != 'T'){
                   same = 0;
                   break;
               }
               start += 4;
           }
           if(same){
               if(val == 'X'){
                   X_win = 1;
               }else{
                   O_win = 1;
               }
               break;
           }
       }
       if(X_win){
           outf << "Case #" << cases + 1 << ": X won" << endl;
           continue;
       }else if(O_win){
           outf << "Case #" << cases + 1 << ": O won" << endl;
           continue;
       }
        
       char* start = board;
       char val = *start;
       int same = 1;
       int has_dot = 0;
       if(board[0] == '.' || board[5] == '.' || board[10] == '.' || board[15] == '.'){
           not_complete = 1;
           has_dot = 1;
       }
       if(!has_dot){
       for(int i = 0; i < 4; i++){
           if(val == 'T'){
               val = *start;
           }
           if(val != 'T' && *start != val && *start != 'T'){
               same = 0;
               break;
           }
           start += 5;
       }
       if(same){
           if(val == 'X'){
               X_win = 1;
           }else{
               O_win = 1;
           }
       }
       if(X_win){
           outf << "Case #" << cases + 1 << ": X won" << endl;
           continue;
       }else if(O_win){
           outf << "Case #" << cases + 1 << ": O won" << endl;
           continue;
       }
       }

       start = board + 12;
       val = *start;
       same = 1;
       has_dot = 0;
       if(board[3] == '.' || board[6] == '.' || board[9] == '.' || board[12] == '.'){
           not_complete = 1;
           has_dot = 1;
       }
       if(!has_dot){
       for(int i = 0; i < 4; i++){
           if(val == 'T'){
               val = *start;
           }
           if(val != 'T' && *start != val && *start != 'T'){
               same = 0;
               break;
           }
           start -= 3;
       }
       if(same){
           if(val == 'X'){
               X_win = 1;
           }else{
               O_win = 1;
           }
       }
       if(X_win){
           outf << "Case #" << cases + 1 << ": X won" << endl;
           continue;
       }else if(O_win){
           outf << "Case #" << cases + 1 << ": O won" << endl;
           continue;
       }
       }

       if(not_complete){
           outf << "Case #" << cases + 1 << ": Game has not completed" << endl;
       }else{
           outf << "Case #" << cases + 1 << ": Draw" << endl;
       }
    }
}

#endif
