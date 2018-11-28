#include<stdio.h>
#include<vector>
#include<iostream>

using namespace std;

int h,w;
int M[101][101];
char N[101][101];
char ULTIMA[101][101];
int flag[30];

void gg(int i,int j)
{
    if(i > 0)
    {
        if(N[i - 1][j] == 'S')
        {
            N[i - 1][j] = N[i][j];
            gg(i - 1,j);
        }
    }
    if(i < h - 1)
    {
        if(N[i + 1][j] == 'N')
        {
            N[i + 1][j] = N[i][j];
            gg(i + 1,j);
        }
    }
    if(j > 0)
    {
        if(N[i][j - 1] == 'E')
        {
            N[i][j - 1] = N[i][j];
            gg(i,j - 1);
        }
    }
    if(j < w - 1)
    {
        if(N[i][j + 1] == 'W')
        {
            N[i][j + 1] = N[i][j];
            gg(i,j + 1);
        }
    }
}

int main()
{
    int ncase,ccase;
    int x,y,z;
    int i,j;
    vector<int> k,l;
    char a;
    
    cin >> ncase;
    for(ccase = 1;ccase <= ncase;ccase++)
    {
        cin >> h >> w;
        
        for(y = 0;y < h;y++)
        {
            for(x = 0;x < w;x++)
                cin >> M[y][x];
        }
        
        a = 'a';
        k.clear();
        l.clear();
        for(y = 0;y < h;y++)
        {
            for(x = 0;x < w;x++)
            {
                z = 0;
                i = y;
                j = x;
                if(y > 0)
                {
                    if(M[y][x] > M[y - 1][x])
                    {
                        z = 1;
                        if(M[y - 1][x] < M[i][j])
                        {
                            i = y - 1;
                            j = x;
                        }
                    }
                }
                if(x > 0)
                {
                    if(M[y][x] > M[y][x - 1])
                    {
                        z = 1;
                        if(M[y][x - 1] < M[i][j])
                        {
                            i = y;
                            j = x - 1;
                        }
                    }
                }
                if(x < w - 1)
                {
                    if(M[y][x] > M[y][x + 1])
                    {
                        z = 1;
                        if(M[y][x + 1] < M[i][j])
                        {
                            i = y;
                            j = x + 1;
                        }
                    }
                }
                if(y < h - 1)
                {
                    if(M[y][x] > M[y + 1][x])
                    {
                        z = 1;
                        if(M[y + 1][x] < M[i][j])
                        {
                            i = y + 1;
                            j = x;
                        }
                    }
                }
                
                if(z == 0)
                {
                    N[y][x] = a;
                    flag[a - 'a'] = 0;
                    a++;
                    k.push_back(y);
                    l.push_back(x);
                }
                else
                {
                    if(i == y - 1) N[y][x] = 'N';
                    else if(i == y + 1) N[y][x] = 'S';
                    else if(j == x - 1) N[y][x] = 'W';
                    else if(j == x + 1) N[y][x] = 'E';
                }
                
                ULTIMA[y][x] = ' ';
            }
        }
        /*
        for(y = 0;y < h;y++)
        {
            for(x = 0;x < w;x++)
                cout << N[y][x] << " ";
            cout << endl;
        }
        */
        for(x = 0;x < k.size();x++)
            gg(k[x],l[x]);
        
        a = 'a';
        for(y = 0;y < h;y++)
        {
            for(x = 0;x < w;x++)
            {
                if(flag[N[y][x] - 'a'] == 0)
                {
                    flag[N[y][x] - 'a'] = a;
                    a++;
                }
                ULTIMA[y][x] = flag[N[y][x] - 'a'];
            }
        }
        
        cout << "Case #" << ccase << ":" << endl;
        for(y = 0;y < h;y++)
        {
            for(x = 0;x < w;x++)
                cout << ULTIMA[y][x] << " ";
            cout << endl;
        }
    }

    while(getchar()!=EOF);
    return 0;
}
