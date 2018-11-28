#include<iostream>
using namespace std;
int main(){
    char c[505],r;
    int i,j,T,t,temp,test=0,ta,tb,pa,pb,num,n,rob;
    cin>>T;
    //cin.getline(c,504);
    while(T--){
        cin>>num;
        ta=tb=t=0;
        pa=pb=1;
        rob=0;
        for(i=0;i<num;i++){
            cin>>r;
            if(r=='O' ||r=='B')rob=(r=='O');
            cin>>n;
            if(rob==0){
                temp=((n>pb)?(n-pb):(pb-n)) + tb +1;
                pb=n;
                if(temp>t) tb=t=temp;
                else tb=t=t+1;
            }
           else{
                temp=((n>pa)?(n-pa):(pa-n)) + ta +1;
                pa=n;
                if(temp>t) ta=t=temp;
                else ta=t=t+1;
            }
        }
        cout<<"Case #"<<(++test)<<": "<<t<<endl;
    }
    return 0;
}
                    
