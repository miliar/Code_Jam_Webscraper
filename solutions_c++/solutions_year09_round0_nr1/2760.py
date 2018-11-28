#include <cstdio>
#include <cstring>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int n, d, l;
char words[5000][16];
vector<string> word;
char str[10000];

FILE *in = fopen("input.txt","rt");
FILE *out = fopen("output.txt","wt");

void input(){
    int i;
    fscanf(in,"%d %d %d",&l,&d,&n);
    for( i=0; i<d; i++ ) fscanf(in,"%s", words[i]);
}

void process(){
    string save;
    int i, j, is_open, ans, k, l;
    for( i=0; i<n; i++ ) {
        fscanf(in,"%s", str);
        int temp=strlen(str);
        word.clear(); save=""; is_open = 0;
        for( j=0;j<(int)temp; j++ ) {
            if( str[j] == ')' ) {
                word.push_back( save );
                is_open = 0;
                save.clear();
            } else if( str[j] == '(' ) {
                is_open=1;
            } else if( is_open == 1 ) {
                save += str[j];
            } else {
                save += str[j];
                word.push_back( save );
                save.clear();
            }
        }
        ans = 0;
        for( j=0; j<d; j++ ) {
            int temp = strlen(words[j]);
            for( k=0; k<temp; k++ ){
                int temp2 = word[k].size();
                for( l=0; l<temp2; l++ ) 
                    if( word[k][l] == words[j][k] ) break;
                if( l == temp2 ) break;
            }
            if( k == temp ) ans++;
        }
        fprintf(out,"Case #%d: %d\n", i+1,ans);
    }
}

int main(){
    input();
    process();
    return 0;
}