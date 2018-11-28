//---------------------------------------------------------------------------
//-- Code Jam 2012 - Qalification Round Problem A. Speaking in Tongues
//-- @Carlos Mendoza
//--
//-- Simple String Manipulation
//---------------------------------------------------------------------------
#include <stdio.h>
#include <string.h>

char Vec[30];

void init()
{
        Vec['a' - 'a'] = 'y';
        Vec['b' - 'a'] = 'h';
        Vec['c' - 'a'] = 'e';
        Vec['d' - 'a'] = 's';
        Vec['e' - 'a'] = 'o';
        Vec['f' - 'a'] = 'c';
        Vec['g' - 'a'] = 'v';
        Vec['h' - 'a'] = 'x';
        Vec['i' - 'a'] = 'd';
        Vec['j' - 'a'] = 'u';
        Vec['k' - 'a'] = 'i';
        Vec['l' - 'a'] = 'g';
        Vec['m' - 'a'] = 'l';
        Vec['n' - 'a'] = 'b';
        Vec['o' - 'a'] = 'k';
        Vec['p' - 'a'] = 'r';
        Vec['q' - 'a'] = 'z';
        Vec['r' - 'a'] = 't';
        Vec['s' - 'a'] = 'n';
        Vec['t' - 'a'] = 'w';
        Vec['u' - 'a'] = 'j';
        Vec['v' - 'a'] = 'p';
        Vec['w' - 'a'] = 'f';
        Vec['x' - 'a'] = 'm';
        Vec['y' - 'a'] = 'a';
        Vec['z' - 'a'] = 'q';
}

int main()
{
        freopen("A-small-attempt0.in","rt",stdin);
        freopen("out.txt","wt",stdout);

        int T,len,ntest=1;
        char G[500],R[500];

        init();
        scanf("%d\n",&T);
        while(T--)
        {
                gets(G);
                len = strlen(G);
                for(int i=0; i<len; i++)
                        if(G[i] == ' ')
                                R[i] = G[i];
                        else
                                R[i] = Vec[G[i] - 'a'];
                R[len] = '\0';
                printf("Case #%d: ",ntest++); puts(R);

        }
        return 0;
}



