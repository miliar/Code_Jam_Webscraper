#include <stdio.h>

char str[100], ma[100][100];

int main(){
    int testnum, n, k, pos, I, J;
    bool B, R;

    scanf("%d", &testnum);
    for(int test = 1;test <= testnum;test++){
        scanf("%d%d", &n, &k);
        for(int i = 0;i < n;i++){
            scanf("%s", str);
            pos = 0;
            for(int j = n - 1;j >= 0;j--){
                if(str[j] == 'R' || str[j] == 'B'){
                    ma[i][pos++] = str[j];
                }
            }
            while(pos < n){
                ma[i][pos++] = '.';
            }
        }
        B = R = false;
        for(int i = 0;i < n;i++){
            for(int j = 0;j < n;j++){
                if(ma[i][j] != '.'){
                    I = i;J = j;
                    while(J < n && J < j + k){
                        if(ma[I][J] == ma[i][j]){
                            J++;
                        }else{
                            break;
                        }
                    }
                    if(J == j + k && (j == 0 || (j > 0 && ma[i][j - 1] != ma[i][j]))){
                        if(ma[i][j] == 'B')
                            B = true;
                        else
                            R = true;
                    }
                    I = i;J = j;
                    while(I < n && I < i + k)
                        if(ma[I][J] == ma[i][j])
                            I++;
                        else
                            break;
                    if(I == i + k && (i == 0 || (i > 0 && ma[i - 1][j] != ma[i][j])))
                        if(ma[i][j] == 'B')
                            B = true;
                        else
                            R = true;
                    I = i;J = j;
                    while(I < n && J < n && I < i + k && J < j + k)
                        if(ma[I][J] == ma[i][j]){
                            I++;J++;
                        }else
                            break;
                    if(I == i + k && J == j + k && (i == 0 || j == 0 || (ma[i - 1][j - 1] != ma[i][j])))
                        if(ma[i][j] == 'B')
                            B = true;
                        else
                            R = true;
                    I = i;J = j;
                    while(I < n && J >= 0 && I < i + k && J > j - k)
                        if(ma[I][J] == ma[i][j]){
                            I++;J--;
                        }else
                            break;
                    if(I == i + k && J == j - k && (i == 0 || j == n - 1 || (ma[i - 1][j + 1] != ma[i][j])))
                        if(ma[i][j] == 'B')
                            B = true;
                        else
                            R = true;
                }
            }
        }
        printf("Case #%d: ", test);
        if(B)
            if(R)
                puts("Both");
            else
                puts("Blue");
        else
            if(R)
                puts("Red");
            else
                puts("Neither");
    }
    return 0;
}
