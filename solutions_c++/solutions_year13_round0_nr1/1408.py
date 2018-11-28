#include<iostream>
#include<conio.h>
#include<vector>
using namespace std;
int main() {
    int count = 0;
    cin>>count;
    int q = 0;
    vector<int> row;
    vector<int> col;
    int diag1;
    int diag2;
    while(q<count) {
                   row.clear();
                   row.resize(4,0);
                   col.clear();
                   col.resize(4,0);
                   diag1 = 0;
                   diag2 = 0;
                   char inp;
                   int output = 0;
                   int intinp;
                   int modinp;
                   int divinp;
                   bool possibleIncomplete = false;
                   for(int i=0; i<16; i++) {
                           cin>>inp;
                           if(inp == 'X') {
                                  intinp = 1;
                           } else if(inp == 'O') {
                                  intinp = -1;
                           } else if(inp == 'T') {
                                  intinp = 10;
                           } else {
                                  possibleIncomplete = true;
                                  intinp = 0;
                           }
                           modinp = i%4;
                           divinp = i/4;
                           row[divinp] = row[divinp] + intinp;
                           if(row[divinp] == 13 || row[divinp] == 4) {
                                          output = 1;
                           } else if(row[divinp] == -4||row[divinp] == 7) {
                                          output = 2;
                           }
                           col[modinp] = col[modinp] + intinp;
                           if(col[modinp] == 13 || col[modinp] == 4) {
                                          output = 1;
                           } else if(col[modinp] == -4||col[modinp] == 7) {
                                          output = 2;
                           }
                           if(modinp==divinp) {
                                              diag1 = diag1 + intinp;
                           }
                           if(modinp + divinp == 3) {
                                              diag2 = diag2 + intinp;
                           }
                           if(diag1 == 13||diag2 == 13|| diag1 == 4|| diag2 == 4) {
                                    output = 1;
                           }
                           if(diag1 == -4||diag2 == -4|| diag1 == 7||diag2 ==7) {
                                    output = 2;
                           }
                   }
                   cout<<"Case #"<<q+1<<": ";
                   if(output == 0) {
                             if(possibleIncomplete) {
                                                    output = 4;
                                                    cout<<"Game has not completed";
                             } else {
                                                    cout<<"Draw";
                                                    output = 3;
                             }
                   }
                   if(output == 1) {
                             cout<<"X won";
                   }
                   if(output == 2) {
                             cout<<"O won";
                   }
                   cout<<endl;
                   q++;
    }
}
