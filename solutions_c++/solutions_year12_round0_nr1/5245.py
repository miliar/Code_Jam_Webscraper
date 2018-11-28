#include<iostream>
#include<cstring>
#include<cstdio>
#include<fstream>

using namespace std;

char code[27] = "abcdefghijklmnopqrstuvwxyz";
char key[27] = "ynficwlbkuomxsevzpdrjgthaq";
void letter_replace(char &a)
{
    int i;
    for(i = 0; i < 26; i++)
    {
        if(a == key[i])
        {
            a = code[i];
            break;
        }
    }
}

void translate(char input_string[200])
{
    for(int i = 0; i < strlen(input_string); i++)
        letter_replace(input_string[i]);
}

int main()
{
    char inp[200];
    int cases;
    fstream x,y;
    y.open("output.txt", ios::out);
    x.open("A-small-attempt1.in", ios::in);
    x >> cases;
    x.seekg(3, ios::beg);
    for(int i = 0; i < 30; i++)
    {
        x.getline(inp, 200, '\n');
        translate(inp);
        y << "Case #" << i + 1 << ": " << inp << endl;
    }
    x.close();
    y.close();
    return 0;
}
