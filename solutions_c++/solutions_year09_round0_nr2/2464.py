#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

int Map[102][102];
int Set[100];
char ID[100];
char Attr[102][102];
char Buf[1200000];

int main(int arg, char *argv)
{
    int t;

    fgets(Buf, sizeof(Buf), stdin);
    t=atoi(Buf);
    for(int i=1; i<=t; ++i) {
        int h, w;
        fgets(Buf, sizeof(Buf), stdin);
        char *p=strtok(Buf, " \t\n\r");
        assert(NULL!=p);
        h=atoi(p);
        p=strtok(NULL, " \t\n\r");
        w=atoi(p);      
        assert(h<=100);
        assert(w<=100);
        //printf("%d %d", h, w);       
        for(int j=1; j<=h; ++j) {
            Map[j][0]=100000;
            Map[j][w+1]=100000;
            fgets(Buf, sizeof(Buf), stdin);
            //printf("%d -> %s\n", j, Buf);
            p=strtok(Buf, " \t\n\r");
            for(int k=1; k<=w; ++k) {                
                assert(NULL!=p);
                Map[j][k]=atoi(p);
                Attr[j][k]=0;
                p=strtok(NULL, " \t\n\r");
            }
        }  
        
        for(int k=1; k<=w; ++k) {
            Map[0][k]=100000;
            Map[h+1][k]=100000;                
        }
        
        Attr[1][1]=1;
        int an=1;
        memset(Set, 0, sizeof(Set));
        memset(ID, 0, sizeof(Set));
        for(int j=1; j<=h; ++j) {        
            for(int k=1; k<=w; ++k) {   
                int x=k; 
                int y=j;               
                int min=Map[j][k];
                if((min>Map[j-1][k]) && (j>1)) {
                    min=Map[j-1][k];
                    y=j-1;
                    x=k;
                }
                if((min>Map[j][k-1]) && (k>1)) {
                    min=Map[j][k-1];
                    y=j;
                    x=k-1;
                }
                if((min>Map[j][k+1]) && (k<w)) {
                    min=Map[j][k+1];
                    y=j;
                    x=k+1;
                }
                if((min>Map[j+1][k]) && (j<h)) {
                    min=Map[j+1][k];
                    y=j+1;
                    x=k;
                }                    
                
                if(Attr[j][k]==0) {
                    if(min==Map[j][k]) {
                       Attr[j][k]=an;
                       ++an;
                    }
                    else {
                        if(Attr[y][x]==0) {
                           Attr[j][k]=an;
                           Attr[y][x]=an;
                           ++an;
                        }
                        else {
                            Attr[j][k]=Attr[y][x];
                        }    
                    }
                }
                else {
                    if(min!=Map[j][k]) {
                        if(Attr[y][x]==0) {
                           Attr[y][x]=Attr[j][k];
                        }  
                        else {
                            if(Set[Attr[y][x]]!=Attr[j][k]) {
                                int s;
                                for(s=Attr[y][x]; Set[s]!=0; s=Set[s]);
                                Set[s]=Attr[j][k];
                            } 
                        }                              
                    }
                }                                               
            }
        }           

        printf("Case #%d:\n", i);
        char c='a';
        char pc;
        for(int j=1; j<=h; ++j) {
            for(int k=1; k<=w; ++k) { 
                assert(Attr[j][k]!=0);  
                if(Set[Attr[j][k]]==0) {
                    if(ID[Attr[j][k]]) 
                        pc=ID[Attr[j][k]];
                    else {
                        pc=c;
                        ID[Attr[j][k]]=pc;
                        ++c;             
                    }
                }
                else {
                    int s;
                    for(s=Set[Attr[j][k]]; Set[s]!=0; s=Set[s]);
                    pc=ID[s];
                    if(0==pc) {
                        pc=c;
                        ID[s]=pc;
                        ++c;             
                    }                        
                }                    
                 
                printf("%c ", pc);
            }
            printf("\n");
        } 
    }
    return 0;    
}

