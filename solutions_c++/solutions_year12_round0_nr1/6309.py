#include <iostream>
#include <fstream>
using namespace std;

main()
{
    char one[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m',
                    'n','o','p','q','r','s','t','u','v','w','x','y','z'};

    char two[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l',
                    'b','k','r','z','t','n','w','j','p','f','m','a','q'};

        ofstream fout("output.txt");

//
//3
//ejp mysljylc kd kxveddknmc re jsicpdrysi
//rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
//de kr kd eoya kw aej tysr re ujdr lkgc jv
//
//our language is impossible to understand
//there are twenty six factorial possibilities
//so it is okay if you want to just give up

    int num;
                        //    string strs[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
    //                    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    //                    "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    string str;
    cin >> num;
    cin.ignore(1,'\n');

    for (int i=1; i<=num; i++)
    {
        getline(cin, str);
        //str = strs[i-1];
        fout << "Case #" << i <<": ";
        for (int j=0;j<str.length(); j++)
        {
            if (str[j] == ' ')
            	fout << str[j];
            else
                fout << two[str[j]-'a'];
        }
        fout << endl;

    }






}
