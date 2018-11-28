//
//  main.cpp
//  Codejam
//
//  Created by Sorawit Suriyakarn on 4/13/13.
//  Copyright (c) 2013 Sorawit Suriyakarn. All rights reserved.
//

#include <iostream>
#include <cstdio>

int t;
char A[20][20];

void prog()
{
    for(int c=11;c<=14;c++) scanf("%s",A[c]+11);
    
    //for(int c=11;c<=14;c++) { for(int d=11;d<=14;d++) printf("%c ",A[c][d]); printf("\n"); }
    
    for(int c=11;c<=14;c++) for(int d=11;d<=14;d++)
    {
        if( A[c][d] == 'X' )
        {
            for(int i=-1;i<=1;i++) for(int j=-1;j<=1;j++) if( i != 0 or j != 0 )
            {
                bool p = true;
                for(int k=1;k<=3;k++) if( A[c+k*i][d+k*j] != 'X' ) p = false;
                if( p ) { printf("X won\n"); return;}
            }
        }
        if( A[c][d] == 'O' )
        {
            for(int i=-1;i<=1;i++) for(int j=-1;j<=1;j++) if( i != 0 or j != 0 )
            {
                bool p = true;
                for(int k=1;k<=3;k++) if( A[c+k*i][d+k*j] != 'O' ) p = false;
                if( p ) { printf("O won\n"); return;}
            }
        }
        if( A[c][d] == 'T' )
        {
            for(int i=-1;i<=1;i++) for(int j=-1;j<=1;j++) if( i != 0 or j != 0 )
            {
                if( A[c+i][d+j] == 'O' and A[c+2*i][d+2*j] == 'O' and A[c+3*i][d+3*j] == 'O' ) { printf("O won\n"); return;}
                if( A[c+i][d+j] == 'X' and A[c+2*i][d+2*j] == 'X' and A[c+3*i][d+3*j] == 'X' ) { printf("X won\n"); return;}
            }
        }
    }
    
    
    for(int c=11;c<=14;c++) for(int d=11;d<=14;d++) if( A[c][d] == '.' )
    {
        printf("Game has not completed\n");
        return;
    }
    printf("Draw\n");
}

int main(int argc, const char * argv[])
{
    freopen("/Users/thepsint/Desktop/in.txt","r",stdin);
    freopen("/Users/thepsint/Desktop/out.txt","w",stdout);
    //printf("gg\n");
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        printf("Case #%d: ",c);
        prog();
    }

    return 0;
}

