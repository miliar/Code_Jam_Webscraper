#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
  int L, D, N;
  
  ifstream in("A-large.in");
  ofstream out("output.txt");
  
  in >> L;
  in >> D;
  in >> N;
  
  char dictionary[D][L];
  
  for( int i = 0; i < D; i++ )
  {
    string word;
    in >> word;
    for( int j = 0; j < L; j++ )
    {
      dictionary[i][j] = word.at(j);
    }
  }
  
  for( int i = 0; i < N; i++ )
  {
    string testword;
    in >> testword;
    
    char ltrlist[L][testword.size()];
    
    for( int j = 0; j < testword.size(); j++ )
    {
      for( int k = 0; k < L; k++ )
      {
        ltrlist[k][j] = '\0';
      }
    }
    
    int ii = 0;
    
    for( int j = 0; j < testword.size(); j++ )
    {
      if ( testword.at(j) == '(' )
      {
        j++;
        
        int jj = 0;
        
        while ( testword.at(j) != ')' )
        {
          ltrlist[ii][jj] = testword.at(j);
          jj++;
          j++;
        }
        
        ii++;
      }
      else
      {
        ltrlist[ii][0] = testword.at(j);
        ii++;
      }
    }
    
    int flags[D][L];
    
    for( int j = 0; j < D; j++ )
    {
      for( int k = 0; k < L; k++ )
      {
        flags[j][k] = 0;
      }
    }
    
    for( int j = 0; j < L; j++ )
    {
      int jj = 0;
      while ( ltrlist[j][jj] != '\0' )
      {
        for( int k = 0; k < D; k++ )
        {
          if ( ltrlist[j][jj] == dictionary[k][j] )
          {
            flags[k][j] = 1;
          }
        }
        jj++;
      }
    }
    
    int num_possible = 0;
    
    for( int ii = 0; ii < D; ii++ )
    {
      int flag = 1;
      for( int j = 0; j < L; j++ )
      {
        if ( flags[ii][j] == 0 )
        {
          flag = 0;
        }
      }
      
      if ( flag == 1 )
      {
        num_possible++;
      }
    }
    
    out << "Case #" << i + 1 << ": " << num_possible << endl;
  }
  
  in.close();
  out.close();
  
  return 0;
}
