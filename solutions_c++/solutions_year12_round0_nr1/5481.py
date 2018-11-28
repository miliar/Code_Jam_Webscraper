#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int index(string a)
{
    string eng[27] = {" ", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
    string gog[27] = {" ", "y","n","f","i","c","w","l","b","k","u","o","m","x","s","e","v","z","p","d","r","j","g","t","h","a","q"};
    for(int x = 0; x < 27; x++)
    {
        if(gog[x] == a)
        return x;
    }
}

string translate(string l)
{
    string ans = "";
    string eng[27] = {" ", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
    string gog[27] = {" ", "y","n","f","i","c","w","l","b","k","u","o","m","x","s","e","v","z","p","d","r","j","g","t","h","a","q"};
    for(int x = 0; x < l.size(); x++)
    {
        ans += eng[index(l.substr(x,1))];
    }
    return ans;
}

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A_output.out");

    int N;
    fin >> N;
    string s;
    getline(fin,s);
    for(int a = 0; a < N; a++)
    {
        string s;
        getline(fin,s);
        fout << "Case #" << a+1 << ": " << translate(s) << endl;
    }
    return 0;

}
