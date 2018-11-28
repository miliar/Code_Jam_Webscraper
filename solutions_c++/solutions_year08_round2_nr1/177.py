#include<iostream>
using namespace std;
int NN;
long long n,a,b,c,d,x0,y0,m,x,y;
long long s[3][3];
int main()
{
    int nt,i,j,k;
    long long total;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>NN;
    for (nt=1;nt<=NN;nt++)
    {
        cin>>n>>a>>b>>c>>d>>x0>>y0>>m;
        memset(s,0,sizeof(s));
        total=0;
        x=x0; y=y0;
        s[x % 3][y % 3]+=1;
        for (i=1;i<n;i++)
        {
            x=(a*x+b) % m;
            y=(c*y+d) % m;
            s[x % 3][y % 3]+=1;
        }
        for (i=0;i<9;i++)
            if (s[i / 3][i % 3]>=3)
                total+=s[i / 3][i % 3]*(s[i / 3][i % 3]-1)*(s[i / 3][i % 3]-2)/6;
        for (i=0;i<9;i++)
            for (j=0;j<9;j++)
                if (i!=j && (((i/3)*2+j/3)%3==0) && ((i%3)*2+(j%3)%3)==0 && s[i /3][i %3]>=2)
                    total+=(s[i / 3][i % 3]*(s[i / 3][i % 3]-1)/2)*s[j /3][j %3];
        for (i=0;i<7;i++)
            for (j=i+1;j<8;j++) 
               for (k=j+1;k<9;k++) if (((i/3+j/3+k/3) %3)==0 && ((i%3+j%3+k%3) %3)==0)
                   total+=s[i/3][i%3]*s[j/3][j%3]*s[k/3][k%3];
        cout<<"Case #"<<nt<<": "<<total<<endl;
    }
    return 0;
}
