#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  ifstream input;
  ifstream output;
  input.open("/home/baran/projects/prjs/01/input.txt");
  output.open("/home/baran/projects/prjs/01/output.txt");
  string inputline, outputline;
  int havecoding = 0;
  int rows, i;
  char coding[26];
  if(input.is_open())
  {
    coding['q' - 97] = 'z';
    coding['z' - 97] = 'q';
    input >> rows;
    getline(input,inputline);
//    cout << "Rows: " << rows << " " << (int)'o' - 97 << " " << (int)'z' - 97 << endl;
    char ic, oc;
    while(input.good() && output.good() && rows-- > 0)
    {
      getline(input,inputline);
      getline(output,outputline);
      outputline = outputline.substr(outputline.find(": ") + 2);
      for(i = 0; i < inputline.length(); i++)
	if(inputline[i] != ' ')
	{
//	  cout << inputline[i] - 97 << " " << inputline[i] << " " << outputline[i] << endl;
	  coding[inputline[i] - 97] = outputline[i];
	}
/*      cout << ic << " " << int(ic) << " " << (int)'a' << " " << (int)'z' << endl;
      outputline = outputline.substr(outputline.find(": ") + 2);
      cout << inputline << endl;
      cout << outputline << endl;*/
    }
    for(char j = 97; j <= 122; j++)
      cout << j;
    cout << endl;
    cout << coding << endl;
    havecoding = 1;
  }

  input.close();
  output.close();
  
  if(havecoding)
  {
    int k;
    input.open("/home/baran/projects/prjs/01/A-small-attempt0.in");
    input >> rows;
    getline(input,inputline);
    for(i = 0; i < rows; i++)
    {
      getline(input,inputline);
//      cout << inputline << endl;
      cout << "Case #" << i + 1 << ": ";
      for(k = 0; k < inputline.length(); k++)
      {
	if(inputline[k] == ' ')
	  cout << ' ';
	else
	  cout << coding[inputline[k]-97];
      }
      cout << endl;
    }
    input.close();
  }
}
