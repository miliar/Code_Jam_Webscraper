#include<iostream>
#include<fstream>
using namespace std;

int dy[]={-1,0,0,1};
int dx[]={0,-1,1,0};

const int MXSIZE=110;
bool used[MXSIZE][MXSIZE];
char map[MXSIZE][MXSIZE];
int grid[MXSIZE][MXSIZE];
int height,width;

string array="abcdefghijklmnopqrstuvwxyz";
int cplace;

void display()
{
    for(int i=0;i<height;i++)
    {
        for(int j=0;j<width;j++)
        {
            cout<<grid[i][j];
            if(j==(width-1))
                cout<<endl;
            else cout<<" ";
        }
    }
}

bool isvalid(int y,int x)
{
    if(y<0 || x<0 || y>=height || x>=width)return false;
    return true;
}

char fill(int y,int x)
{
    if(used[y][x])return map[y][x];
    used[y][x]=true;
    //for all directons
    //find min
    int besty=-1,bestx=-1;
    int curval=grid[y][x];
    int bestvalue=curval;
    for(int i=0;i<4;i++)
    {
        int ny=dy[i]+y;
        int nx=dx[i]+x;
        //if is valid and is less than current
        /*
        if(isvalid(ny,nx))
        {
            cout<<"ny= "<<ny<<" nx "<<nx<<endl;
            cout<<"grid[ny][nx] "<<grid[ny][nx]<<" bestvalue "<<bestvalue<<endl;
        }
        */
        if(isvalid(ny,nx) && grid[ny][nx]<bestvalue)
        {
            besty=ny;bestx=nx;
            bestvalue=grid[ny][nx];
        }
    }
    //if reached sink
    if(besty==-1)
    {
        //cout<<"best not found "<<y<<" "<<x<<endl;
        used[y][x]=true;
        return map[y][x]=array[cplace++];
    }
    else
    {
        return map[y][x]=fill(besty,bestx);
    }
}
        

void flood_fill()
{
    //fill north west first
    for(int i=0;i<height;i++)
    {
        for(int j=0;j<width;j++)
        {
            if(!used[i][j])
            {
                map[i][j]=fill(i,j);
            }
        }
    }
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("output.out");
    int ntests;
    fin>>ntests;
    //for all tests
    for(int ij=0;ij<ntests;ij++)
    {
        fin>>height>>width;
        cplace=0;
        for(int i=0;i<height;i++)
        {
            for(int j=0;j<width;j++)
            {
                fin>>grid[i][j];
                used[i][j]=false;
                map[i][j]='@';
            }
        }
        
        flood_fill();
        //output
        fout<<"Case #"<<ij+1<<":"<<endl;
        for(int i=0;i<height;i++)
        {
            for(int j=0;j<width;j++)
            {
                fout<<map[i][j];
                if(j==(width-1))
                    fout<<endl;
                else fout<<" ";
            }
        }
    }
    cout<<"done\n";
    int z;
    cin>>z;
    return 0;
}
        
