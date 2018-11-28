#include <boost/thread.hpp>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;
string output[30];

void task1(int i, string g) { 

    map<char, string> Map;
    Map['a'] = "y";                                                                    
    Map['b'] = "h";                                                                    
    Map['c'] = "e";                                                                    
    Map['d'] = "s";                                                                    
    Map['e'] = "o";                                                                    
    Map['f'] = "c";                                                                    
    Map['g'] = "v";                                                                    
    Map['h'] = "x";                                                                    
    Map['i'] = "d";                                                                    
    Map['j'] = "u";                                                                    
    Map['k'] = "i";                                                                    
    Map['l'] = "g";                                                                    
    Map['m'] = "l";                                                                    
    Map['n'] = "b";                                                                    
    Map['o'] = "k";                                                                    
    Map['p'] = "r";                                                                    
    Map['q'] = "z";                                                                    
    Map['r'] = "t";                                                                    
    Map['s'] = "n";                                                                    
    Map['t'] = "w";                                                                    
    Map['u'] = "j";                                                                    
    Map['v'] = "p";                                                                    
    Map['w'] = "f";                                                                    
    Map['x'] = "m";                                                                    
    Map['y'] = "a";                                                                    
    Map['z'] = "q";                                                                    
    Map[' '] = " ";  

    string out;
    string fout = "";
    for(int j = 0, l = g.length(); j < l; j++) {
        out.append(Map[g[j]]);
    }

    stringstream ss;
    ss << i + 1;
    fout.append("Case #");
    fout.append(ss.str());
    fout.append(": ");
    fout.append(out);
    fout.append("\n");

    output[i] = fout;
    // cout<<"thread #"<<i<<" complete \n";
}


int main (int argc, char ** argv) {
    using namespace boost; 


    ifstream input_file;
    input_file.open("input.txt");

    assert(input_file.is_open());

    string line;
    // The first line contains the number of maps.
    getline(input_file, line); 

    int num_test = atoi(line.c_str());

    // cout<<num_test<<"\n";

    thread _thread[num_test];

    int case_num = 0;
    while (case_num < num_test) {
        assert(!input_file.eof());

        getline(input_file, line);
        // cout<<line<<"\n";

        _thread[case_num] = thread(
            boost::bind(task1, case_num, line));
        // out.append(Map[g[i]]);
        // cout<<"creating thread #"<<case_num<<"\n";

        case_num++;
    }

    // do other stuff
    for(int i = 1; i < case_num; i++)
       _thread[i].join();

    for(int i = 0; i < case_num; i++)
        cout<<output[i];

    return 0;
}

