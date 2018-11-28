#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
	ifstream infile;
	ofstream outfile;
        int i=0,j=0,temp,Case;
	char myBuffer[101];

	infile.open("Input.txt", ios::in);
	outfile.open("Output.txt", ios::out);

	while(infile.getline(myBuffer,101))
	{
            temp=strlen(myBuffer);
            if (i>0)
            {
                for (j=0;j<temp;j++)
                {
                    if (myBuffer[j]=='a')
                    {
                        myBuffer[j]='y';
                    }
                    else if (myBuffer[j]=='b')
                    {
                        myBuffer[j]='h';
                    }
                    else if (myBuffer[j]=='c')
                    {
                        myBuffer[j]='e';
                    }
                    else if (myBuffer[j]=='d')
                    {
                        myBuffer[j]='s';
                    }
                    else if (myBuffer[j]=='e')
                    {
                        myBuffer[j]='o';
                    }
                    else if (myBuffer[j]=='f')
                    {
                        myBuffer[j]='c';
                    }
                    else if (myBuffer[j]=='g')
                    {
                        myBuffer[j]='v';
                    }
                    else if (myBuffer[j]=='h')
                    {
                        myBuffer[j]='x';
                    }
                    else if (myBuffer[j]=='i')
                    {
                        myBuffer[j]='d';
                    }
                    else if (myBuffer[j]=='j')
                    {
                        myBuffer[j]='u';
                    }
                    else if (myBuffer[j]=='k')
                    {
                        myBuffer[j]='i';
                    }
                    else if (myBuffer[j]=='l')
                    {
                        myBuffer[j]='g';
                    }
                    else if (myBuffer[j]=='m')
                    {
                        myBuffer[j]='l';
                    }
                    else if (myBuffer[j]=='n')
                    {
                        myBuffer[j]='b';
                    }
                    else if (myBuffer[j]=='o')
                    {
                        myBuffer[j]='k';
                    }
                    else if (myBuffer[j]=='p')
                    {
                        myBuffer[j]='r';
                    }
                    else if (myBuffer[j]=='q')
                    {
                        myBuffer[j]='z';
                    }
                    else if (myBuffer[j]=='r')
                    {
                        myBuffer[j]='t';
                    }
                    else if (myBuffer[j]=='s')
                    {
                        myBuffer[j]='n';
                    }
                    else if (myBuffer[j]=='t')
                    {
                        myBuffer[j]='w';
                    }
                    else if (myBuffer[j]=='u')
                    {
                        myBuffer[j]='j';
                    }
                    else if (myBuffer[j]=='v')
                    {
                        myBuffer[j]='p';
                    }
                    else if (myBuffer[j]=='w')
                    {
                        myBuffer[j]='f';
                    }
                    else if (myBuffer[j]=='x')
                    {
                        myBuffer[j]='m';
                    }
                    else if (myBuffer[j]=='y')
                    {
                        myBuffer[j]='a';
                    }
                    else if (myBuffer[j]=='z')
                    {
                        myBuffer[j]='q';
                    }
                }
                outfile<<"Case #"<<i<<": "<<myBuffer;
                if (Case!=i)
                        outfile<<endl;
                i++;
            }
            else
            {
                Case=atoi(myBuffer);
                i++;
            }
	}
	infile.close();
	outfile.close();
        return 0;
}



