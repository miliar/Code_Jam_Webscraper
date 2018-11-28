#include <iostream>
#include <fstream>

using namespace std;

/*int main()
{
    char asd[26];
    char lol[26];
    for(int i=0;i<26;i++)
        lol[i]='-';
    lol[0] = 'y';
    lol[24] = 'q';
    lol[14] = 'e';
    char lettera='a';
    for(int i=0;i<26;i++)
    {
        asd[i] = lettera + i;
    }
    char test[30][100];
    ifstream in("input");
    int j=0;
    while(in)
        in.getline(test[j++], 100);
    lettera='a';
    for(int i=0;i<6;i+=2)
    {
        for(int j=0; j< 40; j++)
        {
            for(int k=0; k< 26; k++)
            {
                if(test[i+1][j] == lettera)
                {
                    int a = (int)(lettera - 'a');
                    lol[a] = test[i][j];
                }
                lettera++;
            }
            lettera='a';
        }
        ofstream out("output");
        for(int i=0;i<26;i++)
        {
            out << lol[i];
        }
        out.close();
    }
    return 0;
}*/


int main()
{
    char test[50][150];
    string result[50];
    char alpha[26] = { 'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
    int n = 0;
    ifstream in("input");
    in >> n;
    cout << n;
    in.get();
    for(int i=0;i<n;i++)
        in.getline(test[i],150);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<100;j++)
        {
            if(test[i][j]==' ')
                        result[i] += ' ';
            else
            {
                for(int k=0;k<26;k++)
                {
                      if(test[i][j] == alpha[k])
                            result[i] += ('a' + k );

                }
            }
        }
    }
    ofstream out("output");
    for(int i=0;i<n;i++)
    {
        out << "Case #" << i+1 << ": " << result[i] << endl;
    }
    out.close();
}
