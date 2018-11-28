#include<iostream>
#include<string>
using namespace std;

int main()
{
        int n;
        cin >> n;
        getchar();
        for(int i=0;i<n;i++)
        {
                string input;
                getline(cin,input);
                for(int j=0;j<input.length();j++)
                {
                        switch(input[j])
                        {
                                case 'a': input[j]='y'; break;
                                case 'b': input[j]='h'; break;
                                case 'c': input[j]='e'; break;
                                case 'd': input[j]='s'; break;
                                case 'e': input[j]='o'; break;
                                case 'f': input[j]='c'; break;
                                case 'g': input[j]='v'; break;
                                case 'h': input[j]='x'; break;
                                case 'i': input[j]='d'; break;
                                case 'j': input[j]='u'; break;
                                case 'k': input[j]='i'; break;
                                case 'l': input[j]='g'; break;
                                case 'm': input[j]='l'; break;
                                case 'n': input[j]='b'; break;
                                case 'o': input[j]='k'; break;
                                case 'p': input[j]='r'; break;
                                case 'q': input[j]='z'; break;
                                case 'r': input[j]='t'; break;
                                case 's': input[j]='n'; break;
                                case 't': input[j]='w'; break;
                                case 'u': input[j]='j'; break;
                                case 'v': input[j]='p'; break;
                                case 'w': input[j]='f'; break;
                                case 'x': input[j]='m'; break;
                                case 'y': input[j]='a'; break;
                                case 'z': input[j]='q'; break;
                        }
                }
                cout << "Case #" << i+1 << ": " << input << endl;
        }
        return 0;
}
