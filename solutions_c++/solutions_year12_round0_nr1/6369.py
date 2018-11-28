#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int lines;
    char codes[30][301];

    char decrypter[2][26] = {{'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'},{'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'}};

    cout << "Input: ";
    cin >> lines;
    cout << endl;
    cin.ignore();


    for(int i = 0; i < lines; i++)
        cin.getline(codes[i],300);

    for(int i = 0; i < lines; i++)
    {
        for(int j = 0; codes[i][j] != 0 ; j++)
        {
            for(int a = 0; a <26 ; a++)
                if(codes[i][j] == decrypter[0][a])
                {
                    codes[i][j] = decrypter[1][a];
                    break;
                }
        }
    }

ofstream output;
output.open("a.txt");

cout << "\nOutput: \n";
    for(int i = 0; i < lines; i++)
    {
        output << "Case #" << i+1 << ": ";
        for(int j = 0; codes[i][j] ; j++)
        {
            cout << codes[i][j];
            output << codes[i][j];

        }
        cout << endl;
        output << endl;
    }

output.close();

}
