#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
    char arr[26][2] = {{'a','y'},{'b','n'},{'c','f'},{'d','i'},{'e','c'},{'f','w'},{'g','l'},{'h','b'},{'i','k'},{'j','u'},{'k','o'},{'l','m'},{'m','x'},{'n','s'},{'o','e'},{'p','v'},{'q','z'},{'r','p'},{'s','d'},{'t','r'},{'u','j'},{'v','g'},{'w','t'},{'x','h'},{'y','a'},{'z','q'}};
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");
    int cases;

    fin >> cases;
    cout << cases << endl;
    //char str[100];
    string str1;
        getline(fin,str1);
    //fout << "Output\n";
    for(int i = 1 ; i <= cases; i ++)
    //while(fin.good())
    {
        string str;
        getline(fin,str);
        cout << str.length()<< endl;
        for(int j = 0 ; j < str.length(); j ++)
        {
            for(int k = 0; k < 26; k ++)
            {
                if(arr[k][1] == str[j])
                {
                    str[j] = arr[k][0];
                    break;
                }
            }
        }
    //fin >> str;
        //cout << cases;
    //putline(cout,str);
    //cout << str << endl;
    fout << "Case #" << i << ": " << str << endl;
    }
    fout.close();
    fin.close();
}
