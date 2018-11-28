//
//  main.cpp
//  GCJ
//
//  Created by Aleksandra Vorontsova on 4/13/13.
//  Copyright (c) 2013 Aleksandra Vorontsova. All rights reserved.
//

#include <iostream>

int field[4][4];

void read_field() {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            char c;
            scanf("%c", &c);
            if (c == '.')
                field[i][j] = 17;
            if (c == 'O')
                field[i][j] = 1;
            if (c == 'X')
                field[i][j] = -1;
            if (c == 'T')
                field[i][j] = 0;
        }
        scanf("\n");
    }
//    for (int i = 0; i < 4; ++i) {
//        for (int j = 0; j < 4; ++j){
//            printf("%3.d", field[i][j]);
//        }
//        printf("\n");
//    }
}


void check_field(int num) {
    bool empty = false, Owon = false, Xwon = false;
    
    for (int i = 0; i < 4; ++i) {
        int rowsum = 0,columnsum = 0;
        for (int j = 0; j < 4; ++j) {
            rowsum += field[i][j];
            columnsum += field[j][i];
            if (field[i][j] == 17)
                empty = true;
        }
//        printf("%d:: row = %d, column = %d\n", i+1, rowsum, columnsum);
        if (rowsum == 3 || rowsum == 4 || columnsum == 3 || columnsum == 4)
            Owon = true;
        
        if (rowsum == -3 || rowsum == -4 || columnsum == -3 || columnsum == -4)
            Xwon = true;
    }
    
    int maindiag = 0, seconddiag = 0;
    for (int i = 0; i < 4; ++i) {
        maindiag += field[i][i];
        seconddiag += field[i][3-i];
    }
    
    if (maindiag == 3 || maindiag == 4 || seconddiag == 3 || seconddiag == 4)
        Owon = true;
    
    if (maindiag == -3 || maindiag == -4 || seconddiag == -3 || seconddiag == -4)
        Xwon = true;

    if (Xwon)
        printf("Case #%d: X won\n", num);
    if (Owon)
        printf("Case #%d: O won\n", num);
    if (!Xwon && !Owon && !empty) 
         printf("Case #%d: Draw\n", num);
    if (!Xwon && !Owon && empty)
         printf("Case #%d: Game has not completed\n", num);
}

int main(void) {
    freopen("/Users/Alexandret/Downloads/a.in", "r", stdin);
    freopen("/Users/Alexandret/Downloads/a.out", "w", stdout);
    int t;
    scanf("%d\n", &t);
    for (int i = 0; i < t; ++i) {
        read_field();
        check_field(i + 1);
    }
    return 0;
}

