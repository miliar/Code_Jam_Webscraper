#include <cstdio>
using namespace std;

char alphabnz[100] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char alphabet[100] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main() {

    int numlines;
    scanf("%d\n", &numlines);
    char input[101][101];
    for(int i=0; i<numlines; i++) {
        fgets(input[i], 10000, stdin);
    }
    char output[101][101];
    for(int i=0; i<numlines; i++) {
        printf("Case #%d: ", i+1);
        for(int k=0; k<=100; k++) {
            int position = input[i][k]-'a';
            if(position>=0 && position<=100) {
                output[i][k] = alphabet[position];
                printf("%c", output[i][k]);
            } 
            if(input[i][k] == ' ') {
                output[i][k] = ' ';
                printf(" ");
            }
        }
        printf("\n");
    }


}
