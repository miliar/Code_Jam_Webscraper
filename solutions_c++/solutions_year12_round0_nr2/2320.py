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

struct Case
{
	int numPeople;
	int surprises;
	int minScore;
	std::vector<int> scores;
};

typedef std::list<Case> caseList;

class Input
{
public:
   Input(std::string const & filename);

   ~Input(){}

   bool parseFile();

   bool const &failed(){ return m_failed;}

   void processCases();

   bool checkScore(int const & score, int const & threshold, bool const & surprise);


private:
   int                 m_numExamples;
   std::string         m_filename;
   bool                m_failed;
   caseList            m_cases;
   
};
#endif
