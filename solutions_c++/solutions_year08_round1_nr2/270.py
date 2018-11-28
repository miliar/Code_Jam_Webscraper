#include <cstdio>

FILE* in = fopen("bbig.txt", "r");

int nFlav, nCust;
int type[2001];
bool likes[2001][2001];
int noMalt[2001];
bool done[2001];
int maltType[2001];

int getNext(){
    int ret = -1;
    for(int i = 0; i < nCust; i++) if(!done[i]) {
        if(ret == -1 || noMalt[i] < noMalt[ret])
            ret = i;
    }
    return ret;
}

void fixMalt(int type){
    for(int i = 0; i < nCust; i++){
        if(likes[i][type]) noMalt[i]--;
    }
}

bool solve(){
    fscanf(in, "%d", &nCust);
    for(int i = 0; i < nCust; i++){
        for(int j = 0; j < nFlav; j++) likes[i][j] = false;
        done[i] = false;
        int tmp;
        fscanf(in, "%d", &tmp);
        maltType[i] = -1;
        noMalt[i] = 0;
        for(int j = 0; j < tmp; j++){
            int flav, malt;
            fscanf(in, "%d %d", &flav, &malt);
            flav--;
            if(malt == 1) maltType[i] = flav;
            else {
                noMalt[i]++; 
                likes[i][flav] = true;
            }
        }
        //printf("\nPerson %d nomalt %d\n", i, noMalt[i]);
    }
    
    while(true){
        int person = getNext();
        //printf("\nFixing %d -  %d\n", person,  noMalt[person]);
        if(person == -1 || noMalt[person] > 0) break;
        if(maltType[person] == -1) return false;
        //printf("\nBy malting %d\n", maltType[person]);
        done[person] = true;
        type[maltType[person]] = 1;
        fixMalt(maltType[person]);
    }
    
    return true;
}

int main(){
    int c; fscanf(in, "%d", &c);
    for(int i = 1; i <= c; i++){
        printf("Case #%d:", i);
        fscanf(in, "%d", &nFlav);
        for(int j = 0; j < nFlav; j++) type[j] = 0;
        if(!solve()) printf(" IMPOSSIBLE");
        else {
            for(int j = 0; j < nFlav; j++)
                printf(" %d", type[j]);
        }
        printf("\n");
    }
}
