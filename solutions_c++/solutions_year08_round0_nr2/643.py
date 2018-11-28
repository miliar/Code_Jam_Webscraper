#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string>
#include <vector>
using namespace std;

int froa[101],tob[101];
int frob[101],toa[101];
int na,nb;

int getTime(string time)
{
    return (time[4]-'0')+10*(time[3]-'0')+60*(time[1]-'0')+600*(time[0]-'0');
}

int func1()
{
    int pfro=0,pto=0;
    int num=0;
    while (pfro<na && pto<nb)
    {
        while (froa[pfro]<toa[pto] && pfro<na)
        {
            num++;
            pfro++;
        }
        while (froa[pfro]>=toa[pto] && pto<nb && pfro<na)
        {
            pfro++;
            pto++;
        }
    }
    while (pfro<na)
    {
        num++;
        pfro++;
    }
    return num;
}

int func2()
{
    int pfro=0,pto=0;
    int num=0;
    while (pfro<nb && pto<na)
    {
        while (frob[pfro]<tob[pto] && pfro<nb)
        {
            num++;
            pfro++;
        }
        while (frob[pfro]>=tob[pto] && pto<na && pfro<nb)
        {
            pfro++;
            pto++;
        }
    }
    while (pfro<nb)
    {
        num++;
        pfro++;
    }
    return num;
}


int main()
{
    int caseNum;
    cin >>caseNum;
    int count=1;
    while (caseNum--)
    {
        int restT;
        cin >>restT;
        cin >>na >>nb;
        for (int i=0;i<na;i++)
        {
            string time;
            cin >>time;
            froa[i]=getTime(time);
            cin >>time;
            tob[i]=getTime(time)+restT;
        }
        for (int i=0;i<nb;i++)
        {
            string time;
            cin >>time;
            frob[i]=getTime(time);
            cin >>time;
            toa[i]=getTime(time)+restT;
        }
        
        sort(froa,froa+na);
        sort(toa,toa+nb);
        
        cout <<"Case #" <<count <<": " <<func1();
        
        sort(frob,frob+nb);
        sort(tob,tob+na);
        
        cout <<' ' <<func2() <<endl;
        count++;
    }
    return 0;
}
