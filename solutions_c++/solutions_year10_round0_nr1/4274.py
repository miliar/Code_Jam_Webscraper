#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

typedef enum
{
    NOPOWER,
    POWER
} powerState;

typedef enum
{
    OFF,
    ON
} snapperState;

class snapper
{
    public:
        snapper();

        powerState inPwr;
        snapperState state;
};

snapper::snapper()
    :inPwr(NOPOWER),
    state(OFF)
{}


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
                cout << "Usage: snapper -f <FILENAME>";
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
        cout << "Usage: snapper -f <FILENAME>";
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

        int ndevs = atoi(ln.substr(0, ln.find(" ")).c_str());
        int snaps = atoi(ln.substr(ln.find(" ")).c_str());
        
        snapper *sstack = new snapper[ndevs];
   
        sstack[0].inPwr = POWER;
    
        int snap = 1;
        for(snap; snap <= snaps; ++snap)
        {
            for(int i=(ndevs-1); i>-1; --i)
            {
                if(i == 0)
                {
                    sstack[i].state = (sstack[i].state == ON) ? OFF : ON;
                }
                if(i!=0 && sstack[i].inPwr == POWER)
                {
                    sstack[i].state = (sstack[i].state == ON) ? OFF : ON;
                }
    
                if(i<ndevs)
                {
                    for(int j = i+1; j<ndevs; j++)
                    {
                        sstack[j].inPwr = (sstack[j-1].state == ON && sstack[j-1].inPwr == POWER) ? POWER : NOPOWER;
                    }
                }
            }
            
        }

        cout << "Case #" << ncase << ": ";
        if(sstack[ndevs-1].inPwr == POWER && sstack[ndevs-1].state == ON)
        {
            cout << "ON";
        }
        else
        {
            cout << "OFF";
        }
    
        delete [] sstack;
    
        cout << endl;
        ncase++;
        --lines;
    }

    inputsrc.close();
}
