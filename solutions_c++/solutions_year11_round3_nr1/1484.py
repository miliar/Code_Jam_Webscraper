#include <iostream>
#include <cassert>
#include <cstring>
using namespace std;

int tile[50][50];
int R,C;//R = Takasa C = Haba

void initialize()
{
    R = 0;
    C = 0;
    memset(tile,0,sizeof tile);
}

void read_input()
{
    cin >> R >> C;
    for(int y=0;y<R;++y)
    {
	for(int x=0;x<C;++x)
	{
	    char c;cin >> c;
	    assert(c == '.' || c == '#');
	    tile[y][x] = c == '.' ? 0 : 1;
	}
    }
}
    
void calc()
{
    initialize();
    read_input();

    for(int y=0;y<R;++y)
    {
	for(int x=0;x<C;++x)
	{
	    if(x+1<C && y+1<R &&
	       (tile[y+0][x+0] == 1 && tile[y+0][x+1] == 1) &&
	       (tile[y+1][x+0] == 1 && tile[y+1][x+1] == 1))
	    {
		tile[y][x] = 2;
		tile[y][x+1] = 3;
		tile[y+1][x] = 3;
		tile[y+1][x+1] = 2;
	    }
	}
    }

    bool found = false;
    for(int y=0;y<R;++y)
    {
	for(int x=0;x<C;++x)
	{
	    if(tile[y][x] == 1){found = true;goto END;}
	}
    }
END:
    if(found)
	cout << "Impossible" << endl;
    else {
	for(int y=0;y<R;++y)
	{
	    for(int x=0;x<C;++x)
	    {
		switch(tile[y][x])
		{
		case 0:printf(".");break;
		case 2:printf("/");break;
		case 3:printf("\\");break;
		default:assert(false);
		}
	    }
	    puts("");
	}
    }
}
	
int main()
{
    int T;cin >> T;
    for(int i=1;i<=T;++i)
    {
	printf("Case #%d:\n",i);
	calc();
    }
    return 0;
}
