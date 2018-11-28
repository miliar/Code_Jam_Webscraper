#include <iostream>
#include <string>
using namespace std;

class oneone
{
    public:
    char one, two;
}mapping[26];

char find_mapping (char inp)
{
    int left = 0, right = 25, pivot;
    if (mapping[0].one == inp)
    {
        return mapping[0].two;
    }
    else if (mapping[25].one == inp)
    {
        return mapping[25].two;
    }
    else
    {


    for (;;)
    {
        pivot = (left+right)/2;
        if (mapping[pivot].one == inp)
        {
            return mapping[pivot].two;
        }
        else if (mapping[pivot].one > inp)
        {
            right = pivot;
        }
        else
        {
            left = pivot;
        }
    }
    }
}

int main ()
{
    int no_of_tests;
    string input;

mapping[0].one = 'a';
mapping[0].two = 'y';
mapping[1].one = 'b';
mapping[1].two = 'h';
mapping[2].one = 'c';
mapping[2].two = 'e';
mapping[3].one = 'd';
mapping[3].two = 's';
mapping[4].one = 'e';
mapping[4].two = 'o';
mapping[5].one = 'f';
mapping[5].two = 'c';
mapping[6].one = 'g';
mapping[6].two = 'v';
mapping[7].one = 'h';
mapping[7].two = 'x';
mapping[8].one = 'i';
mapping[8].two = 'd';
mapping[9].one = 'j';
mapping[9].two = 'u';
mapping[10].one = 'k';
mapping[10].two = 'i';
mapping[11].one = 'l';
mapping[11].two = 'g';
mapping[12].one = 'm';
mapping[12].two = 'l';
mapping[13].one = 'n';
mapping[13].two = 'b';
mapping[14].one = 'o';
mapping[14].two = 'k';
mapping[15].one = 'p';
mapping[15].two = 'r';
mapping[16].one = 'q';
mapping[16].two = 'z';
mapping[17].one = 'r';
mapping[17].two = 't';
mapping[18].one = 's';
mapping[18].two = 'n';
mapping[19].one = 't';
mapping[19].two = 'w';
mapping[20].one = 'u';
mapping[20].two = 'j';
mapping[21].one = 'v';
mapping[21].two = 'p';
mapping[22].one = 'w';
mapping[22].two = 'f';
mapping[23].one = 'x';
mapping[23].two = 'm';
mapping[24].one = 'y';
mapping[24].two = 'a';
mapping[25].one = 'z';
mapping[25].two = 'q';
    //normal mapping end

    cin >> no_of_tests;
    getline (cin, input);

    for (int i = 0; i < no_of_tests; ++i)
    {
        getline (cin, input);
        cout << "Case #"<< i+1 <<": ";
        for (int j = 0; j < input.length(); ++j)
        {
            if (input[j] != ' ')
            {
                cout << find_mapping(input[j]);
            }
            else
            {
                cout << " ";
            }

        }
        cout << endl;
    }


}
