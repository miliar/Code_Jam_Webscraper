#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>


 
using namespace std;
 
int x[40];
int base;
int y[40];

__int64 ans;

//char store[40] = {'1','0','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char store[40] = {1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39};
void parse(string ip)
{
    int len,i,count = 0,tmp;

    len = ip.size();

    for(i=0;i<40;i++)
    {
        x[i] = 0;
        y[i] = -1;
    }

    base = 0;

    for(i=0;i<len;i++)
    {
        if(ip[i] >= '0' && ip[i] <= '9')
        {
            x[ip[i]-'0']++;
        }
        else
        {
            x[ip[i]-'a'+10]++;
        }
    }

    for(i=0;i<40;i++)
    {
        if(x[i] != 0)
            base++;
    }

    if(base  == 1)
        base = 2;



    for(i=0;i<len;i++)
    {

        if(ip[i] >= '0' && ip[i] <= '9')
        {
            if(y[ip[i]-'0'] == -1)
            {
                y[ip[i]-'0'] = store[count];
                count++;
            }
        }
        else
        {
            if(y[ip[i]-'a'+10] == -1)
            {
                y[ip[i]-'a'+10] = store[count];
                count++;
            }
        }
    }
    
    ans = 0;
    for(i=0;i<len;i++)
    {
        if(ip[i] >= '0' && ip[i] <= '9')
        {
            tmp = y[ip[i]-'0'];
            ans = ans* base + tmp;
        }
        else
        {
            tmp = y[ip[i]-'a' + 10];
            ans = ans* base + tmp ;
        }
    }
}
 
int main()
{

    ifstream fin;
    ofstream fout;

    string ip;


    fin.open ("input.txt", ifstream::in);

    fout.open("output.txt");

    int cases;

    fin >> cases;

    getline(fin, ip);
 
    for(int t = 0; t < cases; t++)
    {
        ip.resize(0);

        getline(fin, ip);

        parse(ip);

        //fout << "Case #" << "t+1" << ": " << ans << "\n";

        printf("Case #%d: %ld\n",t+1,ans);

    }
 
 return 0;
 
 
}