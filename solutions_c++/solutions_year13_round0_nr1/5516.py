#include<iostream>
#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<list>
#include <stack>

using namespace std;
int main()
{
    int T=0;
    cin>>T;    
    for(int z=1;z<=T;z++)
    {
       string temp;
       getline(cin, temp);    
       char game[4][4];
       bool isDotPresent;      
       for(int i=0; i < 4; i++){
          string str;
          getline(cin, str);
          //find dot in the string
          int found = str.find_first_of('.');
          isDotPresent = (found != string::npos);
          for(int j=0;j<4;j++){
             game[i][j] = str[j];
          }
       }
       map<int, bool>sumOfRowColDiag;
       //check all rows
       for(int i=0; i < 4; i++){
         int sum = game[i][0] + game[i][1] + game[i][2] + game[i][3];
         sumOfRowColDiag[sum] = true;
       }       
       //check all cols
       for(int i=0; i < 4; i++){
         int sum = game[0][i] + game[1][i] + game[2][i] + game[3][i];
         sumOfRowColDiag[sum] = true;
       }
       //two diag.
       int sum = game[0][0] + game[1][1] + game[2][2] + game[3][3];
       sumOfRowColDiag[sum] = true;
       sum = game[0][3] + game[1][2] + game[2][1] + game[3][0];
       sumOfRowColDiag[sum] = true;
       
       if(sumOfRowColDiag.count(352) !=0 || sumOfRowColDiag.count(348) !=0){
           cout<<"Case #"<<z<<": X won"<<endl;                         
       }else if(sumOfRowColDiag.count(316) !=0 || sumOfRowColDiag.count(321) !=0){
           cout<<"Case #"<<z<<": O won"<<endl;  
       }else if(isDotPresent){
           cout<<"Case #"<<z<<": Game has not completed"<<endl;  
       }else{
           cout<<"Case #"<<z<<": Draw"<<endl;  
       }
    }
    return 0;
}
