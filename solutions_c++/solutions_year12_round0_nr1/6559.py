#include <iostream>
#include <fstream>

using namespace std;

char proc (char x)
{
    if ((int) x>=97&& (int) x <= 122)   {

    switch (x)
    {

    case 'y':   return 'a';
                break;
    case 'e':   return 'o';
                break;
    case 'q':   return 'z';
                break;
    case 'j':   return 'u';
                break;
    case 'p':   return 'r';
                break;
    case 'm':   return 'l';
                break;
    case 's':   return 'n';
                break;
    case 'l':   return 'g';
                break;
    case 'c':   return 'e';
                break;
    case 'k':   return 'i';
                break;
    case 'd':   return 's';
                break;
    case 'x':   return 'm';
                break;
    case 'v':   return 'p';
                break;
    case 'n':   return 'b';
                break;
    case 'r':   return 't';
                break;
    case 'i':   return 'd';
                break;
    case 'b':   return 'h';
                break;
    case 't':   return 'w';
                break;
    case 'h':   return 'x';
                break;
    case 'w':   return 'f';
                break;
    case 'f':   return 'c';
                break;
    case 'o':   return 'k';
                break;
    case 'a':   return 'y';
                break;
    case 'u':   return 'j';
                break;
    case 'g':   return 'v';
                break;
    case 'z':   return 'q';
                break;
    }
    }

    else return x;



}

int main ()
{
    int n;
    char ci, co;
    string infile, outfile;

    cout<<"Enter the name of the input file: ";
    cin>>infile;
    cout<<"Enter the name of the output file: ";
    cin>>outfile;

    ifstream in(infile.c_str ());
    ofstream out(outfile.c_str());

    in>>n;
    int i = 0;

in.get(ci);
        for (i=1; i<=n; i++) {
        out<<"Case #"<<i<<": ";
        while (in)  {
        in.get (ci);

        //in.get (ci);
        if ((int) ci==10)
        {
            out.put((int)10);
            break;
        }

        if (in.eof())   break;
        co = proc (ci);
        out.put (co);
        }
        if (in.eof()) break;
        }


    in.close ();
    out.close ();

    return 0;
}
/*
    while (in)
    {
        in.get (ci);
        if (in.eof())   break;
        co = ci;
        out.put (co);
    }

    in.close ();
    out.close ();

    return 0;
}
*/
