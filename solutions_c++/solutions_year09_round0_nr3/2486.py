#include <iostream>
#include <list>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
using namespace std;
#include <stdio.h>
#include <string.h>

struct s
{
    char c;
    int pos;
}; 

struct s s1[20];
vector<int> array[12];
uint64_t count = 0;

int getIndex(char c)
{
    switch(c)
    {
        case 'w':
            return 0;
        case 'e':
            return 1;
        case 'l':
            return 2;
        case 'c':
            return 3;
        case 'o':
            return 4;
        case 'm':
            return 5;
        case ' ':
            return 6;
        case 't':
            return 7;
        case 'd':
            return 8;
        case 'j':
            return 9;
        case 'a':
            return 10;
        default:
            return -1;
    }
}

void initialize()
{
    memset(&s1, -1, sizeof(s1));
    s1[0].c = 'w';
    s1[1].c = 'e';
    s1[2].c = 'l';
    s1[3].c = 'c';
    s1[4].c = 'o';
    s1[5].c = 'm';
    s1[6].c = 'e';
    s1[7].c = ' ';
    s1[8].c = 't';
    s1[9].c = 'o';
    s1[10].c = ' ';
    s1[11].c = 'c';
    s1[12].c = 'o';
    s1[13].c = 'd';
    s1[14].c = 'e';
    s1[15].c = ' ';
    s1[16].c = 'j';
    s1[17].c = 'a';
    s1[18].c = 'm';
}

void isComplete(int curr)
{
    if( curr == 18 )
    {
        for( int i = 0; i < array[5].size(); i++ )
        {
            s1[curr].pos = i;
            if(array[5][i] > array[10][s1[17].pos])
            {
                count++;
            }
            else
            {
                continue;
            }
        }
        return;
    }

    for(int i = 0; i < array[getIndex(s1[curr].c)].size(); i++ )
    {
        if( array[getIndex(s1[curr-1].c)].size() > s1[curr-1].pos )
        {
            if( array[getIndex(s1[curr].c)][i] > array[getIndex(s1[curr-1].c)][s1[curr-1].pos] )
            {
                s1[curr].pos = i;
                isComplete(curr + 1);
            }
        }
        else
        {
            continue;
        }
    }
}

int main()
{
    char line[510] = {0};
    int index = -1;
    int i = 0;
    int N = 0;

    cin >> N;
    cin.ignore();
    for( int n = 0; n < N; n++ )
    {
        count = 0;
        memset(line, 0, sizeof(line));
        cin.getline(line, 505);
        for( i = 0; i < 11; i++ )
        {
            array[i].clear();
        }
        for( i = 0; i < strlen(line); i++ )
        {
            index = getIndex(line[i]);
            if( -1 != index )
            {
                array[index].push_back(i);
            }
        }

        for( i = 0; i < array[0].size(); i++ )
        {
            initialize();
            s1[0].pos = i;
            isComplete(1); 
        }

        printf("Case #%d: %0.4d\n", n + 1, (count%10000));
    }
    return 0;
}

