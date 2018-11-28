#include <cstdio>
#include <queue>

using namespace std;

#define DEPART 0
#define ARRIVE 1
#define A 0
#define B 1

struct state{
    int type;
    int time;
    int side;       
};

bool operator<(const state &a,const state &b){
    //if the time is the same, make sure arrivals are first
    if(a.time==b.time) return a.type<b.type;
    //in other way, just order by time
    return a.time>b.time;
}

int main(){
    int test;
    scanf("%d",&test);
    for(int t=0;t<test;t++){
        int turn,na,nb;
        scanf("%d %d %d",&turn,&na,&nb);
        
        priority_queue<state> pq;
        state temp;
    
        for(int i=0;i<na;i++){
            int a,b,c,d;
            scanf("%d:%d %d:%d",&a,&b,&c,&d);
            temp.type=DEPART;
            temp.side=A;
            temp.time=a*60+b;
            pq.push(temp);
            
            temp.type=ARRIVE;
            temp.side=B;
            temp.time=c*60+d+turn;
            pq.push(temp);
        }
        
        for(int i=0;i<nb;i++){
            int a,b,c,d;
            scanf("%d:%d %d:%d",&a,&b,&c,&d);
            temp.type=DEPART;
            temp.side=B;
            temp.time=a*60+b;
            pq.push(temp);
            
            temp.type=ARRIVE;
            temp.side=A;
            temp.time=c*60+d+turn;
            pq.push(temp);            
        }
        
        int ca,cb,ra,rb;
        ca=cb=0;
        ra=rb=0;
        
        while(!pq.empty()){
            temp=pq.top();
            pq.pop();
            
            //printf("%d %d\n",temp.time,temp.type);
            if(temp.type==ARRIVE){
                if(temp.side==A) ca++;
                else cb++;
            }else{
                if(temp.side==A) {
                    if(ca==0) ra++;
                    else ca--;
                }else{
                    if(cb==0) rb++;
                    else cb--;
                }
            }
        }
        printf("Case #%d: %d %d\n",t+1,ra,rb);
    }
    return 0;
}
