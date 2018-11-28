#include<stdio.h>

using namespace std;

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    char arr [10][10];
    int t;
    scanf("%d",&t);
    for (int k = 1;k<=t;k++){
        int found = 0;
        for (int i =0;i<4;i++){
            scanf("%s",arr[i]);
        }
        //horizontal
        for (int i=0;i<4;i++){
            if ((arr[i][0]!='.'&&arr[i][0]==arr[i][1]&&arr[i][1]==arr[i][2]&&(arr[i][3]=='T'||arr[i][3]==arr[i][2]))||(arr[i][1]!='.'&&arr[i][1]==arr[i][2]&&arr[i][2]==arr[i][3]&&(arr[i][0]=='T'||arr[i][0]==arr[i][2]))){
                printf("Case #%d: %c won\n",k,arr[i][2]);
                found = 1;
                break;
            }
        }
        if (found)
            continue;
        //vertical
        for (int i=0;i<4;i++){
            if ((arr[0][i]!='.'&&arr[0][i]==arr[1][i]&&arr[1][i]==arr[2][i]&&(arr[3][i]=='T'||arr[3][i]==arr[2][i]))||(arr[1][i]!='.'&&arr[1][i]==arr[2][i]&&arr[2][i]==arr[3][i]&&(arr[0][i]=='T'||arr[0][i]==arr[3][i]))){
                printf("Case #%d: %c won\n",k,arr[2][i]);
                found = 1;
                break;
            }
        }
        if (found)
            continue;
        //left-right diagonal
        if ((arr[0][0]!='.'&&arr[0][0]==arr[1][1]&&arr[1][1]==arr[2][2]&&(arr[3][3]=='T'||arr[3][3]==arr[0][0]))||(arr[1][1]!='.'&&arr[1][1]==arr[2][2]&&arr[2][2]==arr[3][3]&&(arr[0][0]=='T'||arr[0][0]==arr[3][3]))){
            printf("Case #%d: %c won\n",k,arr[1][1]);
            continue;
        }
        //right-left diagonal
        if ((arr[0][3]!='.'&&arr[0][3]==arr[1][2]&&arr[1][2]==arr[2][1]&&(arr[3][0]=='T'||arr[3][0]==arr[0][3]))||(arr[3][0]!='.'&&arr[3][0]==arr[2][1]&&arr[2][1]==arr[1][2]&&(arr[0][3]=='T'||arr[0][3]==arr[1][2]))){
            printf("Case #%d: %c won\n",k,arr[2][1]);
            continue;
        }
        for (int i=0;i<4;i++){
            for (int j=0;j<4;j++)
                if (arr[i][j]=='.'){
                    printf("Case #%d: Game has not completed\n",k);
                    found = 1;
                    break;
                }
            if (found)
                break;
        }
        if (found)
            continue;
        printf("Case #%d: Draw\n",k);
    }
}
