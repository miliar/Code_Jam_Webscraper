#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int NMAX = 100;
char str[NMAX];
char str2[NMAX];
char str3[NMAX];

int countZeroes(int n){
    int ans = 0;
    for (int i = 0; i < n; i++){
        if (str[i] == '0')
            ans++;
    }
    return ans;    
}

int removeZeroes(int n){
    int i = 0;
    for (int j = 0; j < n; j++){
        if (str[j] != '0'){
            str2[i++] = str[j];
        }
    }    
    return i;
}

void doTest(){
    memset(str,0,sizeof(str));

    scanf("%s",str);     
    int n = strlen(str);
    for (int i = 0; i < n; i++)
        str3[i] = str[i];
    if (!next_permutation(str,str+n)){        
        for (int i = 0; i < n; i++)
            str[i] = str3[i];
        int zeroes = countZeroes(n);
        int _n = removeZeroes(n);
        /*for (int i = 0; i < _n; i++)
            fprintf(stderr,"%c",str2[i]);
        fprintf(stderr,"\n--\n");*/
        sort(str2,str2+_n);
        /*for (int i = 0; i < _n; i++)
            fprintf(stderr,"%c",str2[i]);
        fprintf(stderr,"\n--\n");*/

        printf("%c",str2[0]);
        for (int i = 0; i <= zeroes; i++){
            printf("0");
        }
        for (int i = 1; i < _n; i++)
            printf("%c",str2[i]);
    }else{
        for (int i = 0; i < n; i++)
            printf("%c",str[i]);
    }
    printf("\n");
}

int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    //freopen("test.err","w",stderr);

    int T;
    scanf("%d",&T);
    int test = 0;
    while (T){
        printf("Case #%d: ",test+1);        
        test++;
        doTest();
        T--;
    }

    return 0;
}