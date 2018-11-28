#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    string in("A-small-attempt0.in");
    ifstream infile;
    infile.open(in.c_str(), ifstream::in);
    
    size_t found = in.find_last_of(".in");
    string out = in.replace(found-1, 2, "out");    
    ofstream outfile;
    outfile.open(out.c_str(), ofstream::out);
    
    map<char,char> gmap;
    gmap['y'] = 'a';
    gmap['n'] = 'b';
    gmap['f'] = 'c';
    gmap['i'] = 'd';
    gmap['c'] = 'e';
    gmap['w'] = 'f';
    gmap['l'] = 'g';
    gmap['b'] = 'h';
    gmap['k'] = 'i';
    gmap['u'] = 'j';
    gmap['o'] = 'k';
    gmap['m'] = 'l';
    gmap['x'] = 'm';
    gmap['s'] = 'n';
    gmap['e'] = 'o';
    gmap['v'] = 'p';
    gmap['z'] = 'q';
    gmap['p'] = 'r';
    gmap['d'] = 's';
    gmap['r'] = 't';
    gmap['j'] = 'u';
    gmap['g'] = 'v';
    gmap['t'] = 'w';
    gmap['h'] = 'x';
    gmap['a'] = 'y';
    gmap['q'] = 'z';
    
    int t = 0;
    infile >> t;
    //cout << t << endl;
    char* line = new char[1024];
    infile.getline(line, 1024);    
    
    for (int i = 1; i < t+1; i++)
    {
        strcpy(line, "");
        infile.getline(line, 1024);
        //cout << line << endl;
        outfile << "Case #" << i << ": ";
        string word;
        istringstream strm(string(line), istringstream::in);  
        while (strm >> word)
        {
              int j = 0;
              while (word[j++])
              {
                    char c = gmap[word[j-1]]; 
                    //cout << c; 
                    outfile << c;                   
              }              
              //cout << " ";
              outfile << " ";
        } 
        //cout << endl;     
        outfile << endl;
    }
    infile.close();
    outfile.close();
    //cin.get();    
    return 0;
}
