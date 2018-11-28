#include <iostream>
#include <math.h>

using namespace std;

int min(int n){
    int r = 1;
    for(int i=0; i<n; i++){
        r = r + r;
    }
    return r;
}

int main()
{

    FILE *input;
    input = fopen("A-large.in","r");

    FILE *output = fopen("output.out","w");

    int cases;
    int aparelhos, stalos;
    bool state = false;

    fscanf(input, "%d", &cases);

    int asd;

    for (int i = 0; i < cases; i++) {
        fscanf(input, "%d %d", &aparelhos, &stalos);

        asd = min(aparelhos);
        if ( stalos == (asd-1) ) {
            state = true;
        } else {
            if ( (stalos+1)%asd == 0) {
                state = true;
            } else {
                state = false;
            }
        }
        //cout <<"Aparelhos:"<<aparelhos<<" "<< stalos << "<stalos  "<<asd-1<<"<exato  resp:"<<(state?"ON":"OFF")<<endl;
        fprintf(output, "Case #%d: %s\n", (i+1), (state?"ON":"OFF"));
    }
    fclose(input);
    fclose(output);
    return 0;
}

