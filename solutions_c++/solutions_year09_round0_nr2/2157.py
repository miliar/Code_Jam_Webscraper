#include <iostream>
#include <map>
using namespace std;
typedef enum {NONE, NORTH, WEST, SOUTH, EAST} direction;
int altitudes[100][100];
int basins[100][100];

int main()
{
    int i, j;
    int casenum;
    int T; /* num of test cases */
    int H, W;
    int lowest_altitude;
    direction lowest_altitude_direction;
    map<int,char> seen;
    scanf("%d", &T);
    
    for(casenum = 0; casenum < T; ++casenum)
    {
        
        printf("Case #%d:\n", casenum+1);
        scanf("%d %d", &H, &W);
        for(i = 0; i < H; ++i)
        {
            for(j = 0; j < W; ++j)
            {
                scanf("%d", &(altitudes[i][j]));
                basins[i][j] = i * W + j;
            }
        }
        for(i = 0; i < H; ++i)
        {
            for(j = 0; j < W; ++j)
            {
                lowest_altitude = 10001;
                lowest_altitude_direction = NONE;
                
                if(i > 0 && altitudes[i-1][j] < lowest_altitude)
                {
                    lowest_altitude = altitudes[i-1][j];
                    lowest_altitude_direction = NORTH;
                }
                if(j > 0 && altitudes[i][j-1] < lowest_altitude)
                {
                    lowest_altitude = altitudes[i][j-1];
                    lowest_altitude_direction = WEST;
                }
                if(j < W-1 && altitudes[i][j+1] < lowest_altitude)
                {
                    lowest_altitude = altitudes[i][j+1];
                    lowest_altitude_direction = EAST;
                }
                if(i < H-1 && altitudes[i+1][j] < lowest_altitude)
                {
                    lowest_altitude = altitudes[i+1][j];
                    lowest_altitude_direction = SOUTH;
                }
                
                if(lowest_altitude < altitudes[i][j])
                {
                    int cell1, cell2;
                    if(lowest_altitude_direction == NORTH)
                    {
                        if(basins[i-1][j] < basins[i][j])
                        {
                            cell1 = basins[i-1][j];
                            cell2 = basins[i][j];
                        }
                        else
                        {
                            cell1 = basins[i][j];
                            cell2 = basins[i-1][j];
                        }
                        
                        //basins[i][j] = basins[i-1][j] = cell;
                    }
                    else if(lowest_altitude_direction == WEST)
                    {
                        if(basins[i][j-1] < basins[i][j])
                        {
                            cell1 = basins[i][j-1];
                            cell2 = basins[i][j];
                        }
                        else
                        {
                            cell1 = basins[i][j];
                            cell2 = basins[i][j-1];
                        }
                        
                        //basins[i][j] = basins[i][j-1] = cell;
                    }
                    else if(lowest_altitude_direction == EAST)
                    {
                        if(basins[i][j+1] < basins[i][j])
                        {
                            cell1 = basins[i][j+1];
                            cell2 = basins[i][j];
                        }
                        else
                        {
                            cell1 = basins[i][j];
                            cell2 = basins[i][j+1];
                        }
                        
                        //basins[i][j] = basins[i][j+1] = cell;
                    }
                    else if(lowest_altitude_direction == SOUTH)
                    {
                        if(basins[i+1][j] < basins[i][j])
                        {
                            cell1 = basins[i+1][j];
                            cell2 = basins[i][j];
                        }
                        else
                        {
                            cell1 = basins[i][j];
                            cell2 = basins[i+1][j];
                        }
                        
                        //basins[i][j] = basins[i+1][j] = cell;
                    }
                    
                    int i2;
                    int j2;
                    for(i2 = 0; i2 < H; ++i2)
                    {
                        for(j2 = 0; j2 < W; ++j2)
                        {
                            if(basins[i2][j2] == cell2)
                                basins[i2][j2] =cell1;
                        }
                    }
                }                      
            }
        }
        
      
        /*
        for(i = 0; i < H; ++i)
        {
            for(j = 0; j < W; ++j)
                printf("%d ", basins[i][j]);
            printf("\n");
        }
        */
        
        seen.clear();
        char current = 'a';
        for(i = 0; i < H; ++i)
        {
            for(j = 0; j < W; ++j)
            {
                if(seen[basins[i][j]] == 0)
                {
                    seen[basins[i][j]] = current;
                    current += 1;
                }
            }
        }
        
        for(i = 0; i < H; ++i)
        {
            for(j = 0; j < W; ++j)
            {
                if(j > 0) printf(" ");
                printf("%c", seen[basins[i][j]]);
            }
            printf("\n");
        }
    }
    return 0;
}
    
    
    
    
    
