// ProblemB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>

using namespace std;


int get_int( ifstream& inputFile )
{
  int i;
  inputFile >> i;

  return i;
}

char get_char( ifstream& inputFile )
{
  char c;
  inputFile >> c;

  return c;
}



const int NUM_BASE_ELEMENTS = 3;

void get_base_elements( ifstream& inputFile, char base_elements[] )
{
  for ( int i=0; i<NUM_BASE_ELEMENTS; i++ )
  {
    inputFile >> base_elements[i];  
  }
}




void get_w_and_q( ifstream& inputFile, int *w, int *q )
{
  // string input;
  // getline(inputFile, input);

  inputFile >> *w >> *q;

  // consume to end of line
  string input;
  getline(inputFile, input);
}

struct Combining
{
  char base_element1;
  char base_element2;
  char non_base_element;
};

struct Opposing
{
  char opposing1;
  char opposing2;
};



void get_combining_element( ifstream& inputFile, Combining & combining )
{
  // consume_spaces( inputFile );
  inputFile >> combining.base_element1;
  inputFile >> combining.base_element2;
  inputFile >> combining.non_base_element;
}


void get_combining_elements( ifstream& inputFile, vector< Combining >& combining_elements )
{
  int size = combining_elements.size();

  for ( int i=0; i<size; i++ )
  {
    get_combining_element( inputFile, combining_elements[i] );
  }
}

void get_opposing_element( ifstream& inputFile, Opposing & opposing )
{
  // consume_spaces( inputFile );
  inputFile >> opposing.opposing1;
  inputFile >> opposing.opposing2;
}




void get_opposing_elements( ifstream& inputFile, vector< Opposing >& opposing_elements )
{
  int size = opposing_elements.size();

  for ( int i=0; i<size; i++ )
  {
    get_opposing_element( inputFile, opposing_elements[i] );
  }
}

bool is_combining_match( const Combining& combining, const char char1, const char char2 )
{
  if ( combining.base_element1 == char1 && combining.base_element2 == char2 )
    return true;

  if ( combining.base_element1 == char2 && combining.base_element2 == char1 )
    return true;

  return false;
}


const char should_combine_to( const char char1, const char char2, bool * should_combine_p, const vector< Combining>& combining_elements )
{
  *should_combine_p = false;

  const int size = combining_elements.size();

  for ( int i=0; i<size; i++ )
  {
    if ( is_combining_match( combining_elements[i], char1, char2 ) )
    {
      *should_combine_p = true;
      return combining_elements[i].non_base_element;
    }
  }

  return 0;
}

bool find_in( const vector<char>& s, const char c )
{
  const int size = s.size();

  for ( int i=0; i<size; i++ )
  {
    if ( s[i] == c )
      return true;
  }

  return false;
}

bool is_opposed( const char next_char, const vector<char>& answer, const vector< Opposing >& opposing_elements )
{
  const int size = opposing_elements.size();

  for ( int i=0; i<size; i++ )
  {
    if ( next_char == opposing_elements[i].opposing1 ) 
    {
      if ( find_in( answer, opposing_elements[i].opposing2 ) )
      {
        return true;
      }
    }
    else if ( next_char == opposing_elements[i].opposing2 ) 
    {
      if ( find_in( answer, opposing_elements[i].opposing1 ) )
      {
        return true;
      }
    }
  }

  return false;
}



vector<char> read_and_process_base_elements( ifstream& inputFile, const int N, const vector< Combining>& combining_elements, const vector< Opposing >& opposing_elements )
{
  vector<char> answer;

  answer.reserve(N);

  for ( int i=0; i<N; i++ )
  {
    const char next_char = get_char( inputFile );
    if ( answer.size() == 0 )
    {
      answer.push_back( next_char );
    }

    else
    {
      char& last_char = answer[answer.size()-1];

      bool should_combine = false;
      const char combine_to = should_combine_to( next_char, last_char, &should_combine, combining_elements );

      if ( should_combine )
      {
        last_char = combine_to;
      }
      else
      {
        if ( is_opposed( next_char, answer, opposing_elements ) )
        {
          answer.clear();
        }
        else
        {
          answer.push_back( next_char );
        }
      }
    }
  }

  return answer;
}


string produce_answer( const vector<char>& raw_answer )
{
  string answer;

  const int size = raw_answer.size();

  answer.push_back( '[' );

  for ( int i=0; i<size; i++ )
  {
    if ( i > 0 )
    {
      answer.push_back( ',' );
      answer.push_back( ' ' );
    }

    answer.push_back( raw_answer[i] );
  }

  answer.push_back( ']' );

  return answer;
}

string get_and_process_case_input( ifstream& inputFile )
{
  const int C = get_int( inputFile );
  vector< Combining > combining_elements(C);
  
  get_combining_elements( inputFile, combining_elements );

  const int D = get_int( inputFile );
  vector< Opposing > opposing_elements(D);

  get_opposing_elements( inputFile, opposing_elements );

  const int N = get_int( inputFile );
  vector<char> raw_answer = read_and_process_base_elements( inputFile, N, combining_elements, opposing_elements );

  string answer = produce_answer( raw_answer );

  return answer;
}



int _tmain(int argc, _TCHAR* argv[])
{
  int numCases = 0;
  const string fileName = "B";

  ifstream inputFile((fileName + ".in").c_str());
  ofstream outputFile((fileName + ".out").c_str());
    
  string temp;
  getline(inputFile, temp);
  numCases = atoi(temp.c_str());

  for (int caseNumber = 1; caseNumber <= numCases; ++caseNumber)
  {
    string answer = get_and_process_case_input( inputFile );

    // Output the results
    if ( caseNumber > 1 )
    {
      outputFile << "\n";
    }

    outputFile << "Case #" << caseNumber << ": " << answer;
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

