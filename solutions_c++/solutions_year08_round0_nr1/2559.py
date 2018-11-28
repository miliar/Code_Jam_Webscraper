#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;

#include "saveUniverse.h"

static fstream in, out;

void handleError (bool cond, char *str)
{
    if (cond)
	{
		cout << str << endl;
    	in.close ();
    	out.close ();
		exit (1);
	}
	return;
}

int main (int argc, char *argv[])
{
    if (argc < 3)
	{
		cout << "Usage : save in_file out_file" << endl;
		return 1;
	}
    in.open (argv[1], fstream::in);
    if (in.fail ())
    {
        cout <<"Error in opening input file" << endl;
        return 1;
    }
    out.open (argv[2], fstream::out);
    if (out.fail ())
    {
        cout <<"Error in opening out file" << endl;
        in.close ();
        return 1;
    }

    char buffer[BUFF_SIZE];
    in.getline (buffer, BUFF_SIZE); // Reading the number of cases
    handleError (in.fail (), "Error in reading from input file");

    int noOfCases = atoi (buffer);
	handleError (noOfCases > MAX_CASES,
							"Number of cases exceeded the maimum limit");

    int count = 1;

    while (count <= noOfCases)
        {
        in.getline (buffer, BUFF_SIZE); // Reading no of search engines.
    	handleError (in.fail (), "Error in reading from input file");
        
		int noOfSearchEngines = atoi (buffer);
		handleError (noOfSearchEngines > MAX_SE,
					"Number of search engines exceeded the maimum limit");
        int i, j;

		List s,q;

        for (i = 0; i < noOfSearchEngines; ++i)
            {
                in.getline (buffer, BUFF_SIZE);// Reading name of search engine.
    			handleError (in.fail (), "Error in reading from input file");
                
                s.push_back (buffer);
            }
        in.getline (buffer, BUFF_SIZE); // Reading number of queries.
    	handleError (in.fail (), "Error in reading from input file");
            
        int noOfQueries = atoi (buffer);
		handleError (noOfQueries > MAX_QRY,
					"Number of queries exceeded the maimum limit");

        for (j =0; j < noOfQueries; ++j)
            {
                in.getline (buffer, BUFF_SIZE); //Reading name of search engine.
    			handleError (in.fail (), "Error in reading from input file");
                    
                q.push_back (buffer);
            }
		saveUniverse su (s,q);
#ifdef DEBUG
		cout <<"Case # : " << count << endl;
		su.display ();
		cout << endl << endl;
#endif // DEBUG 
		out << "Case #" << count << ": " << su.minSwitchRequired () << endl;
        ++count;
        } // while case 
    in.close ();
    out.close ();
    return 0;
}

