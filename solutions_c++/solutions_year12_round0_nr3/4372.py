#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  int cases, output, a, b, current;
  
  ifstream myfile("C-small-attempt1.in");
  ofstream answer;
  answer.open ("answerC.out");
  
  myfile >> cases;
  
  for(int i=0; i < cases; ++i)
  {
    output = 0;
	myfile >> a >> b;
    answer << "Case #" << i+1 << ": ";
	for(int k=a; k <= b; ++k)
	{
	  if(k > 9 && k < 100)
	  {
	    current = k/10+k%10*10;
	    if(current > k && current <= b)
		  ++output;
	  }
	  else if(k >= 100)
	  {
	    current = k/100+k%100*10;
		if(current > k && current <= b)
		  ++output;
		current = k/100*10+k%10*100+k/10%10;
		if(current > k && current <= b)
		  ++output;
	  }
	}
	answer << output << endl;
  }
  
  answer.close();
  return 0;
}