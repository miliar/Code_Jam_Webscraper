#include<iostream>
using namespace std;
int main(){
bool isNormal(int,int);
bool isSurprise(int,int);
int t,count=0;
cin>>t;

for(int i=0;i<t;++i){
        int n,s,p;
        cin>>n>>s>>p;
        
        count=0;
        for(int j=0;j<n;++j){
                int m;
                cin>>m;
                
                if(isNormal(m,p))count++;
                else{
                     if(s>0){
                             if(isSurprise(m,p)){
                                                 count++;
                                                 s--;
                                                 }
                             }
                     }
        }
        cout<<"Case #"<<i+1<<": "<<count<<endl;
       
}
}

bool isNormal(int n, int k){
     bool ret=false;
     switch(n){
               case 0:
                    if( k == 0 )
                        ret=true;
                    break;
               case 1:
               case 2:
               case 3:
                    if( k<= 1 )
                        ret=true;
                    break;
               case 4:
               case 5:
               case 6:
                    if( k<=2 )
                        ret=true;
                    break;
               case 7:
               case 8:
               case 9:
                    if( k <= 3 )
                        ret=true;
                    break;
               case 10:     
               case 11:
               case 12:
                   if( k <= 4 )
                        ret=true;
                    break;
               case 13:
               case 14:
               case 15:
                    if( k <= 5 )
                        ret=true;
                    break;
               case 16:
               case 17:
               case 18:
                    if( k <= 6 )
                        ret=true;
                    break;
               case 19:
               case 20:
               case 21:
                    if( k <= 7 )
                        ret=true;
                    break;
               case 22:
               case 23:
               case 24:
                    if( k <= 8 )
                        ret=true;
                    break;
               case 25:
               case 26:
               case 27:
                    if( k <= 9 )
                        ret=true;
                    break;
               case 28:
               case 29:
               case 30:
                    if( k <= 10 )
                        ret=true;
                    break;
                    
     };
     return ret;
}
bool isSurprise(int n, int k){
     bool ret=false;
     switch(n){
               case 3:
               case 2:
               case 4:
                    if( k<=2 )
                        ret=true;
                    break;
               case 5:
               case 6:
               case 7:
                    if(k<=3)
                        ret=true;
                    break;
               case 8:
               case 9:
               case 10:
                    if( k<=4 )
                        ret=true;
                    break;
               case 11:
               case 12:
               case 13:
                    if( k<=5 )
                        ret=true;
                    break;
               case 14:
               case 15:
               case 16:
                    if( k<=6 )
                        ret=true;
                    break;
               case 17:
               case 18:
               case 19:
                    if( k<=7 )
                        ret=true;
                    break;
               case 20:
               case 21:
               case 22:
                    if(k<=8 )
                        ret=true;
                    break;
               case 23:
               case 24:
               case 25:
                    if(k<=9 )
                        ret=true;
                    break;
               case 26:
               case 27:
               case 28:
                    if( k<=10 )
                        ret=true;
                    break;
               
     };
     return ret;
}
