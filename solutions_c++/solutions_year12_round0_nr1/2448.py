#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main()
{
    ifstream in("input.in");
    ifstream min("map.in");
    ofstream ki("output.out");
    int n;
    map<char,char> asg;
    string tmp;


    for (int i=1; i<=26;i++)
    {
        getline(min,tmp);
        asg[tmp[2]]=tmp[0];
    }

    in >> n;
    getline(in, tmp);
    for (int i=1; i<=n; i++)
    {
        ki << "Case #" << i << ": ";
        getline(in,tmp);
        for (int j=0; j<=tmp.length()-1; j++)
        {
            if (tmp[j]==' ')
            {
                ki << " ";
            }
            else
            {
                ki << asg[tmp[j]];
            }
        }
        ki << endl;
    }
    ki.close();
}
