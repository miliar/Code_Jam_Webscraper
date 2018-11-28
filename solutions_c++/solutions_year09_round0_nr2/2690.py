#include <iostream>
#include <limits>
#include <assert.h>
#include <fstream>

using namespace std;

const int INF=numeric_limits<int>::max( );
const int maxX=100, maxY=100;
const int maxAlt=10000;
const int firstBasinNumber=1;

int nX=0,nY=0;
int altsMap[maxX][maxY];
char *basins[maxX][maxY];
const char emptyBasinName=0;//'#';
char basinNames[maxX*maxY];

void getNeighborAlts(int x,int y, int *aNo,int *aWe,int *aEa,int *aSo)
{
    *aNo=*aWe=*aEa=*aSo=INF;
    if (y>=1)       *aNo=altsMap[x][y-1];
    if (y<=nY-2)    *aSo=altsMap[x][y+1];
    if (x>=1)       *aWe=altsMap[x-1][y];
    if (x<=nX-2)    *aEa=altsMap[x+1][y];
}

void init_basins()
{
    memset(basinNames,emptyBasinName,nX*nY);
    for(int y=0;y<nY;++y)
        for (int x=0;x<nX;++x)
            basins[x][y]=&basinNames[x*nY+y];
}


void pack_basins()
{
    char ch='a';
    for (int y=0;y<nY;++y)
        for (int x=0;x<nX;++x)
        {
            if (*basins[x][y]==emptyBasinName)
                *basins[x][y]=ch++;
        }
  //basinNames[nX*nY]=0;
  //cout<<basinNames;
}

void dbg_print_basins(ostream &out)
{
        for (int y=0;y<nY;++y)
        {
            for (int x=0;x<nX;++x)
                out<<(basins[x][y]-basinNames)<<' ';
            out<<'\n';
        }
}


void print_basins(ostream &out)
{
        for (int y=0;y<nY;++y)
        {
            for (int x=0;x<nX;++x)
                out<<*basins[x][y]<<' ';
            out<<'\n';
        }
}


void process()
{
        bool changed=true;
        int aNo,aWe,aEa,aSo;
        while(changed)
        {
            changed=false;
            for (int x=0;x<nX;++x)
                for (int y=0;y<nY;++y)
                {
                    getNeighborAlts(x,y,&aNo,&aWe,&aEa,&aSo);

                    char **bestBass=0;
                    int bestAlt=altsMap[x][y];


                    if (aNo<bestAlt)
                    {
                        bestBass=&basins[x][y-1];
                        bestAlt=aNo;
                    }
                    if (aWe<bestAlt)
                    {
                        bestBass=&basins[x-1][y];
                        bestAlt=aWe;
                    }
                    if (aEa<bestAlt)
                    {
                        bestBass=&basins[x+1][y];
                        bestAlt=aEa;
                    }
                    if (aSo<bestAlt)
                    {
                        bestBass=&basins[x][y+1];
                        bestAlt=aSo;
                    }

                    if (bestBass!=0)
                        if (basins[x][y]!=*bestBass)
                        {
                            //char *minBasName=min(basins[x][y],*bestBass);
                            char *minBasName=(basins[x][y]<*bestBass) ?basins[x][y]:*bestBass;
                            basins[x][y]=*bestBass=minBasName;

                            changed=true;
                            //cout<<"* "<<x<<' '<<y<<'\n';
                            //dbg_print_basins(cout);
                        }
                }
        //print_basins(cout);
        }

}

int main()
{
    cout << "Hello world!" << endl;
    ifstream fin("B-large.in");
    //ostream &fout=cout;
    ofstream fout("output.txt");
    int T;
    fin>>T;
    assert(T>0);
    assert(T<=100);
    for (int t=1;t<=T;++t)
    {
        fout<<"Case #"<<t<<":\n";
        cout<<t<<"=t\n";
        fin>>nY>>nX;
        assert(nY>=1 && nX>=1);
        for (int y=0;y<nY;++y)
            for (int x=0;x<nX;++x)
                fin>>altsMap[x][y];
        init_basins();
        process();
        pack_basins();
        print_basins(fout);
        //cout<<t<<"th map completed\n";
    }
    cout<<"\b\b\b";
    return 0;
}
