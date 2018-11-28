#include <fstream>
using namespace std;

ifstream f("input.in");
ofstream g("output.out");

int ri[]={-1,-1,0,1,1,1,0,-1},rj[]={0,1,1,1,0,-1,-1,-1};

int fsad(int a[][6])
{
    int e=2,i,j,i1,j1,i2,k,e1;
    for(i=1;i<=4&&e>0;++i)
    {
        for(j=1;j<=4&&e>0;++j)
        {
            if(a[i][j]>0)
            {
                for(k=0;k<8;++k)
                {
                    i1=i+ri[k];
                    j1=j+rj[k];
                    if(a[i1][j1]==a[i][j]||a[i1][j1]==0)
                    {
                        e1=1;
                        for(i2=0;i2<2&&e1;++i2)
                        {
                            i1+=ri[k];
                            j1+=rj[k];
                            if(a[i1][j1]!=a[i][j]&&a[i1][j1]!=0) e1=0;
                        }
                        if(e1) e=-a[i][j];
                    }
                }
            }
            else if(a[i][j]==0)
                 {
                     for(k=0;k<8;++k)
                     {
                         i1=i+ri[k];
                         j1=j+rj[k];
                         if(a[i1][j1]==1||a[i1][j1]==2)
                         {
                             e1=a[i1][j1];
                             for(i2=0;i2<2&&e1;++i2)
                             {
                                 i1+=ri[k];
                                 j1+=rj[k];
                                 if(a[i1][j1]!=e1) e1=0;
                             }
                             if(e1) e=-a[i1][j1];
                         }
                     }
                 }
                 else e=1;
        }
    }
    return e;
}

int main()
{
    int i,j,i1,t,a[6][6];
    char c;
    for(i=0;i<6;++i) a[i][0]=a[i][5]=-2;
    for(j=0;j<6;++j) a[0][j]=a[5][j]=-2;
    f>>t;
    for(i=0;i<t;++i)
    {
        for(j=1;j<=4;++j)
        {
            for(i1=1;i1<=4;++i1)
            {
                f>>c;
                switch(c)
                {
                    case 'X':a[j][i1]=1;break;
                    case 'O':a[j][i1]=2;break;
                    case '.':a[j][i1]=-1;break;
                    case 'T':a[j][i1]=0;break;
                }
            }
        }
        /*for(i1=0;i1<6;++i1)
        {
            for(j=0;j<6;++j)g<<a[i1][j]<<" ";
            g<<'\n';
        }*/
        g<<"Case #"<<i+1<<": ";
        switch(fsad(a))
        {
            case -1:g<<"X won";break;
            case -2:g<<"O won";break;
            case 2:g<<"Draw";break;
            default:g<<"Game has not completed";break;
        }
        g<<'\n';
    }
    f.close();
    g.close();
    return 0;
}
