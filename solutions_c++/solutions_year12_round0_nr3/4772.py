#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main ()
{
	string arr[100];
	int loop=0;
	int tot;
	int i;
	int A;
	int B;
	int j;
	int k;
	int count;
	int final2;

	string tempnum;
	string temp1;
	string temp2;
	string final;
	string first;
	string second;
	string sub;
	string line;
	string nline;
	int last;

	char buffer [33];
	ifstream myFile("C:/users/bhcomp/desktop/C-small-attempt1.in");
	if (myFile.is_open())
	{
		while (!myFile.eof())
		{
			getline(myFile,line);
            cout << loop;
			arr[loop]=line;
			loop++;
		}
		myFile.close();
	}
    ofstream f("c:/users/bhcomp/desktop/outputA.txt");
	tot=atoi(arr[0].c_str());

	for(i=1; i<=tot; i++)
	{
	    if (i>1) {f << "\n";}
	    f << "Case #" << i << ": ";
		count=0;
		nline=arr[i];
		first = nline.substr(0,nline.find(" "));
        second = nline.substr(int(nline.find(" ")) + 1,nline.find("\n"));

        A = atoi(first.c_str());
        B = atoi(second.c_str());
        cout << A << B << "\n";
   		for(j=A; j<= B; j++)
		{
		    tempnum = itoa(j,buffer,10);
            for (k = 1; k < tempnum.length(); k++)
            {
                temp1 = tempnum.substr(0,k);
                temp2 = tempnum.substr(k, tempnum.length());

                final = temp2 + temp1;

                final2 = atoi(final.c_str());

                if ((final2 > j) && (final2 <= B) && (final2 != last))
                {
                    count++;
                    last=final2;
                }

            }
		}
		f << count;
	}
return 0;
}
