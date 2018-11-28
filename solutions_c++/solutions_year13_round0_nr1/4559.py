//
//  main.cpp
//  QualifyingA
//
//  Created by Sambhav on 4/13/13.
//  Copyright (c) 2013 Sword Software. All rights reserved.
//

#include <iostream>
#include<fstream>

using namespace std;

int main(int argc, const char * argv[])
{

    ofstream op("/Users/sambhav/Dropbox/codejam/2013/QualifyingA/A-large.op");
	ifstream ip("/Users/sambhav/Dropbox/codejam/2013/QualifyingA/A-large.in");
    
    int T,i,j,k;
    char C[5][5], player;
    bool flag, incomplete;
    
    ip>>T;

    for(i=0;i<T;i++)
    {
        for(j=0;j<4;j++) ip>>C[j];
        
        flag = false;
        incomplete = false;
        
        //Horizontal check
        for(j=0;j<4 && !flag;j++) {
            flag = true;
            player = 'a';
            for (k=0; C[j][k] != '\0'; k++) {
                if (C[j][k] == '.') {
                    flag = false;
                    incomplete = true;
                    break;
                }
                if (player == 'a' && C[j][k] != 'T') player = C[j][k];
                if (C[j][k] != 'T' && C[j][k] != player) flag = false;
                if (C[j][k] == '.') incomplete = true;
            }
        }
        //Vertical check
        for(j=0;j<4 && !flag;j++) {
            flag = true;
            player = 'a';
            for (k=0;k<4;k++) {
                if (C[k][j] == '.') {
                    flag = false;
                    incomplete = true;
                    break;
                }
                if (player == 'a' && C[k][j] != 'T') player = C[k][j];
                if (C[k][j] != 'T' && C[k][j] != player) flag = false;
                if (C[k][j] == '.') incomplete = true;
            }
        }
        //Back Diagonal(\) check
        if (!flag) {
            flag = true;
            player = 'a';
            for (k=0;k<4;k++) {
                if (C[k][k] == '.') {
                    flag = false;
                    incomplete = true;
                    break;
                }
                if (player == 'a' && C[k][k] != 'T') player = C[k][k];
                if (C[k][k] != 'T' && C[k][k] != player) flag = false;
                if (C[k][k] == '.') incomplete = true;
            }
        }
        //Forward Diagonal(/) check
        if (!flag) {
            flag = true;
            player = 'a';
            for (k=0;k<4;k++) {
                if (C[k][3-k] == '.') {
                    flag = false;
                    incomplete = true;
                    break;
                }
                if (player == 'a' && C[k][3-k] != 'T') player = C[k][3-k];
                if (C[k][3-k] != 'T' && C[k][3-k] != player) flag = false;
                if (C[k][3-k] == '.') incomplete = true;
            }
        }
        
        
        if (flag) {
            cout<<"Case #"<<i+1<<": "<<player<<" won\n";
            op<<"Case #"<<i+1<<": "<<player<<" won\n";
        } else if (incomplete) {
            cout<<"Case #"<<i+1<<": "<<"Game has not completed\n";
            op<<"Case #"<<i+1<<": "<<"Game has not completed\n";
        } else {
            cout<<"Case #"<<i+1<<": "<<"Draw\n";
            op<<"Case #"<<i+1<<": "<<"Draw\n";
        }
    }
    op.close();
    ip.close();
    return 0;
}