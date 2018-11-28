#include <stdio.h>
#include <assert.h>
#include <time.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

// [(' ', ' '), ('a', 'y'), ('b', 'h'), ('c', 'e'), ('d', 's'), ('e', 'o'), ('f', 'c'), ('g', 'v'), ('h', 'x'), ('i', 'd'), ('j', 'u'), ('k', 'i'), ('l', 'g'), ('m', 'l'), ('n', 'b'), ('o', 'k'), ('p', 'r'), ('q', 'z'), ('r', 't'), ('s', 'n'), ('t', 'w'), ('u', 'j'), ('v', 'p'), ('w', 'f'), ('x', 'm'), ('y', 'a'), ('z', 'q')]
//clock_t start=clock();
int M[256];
char S[256];

int main() {
	freopen("A.in", "r",stdin);
	freopen("A.out","w",stdout);
	int T,tst=0;
    
    M[int('y')]=int('a');
    M[int('e')]=int('o');
    M[int('q')]=int('z');

    string  s0("ejp mysljylc kd kxveddknmc re jsicpdrysi"),
            t0("our language is impossible to understand"),
            
            s1("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"),
            t1("there are twenty six factorial possibilities"),
            
            s2("de kr kd eoya kw aej tysr re ujdr lkgc jv"),
            t2("so it is okay if you want to just give up");
    
    for(int i=0;i<s0.length();++i){
        if(!M[int(s0[i])]) M[int(s0[i])]=int(t0[i]);
        else {
            if(M[int(s0[i])]!=int(t0[i]))fprintf(stderr,
                "%d %d %d ERR\n",int(s0[i]),
                M[int(s0[i])],int(t0[i]));
        }
    }
    for(int i=0;i<s1.length();++i){
        if(!M[int(s1[i])]) M[int(s1[i])]=int(t1[i]);
        else {
            if(M[int(s1[i])]!=int(t1[i]))fprintf(stderr,
                "%d %d %d ERR\n",int(s1[i]),
                M[int(s1[i])],int(t1[i]));
        }
    }
    for(int i=0;i<s2.length();++i){
        if(!M[int(s2[i])]) M[int(s2[i])]=int(t2[i]);
        else {
            if(M[int(s2[i])]!=int(t2[i]))fprintf(stderr,
                "%d %d %d ERR\n",int(s2[i]),
                M[int(s2[i])],int(t2[i]));
        }
    }
    //for(int i=97;i<97+26;++i)
    //    fprintf(stderr,"%c<->%c\n",(char)i,(char)M[i]);  
    /**
     * The remaining one 
     */
    M[int('z')]=int('q');
    
	scanf("%d",&T);
    gets(S);
	while(T--){
		printf("Case #%d: ",++tst);
		//fprintf(stderr,"Case #%d:\n",tst);
	    string str;
        gets(S);
        //fprintf(stderr,"%s\n",S);
        int i=0;
        while(S[i]!='\0'){
            printf("%c",(char)M[int(S[i])]);
            ++i;
        }
        if(T>0)printf("\n");        
	}
    
	//fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
