#include <stdio.h>


char result[1024];
int pos=0;
int solve(FILE *f);

int main()
{
    FILE *f=fopen("d:/Google_codejam/task2/data/input.txt","r");
    FILE *fOut=fopen("d:/Google_codejam/task2/data/output.txt","w");
    if(f==NULL)
        return 1;
    int total=4,x;
    fscanf(f,"%d",&total);
    for(int h=0; h<total; h++)
    {
        solve(f);
        fprintf(fOut,"Case #%d: [", h+1);
        for(x=0; x<pos-1;x++)
            fprintf(fOut,"%c, ", result[x]);
        if(pos>0)
            fprintf(fOut,"%c]\n", result[pos-1]);
        else
            fprintf(fOut,"]\n");
    }
    fclose(f);
    fclose(fOut);
}


int solve(FILE *f)
{
    char base[64][3];
    char opposed[64][3];
    int nonBaseCount;
    int opposedCount;
    int spells;
    int x,y,h;

    pos=0;

    fscanf(f,"%d ",&nonBaseCount);
    for(h=0; h<nonBaseCount; h++)
    {
        fscanf(f,"%c%c%c ",&base[h][0],&base[h][1],&base[h][2]);
    }

    fscanf(f,"%d ",&opposedCount);
    for(h=0; h<opposedCount; h++)
        fscanf(f,"%c%c ",&opposed[h][0],&opposed[h][1]);


    fscanf(f,"%d ",&spells);
    for(h=0; h<spells; h++)
    {
        fscanf(f,"%c",&result[pos]);
        pos++;

        //Is baseSpell
        for(x=0; x<nonBaseCount; x++)
        {
            if((result[pos-1]==base[x][0] && result[pos-2]==base[x][1]) || (result[pos-2]==base[x][0] && result[pos-1]==base[x][1]))
            {
                result[pos-2]=base[x][2];
                pos--;
            }
        }



        //Is opposed
        for(x=0; x<opposedCount; x++)
        {
            for(y=pos-2; y>=0; y--)
            {
                if((result[pos-1]==opposed[x][0] && result[y]==opposed[x][1]) || (result[y]==opposed[x][0] && result[pos-1]==opposed[x][1]))
                {
                    pos=0;
                }
            }
        }

    }
}
