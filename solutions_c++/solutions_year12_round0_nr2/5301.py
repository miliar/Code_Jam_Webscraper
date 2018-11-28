#include<stdio.h>
#include<stdlib.h>
int counter =0;
int surprize;
typedef struct sstd{
int data;
bool isP;
}*Std;
void setP(Std s,int p){
if(s->data/3>=p){
    s->isP=true;
    counter++;
}
else s->isP=false ;
}
void setSurprize(Std s,int p){
if(!s->isP){
if(s->data%3==0&&s->data!=0){
    if(surprize>0){
         if(((s->data/3)+1)>=p){
            s->isP=true;
            counter++;
            surprize--;
            return;
         }
    }
}
if(s->data%3>=1){
    if(((s->data/3)+1)>=p){
        s->isP=true;
        counter++;
        return;
    }
}
if(s->data%3==2){
    if(surprize>0){
        if(((s->data/3)+2)>=p){
            s->isP=true;
            surprize--;
            counter++;
            return;
        }

    }
}
}
}
Std newPeople(int score){
    Std s = (Std)malloc(sizeof(struct sstd));
    s->data=score;
    s->isP=false;
    return s;
}
int main(){
    int num;
    scanf("%d",&num);
    for(int n=0;n<num;n++){
        counter=0;
    int people,p;
    scanf("%d",&people);
    scanf("%d",&surprize);
    scanf("%d",&p);
    Std d[people];
    for(int i=0;i<people;i++){
        int score;
        scanf("%d",&score);
        d[i]=newPeople(score);
    }
for(int i=0;i<people;i++){
    setP(d[i],p);
}
for(int i=0;i<people;i++)setSurprize(d[i],p);

printf("Case #%d: %d\n",n+1,counter);
}
}
