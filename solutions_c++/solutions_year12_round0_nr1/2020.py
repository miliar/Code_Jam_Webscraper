#include<stdio.h>
#include<string.h>
const int bufferlen = 10000000;
char str[bufferlen+1];
int main(){
    FILE *inf1, *inf2;
    inf1 = fopen("a1.txt","r");
    inf2 = fopen("a2.txt","r");
    char c1,c2;
    int map[26];
    memset(map,0,sizeof(map));
    int i,n,t;
    while (fscanf(inf1,"%c",&c1)!=EOF){
           fscanf(inf2,"%c",&c2);
           if (c1==' ')continue;
           map[c1-'a']=c2;
    }
    map['q'-'a']='z';
    map['z'-'a']='q';
    for (i=0;i<26;i++)
        if(map[i]>0)
            printf("%c:\t%c\n",i+'a',map[i]);
        else
            printf("%c:\tnon\n",i+'a');
    fclose(inf1);
    fclose(inf2);

    FILE *inf, *outf;
    inf = fopen("a.in","r");
    outf = fopen("a.out","w");
    fscanf(inf,"%d\n", &n);
    for (t=0;t<n;t++){
        fgets(str,bufferlen,inf);
        fprintf(outf,"Case #%d: ",t+1);
        for (i=0;i<strlen(str);i++)
            if (str[i]==' ' ||str[i]=='\n')
                fprintf(outf,"%c",str[i]);
            else
                fprintf(outf,"%c",map[str[i]-'a']);
    }
    fclose(inf);
    fclose(outf);
}
