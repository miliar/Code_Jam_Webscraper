#include <cstdio>
#include <cstdlib>
#include <vector>
unsigned int T, N, k, j, Time;
std::vector<int> Targets[2];
std::vector<int>::iterator i[2];
bool Order[256];
int Target, Position[2], Dist;
char Bot;
int main(){
    scanf("%u", &T);
    for(k=0;k<T;k++){
        scanf("%u", &N);
        Time=0;
        Targets[0].clear();
        Targets[1].clear();
        for(j=0;j<N;j++){
            Bot=getchar();
            while(Bot!='B'&&Bot!='O') Bot=getchar();
            Order[j]=Bot=='B';
            scanf("%d", &Target);
            Targets[Order[j]].push_back(Target);
        }
        i[0]=Targets[0].begin();
        i[1]=Targets[1].begin();
        Position[0]=Position[1]=1;
        for(j=0;j<N;j++){
            Dist=abs(Position[Order[j]]-*i[Order[j]]);
            Time+=Dist+1;
            Position[Order[j]]=*i[Order[j]];
            i[Order[j]]++;
            if(i[!Order[j]]!=Targets[!Order[j]].end()){
                if(abs(Position[!Order[j]]-*i[!Order[j]])<=Dist+1) Position[!Order[j]]=*i[!Order[j]];
                else if(Position[!Order[j]]<*i[!Order[j]]) Position[!Order[j]]+=Dist+1;
                else Position[!Order[j]]-=Dist+1;
            }
        }
        printf("Case #%u: %d\n", k+1, Time);
    }
    return 0;
}
