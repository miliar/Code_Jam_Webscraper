#include<stdio.h>
#include<string.h>
#include<iostream.h>
int l,d, n,x,ii,jj;
char slowa[6000][30];
char testy[510][900];
int main(){
    //wczytanie l,d,n
    cin>>l>>d>>n;
    getchar();
    //wczytanie slow
    for(int i=0; i<d; i++){
     gets(slowa[i]);
     slowa[i][l]=0;
    }
    //
    //for(int i=0; i<d; i++){
    //  cout<<"\n";
    //  for(int j=0; j<l; j++){
    //    cout<<slowa[i][j];
    //  }
    //}        
    //wczytanie testow
    for(int i=0; i<n; i++){
     gets(testy[i]);
     ii=strlen(testy[i]);
     testy[i][ii]=0;
    }    
    /////////////////////////////////////////////
    // sprawdzanie testu
    for(int i=0; i<n; i++){
      //cout<<"test1:\n";
      int tok=0;
      // sprawdzanie 1 slowa
      for(int j=0; j<d; j++){
      //cout<<"slowo "<<j<<endl;
         char bl=0;
         int ok=0;
         int cn=0;
         // sprawdzanie literek
         for(int il=0; il<l; il++){
            bl=slowa[j][il];
              //
              if(testy[i][cn]==40){
                int zk=0;
                while(testy[i][cn]!=41){
                   cn++;
                   if(bl==testy[i][cn]) {zk=1;}
                }
                if(zk==1) { cn++; continue; }
                else {ok=1; cn++; break;}                
              //
              } else {
                if(bl==testy[i][cn]) { cn++; continue; }
                else {ok=1; cn++; break;}
              }
         }
      //
      
      if(ok==0) tok++;
      }    
    cout<<"Case #"<<i+1<<": "<<tok<<endl;
    }
    getchar();
return 0;
}
