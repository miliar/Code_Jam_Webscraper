#include <iostream>

using namespace std;

typedef struct _myTime{
    int hh;
    int mm;
}myTime;

typedef struct _train{
    bool start; // 是否起始 
    bool a;     // 是否从 A 出发 
    myTime t;
    int id;    
}train;

train trip[500];

int interval;
int num_a,num_b;

myTime time_add( myTime t,int mm ){
       
    t.hh += mm/60;
    t.mm += mm%60;
    t.hh += t.mm/60;
    t.mm %= 60;
    return t;    
}

int cmp( const void *a,const void *b ){
    train ta,tb;
    ta = *(train*)a;
    tb = *(train*)b;
    if( ta.t.hh!=tb.t.hh ) return ta.t.hh - tb.t.hh;
    if( ta.t.mm!=tb.t.mm ) return ta.t.mm - tb.t.mm; 
    return ta.start - tb.start;
}

void see_trip( int pos ){
    printf("%3d ",trip[pos].id);
    if( trip[pos].start ) printf("%6s","Start ");
    else printf("%6s","End ");
    if( trip[pos].a ) cout << "A->B ";
    else cout << "B->A ";
    printf("%2d:%2d\n",trip[pos].t.hh,trip[pos].t.mm);
}

int main(){
    //freopen("out2.txt","w",stdout);
    //freopen("in2.txt","r",stdin);
    
    int i,j;
    int n;
    
    scanf("%d",&n);
    
    for( i=1;i<=n;i++ ){
        scanf("%d",&interval);
        scanf("%d %d",&num_a,&num_b);
        
        int pos = 0;
        for( j=0;j<num_a;j++ ){
            // 从A出发
            trip[pos].a = trip[pos+1].a = 1;
            trip[pos].start = 1;
            trip[pos+1].start = 0;
            trip[pos].id = trip[pos+1].id = pos/2;
            scanf("%d:%d %d:%d",&trip[pos].t.hh,&trip[pos].t.mm,&trip[pos+1].t.hh,&trip[pos+1].t.mm); 
            trip[pos+1].t = time_add(trip[pos+1].t,interval);
            pos += 2;
        }
        for( j=0;j<num_b;j++ ){
            // 从B出发  
            trip[pos].a = trip[pos+1].a = 0;
            trip[pos].start = 1;
            trip[pos+1].start = 0;
            trip[pos].id = trip[pos+1].id = pos/2;
            scanf("%d:%d %d:%d",&trip[pos].t.hh,&trip[pos].t.mm,&trip[pos+1].t.hh,&trip[pos+1].t.mm); 
            trip[pos+1].t = time_add(trip[pos+1].t,interval);
            pos +=2;
         } 
         qsort(&trip[0],pos,sizeof(train),cmp);
         
         // Debug
         //for( j=0;j<pos;j++ ){
         //    see_trip(j);
         //}
         // End of Debug
         
         int add_a=0,add_b=0;
         int arrive_a=0,arrive_b=0;
         
         for( j=0;j<pos;j++ ){
             if( trip[j].start ){ // 火车启动
                 if( trip[j].a ){ // A->B
                     if( arrive_a ){
                         arrive_a--;    
                     } else add_a++;
                 } else {           // B->A
                     if( arrive_b ){
                         arrive_b--;
                     } else add_b++;    
                 }
             } else {               // 火车到站 
                 if( trip[j].a ){ // A->B
                     arrive_b++;
                 } else {           // B->A
                     arrive_a++;   
                 }   
             }
         }
         printf("Case #%d: %d %d\n",i,add_a,add_b);
         
    }
    
    
    
    
    return 0;
}
