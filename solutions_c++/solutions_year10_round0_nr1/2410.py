// CodeJam2010.cpp : Defines the entry point for the console application.

#include "stdafx.h"
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
typedef std::vector<std::string> strVector; 

class BaseJam
{ 
public:
  BaseJam( const std::string fileName ); 
  ~BaseJam();
  
  std::string get_next_line_str();
  strVector   get_next_line_tokens();

protected:  
  void create_file_streams( const std::string fileName );
  void close_file_streams();

  std::string m_fileName;
  std::ifstream* m_inputFile;
  std::ofstream* m_outputFile;
};

BaseJam::BaseJam( const std::string fileName )
{
  m_fileName = fileName;
  create_file_streams(fileName);
}

BaseJam::~BaseJam()
{
  close_file_streams();
}

void BaseJam::create_file_streams(const std::string fileName)
{
  m_inputFile = new std::ifstream((m_fileName + ".in").c_str());
  m_outputFile= new std::ofstream((m_fileName + ".out").c_str());
}

void BaseJam::close_file_streams()
{
  // Close the streams
  m_inputFile->close();
  m_outputFile->close();

  delete m_inputFile;
  delete m_outputFile;
} 

std::string BaseJam::get_next_line_str()
{ 
  std::string input = "";
  if(m_inputFile != NULL)
  {
    std::getline(*m_inputFile, input);
  }
  return input;
} 

strVector BaseJam::get_next_line_tokens()
{
  strVector tokens;
  std::string next_line = get_next_line_str();
  istringstream iss(next_line);
  copy(istream_iterator<string>(iss), istream_iterator<string>(), back_inserter<vector<string> >(tokens));
  
  return tokens;
}

class Jam1 : public BaseJam
{
public:
  Jam1(const std::string fileName): BaseJam(fileName){}
  void execute(); 
  
private:
  std::string light_status();
  int m_N_snappers;
  int m_K_snaps;
};
 
void Jam1::execute()
{
  int num_cases = atoi(get_next_line_str().c_str());
  for(int i=1;i<=num_cases;++i)
  {
    strVector v = get_next_line_tokens();
    m_N_snappers = atoi(v[0].c_str());
    m_K_snaps    = atoi(v[1].c_str());
    
    *m_outputFile << "Case #" << i << ": " << light_status() << "\n";
  } 
}

std::string Jam1::light_status()
{
  return (((m_K_snaps + 1) % int(pow(2.0, m_N_snappers)) ==0 ) ? "ON" : "OFF");
}

int _tmain(int argc, _TCHAR* argv[])
{
  Jam1 snapper_chain("A-large");
  snapper_chain.execute(); 
  
  return 0;
}

