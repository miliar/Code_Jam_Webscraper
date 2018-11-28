/*
 * =====================================================================================
 *
 *       Filename:  waterSheds.cpp
 *
 *    Description:
 *           
 *            How to run:   ./a.out inputfile outputfile
 *
 *        Version:  1.0
 *        Created:  09/03/2009 09:26:33 PM
 *       Revision:  none
 *       Compiler:  g++
 *
 *         Author:  Mehul Rathod ( rathodmehul@gmail.com )
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;


struct waterShedsData
{
    static const int limit = 100;
    int  H;
    int  V;

    long  altitude  [limit][limit];

    int  sinkRowNo [limit][limit];
    int  sinkColNo [limit][limit];
    
    char basin     [limit][limit];

    char currBasinName;

    waterShedsData(int row, int col)
    {
        H = row;
        V = col;



        currBasinName = 'a';


        for(int i = 0; i < H; i++)
        {
            for(int j = 0; j < V; j++)
            {
                basin     [i][j] = 0; 
                sinkRowNo [i][j] = i; // self row
                sinkColNo [i][j] = j; // self column
            }
        }    
    }

};

static void solveAProblem(int no, ifstream &din, ofstream &dout);

int main(int argc, char** argv)
{
    if(argc < 3)
        return 0;

    int problemCount = 0;

    ifstream din(argv[1]);
    ofstream dout(argv[2]);

    din >> problemCount;    

    string junk;

    getline(din,junk);

    for(int i = 0; i < problemCount; i++)
    {
        solveAProblem(i,din,dout);
    }

    din.close();
    dout.close();

    return 0;

}

static long checkNeighbour(waterShedsData &data, long altitude, 
        int currRow, int currCol, int checkRow, int checkCol)
{
    if(checkRow < 0 || checkRow >= data.H)
        return altitude;
    
    if(checkCol < 0 || checkCol >= data.V)
        return altitude;

    if(data.altitude[checkRow][checkCol] < altitude)
    {
   
       data.sinkRowNo[currRow][currCol] = checkRow;     
       data.sinkColNo[currRow][currCol] = checkCol;     

       return  data.altitude[checkRow][checkCol];
    }

    return altitude;    

}

static void findSink(waterShedsData &data)
{
    for(int i=0; i < data.H; i++)
    {
        for(int j=0; j < data.V; j++)
        {
            long altitude = data.altitude[i][j];
            altitude = checkNeighbour(data,altitude,i,j,i-1,j); // North
            altitude = checkNeighbour(data,altitude,i,j,i,j-1); // West
            altitude = checkNeighbour(data,altitude,i,j,i,j+1); // East
            altitude = checkNeighbour(data,altitude,i,j,i+1,j); // South
        }
    } 
}    

static char traverseForBasinName(waterShedsData &data, int row, int col)
{
    if(data.basin[row][col]!=0) // already assigned name
        return data.basin[row][col];

    char basinName = 0;
    
    if(row == data.sinkRowNo[row][col] &&
       col == data.sinkColNo[row][col]    ) // self sink
    {
         basinName = data.currBasinName; 
         
         data.currBasinName++;   
    }
    else
    {
        basinName = traverseForBasinName(data,
                data.sinkRowNo[row][col],data.sinkColNo[row][col]); 

    }    
    
    data.basin[row][col] =  basinName;

    return basinName;

}

static void applyLabelsOnBasin(waterShedsData &data)
{
    for(int i=0; i < data.H; i++)
    {
        for(int j=0; j < data.V; j++)
        {
            traverseForBasinName(data,i,j);
        }
    }   
}


static void solveAProblem(int no, ifstream &din, ofstream &dout)
{
    

    int row, col;

    din >> row;
    din >> col;
    
    waterShedsData data(row, col);

    string newLine;
    getline(din,newLine);

    
    for(int i=0; i < data.H; i++)
    {
        for(int j=0; j < data.V; j++)
        {
            din >> data.altitude[i][j];
        }
        getline(din,newLine);
    }    

    findSink(data);

    applyLabelsOnBasin(data);

    dout << "Case #" << (no+1) << ":" << endl ;

    for(int i=0; i < data.H; i++)
    {
        for(int j=0; j < data.V; j++)
        {
           if(j!=0)
             dout << " ";   
             dout  <<  data.basin[i][j];
        }
        dout << endl;
    } 

}


