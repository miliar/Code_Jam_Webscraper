#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;
int main()
{
    int T;
    //ifstream cin("in.txt");
   // ifstream cin("A-large.in");
   // ofstream cout("A-large.out");
   cin>>T;
    for(int i=1;i<=T;++i){
        int n;
        cin>>n;
        char co;
        int num,preo=1,preos=0,preb=1,prebs=0,sum=0;
        for(int j=0;j<n;++j){
           cin>>co>>num;
           if(co=='O'){
               if(abs(num-preo)<=sum-preos)
               {
                   sum+=1;
                   preo=num;
                   preos=sum;
               }
               else{
                   sum+=(abs(num-preo)-sum+preos+1);
                   preo=num;
                   preos=sum;
               }
           }
           else{
               if(abs(num-preb)<=sum-prebs)
               {
                   sum++;
                   preb=num;
                   prebs=sum;
               }
               else{
                   sum+=(abs(num-preb)-sum+prebs+1);
                   preb=num;
                   prebs=sum;
               }
           }


    }
    cout<<"Case #"<<i<<": ";
    cout<<sum<<endl;
    }
    return 0;
}




