#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int cc=0;
    int T;
    cin>>T;
    while(T--){
        int N,S,p;
        cin>>N>>S>>p;
        int *sums = new int[N];
        
        for(int i=0;i<N;i++)
            cin>>sums[i];
        
        int sure=0,surp=0,temp,temp2;
        for(int i=0;i<N;i++){
            int rem = sums[i]%3;
            switch(rem){
                case 0:
                     temp = sums[i]/3;
                     if(temp >= p)
                         sure++;
                     else if(temp -1 >= 0 && temp+1>=p)
                         surp++;
                     break;
                case 1:
                     temp=(sums[i]-1)/3;                     
                     if(temp +1 >= p)
                         sure++;
                     break;
                default:
                     temp = (sums[i]+1)/3;
                     temp2 = (sums[i]-2)/3;
                     if(temp-1>=0 && temp >=p)
                         sure++;
                     else if(temp2>=0 && temp2+2>=p)
                         surp++;
                         
            }
        }
        
        int total = sure + min(surp,S);
        ++cc;
        cout<<"Case #"<<cc<<": "<<total<<endl;        
    }
    //system("pause");
    return 0;
}
