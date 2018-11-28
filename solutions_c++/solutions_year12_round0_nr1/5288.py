#include<iostream>
using namespace std;
char sample[3][200];
char result[3][200];
char words[30];
int main(){
    memset(sample, 0, sizeof(sample));
    memset(result, 0, sizeof(result));
    memset(words, 0, sizeof(words));

    strcpy(sample[0], "ejp mysljylc kd kxveddknmc re jsicpdrysi");
    strcpy(sample[1], "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    strcpy(sample[2], "de kr kd eoya kw aej tysr re ujdr lkgc jv");

    strcpy(result[0], "our language is impossible to understand");
    strcpy(result[1], "there are twenty six factorial possibilities");
    strcpy(result[2], "so it is okay if you want to just give up");
    for(int i=0; i<3; i++){
        int len1 = strlen(sample[i]);
    //    printf("%d\n", len1);
        for(int j=0; j<len1; j++){
            if(sample[i][j]!=' '){
                int n = sample[i][j]-'a';
                words[n] = result[i][j];
            }
        }
    }
    words['z'- 'a'] = 'q';
    words['q' - 'a'] = 'z';

    freopen("A-small-attempt2.in", "r", stdin);
    int T;
    scanf("%d", &T);
    char str[300];
    char tmpchar[300];
    char ans[40][300];
    memset(ans, 0, sizeof(ans));
   // getchar(tmpchar);
    gets(tmpchar);
    for(int i=0; i<T; i++){
        memset(str, 0, sizeof(str));

        gets(str);
        int len = strlen(str);
    //    printf("%d %s\n", len, str);
        int begin=0;
        for(int j=0; j<len; j++)
            if(str[j]!=' '){
                begin = j;
                break;
            }

        for(int j=begin; j<len; j++){
            if(str[j]!=' '){
                ans[i][j] = words[str[j]-'a'];
            }
            else
                ans[i][j] = str[j];
        }
      //  printf("%d %s\n", len, str);
      //  strcpy(ans[i], str);
        for(int j=len-1; j>=0; j--){
            if(ans[i][j]!=' '){
                break;
            }
            else
                ans[i][j] = 0;
        }
    }
    freopen("A-small-attempt2.out", "w", stdout);
    for(int i=0; i<T; i++)
        printf("Case #%d: %s\n ", i+1, ans[i]);

  //  while(1);
    return 0;
}
