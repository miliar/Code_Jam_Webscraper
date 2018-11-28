#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>


using namespace std;

bool surprising(int a, int b, int c)
{
    return ((abs(a-c)==2) || (abs(a-b)==2) || (abs(b-c)==2));
}
bool valid(int a, int b, int c)
{

    bool vale=((abs(a-c)<=2) && (abs(a-b)<=2)  && (abs(b-c)<=2));
    vale = vale && (a>=0) &&(b>=0) && (c>=0);

//    if (vale) cout << a << "," << b << "," << c << endl;
    return vale;
}

int solve(int n, int s, int p, int puntajes[])
{
    int answer=0;
    int surpsposibles=s;

    for(int i = 0; i<n; i++)
    {
        int tmp = (puntajes[i]);
        if(tmp>=p*3)
        {
            answer++;
            continue;
        }

        int posibles=0;
        int surps=0;
        for(int q=-2;q!=1;q++)
        {
            for(int j=-2;j!=1;j++)
            {
                if(valid(p,p+q,p+j))
                {
                    if(p+(p+q)+(p+j) == tmp)
                    {
                        if(surprising(p,p+q,p+j))
                            surps++;
                        else
                            posibles++;
                    }
                }
            }
        }
        if(posibles)
            answer++;
        else
            if(surpsposibles && surps)
            {
                answer++;
                surpsposibles--;
            }
    }
    return answer;
}

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("input.in","r",stdin);
        freopen("output.out","w",stdout);
    #endif
    int puntajes[100]; //puntaje por googler
    int n; //cantidad de googlers
    int t; //cantidad de casos
    int s; //cantidad de surprising triplets
    int p; //puntaje minimo

    cin >> t >> ws;
    int caso =0;

    int answer  = 0;
    while(t-->0)
    {
        memset(puntajes,0, sizeof(int)*100);
        cin >> n >> s >> p;
        for(int i =0; i<n;i++)
            cin >> puntajes[i];

        answer = solve(n,s,p,puntajes);


        cout << "Case #" << ++caso << ": " << answer;
        if(t>0) cout << endl;
    }

    return 0;
}

