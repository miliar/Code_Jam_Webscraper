#include <fstream>

using namespace std;

class Pool {
    public:
    int alt;
    int endx;
    int endy;
};

int main()
{
    //N, W, E, S
    ifstream f;
    ofstream g;
    int H,W,x,y,k,l, flag, min, T, r=0;
    Pool p[20][20];
    char zone='a',  out[20][20], d;


    f.open("B-small-attempt0.in");
    g.open("B-small.out");
    f>>T;
    for(int count=1; count<=T; count++)
    {
        f>>H>>W;
        for(int i=1; i<=H; i++)
            for(int j=1; j<=W; j++)
                out[i][j]=' ';
        for(int i=1; i<=H; i++)
            for(int j=1; j<=W; j++)
                f>>p[i][j].alt;
        for(int i=0; i<=H+1; i++) p[i][0].alt=11, p[i][W+1].alt=11;
        for(int i=0; i<=W+1; i++) p[0][i].alt=11, p[H+1][i].alt=11;

        for(int i=1; i<=H; i++)
            for(int j=1; j<=W; j++)
            {
                flag = 1;
                x=i; y=j;
                while(flag) //find end zone
                {
                    d=' ';
                    flag = 0;
                    min = p[x][y].alt;
                    if(p[x+1][y].alt < min) //South
                    {
                        min = p[x+1][y].alt;
                        d='s';
                        flag = 1;
                    }
                    if(p[x][y+1].alt < min || d!=' ') //East
                    {
                        if(p[x][y+1].alt <= min)
                        {
                            min = p[x][y+1].alt;
                            d='e';
                            flag = 1;
                        }

                    }
                    if(p[x][y-1].alt < min || d!=' ') //West
                    {
                        if(p[x][y-1].alt <= min)
                        {
                            min = p[x][y-1].alt;
                            d='w';
                            flag = 1;
                        }

                    }
                    if(p[x-1][y].alt < min || d!=' ') //North
                    {
                        if(p[x-1][y].alt<= min)
                        {
                            min = p[x-1][y].alt;
                            d='n';
                            flag = 1;
                        }

                    }
                    switch(d)
                    {
                        case 'n': x--; break;
                        case 'w': y--; break;
                        case 'e': y++; break;
                        case 's': x++; break;
                    }
                }
                p[i][j].endx = x;
                p[i][j].endy = y;

            }

        r=H*W; zone = 'a';

        for(int i=1; i<=H && r>0; i++)
            for(int j=1; j<=W && r>0; j++)
            {
                x=i; y=j;
                while(x<=H && y<=W && out[x][y]==' ')
                {

                    if(p[i][j].endx == p[x][y].endx && p[i][j].endy == p[x][y].endy)
                    {
                        if(out[x][y]==' ')
                        {
                            out[x][y]=zone;
                            r--;
                        }

                    }

                    if(y==W)
                    { if(x==H) zone++;
                        y=1;
                    x++;
                    }else y++;


                }


            }



        zone='a';
        g<<"Case #"<<count<<":\n";
        for(int i=1; i<=H; i++)
        {
            for(int j=1; j<=W; j++)
                g<<out[i][j]<<" ";
            g<<endl;
        }




    }

    f.close();
    g.close();

    return 0;
}
