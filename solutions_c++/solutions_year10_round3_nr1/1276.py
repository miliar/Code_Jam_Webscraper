#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main(int argc, char *argv[])
{
    opterr = 0;
    char *filename = NULL;
    int c;

    while (( c = getopt(argc, argv, "hf:")) != -1)
    {
        switch(c)
        {
            case 'h':
            {
                cout << "Usage: ropenet -f <FILENAME>" << endl;
                exit(0);
            }
            case 'f':
            {
                filename = optarg;
                break;
            }
        }
    }

    if(!filename)
    {
        cout << "Usage: ropenet -f <FILENAME>" << endl;
        exit(0);
    }
    ifstream inputsrc(filename);

    char buff[30];

    inputsrc.getline(buff, 30);

    int lines = atoi(buff);
    
    int ncase = 1;
    while(lines > 0)
    {
        inputsrc.getline(buff, 30);

        int links = atoi(buff);
        
        map<int, int> linkmap;
        int intersect = 0;
        
        while(links > 0)
        {
            inputsrc.getline(buff, 30);
            string ln(buff);
            
            int bldgA = atoi(ln.substr(0, ln.find(" ")).c_str());
            int bldgB = atoi(ln.substr(ln.find(" ")).c_str());
            
            map<int, int>::iterator iterA  = linkmap.begin();
            while( iterA != linkmap.end())
            {
                if(bldgA < (*iterA).first && bldgB > (*iterA).second)
                    ++intersect;
                else if(bldgA > (*iterA).first && bldgB < (*iterA).second)
                    ++intersect;
                ++iterA;
            }
            linkmap[bldgA] = bldgB;
            
            --links;
        }
 
        cout << "Case #" << ncase << ": " << intersect << endl;
        
        --lines;
        ++ncase;
    }
    inputsrc.close();
}