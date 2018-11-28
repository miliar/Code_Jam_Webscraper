# include <stdio.h>

FILE *fin = fopen("lang.in","r");
FILE *fout = fopen("lang.out","w");

void conv(char c)
{
    if(c == 'y') fprintf(fout,"a");
    else
    if(c == 'n') fprintf(fout,"b");
    else
    if(c == 'f') fprintf(fout,"c");
    else
    if(c == 'i') fprintf(fout,"d");
    else
    if(c == 'c') fprintf(fout,"e");
    else
    if(c == 'w') fprintf(fout,"f");
    else
    if(c == 'l') fprintf(fout,"g");
    else
    if(c == 'b') fprintf(fout,"h");
    else
    if(c == 'k') fprintf(fout,"i");
    else
    if(c == 'u') fprintf(fout,"j");
    else
    if(c == 'o') fprintf(fout,"k");
    else
    if(c == 'm') fprintf(fout,"l");
    else
    if(c == 'x') fprintf(fout,"m");
    else
    if(c == 's') fprintf(fout,"n");
    else
    if(c == 'e') fprintf(fout,"o");
    else
    if(c == 'v') fprintf(fout,"p");
    else
    if(c == 'z') fprintf(fout,"q");
    else
    if(c == 'p') fprintf(fout,"r");
    else
    if(c == 'd') fprintf(fout,"s");
    else
    if(c == 'r') fprintf(fout,"t");
    else
    if(c == 'j') fprintf(fout,"u");
    else
    if(c == 'g') fprintf(fout,"v");
    else
    if(c == 't') fprintf(fout,"w");
    else
    if(c == 'h') fprintf(fout,"x");
    else
    if(c == 'a') fprintf(fout,"y");
    else
    if(c == 'q') fprintf(fout,"z");
    else fprintf(fout,"%c",c);
}

int main()
{
    int t, i;
    char ch;
    fscanf(fin,"%d\n",&t);
    for(i=1; i<=t; i++) {
        fprintf(fout,"Case #%d: ",i);
        while(1) {
            fscanf(fin,"%c",&ch);
            conv(ch);
            if(ch == '\n') break;
        }
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
