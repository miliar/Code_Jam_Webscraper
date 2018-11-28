#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>
#include <map>

using namespace std;

int H, W;
int xmap[128][128];
char ret[128][128];

bool all_filled()
{
    for(int i=0; i<H; i++) for(int j=0; j<W; j++) if(ret[i][j]==0) return false;
    return true;
}

pair <int, int> find_max_point()
{
    int x=0, y=0;
    for(int i=0; i<H; i++) for(int j=0; j<W; j++) if(ret[i][j]==0)
    {
        x=i;
        y=j;
        break;
    }
    for(int i=0; i<H; i++) for(int j=0; j<W; j++) if(ret[i][j]==0)
    {
        if(xmap[i][j]>=xmap[x][y])
        {
            x=i;
            y=j;
        }
    }
    return make_pair(x, y);
}

char recursion(int x, int y)
{
    bool found=false;
    if(ret[x][y]!=0) return ret[x][y];
    int next_x, next_y;
    int min_value=xmap[x][y];
    if(x>0) if(xmap[x-1][y]<min_value) min_value=xmap[x-1][y];
    if(y>0) if(xmap[x][y-1]<min_value) min_value=xmap[x][y-1];
    if(y<W-1) if(xmap[x][y+1]<min_value) min_value=xmap[x][y+1];
    if(x<H-1) if(xmap[x+1][y]<min_value) min_value=xmap[x+1][y];
    if(!found) if(x>0) if(xmap[x-1][y]==min_value)
    {
        next_x=x-1;
        next_y=y;
        found=true;
    }
    if(!found) if(y>0) if(xmap[x][y-1]==min_value)
    {
        next_x=x;
        next_y=y-1;
        found=true;
    }
    if(!found) if(y<W-1) if(xmap[x][y+1]==min_value)
    {
        next_x=x;
        next_y=y+1;
        found=true;
    }
    if(!found) if(x<H-1) if(xmap[x+1][y]==min_value)
    {
        next_x=x+1;
        next_y=y;
        found=true;
    }
    char c=recursion(next_x, next_y);
    if(c!=0) ret[x][y]=c;
    return c;
}

int main()
{
    ifstream fin("b-input.in");
    ofstream fout("b-output.out");
    int T;
    fin >> T;
    for(int i=0; i<T; i++)
    {
        fin >> H >> W;
        char next=1;
        for(int j=0; j<H; j++) for(int k=0; k<W; k++)
        {
            fin >> xmap[j][k];
            ret[j][k]=0;
        }
        for(int j=0; j<H; j++) for(int k=0; k<W; k++)
        {
            if(j!=H-1) if(xmap[j][k]>xmap[j+1][k]) continue;
            if(k!=W-1) if(xmap[j][k]>xmap[j][k+1]) continue;
            if(j!=0) if(xmap[j][k]>xmap[j-1][k]) continue;
            if(k!=0) if(xmap[j][k]>xmap[j][k-1]) continue;
            ret[j][k]=next;
            next++;
        }
        while(!all_filled())
        {
            pair <int, int> max=find_max_point();
            recursion(max.first, max.second);
        }
        map <char, char> translate;
        char chnext='a';
        for(int j=0; j<H; j++) for(int k=0; k<W; k++)
        {
            if(translate.find(ret[j][k])==translate.end())
            {
                translate[ret[j][k]]=chnext;
                chnext++;
            }
        }
        fout << "Case #" << i+1 << ":" << endl;
        for(int j=0; j<H; j++)
        {
            for(int k=0; k<W; k++) fout << translate[ret[j][k]] << " ";
            fout << endl;
        }
    }
    fin.close();
    fout.close();
}
