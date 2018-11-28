#include <fstream>

using namespace std;

#define MAXX 100

int elev[MAXX][MAXX];
char lab[MAXX][MAXX+1];
const char alph[]="abcdefghijklmnopqrstuvwxyz";
int al[26]={0};

void pereb(int i, int j, int h, int w, int& l)
{
    int imin=i, jmin=j,minn=20000,x,y;
    if(i-1>=0&&elev[i-1][j]<elev[i][j])
    {
        imin=i-1;
        jmin=j;
        minn=elev[i-1][j];
    }
    if(j-1>=0&&elev[i][j-1]<elev[i][j]&&elev[i][j-1]<minn)
    {
        imin=i;
        jmin=j-1;
        minn=elev[i][j-1];
    }
    if(j+1<w&&elev[i][j+1]<elev[i][j]&&elev[i][j+1]<minn)
    {
        imin=i;
        jmin=j+1;
        minn=elev[i][j+1];
    }
    if(i+1<h&&elev[i+1][j]<elev[i][j]&&elev[i+1][j]<minn)
    {
        imin=i+1;
        jmin=j;
        minn=elev[i+1][j];
    }
    if(imin==i&&jmin==j)
        return;
    if(lab[imin][jmin]!=' ')
    {
        l=0;
        while(alph[l]!=lab[i][j])
            ++l;
        for(x=0;x<h;++x)
            for(y=0;y<w;++y)
            {
                if((i!=x||j!=y)&&lab[x][y]==lab[i][j])
                {
                    lab[x][y]=lab[imin][jmin];
                    al[l]--;
                }
            }
        lab[i][j]=lab[imin][jmin];al[l]--;
        return;
    }
    lab[imin][jmin]=lab[i][j];
    al[l]++;
    pereb(imin,jmin,h,w,l);
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("output.txt");
    int t,h,w,itmp,jtmp,l;
    int i,j,z,x,y;
    fin>>t;
    for(i=0;i<t;++i)
    {
        l=0;
        fin>>h>>w;
        for(j=0;j<h;++j)
            for(z=0;z<w;++z)
            {
                fin>>elev[j][z];
                lab[j][z]=' ';
            }
        for(j=0;j<26;++j)
            al[j]=0;
        for(x=0;x<h;++x)
            for(y=0;y<w;++y)
                if(lab[x][y]==' ')
                {
                    itmp=x;
                    jtmp=y;
                    lab[x][y]=alph[l];
                    al[l]++;
                    pereb(itmp,jtmp,h,w,l);
                    l=0;
                    for(l=0;l<26;++l)
                        if(al[l]==0)
                            break;
                }
        fout<<"Case #"<<i+1<<":\n";
        for(j=0;j<h;++j)
        {
            for(z=0;z<w;++z)
                fout<<lab[j][z]<<" ";
            fout<<endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}
