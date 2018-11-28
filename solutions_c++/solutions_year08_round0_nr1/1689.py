#include <cstdio>
#include <cstring>

using namespace std;

#define INF 0x3f3f3f3f

char buff[105];

int s,q;
char eng[105][105];
char query[1005][1005];

int main(){
    int test;
    gets(buff);
    sscanf(buff,"%d",&test);
    
    for(int t=0;t<test;t++){
        gets(buff);
        sscanf(buff,"%d",&s);
        for(int i=0;i<s;i++)
            gets(eng[i]);
        
        gets(buff);
        sscanf(buff,"%d",&q);
        for(int i=0;i<q;i++)
            gets(query[i]);
        
        int best=-1,bests,nbests;
        
        for(int i=0;i<s;i++){            
            int tope=q;
            for(int j=0;j<q;j++)
                if(strcmp(eng[i],query[j])==0){
                    tope=j;
                    break;
                }
            if(tope>best){
                best=tope;
                bests=i;
            }
        }
        
        int in=0;
        int res=0;
        while(in<q){
            if(strcmp(query[in],eng[bests])==0){
                best=-1,nbests;
                for(int i=0;i<s;i++)if(i!=bests){            
                    int tope=q;
                    for(int j=in;j<q;j++)
                        if(strcmp(eng[i],query[j])==0){
                            tope=j;
                            break;
                        }
                    if(tope>best){
                        best=tope;
                        nbests=i;
                    }
                }
                bests=nbests;
                res++;
            }
            in++;
        }
        printf("Case #%d: %d\n",t+1,res);
        
    }

    return 0;
}
