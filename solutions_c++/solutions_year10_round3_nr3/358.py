#include<iostream>
using namespace std;

short x[44][44];

int m,n;
bool asd(int xx,int yy,int nn)
{
    int i,j;
    if(xx+nn-1>m)return 0;
    else if(yy+nn-1>n)return 0;
    int d=x[xx][yy];
    if(d==1)d=2;
    else d=1;
    int dd=d;
    for(i=0;i<nn;i++)
    {
        d=dd;
        for(j=0;j<nn;j++)
        {
            if(x[xx+i][yy+j]==0||x[xx+i][yy+j]==d)break;
            d=x[xx+i][yy+j];
        }
        if(dd==1)dd=2;
    else dd=1;
        if(j<nn)break;
    }
    if(i<nn)return 0;
    for(i=0;i<nn;i++)
    {
        for(j=0;j<nn;j++)
        {
            x[xx+i][yy+j]=0;
        }

    }
    return 1;
}
int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
cin>>m>>n;
memset(x,0,sizeof(x));
for(int i=1;i<=m;i++)
{

for(int j=1;j<=n/4;j++)
{
    char s;
    cin>>s;
    if('0'<=s&&s<='9')
    {
        int d=s-'0';
        //cout<<i<<" "<<j<<" "<<d<<endl;
        x[i][(j-1)*4+1]=((d&8)>>3)+1;
        x[i][(j-1)*4+2]=((d&4)>>2)+1;
        x[i][(j-1)*4+3]=((d&2)>>1)+1;
        x[i][(j-1)*4+4]=(d&1)+1;
    }
    else{
    int d=s-'A'+10;
       x[i][(j-1)*4+1]=((d&8)>>3)+1;
        x[i][(j-1)*4+2]=((d&4)>>2)+1;
        x[i][(j-1)*4+3]=((d&2)>>1)+1;
        x[i][(j-1)*4+4]=(d&1)+1;


    }
}
}

int g=m;
if(m>n)g=n;
int aa=0;
int as[34][2];
for(int ii=g;ii>=1;ii--)
{
    int an=0;
    for(int i=1;i<=m;i++)
    {
        for(int j=1;j<=n;j++)
        {
            //cout<<ii<<"=="<<i<<" "<<j<<endl;
            if(x[i][j]==0)continue;
            if(asd(i,j,ii))an++;
            //cout<<an<<"==\n";
        }
    }
    if(an!=0)
    {as[++aa][0]=ii;as[aa][1]=an;}
}
cout<<"Case #"<<i<<": "<<aa<<endl;
for(int i=1;i<=aa;i++)cout<<as[i][0]<<" "<<as[i][1]<<endl;
}

return 0;
}
