#include <iostream>
using namespace std;

// Kikou les gens !
int main(int argc, char **argv) {

    int nbtests;
    cin >> nbtests;
    
    std::string line; 
    std::getline(cin, line);
    //string dico = "abcdefghijklmnopqrstuvwxyz ";
    string code = "yhesocvxduiglbkrztnwjpfmaq ";
    
    for (int test = 0; test < nbtests; test++)
    {
      std::getline(cin, line);
      int longueur = line.length();
      string res(longueur, ' ');
      
      for(int i = 0; i < longueur; i++)
      {
	char c = line.at(i);
	if(c != ' ')
	{ 
	  int nb = c-97;
	  res[i] = code[nb];
	}
	
      }
      cout << "Case #" << test+1 << ": " << res << endl;
    }
    
    return 0;
}
