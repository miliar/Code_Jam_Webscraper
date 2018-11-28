#include"iostream"
#include"algorithm"
using namespace std;
struct node{
   int a,b;
}nod[1001];
int cmp(node p,node q){
    return p.a<q.a;
}
int main(){
    int T,N;
    freopen("A-large.in","r",stdin);
    freopen("Alout.txt","w",stdout);
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
       scanf("%d",&N);
       for(int j=0;j<N;j++){
         scanf("%d%d",&nod[j].a,&nod[j].b);
       }
       sort(nod,nod+N,cmp);
     //  for(int j=0;j<N;j++)printf("%d\n",nod[j].b);
       int cnt=0;
       for(int j=0;j<N;j++){
          for(int k=j+1;k<N;k++){
            if(nod[k].b<nod[j].b)cnt++;
          }
       }
       printf("Case #%d: %d\n",i,cnt);
    }
   // system("pause");
    return 0;
}
