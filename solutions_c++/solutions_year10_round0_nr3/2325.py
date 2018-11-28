// CodeJam2010.cpp : Defines the entry point for the console application.

#include "stdafx.h"
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
typedef std::vector<std::string> strVector; 
typedef std::vector<int>         intVector; 

class BaseJam
{ 
public:
  BaseJam( const std::string fileName ); 
  ~BaseJam();
  
  virtual void execute() = 0;
  
  std::string get_next_line_str();
  strVector   get_next_line_tokens();
  intVector   get_next_line_tokens_int();

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

intVector BaseJam::get_next_line_tokens_int()
{
  intVector tokens;
  std::string next_line = get_next_line_str();
  istringstream iss(next_line);
  copy(istream_iterator<int>(iss), istream_iterator<int>(), back_inserter<vector<int> >(tokens));

  return tokens;
}
 


class Jam3 : public BaseJam
{
public:
  Jam3(const std::string fileName): BaseJam(fileName){}  
  void execute();
  
private:
  void run_daily_roller_coaster();
  void load_next_roller_coaster_run();
  
  int m_Runs_Per_Day            ;
  int m_Roller_Coaster_Capacity ;
  int m_Number_of_Groups        ;
  int m_Euros_Earned_Today      ;
  int m_queue_ix                ;
  int m_Current_Run_Capacity    ;

   
   enum LINE1
   {
     RUNS_IX       =0,
     CAPACITY_IX   =1,
     NUM_GROUPS_IX =2
   };
};

void Jam3::execute()
{
  if(m_outputFile != NULL)
  {
     
    int num_cases = atoi(get_next_line_str().c_str());
    for(int i=1;i<=num_cases;++i)
    {
      //The first line contains three space-separated integers: R, k and N.
      run_daily_roller_coaster();
      *m_outputFile << "Case #" << i << ": " << m_Euros_Earned_Today << "\n";
    }
  }
} 
void Jam3::run_daily_roller_coaster()
{
  strVector line1 = get_next_line_tokens();
  m_Runs_Per_Day            = atoi(line1 [RUNS_IX]      .c_str());
  m_Roller_Coaster_Capacity = atoi(line1 [CAPACITY_IX]  .c_str());
  m_Number_of_Groups        = atoi(line1 [NUM_GROUPS_IX].c_str());
  m_Euros_Earned_Today      = 0;
  m_queue_ix                = 0;
  m_Current_Run_Capacity   = 0;

  if(m_Number_of_Groups > 0)
  {
    load_next_roller_coaster_run();
  }
}

void Jam3::load_next_roller_coaster_run()
{
  intVector line2 = get_next_line_tokens_int();
  for(int j=0; j<m_Runs_Per_Day;++j)
  {
    m_Current_Run_Capacity = 0;
    for(int k=1;m_Current_Run_Capacity < (m_Roller_Coaster_Capacity+1);++m_queue_ix,++k)
    {
      if(k>m_Number_of_Groups) 
      {
        break;
      }
      if(m_queue_ix==m_Number_of_Groups)
      {
        m_queue_ix = 0;
      }
      if(m_Current_Run_Capacity+line2[m_queue_ix] <= m_Roller_Coaster_Capacity)
      {
        m_Current_Run_Capacity += line2[m_queue_ix];
      }
      else
      {
        break;
      }

    }
    m_Euros_Earned_Today+=m_Current_Run_Capacity;
  }
}




int _tmain(int argc, _TCHAR* argv[])
{
  Jam3 theme_park1("C-small-attempt0");
  theme_park1.execute();
  
  
  return 0;
}

