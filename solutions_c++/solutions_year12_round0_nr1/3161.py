#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ifstream input;
    ofstream output;
    output.open ("output.txt");
    input.open ("A-small-attempt0.in");
    int n;
    int i;
    int j;
    input >> n;
    cout  << n<<endl;
    string niz [n+1];
    string a;
    for (i = 0; i < n+1; i++)
    {
        getline (input, a);
        if (!a.empty ())
        {
        output << "Case #" << i << ": " ;
        for (j = 0; j <a.length (); j++)
       {
           if (a[j] == 'e')
           {
               a[j] = 'O';
           }
           else if (a[j] == 'j')
           {
               a[j] = 'U';
           }
           else if (a[j] == 'p')
           {
               a[j] = 'R';
           }
           else if (a[j] == 'm')
           {
               a[j] = 'L';
           }
           else if (a[j] == 'y')
           {
               a[j] = 'A';
           }
            else if (a[j] == 's')
           {
               a[j] = 'N';
           }
           else if (a[j] == 'l')
           {
               a[j] = 'G';
           }
           else if (a[j] == 'c')
           {
               a[j] = 'E';
           }
            else if (a[j] == 'k')
           {
               a[j] = 'I';
           }
           else if (a[j] == 'd')
           {
               a[j] = 'S';
           }
           else if (a[j] == 'x')
           {
               a[j] = 'M';
           }
            else if (a[j] == 'v')
           {
               a[j] = 'P';
           }
           else if (a[j] == 'n')
           {
               a[j] = 'B';
           }
           else if (a[j] == 'r')
           {
               a[j] = 'T';
           }
           else if (a[j] == 'i')
           {
               a[j] = 'D';
           }
           else if (a[j] == 'a')
           {
               a[j] = 'Y';
           }
           else if (a[j] == 'b')
           {
               a[j] = 'H';
           }
           else if (a[j] == 'f')
           {
               a[j] = 'C';
           }
           else if (a[j] == 'g')
           {
               a[j] = 'V';
           }
           else if (a[j] == 'h')
           {
               a[j] = 'X';
           }
           else if (a[j] == 'o')
           {
               a[j] = 'K';
           }
            else if (a[j] == 't')
           {
               a[j] = 'W';
           }
            else if (a[j] == 'w')
           {
               a[j] = 'F';
           }
            else if (a[j] == 'q')
           {
               a[j] = 'Z';
           }
           else if (a[j] == 'u')
           {
               a[j] = 'J';
           }
           else if (a[j] == 'z')
           {
               a[j] = 'Q';
           }
       }

       for (j = 0; j < a.length(); j++)
       {
           if (isupper(a[j]))
           {
               a[j] = tolower(a[j]);
           }
       }

 output <<  a << endl;
    }
    }
    input.close ();
    output.close ();
    return 0;
}
