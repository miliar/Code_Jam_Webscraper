#include<cstdio>
#include<iostream>
using namespace std;
int T[30];
string A ="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string B ="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
void f()
{
    for (int i=0; i<A.size(); i++)
    {
        if (A[i]==' ') continue;
        int x=A[i]-'a';
        int y=B[i]-'a';
        T[x]=y;   
    }
    T[25]=16;
    T[16]=25;
//    for (int i=0; i<30 ; i++) printf ("%c %d-> %c\n", i+'a', i, T[i]+'a');
}   
int main ()
{
    f();
    int t,p=0;
    scanf ("%d", &t);
    char x[150],z;
    for (int i=1; i<=t; i++)
    {
        int ss=1;
        while (ss)
        {
            scanf ("%c%s", &z,x);
            if (z=='\n')
            {
  	      if (i==t) 
	      {
		printf("\n");
		return 0;
	      }
                if (p)
                {
                    ss=0;
                    printf("\nCase #%d: ", i+1);   
                }
                else printf("Case #%d: ", i);
            }
            for (int i=0; x[i]; i++)
            {
                int xx=x[i]-'a';
                printf ("%c", T[xx]+'a');
            }
            printf (" ");
            p=1;
        }
    }
return 0;
}
