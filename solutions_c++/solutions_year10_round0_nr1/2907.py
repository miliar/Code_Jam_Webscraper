#include<iostream>
#include<fstream>
using namespace std;
int pow(int a, int b)
{
    if(b==0)return 1;
    if(b>0) return a*pow(a,b-1);
}
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int t,ans=0,n[20000],k[20000];
    fin>>t;
    for(int i=0;i<t;i++)
    {
        fin>>n[i]>>k[i];
        fout<<"Case #"<<i+1<<':'<<" ";
        ans=pow(2,n[i]);
        if((k[i]+ans)%ans==(ans-1))
        fout<<"ON"<<endl;
        else fout<<"OFF"<<endl;
    }
    return 0;
}
