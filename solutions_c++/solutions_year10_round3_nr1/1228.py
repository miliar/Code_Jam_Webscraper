#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;
int main()
{
    int t,n,i,j,k;
    long a[1000],b[1000],c;
    ofstream f("A.out");
    cin>>t;
    for(i=0;i<t;i++)
    {
                    f<<"Case #"<<(i+1)<<":"<<" ";
                    cin>>n;
                    c=0;
                    for(j=0;j<n;j++)
                    cin>>a[j]>>b[j];
                    for(j=0;j<n;j++)
                    for(k=j+1;k<n;k++)
                    if((a[k]<a[j] && b[k]>b[j]) || (a[k]>a[j] && b[k]<b[j]))
                    c++;
                    f<<c<<"\n";
                    }
                    f.close();
                    getch();
                    }
