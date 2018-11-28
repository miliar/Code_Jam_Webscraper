#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;

int T,R;
int X1,Y1,X2,Y2,mx,my;
int ti;

int main()
{
    int i,j,k,l;
    ifstream fin("C-small-attempt0.in");
    FILE* fp=fopen("C_small.txt","w+");
    
    bool cell[110][110];
    bool die,north,west;
    
    fin>>T;
    for(i=0;i<T;++i)
    {
        for(j=0;j<110;++j)
            memset(cell[j],0,sizeof(bool)*110);
        
        fin>>R;
        mx=0;
        my=0;
        for(j=0;j<R;++j)
        {
            fin>>X1>>Y1>>X2>>Y2;
            if(mx<X2)mx=X2;
            if(my<Y2)my=Y2;
            --X1;--Y1;--X2;--Y2;
            for(k=X1;k<=X2;++k)
            for(l=Y1;l<=Y2;++l)
                cell[k][l]=1;
        }
        
        ti=0;
        die=0;
        while(!die)
        {
            ++ti;
            die=1;
            for(j=mx-1;j>=0;--j)
            for(k=my-1;k>=0;--k)
            {
                north=(j>0);
                if(north)north*=(cell[j-1][k]==1);
                west=(k>0);
                if(west)west*=(cell[j][k-1]==1);
                if(north*west==1)
                    cell[j][k]=1;
                else
                    cell[j][k]*=(north||west);
                if(cell[j][k]==1)
                    die=0;
            }
        }
        
        fprintf(fp,"Case #%d: %d\n",i+1,ti);
    }
    return 0;
    
}
