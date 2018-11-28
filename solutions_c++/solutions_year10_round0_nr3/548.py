#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

const int MAXN = 1001;
int T, R, N, K;
int avail[MAXN][MAXN];
long long group[MAXN], myGain[MAXN*MAXN];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin>>T;
    
    for(int t = 1; t <= T; t++)
    {
        memset(avail, false, sizeof(avail));
        int start = 0, fin;
        long long sum, totalgain = 0, temp = 0, nowR = 0, realLength = 0, multi, cycles = 0;
        cin>>R>>K>>N;
        bool nh = false, ah = false, collide = false;
        
        //special case        
        //one not able to hold
        for(int i = 0; i < N; i++)
        {
            cin>>group[i];
            if(!nh) temp += group[i];
            if(group[i] > K) nh = true, totalgain = temp;
        }
        
        //all hold
        if(temp <= K)
        {
            ah = true;
            totalgain = temp*R;
        }
        
        //normal case
        if(!ah && !nh)
        {
            while(nowR < R)
            {
                sum = group[start];
                fin = start;
                
                while(start != (fin+1)%N)
                {
                    if(sum + group[(fin+1)%N] <= K)
                    {
                        sum += group[(fin+1)%N];
                        fin = (fin+1)%N;
                    }
                    else
                        break;
                }
                
                if(avail[start][fin])
                {
                    cycles = avail[start][fin];
                    collide = true;
                    break;
                }
                else
                {
                    avail[start][fin] = ++nowR;
                }
                
                myGain[nowR] = sum;
                totalgain += sum;
                start = (fin+1)%N;
            }
            
            if(collide)
            {
                multi = 0;
                for(int i = cycles; i <= nowR; i++)
                    multi += myGain[i];
                
                realLength = nowR-cycles+1;
                totalgain += ((R-nowR)/realLength)*multi;
                R = (R-nowR)%realLength;
                
                for(int i = cycles; i < cycles+R; i++)
                    totalgain += myGain[i];
            }
            else
            {
                totalgain = 0;
                for(int i = 1; i <= R; i++)
                    totalgain += myGain[i];
            }
        }
        
        printf("Case #%d: ", t);
        cout<<totalgain<<endl;
    }
    return 0;
}
