#include<fstream>
using namespace std;
int n,m,i,j,k,l,t,tt;
int c[1000001][2];
long long a[2],b[2];
ifstream fin;
ofstream fout;
long long ans;

void work(long long x,long long y,long long l,long long r)
{
     long long ans1;
     if ((y<l)||(x>r)) {ans1=y-x+1;} else
     if ((x>=l)&&(y<=r)) {ans1=0;} else
     if ((l>=x)&&(r<=y)) {ans1=y-x+1-(r-l+1);} else
     if (x<=l) {ans1=l-x;} else {ans1=y-r;}
     
     ans+=ans1;
}

int main()
{
    int ll;
    c[1][0]=c[1][1]=1;ll=1;
    for (i=2;i<=1000000;i++)
    {
        if (c[i][0]==0) {c[i][0]=i;ll++;}
        c[i][1]=c[i][0]+i-1;
        int kk=c[i][1];
        if (kk>1000000) {kk=1000000;}
        for (j=ll+1;j<=kk;j++) {c[j][0]=i;}
        ll=kk;
    }
    
    fin.open("C-large.in");
    fout.open("c.out");
    fin>>tt;
    long long one=1;
    for (t=1;t<=tt;t++)
    {
        fin>>a[0]>>a[1]>>b[0]>>b[1];ans=0;
        for (i=a[0];i<=a[1];i++)
        {
           work(b[0],b[1],c[i][0],c[i][1]);   
           ans=ans;
        }
        fout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
