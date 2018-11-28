#include <iostream>
#include <fstream>
using namespace std;

enum direction_t {NORTH = 0, WEST, EAST, SOUTH, BASIN};

char traceMap(char* finalMap, direction_t* dirMap, int width, int height, int i, char currentBasin)
{
    int col = i % width;
    int row = i / width;
    if(finalMap[i] != 0)
    {
        return finalMap[i];
    }
    else if(dirMap[i] == BASIN)
    {
        finalMap[i] = currentBasin;
        return currentBasin;
    }
    else if(dirMap[i] == WEST)
    {
        finalMap[i] = traceMap(finalMap, dirMap, width, height, i - 1, currentBasin);
    }
    else if(dirMap[i] == EAST)
    {
        finalMap[i] = traceMap(finalMap, dirMap, width, height, i + 1, currentBasin);
    }
    else if(dirMap[i] == SOUTH)
    {
        finalMap[i] = traceMap(finalMap, dirMap, width, height, i + width, currentBasin);
    }
    else if(dirMap[i] == NORTH)
    {
        finalMap[i] = traceMap(finalMap, dirMap, width, height, i - width, currentBasin);
    }
    return finalMap[i];
}

void solve(int* map, int width, int height, ofstream& outStream)
{
    direction_t* dirMap = new direction_t[width * height];
    for(int i = 0; i < width * height; i++)
    {
        int row = i / width;
        int col = i % width;

        int minHeight = map[i];
        dirMap[i] = BASIN;

        if(row - 1 >= 0) //North
        {
            int northValue = map[(row-1) * width + col];
            if(northValue < minHeight)
            {
                minHeight = northValue;
                dirMap[i] = NORTH;
            }
        }
        if(col - 1 >= 0) //West
        {
            int westValue = map[row * width + col - 1];
            if(westValue < minHeight)
            {
                minHeight = westValue;
                dirMap[i] = WEST;
            }
        }
        if(col + 1 < width) //East
        {
            int eastValue = map[row * width + col + 1];
            if(eastValue < minHeight)
            {
                minHeight = eastValue;
                dirMap[i] = EAST;
            }
        }
        if(row + 1 < height) //South
        {
            int southValue = map[(row+1) * width + col];
            if(southValue < minHeight)
            {
                minHeight = southValue;
                dirMap[i] = SOUTH;
            }
        }
    }
    /*if(dirMap[i] == NORTH)
        outStream << "^";
    else if(dirMap[i] == SOUTH)
        outStream << "v";
    else if(dirMap[i] == WEST)
        outStream << "<";
    else if(dirMap[i] == EAST)
        outStream << ">";
    else if(dirMap[i] == BASIN)
        outStream << "0";*/
    
    char* finalMap = new char[width * height];
    for(int i = 0; i < width * height; i++)
        finalMap[i] = 0;

    char currentBasin = 'a';
    for(int i = 0; i < width * height; i++)
    {
        if(finalMap[i] == 0)
        {
            if(traceMap(finalMap, dirMap, width, height, i, currentBasin) == currentBasin)
                currentBasin++;
        }
    }

    for(int h = 0; h < height; h++)
    {
        for(int w = 0; w < width; w++)
        {
            outStream << finalMap[width * h + w];
            if(w != width - 1)
                outStream << " ";
        }
        outStream << endl;
    }

    delete[] dirMap;
    delete[] finalMap;
}

int main(char** argv, int argc)
{
    ifstream myFile("example.txt");
    ofstream myAnswer("answer.txt");
    if (myFile.is_open())
    {
        int numberOfMaps = 0;
        myFile >> numberOfMaps;

        for(int i = 0; i < numberOfMaps; i++)
        {
            int height;
            int width;
            
            myFile >> height;
            myFile >> width;

            int* map = new int[width * height];
            for(int j = 0; j < width * height; j++)
            {
                myFile >> map[j];
            }
            myAnswer << "Case #" << i + 1 << ":" << endl;
            solve(map, width, height, myAnswer);
            delete[] map;
        }
    }
}