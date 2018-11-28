#include <string.h>
#include <iostream>

using namespace std;

int main(){
    
    freopen("a.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    char engine[128][1000],queri[1024][1000];
    int panjang1[128],panjang2[128];
    int jlhEngine,jlhQueri;
    int jlhTestcase;
    char cc;
    
    cin>>jlhTestcase;
    
    for (int test=0;test<jlhTestcase;test++){
        
        cin>>jlhEngine;
        while ((cc=getchar())!='\n');
        
        for (int i=0;i<jlhEngine;i++){
            panjang1[i]=0;
            while ((cc=getchar())!='\n'){
                  engine[i][panjang1[i]++]=cc;
            }
            engine[i][panjang1[i]]=0;
            
//           cout<<engine[i]<<endl;        
        }
        cin>>jlhQueri;
//        cout<<jlhQueri;
        
        while ((cc=getchar())!='\n');
    //    cout<<jlhQueri<<endl;
        
        for (int i=0;i<jlhQueri;i++){
            panjang2[i]=0;
            while ((cc=getchar())!='\n'){
                  queri[i][panjang2[i]++]=cc;
            }
            queri[i][panjang2[i]]=0;
            
    //        cout<<queri[i]<<endl;
        }
        
        int now = 0,jlhpindah = -1;
        int maxjarak,ii;
        
        char sama;
        int panjang;
        int tabel[128][1024];
        
              for (int i=0;i<jlhEngine;i++){
                  for (int j=0;j<jlhQueri;j++){
                     sama = 0; 
                     if (panjang1[i]==panjang2[j]){
                        panjang = panjang1[i];
                        
                        for (ii=0;ii<panjang;ii++){
                            if (engine[i][ii]!=queri[j][ii]){
                               break;                              
                            }
                        }                           
                        
                        if (ii==panjang) {
                            sama = 1;              
                        }
                     }
                     
                     tabel[i][j] = sama;
//                     cout<<i<<" "<<j<<" "<<tabel[i][j]<<endl;
                  }
              }
              
              
        int i,j;      
        while (now<jlhQueri){
              jlhpindah++;
              maxjarak = now;
              
              for (i=0;i<jlhEngine;i++){
                  for (j=now;j<jlhQueri;j++){
                      if (tabel[i][j]) break;
                  }
                  if (maxjarak<j) maxjarak = j;
//                  cout<<i<<" "<<j<<endl;
              }
              now = maxjarak;
        }
        
        cout<<"Case #"<<test+1<<": "<<jlhpindah<<endl;
    }
    
    
}
