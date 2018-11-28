#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    int T;
    vector<string> G, R;
    string const shifra("yhesocvxduiglbkrztnwjpfmaq");

    ifstream file("A-small-attempt0.in");

    //Star reading the file
    if(file)
    {
        file >> T;
        file.ignore();
        for(int i=0; i<T; i++)
        {
            string line;
            getline(file, line);
            G.push_back(line);
        }
    }
    else
        cout << "Error, The file A-small-practice.in not found!!" << endl;
    //End reading the file

    //Star solving the problem
    for(int i=0; i<T; i++)
    {
        R.push_back({});
        for(int j=0; j<G[i].size(); j++)
        {
            int tmp=G[i][j];

            if( G[i][j]==' ' )
                R[i]+=' ';
            else
                R[i]+=shifra[tmp-97];
        }
    }

    for(int i=0; i<T; i++)
    {
        cout << "Case #" << (i+1) << ": " << R[i] << endl;
    }
    //End solving the problem

    //Star writing th output
    string const fileN("output.out");
    ofstream outfile(fileN.c_str());
    if(outfile)
    {
        for(int i=0; i<T; i++)
        {
            outfile << "Case #" << (i+1) << ": " << R[i] << endl;
        }
    }
    else
    {
        cout << "ERROR: Can not open the file." << endl;
    }
    //End writing the output

    return 0;
}
