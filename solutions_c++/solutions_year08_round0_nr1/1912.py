#include <iostream>
#include <fstream>
#include <string>
using namespace std;
const int MAXP=100;
const int MAXQ=1000;
string a[MAXQ],s[MAXP],t;
int f[MAXQ][MAXP];
int i,j,k,temp,p,q,n,ii;
int main(){
    ifstream fin("A-small.in");
    ofstream fout("A-small.out");
    fin>>n;
    for(ii=1;ii<=n;ii++){
        memset(f,0,sizeof(f));
        fin>>p;
        getline(fin,t);
        for(i=0;i<p;i++) getline(fin,s[i]);
        
        fin>>q;
        getline(fin,t);        
        for(i=0;i<q;i++) getline(fin,a[i]);
        for(i=1;i<q;i++){
            k=-1;
            temp=1<<30;
            for(j=0;j<p;j++){
                if(a[i]==a[i-1])
                    if(a[i]==s[j]){
                        k=j;
                    }
                    else{
                        f[i][j]=f[i-1][j];
                        if(f[i][j]<temp) temp=f[i][j];                        
                    }    
                else if(a[i]==s[j]){
                         k=j;
                     }
                     else{ 
                         if(a[i-1]==s[j]) f[i][j]=f[i-1][j]+1;
                         else f[i][j]=f[i-1][j];
                         if(f[i][j]<temp) temp=f[i][j];                                              
                     }    
//                cout<<"i="<<i<<" j="<<j<<" "<<f[i][j]<<endl;
//                system("pause");
            }
            if(k>=0) f[i][k]=temp;
//                cout<<"i="<<i<<" j="<<3<<" "<<f[i][3]<<endl;
//                system("pause");
        }
     temp=1<<30;
     if(q==0) temp=0;
     else   
        for(j=0;j<p;j++){
            if(f[q-1][j]<temp && a[p-1]!=s[j]){
                temp=f[q-1][j];
            }    
        }    
//        cout<<"Case #"<<ii<<" "<<temp<<endl;                    
        fout<<"Case #"<<ii<<": "<<temp<<endl;                                              
    }  
//    system("pause");
}      
            

