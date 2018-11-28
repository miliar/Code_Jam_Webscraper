#include <iostream>
#include <fstream>

// Files
#define INFILE "D:\\personal\\Workspace\\GoogleCodeJam\\iofiles\\B-large.in"
#define OUTFILE "D:\\personal\\Workspace\\GoogleCodeJam\\iofiles\\B-large.out"

using namespace std;

int max(int sc)
{
    switch(sc%3)
    {
    case 0:
        return sc/3;
    case 1:
        return (sc/3) + 1;
    case 2:
        return (sc/3) + 1;
    default:
        return (0);
    }
}

int smax(int sc)
{
    switch(sc%3)
    {
    case 0:
        return (sc/3) + 1;
    case 1:
        return (sc/3) + 1;
    case 2:
        return (sc/3) + 2;
    default:
        return (0);
    }
}

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

    for(int i=0; i<testcases;i++)
    {       
        // Solve problem here

        int goog = 0;

        int N;
        int S;
        int p;

        infile>>N>>S>>p;

        for(int j = 0; j<N;j++)
        {
            int score;
            infile>>score;
            if(!score)
            {
                if(!p)
                {
                    goog++;
                }
            }
            else if(max(score) >= p)
            {
                goog++;
            }
            else if((smax(score) >= p) && S>0)
            {
                goog++;
                S--;
            }
        }
        // Print output here
        outfile<<"Case #"<<i+1<<": "<<goog<<"\n";
    }
    infile.close();
    outfile.close();

    cout<<"\nDone! Press a key to close";
    cin.get();

	return 0;
}
