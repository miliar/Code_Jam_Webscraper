#include<iostream.h>
#include<fstream.h>

int main()
{
    ifstream f1;
    f1.open("input.txt");
    ofstream f2;
    f2.open("output.txt");
    int t;
    f1>>t;
    int k=1;
    while(t--)
    {
        long long n,pd,pg;

        f1>>n>>pd>>pg;

        int flag=0;
        if(n>=100){
            flag=1;}
            else{
        for(long long i=1;i<=n;i++){
            if((pd*i)%100==0){
             flag=1;
             break;
            }
        }
            }
        if(pg==100&pd!=100){
            flag=0;
        }
        if(pg==0&pd!=0){
            flag=0;
        }
        if(flag==1){
            f2<<"Case #"<<k<<": Possible\n";
        }
        else {            f2<<"Case #"<<k<<": Broken\n";
        }
        k++;
    }
}



