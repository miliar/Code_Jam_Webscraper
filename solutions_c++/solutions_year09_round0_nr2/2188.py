#include<iostream>
#include<algorithm>
#include<iostream>
#include<cstring>
#include<set>
#include<map>
#include<string>
#include<vector>

#define FOR(i, n) for( i = 0; i < n; ++i )
#define pb(x) push_back( x )

using namespace std;

int h, w, n;

class node
{
    public:
    int i, j;
    char color;
};

vector< vector<int> > maze;
vector< vector<bool> > visited;
vector< vector<node> >drainPoint;

void resizeDrainPoint()
{
    drainPoint.clear();
    drainPoint.resize( h );
    int i;
    FOR( i, h )
        drainPoint[i].resize( w );
}


void takeInput()
{
    int i, j;
    maze.clear();
    maze.resize( h );
    FOR( i, h )
    {
        FOR( j, w )
        {
            int temp;
            cin>>temp;
            maze[i].pb( temp );
        }
    }
}

void resetVisited()
{
    visited.clear();
    visited.resize( h );
    int i, j;
    FOR( i, h )
        visited[i].resize( w );
    FOR( i, h )
        FOR( j, w )
            visited[i][j] = false;
}

node findNextNode(int i, int j)
{
    int minI = 30000, minJ = 30000, minVal = 30000;
    if( i-1>=0 )
    {
        if( maze[i-1][j] < minVal )
        {
            minI = i-1;
            minJ = j;
            minVal = maze[i-1][j];
        }
    }
    if( j-1>=0 )
    {
        if( maze[i][j-1] < minVal )
        {
            minI = i;
            minJ = j-1;
            minVal = maze[i][j-1];
        }
    }
    if( j+1 < w )
    {
        if( maze[i][j+1] < minVal )
        {
            minI = i;
            minJ = j+1;
            minVal = maze[i][j+1];
        }
    }
    if( i+1 < h )
    {
        if( maze[i+1][j] < minVal )
        {
            minI = i+1;
            minJ = j;
            minVal = maze[i+1][j];
        }
    }
    node n;

    if( minVal < maze[i][j] )
    {
        n.i = minI;
        n.j = minJ;
    }
    else
    {
        n.i = i;
        n.j = j;
    }
    return n;
}

char c;

node findDrainPoint(int i,int j)
{
    node next = findNextNode(i, j);
    visited[i][j] = true;
    vector< node > nodes;
    if( next.i == i && next.j == j )
    {
        //cout<<"Returning next "<<endl;
        next.color = ' ';
        return next;
    }
    else
    {
        node temp;
        temp.i = temp.j = -1;
        while( !( next.i == temp.i && next.j == temp.j )  )
        {
            nodes.pb( next );
            temp = next;
            next = findNextNode( next.i, next.j );
        }
    }
    int k;
    next.color = ' ';
    FOR( k, nodes.size() )
    {
        int x = nodes[k].i, y = nodes[k].j;
        visited[x][y] = true;
        //cout<<"next.c = "<<c-1<<endl;

        drainPoint[x][y] = next;

    }
    return next;
}

void displayDrainPointMatrix()
{
    int i, j;
    FOR( i, h )
    {
        FOR( j, w )
        {
            //cout<<drainPoint[i][j].i<<drainPoint[i][j].j<<" ";
            int x, y;
            x = drainPoint[i][j].i;
            y = drainPoint[i][j].j;
            if( drainPoint[x][y].color == ' ' )
                drainPoint[x][y].color = c++;
            cout<<drainPoint[x][y].color<<" ";
        }
        cout<<endl;
    }
}

map< node, char > m;

void solve()
{
    c = 'a';
    int i, j, k;
    cin>>h>>w;
    takeInput();
    resetVisited();
    resizeDrainPoint();
    FOR( i, h )
    {
        FOR( j, w )
        {
            if( visited[i][j] == false )
            {
                drainPoint[i][j] = findDrainPoint(i, j);
            }
        }
    }
    displayDrainPointMatrix();
}

int main()
{
    freopen( "waterLargeInput.in", "r", stdin );
    freopen( "waterLargeOutput.out", "w", stdout );
    cin>>n;
    int i;
    FOR( i, n )
    {
        //vector<string>solution = solve();
        cout<<"Case #"<<i+1<<": "<<endl;
        //int j;
        //FOR( j, solution.size() )
        //    cout<<solution[i]<<endl;

        solve();
    }
}

