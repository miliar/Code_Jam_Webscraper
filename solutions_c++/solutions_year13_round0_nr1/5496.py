#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream infile;
    ofstream outfile;
    infile.open("A-small-attempt2.in");
    outfile.open("A-small-attempt2.out");   
    int T;
    infile >> T;
    int t = 0;
    char matrix[4][4];
    int count;
    char c;

    while(t < T)
    {
                t++;
                bool haswon = false;
                char winner;
                bool incomplete = false;
              for(int i = 0; i < 4; i++)
              {
                      count = 0;
                      for(int j = 0; j < 4; j++)
                      {
                              infile >> matrix[i][j];
                              if(matrix[i][j] == '.')
                              {
                                             incomplete = true;
                              }
                              if((j == 0) || (j == 1 && c == 'T'))
                              {
                                   c = matrix[i][j];
                                   count++;
                              }
                              else if(c == matrix[i][j] || matrix[i][j] == 'T')
                              {
                                   count++;
                              }
                      }
                      if(count == 4 && c != '.')
                      {
                               haswon = true;
                               winner = c;
                      }
              }
              if(haswon)
              {
                        outfile << "Case #" << t << ": " << winner << " won" << endl;
                        continue;
              }
              
              for(int j = 0; j < 4; j++)
              {
                      count = 0;
                      for(int i = 0; i < 4; i++)
                      {
                              if(matrix[i][j] == '.')
                              {
                                             incomplete = true;
                              }
                              if((i == 0) || (i == 1 && c == 'T'))
                              {
                                   c = matrix[i][j];
                                   count++;
                              }
                              else if((c == matrix[i][j] || matrix[i][j] == 'T'))
                              {
                                   count++;
                              }
                      }
                      if(count == 4 && c != '.')
                      {
                               haswon = true;
                               winner = c;
                               break;
                      }
              }
              if(haswon)
              {
                        outfile << "Case #" << t << ": " << winner << " won" << endl;
                        continue;
              }
              c = matrix [0][0];
              count = 1;
              if(c != '.')
              {
                  if(c == 'T')
                        c = matrix[1][1];
                   for(int i = 1; i < 4; i++)
                   {
                      if(matrix[i][i] == c || matrix[i][i] == 'T')
                          count++;
                      else
                          break;
                   }
              }
              if(count == 4 && c != '.')
              {
                        outfile << "Case #" << t << ": " << c << " won" << endl;
                        continue;
              }
              c = matrix [0][3];
              count = 1;
              if(c != '.')
              {
                   if(c == 'T')
                        c = matrix[1][2];
                   for(int i = 1; i < 4; i++)
                   {
                      if(matrix[i][3-i] == c || matrix[i][3-i] == 'T')
                          count++;
                      else
                          break;
                   }
              }
              if(count == 4)
              {
                        outfile << "Case #" << t << ": " << c << " won" << endl;
                        continue;
              }
              if(incomplete)
              {
                         outfile << "Case #" << t << ": " << "Game has not completed" << endl;
              }
              else
              {
                         outfile << "Case #" << t << ": " << "Draw" << endl;
              }
    }
    return 0;
}
