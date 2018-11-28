#include <algorithm>

#include <cstdio>

#include <cstdlib>

#include <cmath>

#include <iostream>

#include <queue>

#include <map>

#include <cstring>

#include <vector>

using namespace std;



#define MAXN 520

int N, M;

int m[MAXN][MAXN];

int width[MAXN][MAXN];

int num[MAXN];



int decode(char c){

        if(c >= '0' && c <= '9')

                return c - '0';

        else

                return c - 'A' + 10;

}



bool isrec(int size, int x, int y){

        //if(size == 1)printf("%d\n", width[x][y]);

        if(x - size + 1 < 0)return false;

        if(width[x][y] < size)return false;

        for(int i = 1; i < size; i++){

                if(width[x-i][y] < size)return false;

                if(m[x - i][y] != (!m[x - i + 1][y]))return false;

                if(m[x - i][y] == 2)return false;

        }

        return true;

}



void clr(int size, int x, int y){

        for ( int i = 0; i < size; i++)

                for ( int j = 0; j < size; ++j)

                        m[x - i][y - j] = 2;

}



void cntwidth(){

        memset(width, 0, sizeof(width));

        for ( int i=0; i<M; ++i){

                if (m[i][0] != 2)

                        width[i][0] = 1;

        }



        for ( int i=0; i<M; ++i){                      // 計算每個橫條

                for ( int j=1; j<N; ++j){



                        if (m[i][j] == 2)

                                width[i][j] = 0;

                        else if (m[i][j] == (!m[i][j - 1]))

                                width[i][j] = width[i][j-1] + 1;

                        else

                                width[i][j] = 1;

                }

        }

}



void find_rec(int size){







        for ( int i = 0; i < M; ++i)

                for ( int j = 0; j < N; ++j) {

                        if(isrec(size, i, j)){

                                num[size]++;

                                clr(size, i, j);

                                cntwidth();

                        }



                }

/*

        for ( int i=0; i<M; ++i){                      // 計算每個橫條

                for ( int j=0; j<N; ++j){

                        printf("%d", width[i][j]);

                }

                printf("\n");

        }*/

}





int main()

{

        int c = 1, cases;

        char tmp[200];

        //freopen("c.in", "r", stdin);

        //freopen("c.txt", "w", stdout);



        scanf("%d", &cases);

        while(cases--){

                memset(num, 0, sizeof(num));

                memset(m, 0, sizeof(m));

                scanf("%d%d", &M, &N);

                for(int i = 0;i < M; i++){

                        scanf("%s", tmp);

                        for(int j = 0;j < (N/4); j++){

                                m[i][4 * j + 0] = (decode(tmp[j]) >> 3) % 2;

                                m[i][4 * j + 1] = (decode(tmp[j]) >> 2) % 2;

                                m[i][4 * j + 2] = (decode(tmp[j]) >> 1) % 2;

                                m[i][4 * j + 3] = (decode(tmp[j]) >> 0) % 2;

                        }

                }



                cntwidth();

                /*

                for(int i = 0;i < M; i++){

                        for(int j = 0;j < N; j++){

                                printf("%d", m[i][j]);

                        }

                        printf("\n");

                }*/

                int s = 0;

                for(int i = min(M, N); i >= 1; i--){

                        find_rec(i);

                        if(num[i] != 0)s++;

                }











                printf("Case #%d: %d\n", c++, s);

                for(int i = min(M, N); i >= 1; i--){

                        if(num[i] != 0)

                                printf("%d %d\n", i, num[i]);

                }



        }

        return 0;

}
