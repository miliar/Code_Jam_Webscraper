#include<cstdio>

#define _in "A-large.in"
#define _out "out.txt"




double wp(char* games, int count, int except=-1){
    int sum = 0, matches = 0;
    for(int i = 0; i < count; i++)
        if(games[i]!='.' && i!=except){
            if(games[i]=='1')
                sum++;
            matches++;
        }
        return matches > 0 ? sum/(double)matches : 0.0;
}

double owp(char** games, int count, int index){
    int opponents = 0;
    double sum = 0.0;

    for(int i=0; i<count; i++){
        if(games[index][i]!='.'){
            sum += wp(games[i], count, index);
            opponents+=1;
        }
    }
    return opponents>0 ? sum/opponents: 0.0;
}

double oowp(char** games, int count, int index){
    int opponents = 0;
    double sum = 0.0;

    for(int i=0; i< count; i++){
        if(games[index][i]!='.'){
            sum += owp(games, count, i);
            opponents+=1;
        }
    }
    return opponents>0?sum/opponents: 0.0;
}

double rpi(char** table, int count, int index)
{
    return 0.25*wp(table[index], count) + 0.5*owp(table, count, index) + 0.25*oowp(table, count, index);
}

int main(int argc, void** argv)
{
    FILE *fin, *fout;

    fin = fopen(_in, "r");
    fout = fopen(_out, "w");
    
    int nCases;
    fscanf(fin,"%d", &nCases);
    for(int i = 1; i<=nCases; i++)
    {
        int nCommands;
        fscanf(fin,"%d ", &nCommands);
        
        char** table = new char*[nCommands];
        for(int j=0; j<nCommands; j++)
        {
            table[j] = new char[nCommands];
            fscanf(fin,"%s", table[j]);
        }

        fprintf(fout,"Case #%d:\n", i);
        for(int k=0; k<nCommands; k++)
            fprintf(fout, "%.12lg\n", rpi(table, nCommands, k));

        /*
        for(int k=0; k<nCommands; k++)
            delete[] table[k];
        */
        delete[] table;
        
    }
    

    fclose(fin);
    fclose(fout);
}
