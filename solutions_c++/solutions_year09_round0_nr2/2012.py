#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

int H, W;
int altitudes[100][100];
char current_label;
char sinks[100][100];
char labels[100][100];
    
int d_x[] = {0, -1, 1, 0};
int d_y[] = {-1, 0, 0, 1};

char find_label(int y, int x)
{
    int min_y = -1, min_x = -1;
    int c_altitude = altitudes[y][x];
    for (int i = 0; i < 4; i++)
    {
        int n_x = x + d_x[i];
        int n_y = y + d_y[i];
        if (n_y >= 0 && n_y < H && n_x >= 0 && n_x < W)
        {
            int n_altitude = altitudes[n_y][n_x];
            if (n_altitude < c_altitude && 
                ((min_y == -1 && min_x == -1) || (n_altitude < altitudes[min_y][min_x])))
            {
                min_y = n_y;
                min_x = n_x;
            }
        }
    }
    
    if (min_y == -1 && min_x == -1)
    {
        if (sinks[y][x] < 'a')
            sinks[y][x] = ++current_label;
        return sinks[y][x];
    }
    return find_label(min_y, min_x);
}

void find_labels()
{
    for (int i = 0; i < H; i++)
        for (int j = 0; j < W; j++)
            labels[i][j] = find_label(i, j);
}

void print_labels()
{
    for (int i = 0; i < H; i++)
    {
        for (int j = 0; j < W; j++)
            cout << labels[i][j] << (j + 1 < W ? " " : "");
        cout << endl;
    }
}

void read_altitudes()
{
    for (int i = 0; i < H; i++)
        for (int j = 0; j < W; j++)
            cin >> altitudes[i][j];
}

int main()
{
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++)
    {
        current_label = 'a' - 1;
        memset(altitudes, -1, sizeof(altitudes));
        memset(sinks, current_label, sizeof(sinks));
        memset(labels, current_label, sizeof(labels));
        
        cin >> H >> W;
        read_altitudes();
        find_labels();
        cout << "Case #" << i + 1 << ":" << endl;
        print_labels();
    }
    
    return 0;    
}
