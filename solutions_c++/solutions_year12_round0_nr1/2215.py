#ifndef __INPUT_H__
#define __INPUT_H__

#include <iostream>
#include <string>
#include <list>
#include <cstdlib>
#include <fstream>
#include "key.h"
#include <algorithm>

typedef std::map<char,char> charMap;
static const size_t UPPER_LIMIT = 100;

class Input
{
public:
   Input(std::string const & filename);

   ~Input(){}

   bool parseFile();

   bool const &failed(){ return m_failed;}

   void decode(Key &key);

private:
   int                       m_numExamples;
   std::string               m_filename;
   bool                      m_failed;
   std::list<std::string>    m_coded;

   
};
#endif
