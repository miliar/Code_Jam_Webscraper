#include <iostream>

using namespace std;

int awal,akhir;
int tabelA[3000],tabelB[3000];

int main(){
    freopen("in.txt","r",stdin);
    freopen("outB.txt","w",stdout);
    
    int jlhtestcase;
    int T;
    int NA,NB;
    
    cin>>jlhtestcase;
    
    for (int test=1;test<=jlhtestcase;test++){
    
    memset(tabelA,0,sizeof(tabelA));
    memset(tabelB,0,sizeof(tabelB));
    
    cin>>T;
    cin>>NA>>NB;
    
    int a,b;
    
    for (int i=0;i<NA;i++){
    
        scanf("%d:%d",&a,&b);
        awal = a*60+b;
    
        scanf("%d:%d",&a,&b);
        akhir = a*60+b+T;
        
        tabelA[awal]++;
        tabelB[akhir]--;      
    }
    
    for (int i=0;i<NB;i++){
    
        scanf("%d:%d",&a,&b);
        awal = a*60+b;
    
        scanf("%d:%d",&a,&b);
        akhir = a*60+b+T;
        
        tabelB[awal]++;
        tabelA[akhir]--;       
    }
    
    int jlhA,jlhB,availA,availB;
    jlhA=0;
    jlhB=0;
    
    availA=0;
    availB=0;
    
    for (int i=0;i<24*60;i++){
        availA-=tabelA[i];
        availB-=tabelB[i];
        
        if (availA<0) {jlhA+=-availA; availA = 0;}
        if (availB<0) {jlhB+=-availB; availB = 0;}
//        cout<<i<<" "<<availA<<" "<<availB<<endl;
    }
    
    cout<<"Case #"<<test<<": "<<jlhA<<" "<<jlhB<<endl;
    }
}
