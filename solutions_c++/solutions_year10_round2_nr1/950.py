#include <stdio.h>
#include <tchar.h>
#include <string>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

class Dir
{
  public:
    string          m_name_s;
    map<string,Dir> m_child_dirs;
    
    Dir( string name_s ) : m_name_s( name_s )
    {
    }
    
    bool sub_dir_exists( string sub_dir_name_s )
    {
      return( m_child_dirs.find( sub_dir_name_s ) != m_child_dirs.end() );
    }
    
    int add_sub_dir( string sub_dir_name_s )
    {
      string            name_s           = "";
      int               num_dirs_created = 0;
      string            remaining_path_s = "";
      string::size_type next_slash       = sub_dir_name_s.find( "/", 1 );
      
      if( next_slash != string::npos )
      {
        name_s = sub_dir_name_s.substr( 1, next_slash - 1 );
        remaining_path_s = sub_dir_name_s.substr( next_slash ); 
      }
      else
      {
        name_s = sub_dir_name_s.substr( 1 );
      }
     
      map<string,Dir> ::iterator map_iter;
      map_iter = m_child_dirs.find( name_s );
      
      if( map_iter == m_child_dirs.end() )
      {
        Dir new_dir( name_s );
        
        if( remaining_path_s != "" )
        {
          num_dirs_created += new_dir.add_sub_dir( remaining_path_s );
        }
        
        ++num_dirs_created;
        m_child_dirs.insert( pair<string,Dir>( name_s, new_dir ) ); 
      }
      else if( remaining_path_s != "" )
      {
        num_dirs_created += map_iter->second.add_sub_dir( remaining_path_s );
      }
      
      return( num_dirs_created );
    }
};

int _tmain(int argc, char* argv[])
{
  int          num_cases   = 0;
  //xconst string file_name_s = "A-practice";
  //xconst string file_name_s = "A-small-attempt0";
  const string file_name_s = "A-large";

  ifstream input_file ( ( file_name_s + ".in"  ).c_str() );
  ofstream output_file( ( file_name_s + ".out" ).c_str() );

  input_file >> num_cases;
  
  for( int case_num = 1; case_num <= num_cases; ++case_num )
  {
    int n = 0;
    int m = 0;
    
    input_file >> n;
    input_file >> m;
    
    Dir root( "/" );
    
    for( int n_ix = 0; n_ix < n; ++n_ix )
    {
      string dir_name_s = "";
      input_file >> dir_name_s;
      
      root.add_sub_dir( dir_name_s );
    }
    
    int num_mkdirs = 0;
    for( int m_ix = 0; m_ix < m; ++m_ix )
    {
      string dir_name_s = "";
      input_file >> dir_name_s;
      
      num_mkdirs += root.add_sub_dir( dir_name_s );
    }
    
    // Output the results
    output_file << "Case #" << case_num << ": " << num_mkdirs << "\n";
  }

  // Close the streams
  input_file.close();
  output_file.close();

  return 0;
}

