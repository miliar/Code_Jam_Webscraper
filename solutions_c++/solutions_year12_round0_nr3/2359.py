#ifndef __INPUT_H__
#define __INPUT_H__

#include <iostream>
#include <string>
#include <list>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>

struct Case
{
	std::vector<long int> upper;
	std::vector<long int> lower;
};

typedef std::list<Case> caseList;

static const long int MAX_UPPER_BOUND = 2000000;
static const long int MIN_LOWER_BOUND = 1;

class Input
{
public:
   Input(std::string const & filename);

   ~Input(){}

   bool parseFile();

   bool const &failed(){ return m_failed;}

   void processCases();

   long int countRecycled( Case const &incase);

   void combos(std::vector<long int> const & in, long int const & base,  long int const & max, long int const & min);

   long int convertToInt(std::vector<long int> const & in);


private:
   int                 m_numExamples;
   std::string         m_filename;
   bool                m_failed;
   caseList            m_cases;
   std::vector<int>    m_mask;
   
};
#endif
