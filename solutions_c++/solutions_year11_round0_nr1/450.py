#include<iostream>
#include<cstdlib>
#include<cstdio>

using namespace std;

int T;
int N;
char color;
int pos;
int num = 0;
int nowo,nowp;
int timeo,timep;

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>T;
    while(T--)
    {
        cin >> N;
        nowo = 1;
        nowp = 1;
        timeo = timep = 0;
        for(int i=1;i<=N;i++)
        {
            cin >> color;
            if(color!='O'&& color!='B') cin >> color;
            cin >> pos;
            if (color=='O')
            {
                timeo += abs(nowo-pos);
                if(timeo<timep) timeo = timep;
                timeo ++;
                nowo = pos;
            }
            else
            {
                timep += abs(nowp-pos);
                if(timep<timeo) timep = timeo;
                timep ++;
                nowp=pos;
            }
        }
        num++;
        cout << "Case #" << num << ": ";
        if(timeo<timep)timeo=timep;
        cout << timeo << endl;
    }
}
