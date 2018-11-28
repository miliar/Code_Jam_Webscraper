#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <stdio.h>
using namespace std;
//a b c d e f g h i j k l m n o p q r s t u v w x y z
/*char encrypted [26] = {'y' , 'h' , 'e' , 's' , 'o' , 'c' , 'v' , 'x' , 'd' , 'u' , 'i'
                      ,'g' , 'l' , 'b' , 'k' , 'r' , '' , 't' , 'n' , 'w' , 'j' , 'p'
                      ,'f' , 'm' , 'a' , 'q'}*/
int main()
{
    freopen("A-small-attempt3.in" , "rt" , stdin);
    freopen("out3.txt" , "wt" , stdout);
    //'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'.

    string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string s11 = "our language is impossible to understand";

    string s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    string s22 = "there are twenty six factorial possibilities";

    string s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string s33 = "so it is okay if you want to just give up";
    int tCases;
    cin>>tCases;
    //cin.ignore(1);
    getchar();
    for(int i=0; i<tCases; i++)
    {
        string in;
        getline(cin , in);
        string out;

        for(int i=0; i<in.size(); i++)
        {
            if(in[i] == 'q')
            {
                out += 'z';
                continue;
            }
            if(in[i] == 'z')
            {
                out += 'q';
                continue;
            }
            int ind;
            ind = find(s1.begin() , s1.end() , in[i]) - s1.begin();
            if(ind < s1.size())
            {
                out += s11[ind];
                continue;
            }

            ind = find(s2.begin() , s2.end() , in[i]) - s2.begin();
            if(ind < s2.size())
            {
                out += s22[ind];
                continue;
            }

            ind = find(s3.begin() , s3.end() , in[i]) - s3.begin();
            if(ind < s3.size())
            {
                out += s33[ind];
                continue;
            }

        }
        cout<<"Case #"<<(i+1)<<": ";
        cout<<out<<endl;
    }
    //cout<<(int)'o' - (int)'e'<<endl;
    //cout<<((int)'e')<<endl;;
    //cout<<(((int)'p' - 10)%123) <<endl;

    //cout << "Hello world!" << endl;
    return 0;
}
