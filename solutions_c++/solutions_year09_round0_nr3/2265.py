#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

string welcome("welcome to code jam");
string line;

int lengthW = 19;
int lengthL = 0;

int array[19][500];

string getLine() {
  string s;
  while(!feof(stdin)) {
    char c = fgetc(stdin);
    if(c == 13) continue;
    if(c == 10) return s;
    s += c;
    }
  return s;
}

int findQnt(int wi, int li)
{

    if(array[wi][li] != -1)
    {
        return array[wi][li];
    }

    int qnt = 0;
    
    if(welcome[wi] == line[li])
    {
        if(wi >= lengthW -1)
        {
            qnt = 1;

        }
        else
        {
            qnt += findQnt(wi+1, li+1);
        }
    }
    
    if(li < lengthL -1)
    {
        qnt += findQnt(wi, li+1);
    }
    
    qnt = qnt%10000;
    
    array[wi][li] = qnt;
    return qnt;
}

void initialize()
{
    for(int i = 0; i < 19; i++)
    {
        for(int j = 0; j < 500; j++)
        {
            array[i][j] = -1;
        }   
    } 
}

void read()
{
    line = getLine();
    lengthL = line.length();
}

int main()
{
    freopen("C.in", "r", stdin);
    freopen("Clarge2.out", "w", stdout);
   
    int N = 0;
    scanf("%d", &N);
    
    getLine();
    
    for(int i = 1; i <= N; i++)
    {
       read();
       initialize();
       printf("Case #%d: %04d\n", i, findQnt(0,0));
    }
    
}
