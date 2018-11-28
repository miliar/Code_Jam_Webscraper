#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

#define MAX_BASE    10

int mul_table [MAX_BASE+1][MAX_BASE+1][2];
int sqr_table [MAX_BASE];

int happy_tab[MAX_BASE+1][1000];
int yes_tab[MAX_BASE+1][1000];
int hit[11];

int quickans(long long *ans)
{
    if( 
        
        
        hit[5] &&
        hit[6] &&
        hit[7] &&
        hit[8] &&
        hit[9] &&
        hit[10])
        {
            *ans = 11814485;
            return 1;
        }

    if( !(hit[2]) &&
        !(hit[3]) &&
        !(hit[4]) &&
        !(hit[5]) &&
        hit[6] &&
        hit[7] &&
        hit[8] &&
        hit[9] &&
        hit[10])
        {
            *ans = 2662657;
            return 1;
        }
    if( 
        hit[3] &&
        
        !(hit[5]) &&
        hit[6] &&
        hit[7] &&
        hit[8] &&
        hit[9] &&
        hit[10])
        {
            *ans = 4817803;
            return 1;
        }

    return 0;
}

void prepare_happy(void)
{
    for(int base=2; base<=10; base++)
    {
        for(int i=0; i<1000; i++)
        {
            int x = i, newx = 0;
            for(; x; )
            {
                int digit = x%base;
                newx += sqr_table[digit];
                x /= base;
            }
            happy_tab[base][i] = newx;
        }
    }
//printf("!!!! A\n");
//    memset(yes_tab, 0, sizeof(yes_tab));
    
    for(int base=2; base<=10; base++)
    {
        for(int i=0; i<1000; i++)
        {
            int x = i;
            int yes = 0;
            for(int j=0; j<1000; j++)
            {
                x = happy_tab[base][x];
                if(x==1)
                    yes = 1;
                if(yes_tab[base][x])
                    yes = 1;
                if(!x)
                    break;
                if(yes)
                    break;
            }
            yes_tab[base][i] = yes;
        }
//        printf("!!!!!!!!!! base %d\n", base);
    }
}

int ishappy(long long x, int base)
{
    int newx = 0;
    while( x>999 )
    {
        for(; x; )
        {
            int digit = x%base;
            newx += sqr_table[digit];
            x /= base;
        }
        x = newx;
        newx = 0;
    };
    return yes_tab[base][x];
}

int main()
{
    
    int T=0;
    char tmp[10];
    cin.getline(tmp, 10);
    int l = strlen(tmp);
    for(int i=0; i<l; i++)
    {
        T *= 10;
        T += (tmp[i] - '0');
    }

    for(int i=0; i<MAX_BASE; i++)
    {
        sqr_table[i] = i*i;
    }
    prepare_happy();
//    cout << yes_tab[10][T] << endl;
    
    for(int base=2; base<=10; base++)
    {
        for(int x=0; x<base; x++)
        {
            int sqr = x*x;
            mul_table[base][x][0] = sqr % base;
            mul_table[base][x][1] = sqr / base;
        }
    }
            
    for(int i=1; i<=T; i++)
    {
        char line[40];
        int bases[10];
        int num_b=0;
        
        cin.getline(line, 40);
        int linelen = strlen(line);
        int start = -1;
        for(int j=0; j<=linelen; j++)
        {
            if(line[j]==' ' || line[j]==0)
            {
                int in = (line[j-1] - '0');
                if( (j-start)==3 )
                {
                    in += 10 * (line[j-2] - '0');
                }
                start = j;
                bases[num_b] = in;
                num_b++;
            }
        }
        for(int j=0; j<11; j++)
            hit[j] = 0;
        for(int j=0; j<num_b; j++)
            hit[bases[j]] = 1;

        long long ans;
        if(quickans(&ans))
            ;
        else
        {
            for(long long j=2; ;j++ )
            {
                int happy = 1;
                for(int k=0; k<num_b; k++)
                {
                    if( ! ishappy(j, bases[k]) )
                    {
                        happy=0;
                        break;
                    }
                }
                if(happy)
                {
                    ans = j;
                    break;
                }
            }
        }
        
        cout << "Case #" << i << ": ";
        cout << ans;
        cout << endl;
    }
    
    //cin >> T;
    return 0;
}
