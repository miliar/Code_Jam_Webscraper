#include<iostream>
#include<cstring>
#include<fstream>
#include<algorithm>
#include<conio.h>
using namespace std;

int numdig(int g)
{int ans=0;
    while(g>0)
    {
        g=g/10;
        ans++;
    }
    return ans;
}
string perm2[2]={"01","10"};
string perm3[3]={"012","201","120"};

int gennum(int g, string f,int &y)
{
    int a[3];
    a[2]=g%10;g=g/10;
    a[1]=g%10;g=g/10;
    a[0]=g;
y=(a[(int)f.at(0)-48]*100)+(a[(int)f.at(1)-48]*10)+a[(int)f.at(2)-48];
if(a[(int)f.at(0)-48]==0)
{
y=0;
}
return 1;
}
int genperm(int k,int perm[])
{
    if(numdig(k)==1)
    {
        return 0;
    }
    else if(numdig(k)==2)
    {
        perm[0]=k;
        perm[1]=((k%10)*10)+(k/10);
    return 2;
    }
    else if(numdig(k)==3)
    {
        int casa=0;
        perm[0]=k;
        for(int i=0;i<3;i++)
        {
        gennum(k,perm3[i],perm[i]);

        }
        return 3;
    }
}
int checkon(int a,int b,int n)
{
    if(n>=a&&n<=b)
    return 1;
    return 0;
}
int findnum(int a,int b)
{
    int sum=0;
    for(int i=a;i<=b;i++)
    {if(i==1000)
    {continue;}
                if(numdig(i)==2&&i%10==0){
        continue;}
        int perm[6];
        int t=genperm(i,perm);

        if(t!=0)
        {
            for(int k=1;k<t;k++)
                {

                    if(checkon(a,b,perm[k])==1&&perm[k]!=i)
                    {
                       sum++;
                    }

            }
        }
    }
return sum/2;
}
int main()
{
ifstream gaba("input.txt");
ofstream baga("output.txt");
    int t;
    gaba>>t;
for(int i=0;i<t;i++)
    {
    int a,b,c;
    gaba>>a>>b;
    if(a==b){c=0;}
    else{
      c=findnum(a,b);
    }
 baga<<"Case #"<<i+1<<": "<<c;
 if(i!=t-1)
 {
     baga<<"\n";
 }
    }
}
