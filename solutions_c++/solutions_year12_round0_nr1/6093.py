#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;
int main(){
    /*char m[26] = {' '};
    char c[6000];
    char d[6000];
    int number = 3;
    while(number--){
        cin.getline(c, 6000);
        cin.getline(d, 6000);
        int size = strlen(c);
        for(int i = 0; i < size; i++)
            if(c[i] != ' ') m[c[i]-'a'] = d[i];
    }*/
    /*for(int i = 0; i < 26; i++){
        printf("%c ", m[i]);
    }*/
    //q z
    char mm[] = "yhesocvxduiglbkrztnwjpfmaq";
    char line[6000];
    int i = 0;
    int numb = 0;
    while(cin.getline(line, 6000)){
        int size = strlen(line);
        printf("Case #%d: ", ++i);
        for(int j = 0; j < size; j++)
            printf("%c", (line[j] == ' ')? ' ' : mm[line[j] - 'a']);
        printf("\n");
    }
    return 0;
}