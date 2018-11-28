#include<iostream>
#include<fstream>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
using namespace std;


int main(int argc, char** argv)
{    ifstream in;
        ofstream out("o2");
        if(!out) {
        cout << "Error opening output file";
        exit(1);
            }
    in.open(argv[1]);
    if(!in) {
        cout <<"Error opening file!";
        exit(1);
        }
    long long t,n,a[1000],b[1000];

    in>>t;
    for(int i=0;i<t;i++)
    {
    in>>n;
    for(int j=0;j<n;j++)
{
    in>>a[j];
    in>>b[j];
}int ot=0;
    if(n==1){out<<"Case #"<<i+1<<": "<<ot<<endl; goto l1;}
    for(int k=0;k<n;k++)
    {
        for(int u=k+1;u<n;u++)
{
           
    if(a[u]>a[k]&&b[u]>b[k])
    {     }
    else if(a[u]<a[k]&&b[u]<b[k])
    {     }
    else {ot+=1; }
}
}
    out<<"Case #"<<i+1<<": "<<ot<<endl;
l1:    ot=0;

}

    return 0;
}
