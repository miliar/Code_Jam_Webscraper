#include<iostream>
#include<fstream>
#include<stdio.h>
using namespace std;
void selectionsort(int);
void assign(int);
void usebinary();
long int a[1000];
int b[1000];
int sumS,sumP,fsumS,fsumP,maxsumS,n;
main()
{
    ifstream fin;
    ofstream fout("output.txt");
    fin.open("C-small-attempt0.in");
    int t,j,sum;
    fin>>t;
    for(int i=1;i<=t;i++)
    {
        sum=maxsumS=0;
        fin>>n;
        for(j=0;j<n;j++)
            {
                fin>>a[j];
                sum+=a[j];
            }
        if(sum%2==0)
        {
            selectionsort(n);
            assign(0);
            if(maxsumS>0)
                fout<<"Case #"<<i<<": "<<maxsumS<<endl;
            else
            fout<<"Case #"<<i<<": NO"<<endl;
        }
        else
            fout<<"Case #"<<i<<": NO"<<endl;
    }
}
void assign(int i)
{
    if(i!=n-1)
        for(int x=0;x<=1;x++)
        {
            b[i]=x;
            assign(i+1);
        }
    else
        for(int x=0;x<=1;x++)
            {
                b[i]=x;
                usebinary();
            }
}
void usebinary()
{
    sumS=sumP=fsumS=fsumP=0;
    for(int x=0;x<n;x++)
    if(b[x]==0)
    {
        sumS+=a[x];
        fsumS=fsumS^a[x];
    }
    else
    {
        sumP+=a[x];
        fsumP=fsumP^a[x];
    }
    if(fsumS==fsumP&&sumS>maxsumS&&sumP>0)
        maxsumS=sumS;
}

void selectionsort(int n)
{
    int min,i,j,pos;
    for(i=0;i<n;i++)
    {
        min=a[i];
        pos=i;
        for(j=i+1;j<n;j++)
        {
            if(a[j]>min)
            {
                min=a[j];
                pos=j;
            }
        }
        j=a[i];
        a[i]=a[pos];
        a[pos]=j;
    }
}

