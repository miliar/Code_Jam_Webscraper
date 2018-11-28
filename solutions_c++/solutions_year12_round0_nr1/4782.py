#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <vector>

int main(int argc, char** argv) {
    if (argc<3) {
        printf("not enough parameters: %d\n", argc);
        return 0;
    }
    FILE *fp;
    printf("%s\n", argv[1]);

    if ( (fp = fopen( (const char*) argv[1], "r" )) == NULL ) {
        printf("Open Input File ERROR!\n"); 
        return 0;
    }

    std::ofstream ofs(argv[2]);

    int nT;
    char ch[101];
    memset(ch, 0, sizeof(char)*101);

    fscanf(fp, "%d\n", &nT);

    printf("#T: %d\n", nT);


    char enc[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";

    char dec[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

    int lenc = strlen(enc);

    printf("#lenc: %d\n", lenc);

    char translate[26];

    for (int i=0; i<26; ++i) {
        translate[i]=0;
    }
    translate['a'-'a'] = 'y';
    translate['o'-'a'] = 'e';
    translate['z'-'a'] = 'q';

    for (int i=0; i<lenc; ++i) {
        char encch = enc[i], decch = dec[i];
        int offset = encch - 'a';
        translate[offset]=decch;
    }

    int mark[26];
    memset(mark, 0, 26*sizeof(int));
    for (int i=0; i<26; ++i) {
        ++mark[translate[i]-'a'];
    }

    char lostch = '0';
    for (int i=0; i<26; ++i) {
        if (mark[i]==0) {
            lostch = 'a'+i;
        }
    }
    
    for (int i=0; i<26; ++i) {
        if (translate[i]==0) translate[i] = lostch;
    }

    for (int i=0; i<26; ++i) {
        printf("%c ", translate[i]);
    }

    int rv;
    for (int i=0; i<nT; ++i) {
        rv = fscanf(fp, "%[a-z ]\n", ch);
        if(rv>0) { 
            printf("%s\n", ch);
            int sl = strlen(ch);
            for (int j=0; j<sl; ++j) {
                char cc = ch[j];
                if ( (cc>='a') && (cc<='z') ) {
                    ch[j] = translate[ch[j]-'a'];
                } 
            }
            printf("%s\n", ch);
            printf("#sl: %d\n", sl);
        }
        printf("#rv: %d\n", rv);
        printf("#i: %d\n", i);

        ofs<<"Case #"<<i+1<<": "<<ch;
        if (nT!=i+1) ofs<<std::endl;
    }




    ofs.close();

    fclose(fp);
}

