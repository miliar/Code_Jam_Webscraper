#include <iostream>
#include <fstream>

// Files
#define INFILE "D:\\personal\\Workspace\\GoogleCodeJam\\iofiles\\A-small-attempt1.in"
#define OUTFILE "D:\\personal\\Workspace\\GoogleCodeJam\\iofiles\\A-small-attempt1.out"

using namespace std;

char map[] = {
    'y',
    'h',
    'e',
    's',
    'o',
    'c',
    'v',
    'x',
    'd',
    'u',
    'i',
    'g',
    'l',
    'b',
    'k',
    'r',
    'z',
    't',
    'n',
    'w',
    'j',
    'p',
    'f',
    'm',
    'a',
    'q'
};



int main()
{
    ifstream infile;
    infile.open(INFILE);
    if (!infile.is_open())
    {
        cout<<"\nfailed to open in-file";
        cin.get();
        return 0;
    }

    ofstream outfile;
    outfile.open(OUTFILE); 
    if (!outfile.is_open())
    {
        cout<<"\nfailed to open out-file";
        cin.get();
        return 0;
    }

    int testcases;
    infile>>testcases;
        
    char G[101];
    infile.get();
    for(int i=0; i<testcases;i++)
    {       
        // Solve problem here
        memset(G, 0, 101);        
        infile.getline(G, 101, '\n');

        for(int a=0; G[a]; a++)
        {
            if(G[a]>= 'a' && G[a] <= 'z')
            {
                G[a] = map[G[a] - 'a'];
            }
        }
        // Print output here
        outfile<<"Case #"<<i+1<<": "<<G<<"\n";
    }
    infile.close();
    outfile.close();

    cout<<"\nDone! Press a key to close";
    cin.get();

	return 0;
}
