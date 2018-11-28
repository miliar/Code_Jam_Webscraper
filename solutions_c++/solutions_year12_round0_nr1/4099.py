#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small.out");
    int T, N;
    fin >> T;
    
    char map[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    string sentence;
    getline(fin, sentence);
    
    for (int i = 1 ; i <= T; i++)
    {  
		getline(fin, sentence);

		for (int s = 0 ; s < sentence.size() ; s++)
		{
			if (sentence[s] == ' ')
				continue;
		    int a = (int)sentence[s]-97;
		    sentence[s] = map[a];
		}

		fout << "Case #" << i << ": ";
		fout << sentence << endl;
    }
}
