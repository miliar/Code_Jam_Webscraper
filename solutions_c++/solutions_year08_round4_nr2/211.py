#include <iostream>
#include <fstream>
using namespace std;

int area(int x1,int y1,int x2,int y2,int x3,int y3)
{
    int t,tt;
    if (y1>y2)
    {
        t=x1;x1=x2;x2=t;
        t=y1;y1=y2;y2=t;
    }
    if (y1>y3)
    {
        t=x1;x1=x3;x3=t;
        t=y1;y1=y3;y3=t;
    }    
    if (y2>y3)
    {
        t=x2;x2=x3;x3=t;
        t=y2;y2=y3;y3=t;
    }       
    int b=(y2-y1)*(x3-x1)+(y3-y1)*(x1-x2);
    if (b>0) return b; else return -b;
}
    
int solve(int x1,int y1,int x2,int y2,int y3,int A,int n)
{
    if (y2!=y1){
        int t1=A-(y3-y1)*(x1-x2);
        int t2=y2-y1;
        if (t1%t2==0) 
        {
            int t=t1/t2+x1;
            if (t>=0 && t<=n) return t;
        }
        int t3=-A-(y3-y1)*(x1-x2);
        if (t3%t2==0)
        {
            int t=t3/t2+x1;
            if (t>=0 && t<=n) return t;
        }    
        return -1;
    }
    else
    {
        if ((A==(y3-y1)*(x1-x2)) || (-A==(y3-y1)*(x1-x2))) return 0;
        return -1;
    }    
}

int gcd(int a,int b)
{
    if (a==0) return b;
    if (b==0) return a;
    if (a>b) return gcd(b,a-b); else return gcd(a,b-a);
}
    
int solve1(int a,int b,int c,int d)
{
    int ab=gcd(a,b);
    if (c%ab!=0) return -1;
    int i=0;
    for (i=0;i<b;i++) if ((i*a-c)%b==0) break;
    int x;
    for (x=i;x<=d;x+=b)
    {
        if ((a*x-c)%b==0)
        {
            int y=(a*x-c)/b;
            if (y>=0 && y<=d)
            {
                return x*(d+1)+y;
            }    
        }    
    }
    return -1;    
}    
    
int main()
{
    ifstream fin("B-small-attempt1.in");
    ofstream fout("output2.txt");
    int c,n,m,a;
    int x1,x2,y1,y2,x3,y3,z;
    fin>>c;
    for (int i=1;i<=c;i++)
    {
        int success=0;
        y1=0;x1=0;
        fin>>n>>m>>a;
        if (a>n*m) goto bre;
        for (y2=y1;y2<=m;y2++)
        {
            for (y3=y2;y3<=m;y3++)
            {
                if (y3==0 && y2==0) continue;
                int t1=solve1(y2,y3,a,n);
                int t2=solve1(y2,y3,-a,n);
                if (t1!=-1) {success=1; x3=t1/(n+1); x2=t1%(n+1); goto bre;}
                if (t2!=-1) {{success=1; x3=t2/(n+1); x2=t2%(n+1); goto bre;}}
            }    
        }    
bre:
        if (success==1){    
            fout<<"Case #"<<i<<": "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<endl;
            cout<<"Case #"<<i<<": "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<endl;
        }    
        else{
            fout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
           cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        }    
    }    
    
    fin.close();
    fout.close();
    system("pause");
    return 0;
}    
