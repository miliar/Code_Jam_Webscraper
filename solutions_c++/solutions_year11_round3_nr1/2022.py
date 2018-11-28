#include<iostream>
using namespace std;

int main()
{
    int i,j,k,l,r,c,t=0,T,m;
    char A[51][51];
    char ch;
    cin>>T;
    while(T--){
        cin>>r>>c;
        
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                ch='4';
                while((ch!='.')&&(ch!='#'))
                cin>>ch;
                A[i][j]=ch;
            }    
        }
        
        m=0;
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                if(A[i][j]=='#'){
                    if((A[i+1][j]=='#')&&(A[i+1][j+1]=='#')&&(A[i][j+1]=='#')){
                        A[i][j]='/';
                        A[i][j+1]='\\';
                        A[i+1][j]='\\';
                        A[i+1][j+1]='/';    
                    }    
                    else{
                        m=1;    
                        break;
                    }   
                }    
            }    
        if(m==1)
          break;
        }  
    cout<<"Case #"<<(++t)<<":\n";
          
    if(m==0){
        for(i=0;i<r;i++){
            for(j=0;j<c;j++)
                cout<<A[i][j];
            cout<<endl;
            }    
    }
    else{
        cout<<"Impossible\n";    
    }  
}
    
    return 0;
}
