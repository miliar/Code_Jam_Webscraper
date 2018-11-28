#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<fstream>
#include<iostream>
using namespace std;
int rotate(int num,int k)
{
return (num%10)*k+(num/10);
}
int main()
{
ifstream in ("C:/Users/Mohit/Desktop/C-small-attempt0.in");
ofstream out("C:/Users/Mohit/Desktop/output.txt");
int a,b,t;
in>>t;
for(int i =1;i<=t;i++)
{
    int f[200000]={0};
    in >> a;
    in >> b;
    out<<"Case #"<<i<<": ";
    if(b<=9 && b>=0)
    out<<"0";
    else if(b<=99 && b>=10)
    {
    int p=0;
    for(int i=a;i<=b;i++)
    {
        int num=i,c=1,k=2;
        if(f[num]==1)
        continue;
        else
        {
        f[num]=1;
        while(k-1!=0)
        {
        num = rotate(num,10);
        if(num>=a&&num<=b&&f[num]==0)
        {
        f[num]=1;
        c+=1;
        }
        k--;
        }
        }
        if(c>1)
        p+=(c*(c-1))/2;
    }
        out<<p;
}
    else if(b<=999 && b>=100)
    {
    int p=0;
    for(int i=a;i<=b;i++)
    {
        int prev,num=i,c=1,k=3;
        if(f[num]==1)
        continue;
        else
        {
        f[num]=1;
        while(k-1!=0)
        {
        num = rotate(num,100);
        if(num>=a&&num<=b&&f[num]==0)
        {
        f[num]=1;
        c+=1;
        }
        k--;
        }
        }
        if(c>1)
        p+=(c*(c-1))/2;
    }
        out<<p;
}

    else if(b<=9999 && b>=1000)
    {
    int p=0;
    for(int i=a;i<=b;i++)
    {
        int num=i,c=1,k=4;
        if(f[num]==1)
        continue;
        else
        {
        f[num]=1;
        while(k-1!=0)
        {
        num = rotate(num,1000);
        if(num>=a&&num<=b&&f[num]==0)
        {
        f[num]=1;
        c+=1;
        }
        k--;
        }
        }
        if(c>1)
        p+=(c*(c-1))/2;
    }
        out<<p;
}
    else if(b<=99999 && b>=10000)
    {
    int p=0;
    for(int i=a;i<=b;i++)
    {
        int prev,num=i,c=1,k=5;
        if(f[num]==1)
        continue;
        else
        {
        f[num]=1;
        while(k-1!=0)
        {
        num = rotate(num,10000);
        if(num>=a&&num<=b&&f[num]==0)
        {
        f[num]=1;
        c+=1;
        }
        k--;
        }
        }
        if(c>1)
        p+=(c*(c-1))/2;
    }
        out<<p;
}

else if(b<=999999 && b>=100000)
    {
    int p=0;
    for(int i=a;i<=b;i++)
    {
        int prev,num=i,c=1,k=6;
        if(f[num]==1)
        continue;
        else{
            f[num]=1;
        while(k-1!=0)
        {
        num = rotate(num,100000);
        if(num>=a&&num<=b&&f[num]==0)
        {
        f[num]=1;
        c+=1;
        }
        k--;
        }
        }
        if(c>1)
        p+=(c*(c-1))/2;
    }
        out<<p;
}

else if(b<=2000000 && b>=1000000)
    {
    int p=0;
    for(int i=a;i<=b;i++)
    {
        int num=i,c=1,k=7;
        if(f[num]==1)
        continue;
        else
        {
        f[num]=1;
        while(k-1!=0)
        {
        num = rotate(num,1000000);
        if(num>=a&&num<=b&&f[num]==0)
        {
        f[num]=1;
        c+=1;
        }
        k--;
        }
        }
        if(c>1)
        p+=(c*(c-1))/2;
    }
        out<<p;
}
out<<endl;
}

}


