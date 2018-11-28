#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <cmath>

int main(){

    std::freopen("large.in", "r", stdin);
    std::freopen("large.out", "w", stdout);

    int t;
    std::scanf("%d", &t);

    for(int i = 0; i < t; i++){

        int numBlue = 0;

        int R, C;
        std::scanf("%d %d\n", &R, &C);
        char grid[R][C];
        for(int j = 0; j < R; j++){
            for(int k = 0; k < C; k++){
                char t;
                if(k == C-1){
                    std::scanf("%c\n",&t);
                }
                else{
                    std::scanf("%c", &t);
                }
                if(t == '#'){
                    numBlue++;
                }
                grid[j][k]=t;

            }

        }

        bool possible = true;

        if(numBlue % 4 != 0){
            possible = false;
        }
        else{

            for(int j = 1; j < R - 1; j++){
                for(int k = 1; k < C - 1; k++){
                    if(grid[j][k]=='#'){
                        possible = false;
                        for(int l = 0; l < 4; l++){
                            int r,c;
                            if(l == 0){ r=j-1;c=k-1; }
                            else if(l == 1){ r=j;c=k-1; }
                            else if(l == 2){ r=j-1;c=k; }
                            else if(l == 3){ r=j;c=k; }

                            int count = 0;
                            if(grid[r][c]=='#'){count++;}
                            if(grid[r+1][c]=='#'){count++;}
                            if(grid[r][c+1]=='#'){count++;}
                            if(grid[r+1][c+1]=='#'){count++;}

                            if(count == 4){
                                grid[r][c] = '/';
                                grid[r][c+1] = '\\';
                                grid[r+1][c] = '\\';
                                grid[r+1][c+1] = '/';
                                possible = true;
                                break;
                            }
                        }
                        if(possible == false){
                            break;
                        }
                    }
                }
                if(possible == false){
                    break;
                }
            }

        }



        std::printf("Case #%d:\n", i+1);
        if(possible){
            for(int j = 0; j < R; j++){
                for(int k = 0; k < C; k++){
                    if(k == C-1){
                        std::printf("%c\n", grid[j][k]);
                    }
                    else{
                        std::printf("%c", grid[j][k]);
                    }
                }
            }
        }
        else{
            std::printf("Impossible\n");
        }

    }

    return 0;

}

