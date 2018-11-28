#include<iostream>
#include<map>
#include<string>
#include<fstream>

using namespace std;

int main() 
{
    map<char,int> Googlerese;
    Googlerese['a'] = 'y';
    Googlerese['b'] = 'h';
    Googlerese['c'] = 'e';
    Googlerese['d'] = 's';
    Googlerese['e'] = 'o';
    Googlerese['f'] = 'c';
    Googlerese['g'] = 'v';
    Googlerese['h'] = 'x';
    Googlerese['i'] = 'd';
    Googlerese['j'] = 'u';
    Googlerese['k'] = 'i';
    Googlerese['l'] = 'g';
    Googlerese['m'] = 'l';
    Googlerese['n'] = 'b';
    Googlerese['o'] = 'k';
    Googlerese['p'] = 'r';
    Googlerese['q'] = 'z';
    Googlerese['r'] = 't';
    Googlerese['s'] = 'n';
    Googlerese['t'] = 'w';
    Googlerese['u'] = 'j';
    Googlerese['v'] = 'p';
    Googlerese['w'] = 'f';
    Googlerese['x'] = 'm';
    Googlerese['y'] = 'a'; 
    Googlerese['z'] = 'q';
    Googlerese[' '] = ' ';
    
    const char *ifile_name = "A-small-attempt0.in";
    const char *ofile_name = "A-small-attempt0.out";
    
    ifstream in;
    ofstream out;
    in.open(ifile_name);
    out.open(ofile_name);
    
    if( in.is_open() && out.is_open() )
    {
        int nb_cases;
        int counter = 1,i;
        char result[100];
        string line;
        
        in >> nb_cases;
        getline( in, line );
        for ( ; counter <= nb_cases ; counter++)
        {
             getline( in, line );
             for( i=0 ; i<line.size() ; i++)
             {
                     result[i] = Googlerese[line[i]];
             }
             result[i] = '\0';
             out << "Case #" << counter << ": " << result << endl;               
        }
        
    }
    else
    {
        cerr << "Could not open input and output file" << endl;
    }
    
    return 0;
}
