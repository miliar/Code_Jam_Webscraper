#include <stdio.h>
#include <tchar.h>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

void rotate_board( vector<vector<char>>& board, vector<int>& empty_rows, int n )
{
  for( int row = 0; row < n; ++row )
  {
    int open_col = n-1;
    bool empty_row = true;
    
    while( open_col > 0 && board[ row ][open_col] != '.' )
    {
      --open_col;
      empty_row = false;
    }
    
    if( open_col > 0 )
    {
      for( int col = open_col - 1; col >=0 && open_col > 0; --col )
      {
        if( board[row][col] != '.' )
        {
          empty_row = false;
          board[row][open_col] = board[row][col];
          board[row][col] = '.';
          
          --open_col;
          while( open_col > 0 && board[ row ][open_col] != '.' )
          {
            --open_col;
          }
        }
      }
    }
    
    if( empty_row )
    {
      empty_rows.push_back( row );
    }
  }
}

void transpose_board( vector<vector<char>>& board, int n )
{

  for( int row = 0; row < n; ++row )
  {
    for( int col = row + 1; col < n; ++col )
    {
      char temp = board[col][row];
      board[col][row] = board[row][col];
      board[row][col] = temp;
    }
  }
}

void verticalize_board( vector<vector<char>>& board, vector<vector<char>>& new_board, int n, int k )
{
  int total_num_rows = 2*n - 1;
  int min_start = k - 1;
  int min_end   = total_num_rows - min_start;
  
  for( int ix = min_start; ix < min_end; ++ix )
  {
    int row = min( ix, n - 1 );
    int col = ( ix >= n ? ix - n + 1 : 0 ); 
    vector<char> temp;
    
    while( row >= 0 && col < n )
    {
      temp.push_back( board[row][col] );
      --row;
      ++col;
    }
    
    new_board.push_back( temp );
  }
}

void k_in_a_row( const vector<vector<char>>& board, int n, int k, bool& red, bool& blue )
{
  std::string result = "";
  int empty_ix = 0;
  int row_size = board.size();
  
  for( int row = 0; row < row_size && ( !red || !blue ); ++row )
  {
    int col_size = board[row].size();
    for( int col = 0; col < col_size && ( !red || !blue ); ++col )
    {
      if( board[row][col] != '.' )
      {
        int in_a_row = 1;
        
        if( col_size - col >= k )
        {
          int next_col = col + 1;
          for( ; next_col < col_size && in_a_row < k; ++next_col )
          {
            if( board[row][col] != board[row][next_col] )
            {
              break;
            }
            else
            {
              ++in_a_row;
            }
          }
          
          if( in_a_row == k )
          {
            if( board[row][col] == 'R' )
            {
              red = true;
            }
            else
            {
              blue = true;
            }
            
            col = next_col + 1;
          }
        }
      }
    }
  }
}

void output_board( const vector<vector<char>>& board, int n, ofstream& output_file )
{
  for( int row = 0; row < board.size(); ++row )
  {
    for( int col = 0; col < board[row].size(); ++col )
    {
      output_file << board[ row ][ col ];
    }
    output_file << "\n";
  }
}

int _tmain(int argc, char* argv[])
{
  int          num_cases   = 0;
  const string file_name_s = "A-small-attempt0";

  ifstream input_file ( ( file_name_s + ".in"  ).c_str() );
  ofstream output_file( ( file_name_s + ".out" ).c_str() );

  input_file >> num_cases;
  
  for( int case_num = 1; case_num <= num_cases; ++case_num )
  {
    int n = 0;
    int k = 0;
    
    vector<vector<char>> board;
    vector<int> empty_rows;
    
    input_file >> n;
    input_file >> k;
    
    for( int row = 0; row < n; ++row )
    {
      vector<char> temp;
      for( int col = 0; col < n; ++col )
      {
        char c;
        input_file >> c;
        
        temp.push_back( c );
      }
      board.push_back( temp );
    }
    
    rotate_board( board, empty_rows, n );
    
    bool red = false;
    bool blue = false;
    
    //xoutput_board( board, n, output_file );
    
    k_in_a_row( board, n, k, red, blue );
    
    if( !red || !blue )
    {
      transpose_board( board, n );
      //xoutput_file << "Transposed: \n";
      //xoutput_board( board, n, output_file );
      
      k_in_a_row( board, n, k, red, blue );
    }
    
    if( !red || !blue )
    {
      vector<vector<char>> new_board;
      verticalize_board( board, new_board, n, k );
      
      //xoutput_file << "Verticalized: \n";
      //xoutput_board( new_board, n, output_file );
      
      k_in_a_row( new_board, n, k, red, blue );
    }
    
    string result_s = ( red ? ( blue ? "Both" : "Red" ) : ( blue ? "Blue" : "Neither" ) );
   
    // Output the results
    output_file << "Case #" << case_num << ": " << result_s << "\n";
  }

  // Close the streams
  input_file.close();
  output_file.close();

  return 0;
}

