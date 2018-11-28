#include <iostream>
#include <fstream>

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
                cout << "Usage: snapper -f <FILENAME>" << endl;
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
        cout << "Usage: snapper -f <FILENAME>" << endl;
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
        string ln(buff);
        
        int snappers = atoi(ln.substr(0, ln.find(" ")).c_str());
        int snaps = atoi(ln.substr(ln.find(" ")).c_str());
        
        int times = snappers;
        int mod_result;
        int snaps_q = snaps;
        bool wtblight = true;
        while(times > 0)
        {        
            mod_result = snaps_q % 2;
            snaps_q = snaps_q/2;

            if(mod_result != 1)
            {
                cout << "Case #" << ncase << ": OFF" << endl;
                wtblight = false;
                break;
            }
            --times;
        }
        if(wtblight)
        {
            cout << "Case #" << ncase << ": ON" << endl;
        }
        
        --lines;
        ++ncase;
    }
    
    inputsrc.close();
}
