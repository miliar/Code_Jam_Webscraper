#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

using namespace std;

char trans[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
    int N, length, index;
    char c;
    string mystr;
    ifstream file_in("A-small-attempt0.in");
    ofstream file_out("output.txt");

    file_in>>N;
    getline(file_in, mystr);
    for(int i=1; i<=N; i++)
    {
        getline(file_in, mystr);
        for(length = 0; mystr[length]!='\0'; length++);
        file_out<<"Case #"<<i<<": ";

        for(int j=0; j<length; j++)
        {
            c = mystr[j];
            if(isalpha(c))
            {
                index = (int)(c - 'a');
                file_out<<trans[index];
            }
            else
            {
                file_out<<c;
            }
        }
        file_out<<endl;
    }
    return 0;
}
