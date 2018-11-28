#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    string in("A-small-attempt0.in");
    string out("output_1.txt");
    ifstream infile;
    infile.open(in.c_str(), ifstream::in);
    ofstream outfile;
    outfile.open(out.c_str(), ofstream::out);
    
    map<char,char> gmap;
    gmap.insert(pair<char,char>('y','a'));
    gmap.insert(pair<char,char>('n','b'));
    gmap.insert(pair<char,char>('f','c'));
    gmap.insert(pair<char,char>('i','d'));
    gmap.insert(pair<char,char>('c','e'));
    gmap.insert(pair<char,char>('w','f'));
    gmap.insert(pair<char,char>('l','g'));
    gmap.insert(pair<char,char>('b','h'));
    gmap.insert(pair<char,char>('k','i'));
    gmap.insert(pair<char,char>('u','j'));
    gmap.insert(pair<char,char>('o','k'));
    gmap.insert(pair<char,char>('m','l'));
    gmap.insert(pair<char,char>('x','m'));
    gmap.insert(pair<char,char>('s','n'));
    gmap.insert(pair<char,char>('e','o'));
    gmap.insert(pair<char,char>('v','p'));
    gmap.insert(pair<char,char>('z','q'));
    gmap.insert(pair<char,char>('p','r'));
    gmap.insert(pair<char,char>('d','s'));
    gmap.insert(pair<char,char>('r','t'));
    gmap.insert(pair<char,char>('j','u'));
    gmap.insert(pair<char,char>('g','v'));
    gmap.insert(pair<char,char>('t','w'));
    gmap.insert(pair<char,char>('h','x'));
    gmap.insert(pair<char,char>('a','y'));
    gmap.insert(pair<char,char>('q','z'));
    
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
                    cout << c; 
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
