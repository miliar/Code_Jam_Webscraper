/*********************************************************************/
/*                                                                   */
/* Program to solve the "Speaking in Tongues" problem, posed for the */
/* 2012 Google Code Jam. Uses only standard C++ libraries.           */
/*                                                                   */
/* Using gcc, compile as: g++ -o tongues tongues.cpp                 */
/*                                                                   */
/* Usage: tongues <input data file> <output file>                    */
/*                                                                   */
/* By Peter Mattsson (peter.mattsson@lineone.net)                    */
/*                                                                   */
/* Licence: Public Domain (or as specified by Google)                */
/*                                                                   */
/*********************************************************************/

#include <iostream>
#include <fstream>
using namespace std;
  
int main(int argc, const char* argv[]) {
  if (argc != 3) {
    cout << "Usage: " << argv[0] << " <input data file> <output file>\n";
    return 1;
  }
  ifstream input;
  ofstream output;
  int num_inputs;
  string googlerese;
  string english;
  char mapping[27] = "yhesocvxduiglbkrztnwjpfmaq";
  input.open(argv[1]);
  output.open(argv[2]);
  if ((!input.is_open()) || (!output.is_open())) return 1;
  input >> num_inputs;
  getline(input, googlerese);
  for (int n = 0; n < num_inputs; n++) {
    getline(input, googlerese);
    english = "";
    for (int m = 0; m < googlerese.length(); m++) {
      char character = googlerese.at(m);
      if (character != ' ') character = mapping[character-'a'];
      english += character;
    }
    output << "Case #" << (n+1) << ": " << english << "\n";
  }
  input.close();
  output.close();
  return 0;
}