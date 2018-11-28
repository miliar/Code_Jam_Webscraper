/*********************************************************************/
/*                                                                   */
/* Program to solve the "Dancing With the Googlers" problem, posed   */
/* for the 2012 Google Code Jam. Uses only standard C++ libraries.   */
/*                                                                   */
/* Using gcc, compile as: g++ -o dancing dancing.cpp                 */
/*                                                                   */
/* Usage: dancing <input data file> <output file>                    */
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
  int N, S, p;
  int regular_thresh, surprising_thresh;
  int must_be_surprising, can_be_regular;
  int score;
  input.open(argv[1]);
  output.open(argv[2]);
  if ((!input.is_open()) || (!output.is_open())) return 1;
  input >> num_inputs;
  for (int n = 0; n < num_inputs; n++) {
    input >> N >> S >> p;
    switch (p) {
      case 0:
	regular_thresh = 0;
	surprising_thresh = 2;
	break;
      case 1:
	regular_thresh = 1;
	surprising_thresh = 2;
	break;
      default:
	regular_thresh = 3*p-2;
	surprising_thresh = 3*p-4;
	break;
    }
    must_be_surprising = 0;
    can_be_regular = 0;
    for (int m = 0; m < N; m++) {
      input >> score;
      if (score >= regular_thresh) can_be_regular++;
      else if (score >= surprising_thresh) must_be_surprising++;
    }
    if (must_be_surprising > S) must_be_surprising = S;
    output << "Case #" << (n+1) << ": " << (can_be_regular+must_be_surprising) << "\n";
  }
  input.close();
  output.close();
  return 0;
}