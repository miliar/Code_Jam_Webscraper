#include <iostream>
using namespace std;
int L, D, N;
string s[10000];
string pat;
int jump[3000];

void solve (int pos)
{
 cin >> pat;
 int i;
 int wh = -1;
 memset (jump, -1, sizeof (jump));
 
 for (i =pat.size () - 1; i >=0; i--)
 {
        if (pat[i] == ')') wh = i;
        else
        if (pat[i] == '(') jump[i] = wh, wh = -1;
        else
        jump [i] = wh; 
}


int cj = -1;
int p = 0;
int j; int res  = 0;
for (j = 0; j < D; j++)
{    
    cj = -1; p = 0;
for (i = 0; i < pat.size (); i++)
{
    if (pat[i] =='(') {cj = jump[i];continue;}
    
    if (s[j][p] == pat[i]) 
    {
        p++;
    if (cj != -1) i = cj, cj = -1; 
    }
    else
        if (cj == -1) break;
}
    if (p == L) res++;
}
printf ("Case #%d: %d\n",pos, res);
}
int main ()
{
    scanf ("%d%d%d", &L, &D, &N);

int i;
for (i =0; i< D; i++) cin >> s[i];

for (i = 0; i< N; i++) solve (i+1);    
    
    
    
    return 0;
}
