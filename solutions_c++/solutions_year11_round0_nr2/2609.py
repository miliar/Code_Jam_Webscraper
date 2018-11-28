#include <stdio.h>
#include <tchar.h>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class Combine
{
  public:
    Combine( char e1, char e2, char result ) 
    {
      m_pattern.push_back( e1 ); 
      m_pattern.push_back( e2 ); 
      m_result.push_back( result ); 
    }
    
    bool match( std::string pattern )
    {
      if( pattern == m_pattern )
        return true;
      else if( pattern[ 1 ] == m_pattern[ 0 ] && pattern[ 0 ] == m_pattern[ 1 ] )
        return true;
      
      return false;
    }
    
    std::string m_pattern;
    std::string m_result;
};

class Oppose
{
  public:
    Oppose( char e1, char e2 ) : m_e1( e1 ), m_e2( e2 ), m_e1_found_ix( 0 ), m_e2_found_ix( 0 ) {};
    
    bool forms_opposition( char c )
    {
      if( c == m_e1 )
      {
        if( m_e2_found_ix > 0 )
        {
          m_e2_found_ix = 0;
          return true;
        }
        m_e1_found_ix++;
      }
      else if( c == m_e2 )
      {
        if( m_e1_found_ix > 0 )
        {
          m_e1_found_ix = 0;
          return true;
        }
        m_e2_found_ix++;
      }
      
      return false;
    }
    
    void remove_ix( char c )
    {
      if( c == m_e1 && m_e1_found_ix > 0 )
      {
        m_e1_found_ix--;
      }
      else if( c == m_e2 && m_e2_found_ix > 0 )
      {
        m_e2_found_ix--;
      }
    }
    
    char m_e1;
    int  m_e1_found_ix;
    char m_e2;
    int  m_e2_found_ix;
};

int _tmain(int argc, _TCHAR* argv[])
{
  int numCases = 0;
  //const string fileName = "A-test";
  const string fileName = "B-small-attempt2";
  //const string fileName = "B-large";

  ifstream inputFile((fileName + ".in").c_str());
  ofstream outputFile((fileName + ".out").c_str());

  inputFile >> numCases;

  for( int caseNumber = 1; caseNumber <= numCases; ++caseNumber )
  {
    // Read the inputs...May be multiple lines of inputs per case
    unsigned int c = 0;
    unsigned int ix = 0;
    inputFile >> c;
    
    vector< Combine > combine;
    
    char char1, char2, char3;
    
    for( ix = 0; ix < c; ++ix )
    {
      inputFile >> char1 >> char2 >> char3;
      
      combine.push_back( Combine( char1, char2, char3 ) );
    }
    
    unsigned int d = 0;
    inputFile >> d;
    
    vector< Oppose > oppose;
    
    for( ix = 0; ix < d; ++ix )
    {
      inputFile >> char1 >> char2;
      
      oppose.push_back( Oppose( char1, char2 ) );
    }
    
    unsigned int n = 0;
    inputFile >> n;
    
    std::string result = "";
    
    unsigned int result_size = 0;
    bool combined = false;
    
    for( ix = 0; ix < n; ++ix )
    {
      inputFile >> char1;
      
      result.push_back( char1 );
      
      result_size = result.size();
        
      combined = false;
        
      if( result_size > 1 )
      {
        for( unsigned int comb_ix = 0; comb_ix < combine.size(); ++comb_ix )
        {
          if( combine[ comb_ix ].match( result.substr( result_size - 2, 2 ) ) )
          {
            for( unsigned int opp_ix = 0; opp_ix < oppose.size(); ++opp_ix )
            {
              oppose[ opp_ix ].remove_ix( result[ result_size - 2 ] );
            }
            
            result = result.substr( 0, result_size - 2 ) + combine[ comb_ix ].m_result;
            combined = true;
            break;
          }
        } 
      }
      
      if( !combined )
      {
        for( unsigned int opp_ix = 0; opp_ix < oppose.size(); ++opp_ix )
        {
          if( oppose[ opp_ix ].forms_opposition( char1 ) )
          {
            result = "";
            break;
          }
        }
      }
    }

    // Output the results
    outputFile << "Case #" << caseNumber << ": [";
    
    result_size = result.size();
    for( ix = 0; ix < result_size; ++ix )
    {
      outputFile << result[ ix ];
      
      if( ix < result_size - 1 )
      {
        outputFile << ", ";
      }
    }
    outputFile << "]\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

