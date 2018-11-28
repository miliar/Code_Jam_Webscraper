#include <stdio.h>

int main()
{
    int i,j,k,x, L, D, N, len[15], ans;
    char dic[5000][16], c, line[15][26], find;
    
    FILE *in, *out;
    in = fopen("in.txt","r");
    out = fopen("out.txt","w");
    
    fscanf(in,"%d %d %d\n",&L, &D, &N);
    for (i=0; i<D; i++)
        fscanf(in,"%s\n", dic+i);
    
    for (i=0; i<D; i++)
        printf("%s\n", dic+i);
        
    for (i=1; i<=N; i++) {
        ans = 0;
        
        for (j=0; j<L; j++) {
            c = fgetc(in);
            printf("j = %d %c\n",j,c);
            if (c == '(') {
                len[j] = 0;  
                while (c = fgetc(in))  {
                    if (c == ')')
                        break;
                    line[j][len[j]++] = c;
                    printf("%c",c);
                   
                }
            }
            else {
                line[j][0] = c;
                len[j] = 1;
            }
        }
        fscanf(in,"\n");
        for (j=0; j<D; j++) {
            for (k=0; k<L; k++) {
                find = 0;
                for (x=0; x<len[k]; x++) 
                    if (dic[j][k] == line[k][x]) {
                        find = 1;
                        break;
                    }
                if (!find)
                    break;
            }
            
            if (k == L)
                ans++;
        }
        
        fprintf(out,"Case #%d: %d\n", i, ans);
    }
    fclose(in);
    fclose(out);
     getchar();
}
                    
