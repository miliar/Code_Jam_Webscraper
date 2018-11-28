#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

char currLabel = 'a';

bool isSink(int y, int x, int W, int H, vector<vector<int> > altitudes)
{
    if (W == 1 && H == 1)
        return true;
    if (y == 0 && x == 0)
    {
        if (W == 1 && H != 1)
            return altitudes[0][0] <= altitudes[1][0];
        else if (H == 1 && W != 1)
            return altitudes[0][0] <= altitudes[0][1];
        else
            return (altitudes[0][0] <= altitudes[1][0] && altitudes[0][0] <= altitudes[0][1]);
    }
    else if (y == H-1 && x == 0)
    {
        if (W == 1)
            return altitudes[y][x] <= altitudes[y-1][x];
        else
            return (altitudes[H-1][0] <= altitudes[H-2][0] && altitudes[H-1][0] <= altitudes[H-1][1]);
    }
    else if (y == 0 && x == W-1)
    {
        if (H == 1)
            return altitudes[y][x] <= altitudes[y][x-1];
        else
            return (altitudes[0][W-1] <= altitudes[1][W-1] && altitudes[0][W-1] <= altitudes[0][W-2]);
    }
    else if (y == H-1 && x == W-1)
    {
        if (W == 1)
            return altitudes[y][x] <= altitudes[y-1][x];
        else if (H == 1)
            return altitudes[y][x] <= altitudes[y][x-1];
        else
            return (altitudes[y][x] <= altitudes[H-2][W-1] && altitudes[y][x] <= altitudes[H-1][W-2]);
    }
    else if (x == 0)
    {
        if (W == 1)
            return (altitudes[y][x] <= altitudes[y-1][0] && altitudes[y][x] <= altitudes[y+1][0]);
        else
            return (altitudes[y][x] <= altitudes[y-1][0] && altitudes[y][x] <= altitudes[y+1][0] && altitudes[y][x] <= altitudes[y][1]);
    }
    else if (x == W-1)
        return (altitudes[y][x] <= altitudes[y-1][W-1] && altitudes[y][x] <= altitudes[y+1][W-1] && altitudes[y][x] <= altitudes[y][W-2]);    
    else if (y == 0)
    {
        if (H == 1)
            return (altitudes[y][x] <= altitudes[y][x-1] && altitudes[y][x] <= altitudes[y][x+1]);
        else
            return (altitudes[y][x] <= altitudes[y][x-1] && altitudes[y][x] <= altitudes[y][x+1] && altitudes[y][x] <= altitudes[1][x]);
    }
    else if (y == H-1)
        return (altitudes[y][x] <= altitudes[y-1][x] && altitudes[y][x] <= altitudes[y][x+1] && altitudes[y][x] <= altitudes[y][x-1]);
    else
        return (altitudes[y][x] <= altitudes[y-1][x] && altitudes[y][x] <= altitudes[y][x+1] && altitudes[y][x] <= altitudes[y][x-1] && altitudes[y][x] <= altitudes[y+1][x]);
}

int getAltitude(int y, int x, int W, int H, const vector<vector<int> > & altitudes)
{
    if (y < 0 || y >= H || x < 0 || x >= W)
        return 10000;
    else
        return altitudes[y][x];
}

pair<int, int> lowestAltNeighbor(int y, int x, int W, int H, const vector<vector<int> > & altitudes)
{
    pair <int, int> min(y-1, x);

    if (getAltitude(y, x-1, W, H, altitudes) < getAltitude(min.first, min.second, W, H, altitudes))
    {
        min.first = y;  min.second = x-1;
    }
    if (getAltitude(y, x+1, W, H, altitudes) < getAltitude(min.first, min.second, W, H, altitudes))    
    {
        min.first = y;  min.second = x+1;
    }
    if (getAltitude(y+1, x, W, H, altitudes) < getAltitude(min.first, min.second, W, H, altitudes))  
    {
        min.first = y+1;  min.second = x;
    }
    return min;
}

char labelCell(int y, int x, int W, int H, const vector<vector<int> > & altitudes, vector<vector<char> > & labels)
{
    if (labels[y][x] != ' ')
        return labels[y][x];
    else if (isSink(y, x, W, H, altitudes))
    {
        labels[y][x] = currLabel++;
        return labels[y][x];
    }
    else
    {
        pair <int, int> lowestNeighbor = lowestAltNeighbor(y, x, W, H, altitudes);
        labels[y][x] = labelCell(lowestNeighbor.first, lowestNeighbor.second, W, H, altitudes, labels);
        return labels[y][x];
    }
}

int main(int argc, char* argv[])
{
    /*ifstream in;
    in.open(argv[1]);

    if (!in.is_open())
        return 1;*/
    //ofstream out(argv[2]);

    int T;
    cin >> T;

    for (int map = 0 ; map < T ; map++)
    {
        currLabel = 'a';
        int H, W;
        cin >> H >> W;
        vector<vector<int> > altitudes(H);
        vector<vector<char> > labels(H);
        for (int i = 0 ; i < H ; i++)
        {   
            altitudes[i].resize(W);
            labels[i].resize(W);
            for (int j = 0 ; j < W ; j++)
            {
                int altitude;
                cin >> altitude;
                altitudes[i][j] = altitude;
                labels[i][j] = ' ';
            }
        }

        for (int i = 0 ; i < H ; i++)
        {
            for (int j = 0 ; j < W ; j++)
            {
                labelCell(i, j, W, H, altitudes, labels);
            }
        }

        cout << "Case #" << map+1 << ":" << endl;
        for (int i = 0 ; i < H ; i++)
        {
            for (int j = 0 ; j < W ; j++)
            {
                if (j == W-1)
                    cout << labels[i][j] << endl;
                else
                    cout << labels[i][j] << " ";
            }
        }
    }
    return 0;
}