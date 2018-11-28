#include <iostream>
#include <fstream>

using namespace std;

ifstream in("B-large.in");
ofstream out("B.out");

int altitud[100][100];
char direction[100][100];
char label[100][100];
int T, X, H, W;


bool inside(int h, int w)
{
    if (h >= 0 && h < H)
    {
        if (w >= 0 && w < W)
        {
            return true;
        }
    }
    return false;
}

void flowFrom(int h, int w, char c)
{
    //North
    if (inside(h-1, w))
        if (label[h-1][w] == ' ')
            if (direction[h-1][w] == 'S')
            {
                label[h-1][w] = c;
                flowFrom(h-1, w, c);
            }
    //West
    if (inside(h, w-1))
        if (label[h][w-1] == ' ')
            if (direction[h][w-1] == 'E')
            {
                label[h][w-1] = c;
                flowFrom(h, w-1, c);
            }
    //East
    if (inside(h, w+1))
        if (label[h][w+1] == ' ')
            if (direction[h][w+1] == 'W')
            {
                label[h][w+1] = c;
                flowFrom(h, w+1, c);
            }
    //South
    if (inside(h+1, w))
        if (label[h+1][w] == ' ')
            if (direction[h+1][w] == 'N')
            {
                label[h+1][w] = c;
                flowFrom(h+1, w, c);
            }
}

void flowTo(int h, int w, char c)
{
    label[h][w] = c;
    
    flowFrom(h, w, c);
    
    if (direction[h][w] != 'Z')
    {
        if (direction[h][w] == 'N')
        {
            flowTo(h-1, w, c);
        }
        else if (direction[h][w] == 'W')
        {
            flowTo(h, w-1, c);
        }
        else if (direction[h][w] == 'E')
        {
            flowTo(h, w+1, c);
        }
        else //if (direction[h][w]=='S')
        {
            flowTo(h+1, w, c);
        }
    }
}

void direccion(int h, int w)
{
    int actual = altitud[h][w];
    if (inside(h-1,w))
        if (altitud[h-1][w]<actual)
        {
            actual = altitud[h-1][w];
            direction[h][w] = 'N';
        }
    if (inside(h,w-1))
        if (altitud[h][w-1]<actual)
        {
            actual = altitud[h][w-1];
            direction[h][w] = 'W';
        }
    if (inside(h,w+1))
        if (altitud[h][w+1]<actual)
        {
            actual = altitud[h][w+1];
            direction[h][w] = 'E';
        }
    if (inside(h+1,w))
        if (altitud[h+1][w]<actual)
        {
            actual = altitud[h+1][w];
            direction[h][w] = 'S';
        }
}
    
int main()
{
    int h, w, basinLabel;

    //input
    in>>T;
    for (X=1; X<=T; X++)
    {
        in>>H>>W;
        
        for (h=0; h<H; h++)
        {
            for (w=0; w<W; w++)
            {
                in>>altitud[h][w];
                //init
                direction[h][w] = 'Z';
                label[h][w] = ' ';
            }
        }
        
        //init
        for (h=0; h<H; h++)
        {
            for (w=0; w<W; w++)
            {
                direccion(h, w);
            }
        }
        
        //algorithm
        basinLabel = 0;
        for (h=0; h<H; h++)
        {
            for (w=0; w<W; w++)
            {
                if (label[h][w] == ' ')
                {
                    flowTo(h, w, basinLabel+'a');
                    basinLabel++;
                }
            }
        }
        
        //output
        out<<"Case #"<<X<<":"<<endl;
        for (h=0; h<H; h++)
        {
            for (w=0; w<W; w++)
            {
                if (w!=0)
                {
                    out<<" ";
                }
                out<<label[h][w];
            }
            out<<endl;
        }
    }
    
    return EXIT_SUCCESS;
}
