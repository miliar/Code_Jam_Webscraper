#include <iostream>
#include <string>
#include <fstream>
#include <boost/lexical_cast.hpp>
#include <vector>

// Disgusting code

typedef struct smallest_
{
  std::pair<int, int> pos;
  int value;
} smallest;

std::vector<std::vector<char>> basins;
std::vector<std::vector<int>> altitudes;

// First in pair is smallest value, second in pair is parent/child id.
smallest check(int parentX, int parentY, int childX, int childY)
{
  if (altitudes[parentX][parentY] <= altitudes[childX][childY])
  {
    smallest s = {std::pair<int, int>(parentX, parentY), altitudes[parentX][parentY]};
    return s;
  }
  else
  {
    smallest s = {std::pair<int, int>(childX, childY), altitudes[childX][childY]};
    return s;
  }
}

// Non-existent node.
smallest set_invalid(int x, int y)
{
  smallest s = {std::pair<int, int>(x, y), -1};
  return s;
}

int main(int argc, char* argv[])
{
  std::fstream inFile(argv[1]);
  std::string input;
  inFile >> input;
  int numCases = boost::lexical_cast<int>(input);

  for (int c = 1; c <= numCases; ++c)
  {
    inFile >> input;
    int h = boost::lexical_cast<int>(input);
    inFile >> input;
    int w = boost::lexical_cast<int>(input);

    altitudes = std::vector<std::vector<int>>(h, std::vector<int>(w));
    for (int i = 0; i < h; ++i)
    {
      for (int j = 0; j < w; ++j)
      {
        inFile >> input;
        altitudes[i][j] = boost::lexical_cast<int>(input);
      }
    }
    
    // Init basins
    basins = std::vector<std::vector<char>>(h, std::vector<char>(w));
    for (int i = 0; i < h; ++i)
    {
      for (int j = 0; j < w; ++j)
      {
        basins[i][j] = '0';
      }
    }

    char currentChar = 'a';
    basins[0][0] = currentChar;

    for (int i = 0; i < h; ++i)
    {
      for (int j = 0; j < w; ++j)
      {
        int minVal = altitudes[i][j];
        smallest lowest = {std::pair<int, int>(i, j), altitudes[i][j]};
        smallest northS, westS, eastS, southS;
        if (i-1 >= 0)
        {
          northS = check(i, j, i-1, j);
          if (northS.value < minVal)
            minVal = northS.value;
        }
        else
          northS = set_invalid(i, j);
        if(j-1 >= 0)
        {
          westS = check(i, j, i, j-1);
          if (westS.value < minVal)
            minVal = westS.value;
        }
        else
          westS = set_invalid(i, j);
        if (j+1 <= w-1)
        {
          eastS = check(i, j, i, j+1);
          if (eastS.value < minVal)
            minVal = eastS.value;
        }
        else
          eastS = set_invalid(i, j);
        if (i+1 <= h-1)
        {
          southS = check(i, j, i+1, j);
          if (southS.value < minVal)
            minVal = southS.value;
        }
        else
          southS = set_invalid(i, j);
        
        if (northS.value == minVal)
        {
          lowest.pos = northS.pos;
          lowest.value = northS.value;
        }
        else if (westS.value == minVal)
        {
          lowest.pos = westS.pos;
          lowest.value = westS.value;
        }
        else if (eastS.value == minVal)
        {
          lowest.pos = eastS.pos;
          lowest.value = eastS.value;
        }
        else
        {
          lowest.pos = southS.pos;
          lowest.value = southS.value;
        }

        // This is lowest and not labeled
        if (basins[i][j] == '0' && lowest.pos == std::pair<int, int>(i, j))
        {
          currentChar = (char)(currentChar + 1);
          basins[i][j] = currentChar;
        }
        // This is not lowest, but lowest not labeled
        else if (basins[i][j] == '0' && basins[lowest.pos.first][lowest.pos.second] == '0')
        {
          currentChar = (char)(currentChar + 1);
          basins[i][j] = currentChar;
          basins[lowest.pos.first][lowest.pos.second] = currentChar;
        }
        else if (basins[i][j] == '0')
        {
          basins[i][j] = basins[lowest.pos.first][lowest.pos.second];
        }
        else if (basins[lowest.pos.first][lowest.pos.second] == '0')
        {
          basins[lowest.pos.first][lowest.pos.second] = basins[i][j];
        }
        else if (basins[i][j] != basins[lowest.pos.first][lowest.pos.second])
        {
          char oldValue = basins[i][j];
          char newValue;
          if (basins[i][j] < basins[lowest.pos.first][lowest.pos.second])
            newValue = basins[i][j];
          else
            newValue = basins[lowest.pos.first][lowest.pos.second];

          basins[i][j] = basins[lowest.pos.first][lowest.pos.second];
          for (int x = 0; x < h; ++x)
          {
            for (int y = 0; y < w; ++y)
            {
              if (basins[x][y] == oldValue)
              {
                basins[x][y] = newValue;
              }
              else if (basins[x][y] > oldValue)
              {
                basins[x][y] = (char)(basins[x][y]-1);
              }
            }
          }
          currentChar = (char)(currentChar - 1);
        }
      }
    }

    // Output
    std::cout << "Case #" << c << ":\n";
    for (int i = 0; i < h; ++i)
    {
      for (int j = 0; j < w; ++j)
      {
        std::cout << basins[i][j];
        if (j < w-1)
          std::cout << " ";
      }
      std::cout << "\n";
    }
  }

  inFile.close();

  return 0;
}