#include<iostream>
#include<cstdio>
#include<queue>
#include<string>
using namespace std;
int main(){

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    queue<char> presionar;
    char robot;
    queue<int> objO;
    queue<int> objB;
    int casos,ic=1,reglas,O,B,obj,segundos;
    scanf("%d ",&casos);
    while(casos--){
        scanf("%d ",&reglas);
        while(reglas--){
            scanf("%c %d ",&robot,&obj);
            presionar.push(robot);
            if(robot=='O')
                objO.push(obj);
            else
                objB.push(obj);
        }
        O=1;B=1;
        segundos=0;
        char sale='-';
        while(!presionar.empty()){
            if(!objO.empty()){
                //para robot O
                //si esta en su objetivo, presionar
                if(O==objO.front()){
                    if(presionar.front()=='O'){
                        if(sale='-') sale='O';
                    }
                }
                //sino mover hacia su objetivo
                else{
                    //si el objetivo esta a la derecha avanzar
                    if(O<objO.front()) O++;
                    else O--;
                }
            }
            if(!objB.empty()){
                //para robot B
                //si esta en su objetivo, presionar
                if(B==objB.front()){
                    if(presionar.front()=='B'){
                        if(sale='-') sale='B';
                    }
                }
                //sino mover hacia su objetivo
                else{
                    //si el objetivo esta a la derecha avanzar
                    if(B<objB.front()) B++;
                    else B--;
                    //printf("B va a %d   -    ",B);
                }
            }
            if(sale!='-'){
                presionar.pop();
                if(sale=='O')objO.pop();
                if(sale=='B')objB.pop();
                sale='-';
            }
            segundos++;
        }
        printf("Case #%d: %d\n",ic,segundos);
        while(!presionar.empty()) presionar.pop();
        while(!objO.empty()) objO.pop();
        while(!objB.empty()) objB.pop();
        ic++;
    }
    return 0;
}
