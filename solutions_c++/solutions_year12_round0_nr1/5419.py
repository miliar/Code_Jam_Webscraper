#include <cstdio>
#include <cstring>

using namespace std;

char train_data_input[4][110] = {
    "a zoo",
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

char train_data_output[4][110] = {
    "y qee",
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"
};

char mapchars[255], tmp[110];

int main() {
    for(int i = 0; i < 4; ++i) {
        int l = strlen(train_data_input[i]);
        for(int j = 0; j < l; ++j) {
            mapchars[ (int)train_data_input[i][j] ] = train_data_output[i][j];
        }
    }
    
    mapchars['q'] = 'z';

    int t = 0;
    scanf("%d\n", &t);
    for(int test = 0; test < t; ++test) {
        gets(tmp);
        int l = strlen(tmp);
        printf("Case #%d: ", test+1);
        for(int i = 0; i < l; ++i) {
            if( tmp[i] >= 'a' || tmp[i] <= 'z' )
                printf("%c", mapchars[(int)tmp[i]]);
            else
                printf("%c", tmp[i]);
        }
        printf("\n");
    }
    return 0;
}
