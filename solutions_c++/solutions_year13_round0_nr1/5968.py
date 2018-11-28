#include <fstream>
#include <iostream>
#include <map>

using namespace std;

int main(){

    map<char,int> mapp;
    mapp['X']=1;
    mapp['O']=-1;
    mapp['.']=-1000;
    mapp['T']=0;
    
    int t;
    ifstream input("input.txt");
    ofstream output("output.txt");
    input>> t;
    
    int l = 1;
    
    char a[4][4];
    
    int xCount =0;
    int tCount =0;
    int oCount =0;
    
    while(l<=t){
        
        output<<"Case #"<< l<< ": ";
        string p;
        string result = "";
        int drawCount=0;
        
        for(int i=0;i<4;i++){
           for(int j=0;j<4;j++){
              input>>a[i][j];
              if(drawCount == 0 && a[i][j] == '.')
                 drawCount = 1;
           }
        }
        
        for(int i=0;i<4;i++){
           
           int rowCount=0;
           int colCount=0;
           int diagCount = 0;
           int diagCount1 =0;
           
           for(int j=0;j<4;j++){
              rowCount+=mapp.find(a[i][j])->second;
              colCount+=mapp.find(a[j][i])->second;
           }
           
           if(rowCount > -500) {
               if((rowCount >= 3 )){
                   result = "X won";
               }else
               if((rowCount <= -3 )){
                   result = "O won";
               }
           }
           
           if(result == "" && colCount > -500) {
                       
                if((colCount >= 3 )){
                   result = "X won";
               }else
               if((colCount <= -3 )){
                   result = "O won";
               }
           }
        }
        
        if(result == ""){
             
             int p = mapp.find(a[0][3])->second + mapp.find(a[1][2])->second + mapp.find(a[2][1])->second + mapp.find(a[3][0])->second;
             int q = mapp.find(a[0][0])->second + mapp.find(a[1][1])->second + mapp.find(a[2][2])->second + mapp.find(a[3][3])->second;
            
            if(p > -500) {
               if( p >=3 ){
                 result = "X won";
               }else
               if( p <= -3){
                 result = "O won";
               }
            }
            if(result == "" && q > -500) {
               if( q >=3 ){
                 result = "X won";
               }else
               if( q <= -3){
                 result = "O won";
               }
            }
        }
        
        if(result != ""){
           output<<result;
        }
        else{
             if(drawCount == 1)
                 output<<"Game has not completed";
             else
                 output<<"Draw";
        }
        
        output<<endl;
        l++;
    }
    
    system("pause");   
}
        
