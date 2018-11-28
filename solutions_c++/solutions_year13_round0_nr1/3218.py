#include <stdio.h>

#define SOUBOR_VSTUP "A_tic_tac_toe.in"
#define SOUBOR_VYSTUP "A_tic_tac_toe.out"

#define ROZMER 4

int main() {
    FILE *vstup = stdin;
    vstup = fopen(SOUBOR_VSTUP,"r");
    FILE *vystup = stdout;
    vystup = fopen(SOUBOR_VYSTUP,"w");

    char pole[ROZMER][ROZMER];

    int N;
    fscanf(vstup,"%d\n",&N);
    for(int i=1;i<=N;i++) {
        for(int k=0;k<ROZMER;k++) {
            for(int l=0;l<ROZMER;l++) fscanf(vstup,"%c",&pole[k][l]);
            fscanf(vstup,"\n");
        }
        //kontrola jestli nekdo vyhral
        char won = '.';
        int volne = 0;
        int pocetXdiag1=0;
        int pocetXdiag2=0;
        int pocetOdiag1=0;
        int pocetOdiag2=0;
        int pocetTdiag1=0;
        int pocetTdiag2=0;
        for(int k=0;k<ROZMER;k++) {
            if(pole[k][k] == 'X') pocetXdiag1++;
            if(pole[k][ROZMER-k-1] == 'X') pocetXdiag2++;
            if(pole[k][k] == 'O') pocetOdiag1++;
            if(pole[k][ROZMER-k-1] == 'O') pocetOdiag2++;
            if(pole[k][k] == 'T') pocetTdiag1++;
            if(pole[k][ROZMER-k-1] == 'T') pocetTdiag2++;
            int pocetO=0;
            int pocetX=0;
            int pocetT=0;
            int pocetO2=0;
            int pocetX2=0;
            int pocetT2=0;
            for(int l=0;l<ROZMER;l++) {
                if(pole[k][l] == '.') volne++;
                if(pole[k][l] == 'X') pocetX++;
                if(pole[l][k] == 'X') pocetX2++;
                if(pole[k][l] == 'O') pocetO++;
                if(pole[l][k] == 'O') pocetO2++;
                if(pole[k][l] == 'T') pocetT++;
                if(pole[l][k] == 'T') pocetT2++;
            }
            if(pocetX == ROZMER || (pocetX == ROZMER-1 && pocetT>0) || pocetX2 == ROZMER || (pocetX2 == ROZMER-1 && pocetT2>0)) won = 'X';
            else if(pocetO == ROZMER || (pocetO == ROZMER-1 && pocetT>0) || pocetO2 == ROZMER || (pocetO2 == ROZMER-1 && pocetT2>0)) won = 'O';
        }
        if(pocetXdiag1 == ROZMER || (pocetXdiag1 == ROZMER-1 && pocetTdiag1>0) || pocetXdiag2 == ROZMER || (pocetXdiag2 == ROZMER-1 && pocetTdiag2>0)) won = 'X';
        else if(pocetOdiag1 == ROZMER || (pocetOdiag1 == ROZMER-1 && pocetTdiag1>0) || pocetOdiag2 == ROZMER || (pocetOdiag2 == ROZMER-1 && pocetTdiag2>0)) won = 'O';

        if(won == 'X') fprintf(vystup,"Case #%d: X won\n",i);
        else if(won == 'O') fprintf(vystup,"Case #%d: O won\n",i);
        else if(volne>0) fprintf(vystup,"Case #%d: Game has not completed\n",i);
        else fprintf(vystup,"Case #%d: Draw\n",i);

        fscanf(vstup,"\n"); //newline za kazdym testcase
    }

    return 0;
}
