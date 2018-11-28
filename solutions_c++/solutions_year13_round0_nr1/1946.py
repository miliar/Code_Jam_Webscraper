#include<iostream>
#include<fstream>
#include<map>

using namespace std;

int charmap[16];
//ifstream infile ("A-small-attempt0.in");
//ifstream infile ("input.txt");
//ofstream outfile;
//outfile.open("output.txt");

void eval(int charmap[], int size, ofstream& outfile)
//void eval(int charmap[], int size)
{
/*  
    for (int i = 0; i < size; i++)
    {
        outfile << charmap[i] << " ";
        if ((i+1) % 4 == 0)
            outfile << "\n";
    }
*/
    int num_neg = 0;
    for (int i = 0; i < 4; i++)
    {
        int sum = 0;
        for (int j = 0; j < 4; j++)
        {
            sum += charmap[4*i+j];
        }
        if (sum < 0)
            num_neg++;
        if (sum == 0 || sum == 5)
        {
            outfile << "O won";
            cerr << "--1 " << endl;
            return;
        }
        if (sum == 36|| sum == 32)
        {
            outfile << "X won";
            cerr << "--2 " << endl;
            return;
        }
    }

    for (int i = 0; i < 4; i++)
    {
        int sum = 0;
        for (int j = 0; j < 4; j++)
        {
            sum += charmap[i+4*j];
        }
        if (sum == 0 || sum == 5)
        {
            outfile << "O won";
            cerr << "--3 " << endl;
            return;
        }
     
        if (sum == 36|| sum == 32)
        {
            outfile << "X won";
            cerr << "--4 " << endl;
            return;
        }
    }

    int sum1 = charmap[0] + charmap[5] + charmap[10] + charmap[15];
    int sum2 = charmap[3] + charmap[6] + charmap[9] + charmap[12];

    if (sum1 == 0 || sum1 == 5 || sum2 == 0 || sum2 == 5)
    {
        outfile << "O won";
        cerr << "--5 " << endl;
        return;
    }
    if (sum1 == 36 || sum1 == 32 || sum2 == 36 || sum2 == 32)
    {
        outfile << "X won";
            cerr << "--6 " << endl;
        return;
    }

    if (num_neg > 0)
    {
        outfile << "Game has not completed";
            cerr << "--7 " << endl;
        return;
    }
    else
    {
        outfile << "Draw";
            cerr << "--8 " << endl;
    }
    return;
}

int main()
{
    char getch, preChar;
//  ifstream infile ("A-small-attempt0.in");
  ifstream infile ("A-large.in");
//A-large.in
  //  ifstream infile ("input.txt");
  ofstream outfile;
  outfile.open("output.txt");
    int numTests = 0;
    int index = 0;
    int numElem = 0;

    if (infile.is_open())
    {
        while (!infile.eof())
        {
            //infile.get(getch);
            getch = infile.get();
            //if ()
            if (getch >= '0' && getch <= '9')
            {
                numTests = numTests * 10 + getch - '0';
                continue;
            }
            /*
            if (getch == '\n')
            {
                if (index > 0)
                {
                    outfile << "\n";
                }
                index++;
                if (index <= numTests)
                {
                    outfile << "Case #" << index << ": ";
                }
                continue;
            }
            */
            if (getch == 'X' || getch == 'O' || getch == 'T' || getch == '.')
            {
                charmap[numElem] = getch - 'O';
                numElem++;
                if (numElem == 16)
                {
                    index++;
                    if (index <= numTests)
                    {
                        outfile << "Case #" << index << ": ";
                    }
                    eval(charmap, 16, outfile);
                    if (index < numTests)
                    {
                        outfile << "\n";
                    }
                    numElem = 0;
                }

                continue;
            }

        }

    }
    else
    {
        cout << "unable to open file\n";
    }

    return 0;
}
