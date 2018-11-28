#include <iostream>
#include <vector>
#include <map>
using namespace std; 

class Axis
{
    public:
        int x, y;
};
int width, height;
std::vector<std::vector<int> > table1, table2;

void displayTable2()
{
    for(int y = 0; y < height; y++)
    {
        for(int x = 0; x < width; x++)
        {
            cout << table2[y][x] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

// true if move, false if stay.
void nextPoint(int& x, int& y)
{
    int min = table1[y][x];
    int dir = 0; // 1 = S, 2 = E, 3 = W, 4 = N

    if ( y < height-1 )
    {
        if ( min > table1[y+1][x])
        {
            min = table1[y+1][x];
            dir = 1;
        }
    }
    if ( x < width-1 )
    {
        if ( min > table1[y][x+1] )
        {
            min = table1[y][x+1];
            dir = 2;
        }
        else if (min == table1[y][x+1])
            dir = 2;
    }
    if ( x > 0 )
    {
        if ( min > table1[y][x-1] )
        {
            min = table1[y][x-1];
            dir = 3;
        }
        else if (min == table1[y][x-1])
            dir = 3;
    }
    if ( y > 0 )
    {
        if ( min > table1[y-1][x] )
        {
            min = table1[y-1][x];
            dir = 4;
        }
        else if (min == table1[y-1][x])
            dir = 4;
    }

    if (min < table1[y][x])
    {
        switch(dir)
        {
            case 1: // South
                y++; //cout << "South " << endl;
                break;
            case 2: // East
                x++; //cout << "East " << endl;
                break;
            case 3: // West
                x--; //cout << "West " << endl;
                break;
            case 4: // North
                y--; //cout << "North " << endl;
                break;
        }
    }



} // end - nextPoint

void fillTable( size_t fillNo, std::map<int, vector<Axis> >& graph, vector<Axis>& currentList )
{
    for(size_t i = 0; i < currentList.size(); i++)
    {
        //cout << "Writing " << fillNo <<  " (" << currentList[i].x << " , " << currentList[i].y << ")" << endl;
        if (currentList[i].x < 0)
        {
            fillTable( fillNo, graph, graph[ -( currentList[i].x) ] );
            continue;
        }
        
        if (table2[ currentList[i].y ][ currentList[i].x ] > static_cast<int>(fillNo) )
            table2[ currentList[i].y ][ currentList[i].x ] = fillNo;
        
    }
}

int main(int argc, char** argv)
{
    int caseno;
    cin >> caseno;
    for(int currentCase = 1; currentCase <= caseno; currentCase++)
    {
        width = 0, height = 0;
        cin >> height >> width;

        table1.resize(height);
        table2.resize(height);
        for(int y = 0; y < height; y++)
        {
            table1[y].resize( width );
            table2[y].resize( width );
            for(int x = 0; x < width; x++)
            {
                cin >> table1[y][x];
                table2[y][x] = 0;
            }
        }
        // XXX
        // for(int y = 0; y < height; y++)
        // {
        //     for(int x = 0; x < width; x++)
        //     {
        //         cout << table1[y][x] << " ";
        //     }
        //     cout << endl;
        // }
        // XXX

        // fill out the graph.
        int fillNum = 1;
        std::map< int , vector<Axis> > graph;
        for(int y = 0; y < height; y++)
        {
            for(int x = 0; x < width; x++)
            {
                if ( table2[y][x] > 0 )
                    continue;
                // Travel until the end;
                int x2 = x, y2 = y;
                while(1)
                {
                    // If I met another graph.
                    if ( table2[y2][x2] > 0 )
                        break;
                    table2[y2][x2] = fillNum;
                    Axis obj; obj.x = x2; obj.y = y2;
                    graph[fillNum].push_back( obj );

                    nextPoint(x2, y2);
                }

                // Check if the stop point is another graph.
                if ( table2[y2][x2] != fillNum )
                {
                    Axis obj; obj.x = -fillNum; obj.y = 0;
                    graph[ table2[y2][x2] ].push_back( obj );
                    //cout << "insert " << obj.x << " , " << obj.y << endl; // XXX
                }

                fillNum++;
            } // end - for
        } // end - for


        // Fill ahphabet table.
        for(size_t i = 1; i <= graph.size(); i++)
        {
            fillTable( i, graph, graph[i] );
        }


        // Get all the numbers and matches to the correct value.
        std::map<int , char> charMap;
        for(int y = 0; y < height; y++)
        {
            for(int x = 0; x < width; x++)
            {
                charMap[ table2[y][x] ] = 'a';
            }
        }
        char currentChar = 'a';
        for(std::map<int , char>::iterator iter = charMap.begin();
                iter != charMap.end(); iter++)
        {
            iter->second = currentChar++;
        }

        //displayTable2();


        // Display the result
        cout << "Case #" << currentCase <<":" << endl;
        for(int y = 0; y < height; y++)
        {
            for(int x = 0; x < width; x++)
                cout << charMap[ table2[y][x] ] << " ";
            cout << endl;
        }

        
    }
    return 0;
} // end - main
