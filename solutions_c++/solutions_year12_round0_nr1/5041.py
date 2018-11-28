#include <iostream>
#include <string>
#include <vector>

using namespace std;

char replaceLetter ( const char & );

int main ()
{
    unsigned int cases;
    vector<string> my_vector;
    string googlerese_string;

    cin >> cases;
    cin.ignore ();
    for ( unsigned int i = 0; i < cases; ++i )
    {
        getline( cin , googlerese_string );
        my_vector.push_back ( googlerese_string );
    }
    vector <string>::iterator it;
    int actual_case = 1;
    for ( it = my_vector.begin (); it != my_vector.end(); ++it )
    {
        cout << "Case #" << actual_case << ": ";
        for ( unsigned int j = 0; j < it->length(); ++j )
        {
            if ( it->at ( j ) == ' ' )
            {
                cout << " ";
            }
            else
            {
                cout << replaceLetter ( it->at ( j ) );
            }
        }
        cout << "\n";
        actual_case += 1;
    }
    return 0;
}

char replaceLetter ( const char &letter )
{
    switch ( letter )
    {
        case 'a':
            return 'y';
        case 'b':
            return 'h';
        case 'c':
            return 'e';
        case 'd':
            return 's';
        case 'e':
            return 'o';
        case 'f':
            return 'c';
        case 'g':
            return 'v';
        case 'h':
            return 'x';
        case 'i':
            return 'd';
        case 'j':
            return 'u';
        case 'k':
            return 'i';
        case 'l':
            return 'g';
        case 'm':
            return 'l';
        case 'n':
            return 'b';
        case 'o':
            return 'k';
        case 'p':
            return 'r';
        case 'q':
            return 'z';
        case 'r':
            return 't';
        case 's':
            return 'n';
        case 't':
            return 'w';
        case 'u':
            return 'j';
        case 'v':
            return 'p';
        case 'w':
            return 'f';
        case 'x':
            return 'm';
        case 'y':
            return 'a';
        case 'z':
            return 'q';
        default:
            return letter;
    }
}
