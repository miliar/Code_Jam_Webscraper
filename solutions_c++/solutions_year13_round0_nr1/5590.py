#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;

char a[4][4];

char * result[]={" won","Draw","Game has not completed"};

void checkCode(){
     bool incom = true; // True is initialized
     int i,j;
     char fchar;
     
     // check for rows
     for(i=0;i<4;i++){
       fchar = a[i][0];
       if(fchar=='.')
         continue;
       if(fchar=='T'){
           if(a[i][1] == '.')
              continue;
           fchar=a[i][1];
       }
       for(j=1;j<4;j++){
               if ((fchar != a[i][j])&&(a[i][j] != 'T'))
                   break;  
       }
       if(j==4){
          cout<<fchar<<result[0]<<endl;
          return;
       }
     }
     
          
     //check for columns
     for(j=0;j<4;j++){
       fchar = a[0][j];
       if(fchar=='.')
         continue;
       if(fchar=='T'){
           if(a[1][j] == '.')
              continue;
           fchar=a[1][j];
       }
       for(i=1;i<4;i++){
               if ((fchar != a[i][j])&&(a[i][j] != 'T'))
                   break;  
       }
       if(i==4){
          cout<<fchar<<result[0]<<endl;
          return;
       }
     }
     fchar = a[0][0];
     if(fchar=='.')
        goto L1;
     if(fchar=='T'){
         if(a[1][1] == '.')
              goto L1;
         fchar=a[1][1];
     }
     for(i=1;i<4;i++){
         if ((fchar != a[i][i])&&(a[i][i] != 'T'))
                   break;
     }
     if(i==4){
         cout<<fchar<<result[0]<<endl;
         return;
     }
     L1:
     fchar=a[0][3];
     if(fchar=='.')
        goto L2;
     if(fchar =='T'){
        if(a[1][2] == '.')
              goto L2;
        fchar=a[1][2];
     }
     for(i=1;i<4;i++){
         if((fchar!= a[i][3-i]) &&(a[i][3-i] != 'T'))
                   break;
     }
     if(i==4){
        cout<<fchar<<result[0]<<endl;
        return;
     }
     L2:
     for(int i=0;i<4;i++){
             if(strchr(a[i],'.') == NULL){
                    cout<<result[1]<<endl;
                    return;
             }
     }
     cout<<result[2]<<endl;
     return;
}

int main(){
    int T;
    cin>>T;
    int t1=T;
    while(T--){
       for(int i=0;i<4;i++){
          cin>>a[i];
       }
       cout<<"Case #"<<(t1-T)<<": ";
       checkCode();
    }    
    cout<<endl;
    return 0;
}

