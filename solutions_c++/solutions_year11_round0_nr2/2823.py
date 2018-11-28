// magicka.cpp : Defines the entry point for the console application.
//

#include "targetver.h"

#include <tchar.h>

#include <iostream>
#include <fstream>
#include <vector>
#include <cassert>
#include <string>
#include <array>


using namespace std;

void invoke(char c, const vector<std::array<char,3>>& vcombine,
  const vector<std::array<char,2>>& voppose,
  string* presult){

  string& result = *presult;

  if(result.size() == 0){
    result.push_back(c);
    return;
  }

  char last = result.back();
  char next = c;
  for(int icombine = 0, ncombine = vcombine.size(); icombine < ncombine;
    ++icombine){

    const std::array<char,3>& combine = vcombine[icombine];
    if((combine[0] == c && combine[1] == last) ||
      (combine[0] == last && combine[1] == c)){

      result.pop_back();
      next = combine[2];
      break;
    }
  }

  for(int ioppose = 0, noppose = voppose.size(); ioppose < noppose;
    ++ioppose){

    const std::array<char,2>& oppose = voppose[ioppose];
    if((oppose[0] == next && result.find(oppose[1]) != string::npos)
      || (oppose[1] == next && result.find(oppose[0]) != string::npos)){
      result.clear();
      return;
    }
  }

  result.push_back(next);
}

void run(istream& input){
  char *base = "QWERASDF";

  int ncases;
  input >> ncases;

  for(int icase = 0; icase < ncases; ++icase){

    int ncombines;
    input >> ncombines;
    vector<std::array<char,3>> vcombine;

    for(int icombine = 0; icombine < ncombines; ++icombine){
      std::array<char,3> combine;
      input >> combine[0];
      input >> combine[1];
      input >> combine[2];

      vcombine.push_back(combine);
    }

    int noppose;
    input >> noppose;
    vector<std::array<char,2>> voppose;

    for(int ioppose = 0; ioppose < noppose; ++ioppose){
      std::array<char,2> oppose;
      input >> oppose[0];
      input >> oppose[1];

      voppose.push_back(oppose);
    }

    int nchars;
    input >> nchars;

    string chars;
    input >> chars;

    assert(chars.size() == nchars);

    string result;

    for(int ichar = 0; ichar < nchars; ++ichar){
      invoke(chars[ichar], vcombine, voppose, &result);
    }

    string outstr;
    for(int ires = 0, nres = result.size(), ireslast = nres - 1;
      ires < nres; ++ires){

      outstr.push_back(result[ires]);
      if(ires < ireslast){
        outstr.append(", ");
      }
    }

    cout << "Case #" << icase + 1 << ": [" << outstr << "]" << endl;
  }

}

int _tmain(int argc, _TCHAR* argv[])
{

  if(argc > 1)
    run(ifstream(argv[1]));
  else
    run(cin);

	return 0;
}

