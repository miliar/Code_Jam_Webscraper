#include <stdio.h>

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small.out","w",stdout);
    char in[30] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 
                   'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 
                   'j', 'p', 'f', 'm', 'a', 'q'};
    char input[105];
    int Test;
    scanf("%d",&Test);
    gets(input);
    for(int t=0;t<Test;t++){
        gets(input);
        printf("Case #%d: ", t+1);
        for(int j=0;input[j];j++){
            if(input[j] == ' '){
                printf(" ");
            } else {
                printf("%c", in[input[j] - 'a']);
            }
        }
        printf("\n");
    }
return 0;
}
