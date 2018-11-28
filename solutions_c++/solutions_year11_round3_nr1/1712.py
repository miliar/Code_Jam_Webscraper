//
//  main.cpp
//  gcj
//
//  Created by Amr Elsehemy on 5/21/11.
//  Copyright 2011 inovaton. All rights reserved.
//

#include <iostream>
using namespace std;

char tiles[55][55];
int main (int argc, const char * argv[])
{
    
    freopen("/Users/amr/Desktop/gcj/gcj/data.in", "r", stdin);
    freopen("/Users/amr/Desktop/gcj/gcj/data.txt", "w", stdout);
    
    int T;
    cin >> T;
    for(int t = 1; t <= T ; t++)
    {
        cout <<"Case #"<<t<<":"<<endl;
        
        int R, C;
        cin>> R; cin>>C;
        
        //cout << "Rows : "<<R <<" Cols " << C<<endl;
        int cnt = 0;
        for (int r=0; r <R; r++) {
            for (int c=0; c<C; c++) {
                cin>>tiles[r][c];
                
                if(tiles[r][c] == '#')
                    cnt++;
            }
        }
        
        if(cnt%4!=0)
        {cout<<"Impossible" <<endl;
        continue;
        }
        for (int r=0; r <R-1; r++) {
            for (int c=0; c<C-1; c++) {
                if(tiles[r][c] == '#' && tiles[r+1][c] == '#' &&
                   tiles[r][c+1] == '#' && tiles[r+1][c+1] == '#')
                {
                    tiles[r][c] = '/' ;tiles[r+1][c] = '\\';
                    tiles[r][c+1] = '\\' ;tiles[r+1][c+1] = '/'; 
                }
            }
        }
        
//        for (int r=0; r <R; r++) {
//            for (int c=0; c<C; c++) {
//                cout<<tiles[r][c];
//            }
//            cout<<endl;
//        }

        bool b = true;
        
        for (int r=0; r <R; r++) {
            for (int c=0; c<C; c++) {
                if(tiles[r][c] == '#')
                {
                    b = false;
                }
            }
        }
        
        if(!b)
            cout<<"Impossible"<<endl;
        else
        {
            for (int r=0; r <R; r++) {
                for (int c=0; c<C; c++) {
                    cout<<tiles[r][c];
                }
                cout<<endl;
            }
        }
    }
    return 0;
}
