#include <iostream>
#include <list>
#include <algorithm>
using namespace std;
int main()
{
    int t,n,k,r,i,j,begin=0,end,tmp,num,s=0,ktmp,numst=0;
    long sum=0;
    list<int> coll;
    int a[100];
    cin>>t;
    while(t--){
        num=0;
        //while(cin>>r>>k>>n){
        cin>>r>>k>>n;
        for(i=0;i<n;i++) cin>>a[i];
        for(i=0;i<r;i++){

            begin=numst;end=begin+n;ktmp=k;
            while(ktmp){
                if(num<n){
                ktmp=ktmp-a[begin%n];

                if(ktmp<0) break;
                num++;sum+=a[begin%n];begin++;
                }else break;
            }
            //cout<<"sum: "<<sum<<endl;
            //cout<<"begin: "<<begin<<" ";
            //cout<<"numst: "<<numst<<"num: "<<num<<endl;
            /*begin=numst;end=begin+n;
            for(j=begin;j<end;j++){
                tmp=j%n;
                cout<<a[tmp]<<" ";
            }
            cout<<endl;*/
            numst+=num;
            num=0;
        }
    //}
        cout<<"Case #"<<++s<<": "<<sum<<endl;
        begin=0;numst=0;sum=0;
    }
    return 0;
}
