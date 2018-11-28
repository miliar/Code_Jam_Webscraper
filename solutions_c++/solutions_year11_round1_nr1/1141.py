#include<iostream>
using namespace std;

int main(){
    int N;
    cin>>N;
    for(int i=1;i<=N;++i){
        long long num;
        int pd,pg,md,mg;
        bool result=true;
        cin>>num;
        cin>>pd>>pg;
        md=100;mg=100;
        if(pd%4==0)
            md/=4;
        else if(pd%2==0)
            md/=2;
        if(pd%25==0)
            md/=25;
        else if(pd%5==0)
            md/=5;

        if(pg%4==0)
           mg/=4;
        else if(pg%2==0)
            mg/=2;
        if(pg%25==0)
            mg/=25;
        else if(pg%5==0)
            mg/=5;

        if(md>num)
            result=false;

        if(pg==100||pg==0)
        {
            if(pg!=pd)
                result=false;
        }
        
        cout<<"Case #"<<i<<": "<<(result?"Possible":"Broken")<<endl;
    }
    return 0;
}
