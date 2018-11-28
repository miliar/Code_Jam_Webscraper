#include <stdio.h>

int alti[100][100],map[100][100],h,cmpx,cmpy,cnt,set[10001],H,W;

void cmp(int x,int y)
{
    if (h > alti[x][y]) {
        h = alti[x][y];
        cmpx = x;
        cmpy = y;
    }
} 

void fl(int x, int y)
{
    
    h = alti[x][y];
    cmpx = x;
    cmpy = y;
    
    if (x > 0)
        cmp(x-1, y);
    if (y > 0)
        cmp(x, y-1);
    if (y+1 < W)
        cmp(x, y+1);
    if (x+1 < H)
        cmp(x+1, y); 
    
    if (cmpx != x || cmpy != y) {
        if (map[cmpx][cmpy] == 10001) {
            map[cmpx][cmpy] = cnt;
            fl(cmpx,cmpy);
        }
        else
            set[cnt] = set[map[cmpx][cmpy]];
    }
}    

    
//   North, West, East, South.
int main()
{
    int T,casen,i,j,k,c;
    
    FILE *in, *out;
    in = fopen("in.txt", "r");
    out = fopen("out.txt","w");
    
    fscanf(in, "%d", &T);
    for (casen = 1; casen <= T; casen++) {
        fscanf(in,"%d %d",&H, &W);
        
        for (i=0; i<H; i++)
            for( j=0; j<W; j++) {
                fscanf(in,"%d", alti[i]+j);
                map[i][j] = 10001;
            }
        
        cnt = 0;
        
        for (i=0; i<H; i++)
            for (j=0; j<W; j++) 
                if (map[i][j] == 10001) {
                    map[i][j] = cnt;
                    set[cnt] = cnt;
                    fl(i,j);
                    cnt++;
                }
                    
                
                
        
        fprintf(out,"Case #%d:\n",casen);
        printf("case %d\n", casen);
        /*printf("set:");
        for (i=0; i<cnt; i++)
            printf("%d ",set[i]);
        printf("\n");*/
        c = 'a';
        for (i=0; i<cnt; i++)
            if(set[i] == i)
                set[i] = c++;
            else
                set[i] = set[set[i]];
        
        for (i=0; i<H; i++) {
            for(j=0; j<W; j++) {
              //  printf("%7d",map[i][j]);
                fprintf(out,"%c ",set[map[i][j]]);
            }
            fseek(out,-1,SEEK_CUR);
            fprintf(out,"\n");
          //  printf("\n");
        }
    }
    
    fclose(in);
    fclose(out);
    getchar();
}
