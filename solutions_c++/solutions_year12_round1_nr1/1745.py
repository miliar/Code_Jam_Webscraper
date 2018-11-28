
#include <iostream>
#include <algorithm>
using namespace std;

int main ()
{
  int T;
  cin >> T;

  for (int caseNo = 1; caseNo <= T; caseNo ++)
    {
      int A, B;
      cin >> A >> B;

      double p[A];

      for (int i = 0; i < A; i++)
	{
	  cin >> p[i];
	}

      double probAllOk = 1;
      for (int i = 0; i < A; i++)
	{
	  probAllOk *= p[i];
	}

      double probAllExceptLast = 1;
      for (int i = 0; i < A-1; i++)
	{
	  probAllExceptLast *= p[i];
	}
      
      double probAllExceptTwoLast = 1;
      for (int i = 0; i < A-2; i++)
	{
	  probAllExceptTwoLast *= p[i];
	}

      double rightAway = 1 + B + 1;

      double correctedOK =
	probAllExceptLast * (1-p[A-1]) +
	probAllExceptLast * (  p[A-1]);
      
      double withBackspaceOnce = 
	(correctedOK) * (1 + B-A+1 + 1) +
	(1 - correctedOK) * (1 + B-A+1 + 1 + B + 1);
	
      ;

      double withBackspaceTwice = -1;

      if (A == 1)
	{
	  withBackspaceTwice = withBackspaceOnce;
	}
      else
	{
	  double correctedOK =
	    probAllOk +
	    probAllExceptTwoLast * (1-p[A-2]) * (1-p[A-1]) +
	    probAllExceptTwoLast * (  p[A-2]) * (1-p[A-1]) +
	    probAllExceptTwoLast * (1-p[A-2]) * (  p[A-1]);

	  // cout << correctedOK << endl;
	  
	  withBackspaceTwice =
	    correctedOK * (2 + B-A+2 + 1) +
	    (1 - correctedOK) * (2 + B-A+2 + 1 + B + 1);
	}
      
      double keepTyping = probAllOk * (B-A + 1) + (1 - probAllOk) * (B-A + 1 + B + 1);

      cout.precision (6);
      cout << fixed;
      // cout << "A: " << A << ", B: " << B << endl;
      // cout << keepTyping << "\t" << rightAway << "\t" << withBackspaceOnce << "\t" << withBackspaceTwice << endl;

      cout << "Case #" << caseNo << ": " << std::min (std::min (std::min (keepTyping, withBackspaceOnce), withBackspaceTwice), rightAway) << endl;

      // cout << "probAllOk: " << probAllOk << ", other: " << (1 - probAllOk) << ", (B-A + 1): " << ((B-A + 1)) << ", (B-A + 1 + B + 1): " << (B-A + 1 + B + 1) << endl;
    }
  
  return 0;
}
