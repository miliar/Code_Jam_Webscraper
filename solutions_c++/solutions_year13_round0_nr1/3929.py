//
//  main.cpp
//  codeJam
//
//  Created by Zurab Kachukhashvili on 4/13/13.
//  Copyright (c) 2013 Zurab Kachukhashvili. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int k;
    ifstream ifs("input.txt");
    ofstream ofs("output.txt");
    ifs>>k;

    char **table=new char*[4];
    for (int i = 0; i< 4; i++) {
        table[i] = new char[4];
    }
    
    for (int q = 0; q < k; q ++)
    {
        for (int i = 0; i< 4; i++) {
            for (int k = 0; k< 4; k++) {
                ifs>>table[i][k];
               // cout<<table[i][k];
            }
            //cout<<endl;
        }
        
        bool gameCanNotBeFinished(false);
        int answer(0);
        int hx(0),ho(0),vo(0),vx(0);
        
        for (int i = 0; i< 4; i++) {
            
            for (int k = 0; k< 4; k++) {
                if (table[i][k] == 'X' || table[i][k] == 'T') {
                    hx++;
                    if (table[i][k] != 'T') ho=0;
                }
                if(table[i][k] == 'O' || table[i][k] == 'T')
                {
                    ho++;
                    if (table[i][k] != 'T')  hx=0;
                }
                if (table[i][k] == '.')
                {
                    ho=0;
                    hx=0;
                    gameCanNotBeFinished=true;
                }
                
                
                
                if (table[k][i] == 'X' || table[k][i] == 'T') {
                    vx++;
                   if (table[k][i] != 'T')  vo=0;
                }
                if(table[k][i] == 'O' || table[k][i] == 'T')
                {
                    vo++;
                if (table[k][i] != 'T') vx=0;
                }
                if (table[k][i] == '.')
                {
                    vo=0;
                    vx=0;
                    gameCanNotBeFinished=true;
                }
                
            }
            
            if (hx == 4 || vx == 4) {
                answer = 1;
                break;
            }
            else if (ho == 4 || vo == 4)
            {
                answer = 2;
                break;
            }
            vo=0;
            vx=0;
            ho=0;
            hx=0;
        }
        
        
        if (answer == 0) {
            int v1x(0),v2x(0),v1o(0),v2o(0);
            for (int i = 0; i<4; i++) {
                if (table[i][i] == 'X' || table[i][i] == 'T') {
                    v1x++;
                }
                if (table[i][i] == 'O' || table[i][i] == 'T')
                {
                    v1o++;
                }
                
                if (table[i][3-i] == 'X' || table[i][3-i] == 'T') {
                    v2x++;
                }
                if (table[i][3-i] == 'O' || table[i][3-i] == 'T')
                {
                    v2o++;
                }
            }
            
            if (v1x == 4 || v2x == 4) {
                answer = 1;
            }
            if (v1o == 4 || v2o == 4)
            {
                answer = 2;
            }
            
        }
        
        ofs<<"Case #"<<q+1<<": ";
        switch (answer) {
            case 0:
                if (gameCanNotBeFinished) {
                    ofs<<"Game has not completed"<<endl;
                }
                else
                {
                    ofs<<"Draw"<<endl;
                }
                break;
                
            case 1:
                ofs<<"X won"<<endl;
                break;
                
            case 2:
                ofs<<"O won"<<endl;
                break;
                
            default:
                ofs<<"damerxa :D"<<endl;
                break;
        }
    }
    return 0;
}

