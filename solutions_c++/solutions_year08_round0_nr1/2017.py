#include<iostream>
using namespace std;

typedef struct SearchEngine{
    char name[110];
    int where;
} sen;

typedef struct Queries{
    char name[110];
} quer;

int main(int argc, char** argv){
    int N,S,Q,changes,currentSearch,flag;
    sen sens[110];
    quer query[1010];
    
    scanf("%d",&N);
    for(int n=0;n<N;n++){
        scanf("%d",&S);
        getchar();
        for(int s=0;s<S;s++){
            gets(sens[s].name);
        }
        scanf("%d",&Q);
        getchar();
        for(int q=0;q<Q;q++){
            gets(query[q].name);
        }
        for(int s=0;s<S;s++){
            sens[s].where=100000;
            for(int q=0;q<Q;q++){
                if(!strcmp(sens[s].name,query[q].name)){
                    if(sens[s].where>Q) sens[s].where=q;
                }
            }
        }
        currentSearch=0;
        for(int s=0;s<S;s++){
            if(sens[s].where>sens[currentSearch].where){
                currentSearch=s;
            }
        }
        changes=0;
        for(int q1=1;q1<Q;q1++){
            if(!strcmp(query[q1].name,sens[currentSearch].name)){
                flag=0;
                while((q1<Q) && (!strcmp(sens[currentSearch].name,query[q1].name)) &&
                            (!strcmp(sens[currentSearch].name,query[q1+1].name))){
                        if(q1==(Q-1)) changes++;
                        q1++;
                    }
                for(int s=0;s<S;s++){
                    sens[s].where=100000;
                    for(int q=q1;q<Q;q++){
                        if(!strcmp(sens[s].name,query[q].name)){
                            if(sens[s].where>99999) sens[s].where=q;
                        }
                    }
                }
                for(int s=0;s<S;s++){
                    if(sens[s].where>sens[currentSearch].where){
                        currentSearch=s;
                        flag=1;
                    }
                }
                if(flag) changes++;
            }
        }
        printf("Case #%d: %d\n",n+1,changes);
    }
    return 0;
}
