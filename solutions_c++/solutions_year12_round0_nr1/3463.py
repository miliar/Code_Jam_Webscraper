#include<iostream>
using namespace std;
/*
Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand


ynficwlbkuomxsevzpdrjgthaq
abcdefghijklmnopqrstuvwxyz


rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities

de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up

Output
Case #1:
Case #2:
Case #3:
*/
//                0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
//char cars[] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
int cars[] =    {24,  7,  4, 18, 14, 2,  21, 23, 3,  20, 8,  6,  11, 1,  10, 17, 25, 19, 13, 22, 9,  15, 5,  12, 0,  16};

int main()
{
    int lines;
    string cad;
    cin>> lines;
    cin.ignore();
    for (int i = 0; i < lines; i++)
    {
        getline(cin, cad, '\n');
        cout<< "Case #" << i+1 << ": ";
        for(int j = 0; j < cad.size(); j++)
        {
            if(cad[j] == ' ')
                cout << " ";
            else
                cout<<(char)(cars[cad[j] - 'a'] + 'a');
        }
        cout << endl;
    }
}
