#include <iostream>

using namespace std;

#include <fstream>
int main()
{
    ifstream infile("q1.in");
    ofstream outfile("q2.out");
    unsigned short T;
    char str[202];
    infile >> T;
    char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

    cout << T << "\n";
    infile.getline(str,200);
    for (unsigned short i = 0; i<T; i++)
    {
        if (i>0) outfile << "\n";
        infile.getline(str,200);
        cout << i << " " << str << "\n";
        unsigned short k=0;
        while (str[k]!='\0')
        {
            if ((str[k] >= 'a') && (str[k]<='z')) str[k] = map[(unsigned short)str[k]-(unsigned short)'a'];
            k++;
        }

        outfile << "Case #" << i+1 << ": " <<str;
    }
    infile.close();
    outfile.close();
    cin >> T;
    return 0;
}
