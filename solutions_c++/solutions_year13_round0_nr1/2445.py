#include <cstdio>
#include <cstring>
#include <algorithm>
#include<iostream>
#include<fstream.h>
using namespace std;
//Define Global Variables Here


int main() {
    ofstream myfile;
    myfile.open ("AFinSmall.txt");
    int tc; scanf("%d\n", &tc);
    for(int g = 0; g < tc; g++) {
        char s[20];
        char a[4][4];
        bool b[10][2];
        int ti,tj;
        bool check = true;
        for (int i=0; i<10; i++) {
            for (int j=0; j<2; j++) {
                b[i][j] = true;
            }
        }
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                cin>>a[i][j];
                if (a[i][j]=='T') {
                    ti=i;
                    tj=j;
                }
            }
        }
        
        
        
        //X part
        
        a[ti][tj] = 'X';
        
        int countx;
        
        for (int i=0; i<4; i++) {
            countx=0;
            for (int j=0; j<4; j++) {
                if (a[i][j]=='X') {
                    countx++;
                }
            }
            if (countx==4) {
             myfile<<"Case #"<<g+1<<": "<<"X won"<<endl;
                check = false;
                break;
            }
          
        }
        
        for (int i=0; i<4; i++) {
            countx=0;
            for (int j=0; j<4; j++) {
                if (a[j][i]=='X') {
                    countx++;
                }
            }
            if (countx==4) {
                myfile<<"Case #"<<g+1<<": "<<"X won"<<endl;
                check = false;
                break;
            }
            
        }
        
  
        countx=0;
        for (int i=0; i<4; i++) {
            if (a[i][i]=='X') {
                countx++;
            }
        }
        
        if (countx==4) {
            myfile<<"Case #"<<g+1<<": "<<"X won"<<endl;
            check = false;
        }
        
        
         countx=0;
        for (int i=0; i<4; i++) {
            if (a[i][3-i]=='X') {
                countx++;
            }
        }
        
        if (countx==4) {
            myfile<<"Case #"<<g+1<<": "<<"X won"<<endl;
            check = false;
        }
        
     
        
        //O PART
        a[ti][tj] = 'O';

        countx=0;
        
        for (int i=0; i<4; i++) {
            countx=0;
            for (int j=0; j<4; j++) {
                if (a[i][j]=='O') {
                    countx++;
                }
            }
            if (countx==4) {
                myfile<<"Case #"<<g+1<<": "<<"O won"<<endl;
                check = false;
                break;
            }
            
        }
        
        for (int i=0; i<4; i++) {
            countx=0;
            for (int j=0; j<4; j++) {
                if (a[j][i]=='O') {
                    countx++;
                }
            }
            if (countx==4) {
                myfile<<"Case #"<<g+1<<": "<<"O won"<<endl;
                check = false;
                break;
            }
            
        }
        
        
        countx=0;
        for (int i=0; i<4; i++) {
            if (a[i][i]=='O') {
                countx++;
            }
        }
        
        if (countx==4) {
            myfile<<"Case #"<<g+1<<": "<<"O won"<<endl;
            check = false;
        }
        
        
        countx=0;
        for (int i=0; i<4; i++) {
            if (a[i][3-i]=='O') {
                countx++;
            }
        }
        
        if (countx==4) {
            myfile<<"Case #"<<g+1<<": "<<"O won"<<endl;
            check = false;
        }
        
        

        
        
        //OTHER PART
        if (check==true) {
            for (int i=0; i<4 && check==true; i++) {
                for (int j=0; j<4; j++) {
                    if(a[i][j]=='.')
                    {
                        myfile<<"Case #"<<g+1<<": "<<"Game has not completed"<<endl;
                        check = false;
                        break;
                    }
                    
                }
            }
            
        }
        
        
        
        if (check==true) {
            myfile<<"Case #"<<g+1<<": "<<"Draw"<<endl;
            check = false;
        }
        
        
        
        
        
        
                            
                            }
                            return 0;
}
