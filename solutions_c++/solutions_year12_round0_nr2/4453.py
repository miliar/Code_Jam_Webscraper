#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int nor[105][3];
int sup[105][3];
main()
{
    int i,j,x,y,z,N,S,p,F,result,m,n;
    ifstream fin("B-small-attempt2.in");
    ofstream fout("B-small-attempt2.out");


    int total;
    fin>>total;
    for(i=1;i<=total;i++)
    {
        //ini
        for(m=0;m<105;m++)
        {
            for(n=0;n<3;n++)
            {
                nor[m][n]=-1;
                sup[m][n]=-1;
            }
        }
        result=0;
        fin>>N>>S>>p;
        cout<<endl<<"N S P is"<<N<<" "<<S<<" "<<p<<endl;
        for(j=0;j<N;j++)
        {
            fin>>F;
            for(x=F/3+3;x>=0;x--)
            {
                for(y=F/3+3;y>=0;y--)
                {
                    for(z=F/3+3;z>=0;z--)
                    {
                        if(x-y>2 || y-z>2 || x-z>2 || z-x>2 || z-y >2 || y-x>2)continue;
                        if(x+y+z==F)
                        {
                            if(x-y==2 || y-z==2 || x-z==2 || z-x==2 || z-y ==2 || y-x==2)
                            {
                                sup[j][0]=x;
                                sup[j][1]=y;
                                sup[j][2]=z;
                            }
                            else
                            {
                                nor[j][0]=x;
                                nor[j][1]=y;
                                nor[j][2]=z;
                            }
                        }
                    }
                }
            }
            cout<<"sup"<<j<<":"<<endl;
            for(x=0;x<3;x++)
            {
                cout<<sup[j][x]<<" ";
            }
            cout<<endl;
            cout<<"nor"<<j<<":"<<endl;
            for(x=0;x<3;x++)
            {
                cout<<nor[j][x]<<" ";
            }
            cout<<endl;
        }

        for(j=0;j<N;j++)
        {
            if(S<=0)break;
            if(nor[j][2]<p)
            {
                if(sup[j][2]>=p)
                {
                    sup[j][0]=-1;
                    sup[j][1]=-1;
                    sup[j][2]=-1;

                    nor[j][0]=-1;
                    nor[j][1]=-1;
                    nor[j][2]=-1;
                    result++;
                    S--;
                }
            }
        }
        for(j=0;j<N;j++)
        {
            if(S>0)
            {
                if(sup[j][2]>=p)
                {
                    S--;
                    result++;
                }
            }
            else
            {
                if(nor[j][2]>=p)
                {
                    result++;
                }
            }
        }
        if(result<0)result=0;
        fout<<"Case #"<<i<<": "<<result<<endl;

    }
    return 0;
}
