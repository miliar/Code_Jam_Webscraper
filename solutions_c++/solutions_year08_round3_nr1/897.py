#include <iostream>
#include <vector>
#include <algorithm>

#define num unsigned int

using namespace std;



struct sLetter{
    num dOccurence;
    num dOffset;
    sLetter(){
        dOccurence = 0;
        dOffset = 0;
    }
};

bool sort_great(int i,int j){
    return (i>j);
}

struct sKey{
    vector<sLetter> dLetters;
};

struct sKeyboard{
    vector<sKey> dKeys;

    bool f;

    sKeyboard(){
        f = false;
    }

    void init(num pKeys, num pChars){
        num i, j;
        for(i = 0; i < pKeys; i++){
            sKey lCur;
            for(j = 0; j < pChars; j++){
                lCur.dLetters.push_back(sLetter());
            }
            dKeys.push_back(lCur);
        }
    }

    void addLetter(num pLetter){
        num i, j;
        for(i = 0; i < dKeys.size(); i++){

            for(j = 0; j < dKeys[i].dLetters.size(); j++){


                if(
                !(dKeys[i].dLetters[j].dOffset == 0)
                ){
                    num k;
                    for(k = i; k < dKeys.size(); k++){
                        if(dKeys[k].dLetters[j].dOffset == 0){
                            dKeys[k].dLetters[j].dOffset = j+1;
                            dKeys[k].dLetters[j].dOccurence = pLetter;
                            //printf(".. Adding %d to key %d offset %d\n", dKeys[i+1].dLetters[j].dOccurence, i+1, dKeys[i+1].dLetters[j].dOffset);
                            return;
                        }
                    }
                }

                if(dKeys[i].dLetters[j].dOffset == 0){
                    dKeys[i].dLetters[j].dOffset = j + 1;
                    dKeys[i].dLetters[j].dOccurence = pLetter;
                    //printf(".. Adding %d to key %d offset %d\n", dKeys[i].dLetters[j].dOccurence, i, dKeys[i].dLetters[j].dOffset);
                    return;
                }


            }
        }
    }
};

struct sCase{
    num P, K, L;

    vector<num> dLetters;

    sKeyboard lResult;

    void genLayout(){
        sort(dLetters.begin(), dLetters.end(), sort_great);
        num l;
        for(l = 0; l < L; l++){
            //printf("%d ", dLetters[l]);
            lResult.addLetter(dLetters[l]);
            //printf("\n");
        }
    }

    sCase(){
        scanf("%d%d%d", &P, &K, &L);
        num l;
        lResult.init(K, P);
        for(l = 0; l < L; l++){
            num lCur;
            cin >> lCur;
            dLetters.push_back(lCur);
        }
        genLayout();
    }

    void fOutput(){
        num i, j, lRes;
        lRes = 0;
        for(i = 0; i < lResult.dKeys.size(); i++){
            for(j = 0; j < lResult.dKeys[i].dLetters.size(); j++){
                //printf("Key %d Letter %d (%d)\n", i, j, lResult.dKeys[i].dLetters[j].dOccurence);
                lRes += lResult.dKeys[i].dLetters[j].dOccurence * lResult.dKeys[i].dLetters[j].dOffset;
            }
        }
        printf("%d", lRes);
    }
};

int main(){
    num C,c;
    scanf("%d", &C);
    for(c = 1; c <= C; c++){
        sCase lCur;
        printf("Case #%d: ", c);
        lCur.fOutput();
        printf("\n");
    }
    return 0;
}
