#include<iostream>
//#include<stdio>

using namespace std; 

int main(){

    int cases;
    cin >> cases; 

    for(int i=0;i<cases;i++){
        int x[4][4]={0};
        int o[4][4]={0};
        char c;
        bool incomp = false;
        bool done = false;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++){
                cin >> c; 
                if(c == 'X') x[j][k]=1;
                if(c == 'O') o[j][k]=1;
                if(c == 'T') { x[j][k]=1; o[j][k]=1;}
                if(c == '.') incomp = true;
            }
      /* for(int j=0;j<4;j++) 
        {
            for(int k=0;k<4;k++)
                cout <<x[j][k]<<" ";
            cout<<endl;
        } */

        for(int j=0;j<4;j++) 
            if(x[j][0]+x[j][1]+x[j][2]+x[j][3] == 4 || x[0][j]+x[1][j]+x[2][j]+x[3][j] == 4)
            {     cout << "Case #"<<i+1<<": X won"<<endl; done=true; break;}
        if(done) continue;
        if(x[0][0]+x[1][1]+x[2][2]+x[3][3] == 4 || x[3][0]+x[2][1]+x[1][2]+x[0][3] == 4)
            {    cout << "Case #"<<i+1<<": X won"<<endl ; done=true;}
        if(done) continue;
       for(int j=0;j<4;j++) 
            if(o[j][0]+o[j][1]+o[j][2]+o[j][3] == 4 || o[0][j]+o[1][j]+o[2][j]+o[3][j] == 4)
            {    cout << "Case #"<<i+1<<": O won"<<endl; done=true; break;}
        if(done) continue;
        if(o[0][0]+o[1][1]+o[2][2]+o[3][3] == 4 || o[3][0]+o[2][1]+o[1][2]+o[0][3] == 4)
            {    cout << "Case #"<<i+1<<": O won"<<endl; done=true;}
        if(done) continue;

        if(incomp)
            cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
        else
            cout<<"Case #"<<i+1<<": Draw"<<endl; 
              
    }
}
