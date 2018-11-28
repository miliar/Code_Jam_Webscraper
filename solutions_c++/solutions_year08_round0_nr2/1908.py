#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;
const int MAXN=100;
int a[2][MAXN][2];
bool vi[2][MAXN];
int i[2],n[2],ans[2];
int hrs,mi,nn,ii,t,j,k,s,flag;
char ch;
bool cmp(int x[2],int y[2]){
    if(x[0]==y[0]) return x[1]>y[1];
    else return x[0]>y[0];
}    
int main(){
    ifstream fin("B-small.in");
    ofstream fout("B-small.out");
    fin>>nn;
    for(ii=1;ii<=nn;ii++){
        memset(a,0,sizeof(a));
        memset(vi,false,sizeof(vi));
        ans[0]=0; ans[1]=0;
        fin>>t;
        fin>>n[0]>>n[1];
      for(k=0;k<2;k++)  
        for(i[k]=0;i[k]<n[k];i[k]++)
            for(j=0;j<2;j++){
                fin>>hrs>>ch>>mi;
                a[k][i[k]][j]=hrs*60+mi;
            }            
//=====================sort=====================
        for(k=0;k<2;k++) 
            for(i[k]=0;i[k]<n[k];i[k]++){
                int mini[2],kk=i[k];
                mini[0]=a[k][i[k]][0]; mini[1]=a[k][i[k]][1];
                for(j=i[k]+1;j<n[k];j++)
                    if(cmp(mini,a[k][j])){ 
                        kk=j; 
                        mini[0]=a[k][j][0]; mini[1]=a[k][j][1];
                    }    
                a[k][kk][0]=a[k][i[k]][0]; a[k][kk][1]=a[k][i[k]][1];
                a[k][i[k]][0]=mini[0]; a[k][i[k]][1]=mini[1];
            }    
//==================sort ending==============
        s=0;
        while(s<n[0]+n[1]){
            for(k=0;k<2;k++)
                for(i[k]=0;i[k]<n[k]&&vi[k][i[k]];i[k]++);
            if(i[0]==n[0]) flag=1;
            else if(i[1]==n[1]) flag=0;
            else if(cmp(a[0][i[0]],a[1][i[1]])) flag=1; else flag=0;
            ans[flag]++;
            vi[flag][i[flag]]=true;
            s++;
          while(i[1-flag]<n[1-flag]){
            while(i[1-flag]<n[1-flag] && (vi[1-flag][i[1-flag]] || a[1-flag][i[1-flag]][0] < a[flag][i[flag]][1]+t)) i[1-flag]++;
            if(i[1-flag]<n[1-flag]){
                vi[1-flag][i[1-flag]]=true;
                s++;
                flag=1-flag;
            }
          }    
        }   
        cout<<"Case #"<<ii<<": "<<ans[0]<<" "<<ans[1]<<endl;     
        fout<<"Case #"<<ii<<": "<<ans[0]<<" "<<ans[1]<<endl;     
        system("pause");
    }        
}    
