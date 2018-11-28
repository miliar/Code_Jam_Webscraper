#include <cstdlib>
#include <iostream>
#include <fstream>
using namespace std;
bool checkMatrix(char ** matrix, int row_num, int col_num)
{
     int row,col;
                for(row = 0; row<row_num; row++)
                {
                        for(col = 0; col<col_num; col++)
                        {
                               if(matrix[row][col] == '#')
                               {
                                                   if(row == row_num-1 || col == col_num-1)
                                                   return false;
                                   if((matrix[row][col+1] == '#') && (matrix[row+1][col] == '#') && (matrix[row+1][col+1] == '#'))
                                   {
                                                          matrix[row][col] = '/';
                                                          matrix[row][col+1] = '\\';  
                                                          matrix[row+1][col] = '\\'; 
                                                          matrix[row+1][col+1] = '/';}
                                   else
                                   return false; 
                               }
                        }
                }
                return true;
}
void printMatrix(ofstream &ofile, char**matrix, int row_num, int col_num)
{
     int row,col;
      for(row = 0; row<row_num; row++)
                {
                        for(col = 0; col<col_num; col++)
                        {
                                ofile<<matrix[row][col];
                        }
                        ofile<<endl;
                }
}
int main(int argc, char *argv[])
{
    ifstream ifile;
    ifile.open("A-large.in");
    ofstream ofile;
    ofile.open("output.txt");
    int cases_num;
    ifile>>cases_num;
    int test;
    for(test=0; test<cases_num; test++)
    {
                int row_num, col_num;
                ifile>> row_num; ifile>> col_num;
                char ** matrix = new char * [row_num];
                int row,col;
                for(row = 0; row<row_num; row++)
                {
                        matrix[row] = new char[col_num];
                        for(col = 0; col<col_num; col++)
                        {
                                ifile>>matrix[row][col];
                        }
                }
                ofile<< "Case #"<<test+1<<":"<<endl;
                if(checkMatrix(matrix, row_num,col_num))
                {
                                       printMatrix(ofile, matrix, row_num, col_num);
                }
                else
                ofile<<"Impossible"<<endl; 
                for(row = 0; row<row_num; row++)
                { delete  matrix[row];}
                delete [] matrix; matrix =0;                          
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}
