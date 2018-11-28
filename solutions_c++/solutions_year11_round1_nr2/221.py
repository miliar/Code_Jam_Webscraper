#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

int n, m;

bool used[32];
int sz[128];
char s[128][16];
bool letters[128][32];
bool noword[128];

char l[32];
char pat[16];

void read()
{
    scanf("%d %d\n",&n,&m);
    for(int i = 0; i < n; i ++)
    {
        scanf("%s",&s[i]);
        sz[i] = strlen(s[i]);
        for(int j = 0; j < sz[i]; j ++)
            letters[i][ s[i][j] - 'a' ] = 1;
    }
}

bool check(int ind, char let)
{
//    cout << "CHECK: " << s[ind] << " " << let << endl;
    for(int i = 0; i < n; i ++)
        if(!noword[i] && letters[i][let - 'a'] && sz[i] == sz[ind])
        {
            bool fl = true;
            for(int j = 0; j < sz[i]; j ++)
            {
                if(pat[j] != '$' && s[i][j] != pat[j])
                {
//                    cout << "crash1: " << s[i][j] << " " << j << endl;
                    fl = false;
                    break;
                }
                if(used[ s[i][j] - 'a' ] && s[i][j] != pat[j])
                {
//                    cout << "crash2: " << s[i][j] << " " << j << endl;
                    fl= false;
                    break;
                }
            }
            if(!fl) noword[i] = 1;
            else return true;
        }
    return false;
}

void put(int ind, char let)
{
//    cout << "PUT: " << let << endl;
    for(int i = 0; i < sz[ind]; i ++)
        if(s[ind][i] == let)
            pat[i] = let;
}

int calc(int ind)
{
//    cout << "\nSTART\n";
//    cout << ind << " " << s[ind] << ":\n";
    
    memset(noword, 0, sizeof(noword));
    memset(used, 0, sizeof(used));
    for(int i = 0; i < sz[ind]; i ++) pat[i] = '$';
    
    int ret = 0;
    for(int i = 0; i < 26; i ++)
    {
        if(check(ind, l[i]))
        {
            if(letters[ind][ l[i] - 'a' ]) put(ind, l[i]);
            else
            {
  //              cout << "ADD: " << l[i] << endl;
                ret ++;
            }
        }
        used[l[i] - 'a'] = 1;
    }
    return ret;
}

void solve()
{
    int score = -1, idx;
    for(int i = 0; i < n; i ++)
    {
        int tmp = calc(i);
        if(score < tmp)
        {
            score = tmp;
            idx = i;
        }
    }
    //cout << "Write: " << score;
    printf(" %s",s[idx]);
}

void doit()
{
    memset(letters, 0, sizeof(letters));
    
    read();
    
    for(int i = 0; i < m; i ++)
    {
        scanf("%s",&l);
        solve();
    }
    printf("\n");
}

int main()
{
    int t;
    scanf("%d",&t);
    for(int i = 1; i <= t; i ++)
    {
        printf("Case #%d:",i);
        doit();
    }
    
    return 0;
}
