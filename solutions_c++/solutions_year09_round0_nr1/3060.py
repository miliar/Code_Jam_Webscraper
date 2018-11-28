#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main(){
    int L,D,N,i,j,k,m,c,estado,t;
    string dic[5000],sepa[15];
    string bad,posi,pal,parte;
        
    cin>>L>>D>>N;
    for(i=0;i<D;i++) cin>>dic[i];
    for(i=0;i<N;i++){
        c=0; k=0; estado=0; for(j=0; j<L; j++) sepa[j]="";
        cin>>bad;
        for(j=0; j<bad.size(); j++){
            if(bad[j]=='(') { estado=1; continue;}
            if(bad[j]==')') { estado=0; k++; continue;}
            if(estado==0) sepa[k]+=bad[j],k++;
            if(estado==1) sepa[k]+=bad[j];
        }
        for(j=0; j<D; j++){
            pal=dic[j];
            t=0;
            for(k=0; k<L; k++){
                parte=sepa[k];
                for(m=0; m<parte.size(); m++){
                    if(pal[k]==parte[m]){ t++; break; }
                }    
            }
            if(t==L) c++;
        } 
        cout<<"Case #"<<i+1<<": "<<c<<endl;    
    }
    return 0;
}
