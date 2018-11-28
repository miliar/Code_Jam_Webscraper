#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;

struct train{
    int start,end;
    bool reuse,head;
}A[100],B[100];

int N,T,NA,NB,times,cA,cB;
char s[10];
int i,j;

int cmpST(const void* a,const void*b){
    return ((train*)a)->start - ((train*)b)->start;
}
int cmpED(const void* a,const void*b){
    return ((train*)b)->end - ((train*)a)->end;
}

int Time2Int(char* s){
    int i,t;
    for(i=0;s[i]!=':';i++);
    s[i] = '\0';
    t = atoi(s)*60 + atoi(s+i+1);
}

int main(){
    cin>>N;
    for(times=1;times<=N;times++){
        cA = cB = 0;
        cin>>T>>NA>>NB;
        for(i=0;i<NA;i++){
            cin>>s;
            A[i].start = Time2Int(s);
            cin>>s;
            A[i].end = Time2Int(s);
            A[i].reuse = false;
            A[i].head = true;
        }
        for(i=0;i<NB;i++){
            cin>>s;
            B[i].start = Time2Int(s);
            cin>>s;
            B[i].end = Time2Int(s);
            B[i].reuse = false;
            B[i].head = true;
        }

        qsort(A,NA,sizeof A[0],cmpST);
        qsort(B,NB,sizeof B[0],cmpED);

        for(i=0;i<NA;i++){
            for(j=0;j<NB;j++) if(A[i].start >= B[j].end+T && !B[j].reuse) break;
            if(j!=NB){
                A[i].head = false;
                B[j].reuse = true;
            }
        }
        qsort(A,NA,sizeof A[0],cmpED);
        qsort(B,NB,sizeof B[0],cmpST);

        for(i=0;i<NB;i++){
            for(j=0;j<NA;j++) if(B[i].start >= A[j].end+T && !A[j].reuse) break;
            if(j!=NA){
                B[i].head = false;
                A[j].reuse = true;
            }
        }
        qsort(A,NA,sizeof A[0],cmpST);

/*debug
        printf("T : %d, NA : %d, NB : %d\n",T,NA,NB);
        for(i=0;i<NA;i++) printf("(%02d:%02d, %02d:%02d, %d, %d)\n",A[i].start/60,A[i].start%60,A[i].end/60,A[i].end%60,(A[i].head==1?1:0),(A[i].reuse==1?1:0));
        cout<<endl;
        for(i=0;i<NB;i++) printf("(%02d:%02d, %02d:%02d, %d, %d)\n",B[i].start/60,B[i].start%60,B[i].end/60,B[i].end%60,(B[i].head==1?1:0),(B[i].reuse==1?1:0));
        cout<<endl;
//debug*/
        for(i=cA=0;i<NA;i++) if(A[i].head) ++cA;
        for(i=cB=0;i<NB;i++) if(B[i].head) ++cB;
        printf("Case #%d: %d %d\n",times,cA,cB);
    }
//    system("pause");
    return 0;
}
