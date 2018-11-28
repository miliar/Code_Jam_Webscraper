#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    bool a[31],b[31];
    int T,N,K;
    int i;
    
    scanf("%d",&T);
    int j=0;
    do{
        memset(a,0,sizeof(a));//energia
        memset(b,0,sizeof(b));//estado
        a[0]=true;
        scanf("%d %d",&N, &K);
        while(K--){
            for(i=0; i<N; i++){
                //si tiene energia cambiar stado;
                if(a[i]) b[i]=!b[i];
                
                if(i>0){
                    if(b[i-1] && a[i-1]) a[i]=true;
                    else a[i]=false;
                }
                
            }
        }
        printf("Case #%d: ",j+1);
        if( a[N-1] && b[N-1] ) printf("ON");
        else printf("OFF");
        cout<<endl;
        j++;
    } while(j<T);
}
