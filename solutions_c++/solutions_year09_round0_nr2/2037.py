#include <cstdlib>
#include <iostream>
#include <string>
#include <map>

using namespace std;

int main(int argc, char *argv[])
{
    // Input Number of Cases
    int cases;
    cin >> cases;
    
    for(int i = 0;i<cases;i++)  // For Each Case
            {
                cout << "Case #" << i + 1 << ":" << endl;
                
                // Input Height and Width
                int height, width;
                cin >> height;
                cin >> width;
                
                map<int, map<int, int> > altitudes; // Map of Altitudes
                map<int, map<int, char> > basins; // Map of Basins
                
                // Collect Altitudes Into Map
                for(int h = 0;h < height;h++)
                        {
                            for(int w = 0;w < width;w++)
                                    {
                                        cin >> altitudes[h][w];
                                    }
                        }
                        
                // Assign Basins
                char basin = 'a';   // Keeps track of Basin letters. Initialize to lowercase a.
                
                for(int h = 0;h < height;h++)
                        {
                            for(int w = 0;w < width;w++)
                                    {
                                        int altitude = altitudes[h][w]; // Altitude of Current Cell
                                        
                                        // Collect Altitudes From Neighboring Cells
                                        int North, West, East, South;
                                        
                                        // North
                                        if(h > 0)  // If there is a cell to the North
                                             {
                                               North = altitudes[h-1][w];
                                             }
                                        else
                                             {
                                               North = altitude + 1;     // Make sure not to drain to a sink that doesn't exist
                                             }

                                        // West
                                        if(w > 0)  // If there is a cell to the West
                                             {
                                               West = altitudes[h][w-1];
                                             }
                                        else
                                             {
                                               West = altitude + 1;     // Make sure not to drain to a sink that doesn't exist
                                             }
                                        
                                        // East
                                        if (w < width - 1)     // If there is a cell to the East
                                             {
                                               East = altitudes[h][w+1];
                                             }
                                        else
                                             {
                                               East = altitude + 1;
                                             }
                                             
                                        // South
                                        if (h < height - 1)    // If there is a cell to the South
                                             {
                                               South = altitudes[h+1][w];
                                             }
                                        else
                                             {
                                               South = altitude + 1;
                                             }
                                        
                                        
                                        // Is this a Sink?
                                        if (altitude <= North && altitude <= West && altitude <= East && altitude <= South)
                                             {
                                               if (basins[h][w] == char())  // If basin has not been assigned a letter.
                                                  {
                                                   basins[h][w] = basin;
                                                   basin++;
                                                  }
                                             }
                                        else
                                             {
                                               // If not a Sink, find one
                                               
                                               int findbasinh = h; int findbasinw = w;        // Track cell for finding basin
                                               int findbasina = altitude;                     // Track current lowest altitude for finding basin
                                               int currentcellh = h; int currentcellw = w;
                                               
                                               while ((findbasina <= North && findbasina <= West && findbasina <= East && findbasina <= South) == false)    // While Sink Hasn't Been Found                                               
                                                     {                                                                
                                                       currentcellh = findbasinh;
                                                       currentcellw = findbasinw;
                                                       
                                                       if (North < findbasina)
                                                          {
                                                           findbasina = North;
                                                           findbasinh = currentcellh-1;
                                                           findbasinw = currentcellw;
                                                          }
                                                          
                                                       if (West < findbasina)
                                                          {
                                                           findbasina = West;
                                                           findbasinh = currentcellh;
                                                           findbasinw = currentcellw-1;
                                                          }
                                                          
                                                       if (East < findbasina)
                                                          {
                                                           findbasina = East;
                                                           findbasinh = currentcellh;
                                                           findbasinw = currentcellw+1;
                                                          }
                                                          
                                                       if (South < findbasina)
                                                          {
                                                           findbasina = South;
                                                           findbasinh = currentcellh+1;
                                                           findbasinw = currentcellw;
                                                          }
                                                          
                                                       // North
                                                       if(findbasinh > 0)  // If there is a cell to the North
                                                            {
                                                              North = altitudes[findbasinh-1][findbasinw];
                                                            }
                                                       else
                                                            {
                                                              North = findbasina + 1;     // Make sure not to drain to a sink that doesn't exist
                                                            }
                                                       // West
                                                       if(findbasinw > 0)  // If there is a cell to the West
                                                            {
                                                              West = altitudes[findbasinh][findbasinw-1];
                                                            }
                                                       else
                                                            {
                                                              West = findbasina + 1;     // Make sure not to drain to a sink that doesn't exist
                                                            }
                                                       
                                                       // East
                                                       if (findbasinw < width - 1)     // If there is a cell to the East
                                                            {
                                                              East = altitudes[findbasinh][findbasinw+1];
                                                            }
                                                       else
                                                            {
                                                              East = findbasina + 1;
                                                            }
                                                             
                                                       // South
                                                       if (findbasinh < height - 1)    // If there is a cell to the South
                                                            {
                                                              South = altitudes[findbasinh+1][findbasinw];
                                                            }
                                                       else
                                                            {
                                                              South = findbasina + 1;
                                                            }
                                                     }                                               

                                               // Sink Has Been Found
                                               if (basins[findbasinh][findbasinw] != char())     // If basin already has been assigned a letter
                                                  {
                                                   basins[h][w] = basins[findbasinh][findbasinw];
                                                   }
                                               else            // If basin hasn't been assigned a letter
                                                  {
                                                   basins[h][w] = basin;
                                                   basins[findbasinh][findbasinw] = basin;
                                                   basin++;
                                                  }
                                                  
                                             }
                                        
                                    }
                        }
                
                
                // Display Basins
                for(int h = 0;h < height;h++)
                        {
                            for(int w = 0;w < width;w++)
                                    {
                                        cout << basins[h][w];
                                        if (w==width-1)
                                           {
                                                       cout << endl;
                                           }
                                        else
                                           {
                                                       cout << " ";
                                           }
                                    }
                        }
                
                
            }
    
    return EXIT_SUCCESS;
}
