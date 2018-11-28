#include <iostream>
#include <fstream>

using namespace std;

int main(void){

    ifstream fin("test.in");
    ofstream fout("tictactoe.txt");

     char grid[6][6];

    int rows[5][3];
    int cols[5][3];

    int T;
    fin>>T;
    for(int t=1;t<=T;t++){


    int i,j;
    int n=  4;

    for(i=0;i<n;i++){
        for(j=0;j<3;j++){
            rows[i][j] = cols[i][j] =  0;
        }
    }

    int total = 0;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            fin>>grid[i][j];
            if(grid[i][j] == 'O'){
                rows[i][0]++;
                cols[j][0]++;
                total++;
            }
             if(grid[i][j] == 'X'){
                rows[i][1]++;
                cols[j][1]++;
                total++;
            }
             if(grid[i][j] == 'T'){
                rows[i][2]++;
                cols[j][2]++;
                total++;
            }
        }
    }


    int d1[3];
    int d2[3];
    for(i=0;i<3;i++)d1[i]=d2[i]=0;
    for(i=0;i<4;i++){
        if(grid[i][i]=='O'){
            d1[0]++;
        }
        if(grid[i][i]=='X'){
            d1[1]++;
        }
        if(grid[i][i]=='T'){
            d1[2]++;
        }
    }
    for(i=0;i<4;i++){
        if(grid[i][3-i]=='O'){
            d2[0]++;
        }
        if(grid[i][3-i]=='X'){
            d2[1]++;
        }
        if(grid[i][3-i]=='T'){
            d2[2]++;
        }
    }

    bool a =false;
    bool b =false;

    for(i=0;i<n;i++){
      //  cout<<rows[i][0]<<" "<<rows[i][1]<<" "<<rows[i][2]<<" "<<cols[i][0]<<" "<<cols[i][1]<<" "<<cols[i][2]<<endl;
        if(rows[i][0]+rows[i][2]==n){
            a = true;
        }
        if(cols[i][0]+cols[i][2]==n){
            a = true;
        }
        if(rows[i][1]+rows[i][2]==n){
            b = true;
        }
        if(cols[i][1]+cols[i][2]==n){
            b = true;
        }
    }

    if(d1[0]+d1[2]==n||d2[0]+d2[2]==n)a=true;
    if(d1[1]+d1[2]==n||d2[1]+d2[2]==n)b=true;


    fout<<"Case #"<<t<<": ";
    if(a){
        fout<<"O won";
    }else if(b){
        fout<<"X won";
    }else {
        if(total<n*n){
            fout<<"Game has not completed";
        }else fout<<"Draw";
    }
    fout<<endl;

    }

}
