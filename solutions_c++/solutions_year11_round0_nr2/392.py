// Robots.cpp

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _DEBUG
#define ASSERT(x)  {if(!(x)) __asm{int 3};}
#else
#define ASSERT(x)  do{}while(0)
#endif
typedef long long LONG;

#define MAXN 101

char com[26][26];
char opp[26][26];
#define ID(c) (c-'A')
#define Com(x, y) (com[ID(x)][ID(y)])
#define Opp(x, y)  (opp[ID(x)][ID(y)])
#define SetCom(x, y, z) do{ com[ID(x)][ID(y)] = (z); com[ID(y)][ID(x)] = (z);} while(0)
#define SetOpp(x, y) do{ opp[ID(x)][ID(y)] = 1; opp[ID(y)][ID(x)] = 1;} while(0)

bool HasOpp(char * start, char * end, char x);

class Stack
{
public:
    char ns[MAXN];
    int len;
    Stack()
    {
        *ns = 0;
        len = 0;
    }
    char peek()
    {
        ASSERT(len > 0);
        return ns[len-1];
    }
    void pop()
    {
        ASSERT(len > 0);
        len --;
    }
    int size()
    {
        return len;
    }
    void push(char c)
    {
        ASSERT(len < MAXN-1);
        ns[len] = c;
        len ++;
    }
    void clear()
    {
        len = 0;
    }
    bool oppose(char c)
    {
        return HasOpp(ns, ns+len-1, c);
    }

    void print(int caseIndex)
    {
        ns[len] = 0;
        char * p = ns;
        printf("Case #%d: [", caseIndex);
        if(*p)
        {
            printf("%c", *p);
            p = p+1;
            while(*p)
            {
                printf(", %c", *p);
                ++p;
            }
        }
        printf("]\n");
    }
};

void reset()
{
    memset(com, 0, sizeof(com));
    memset(opp, 0, sizeof(opp));
}

//inclusive
bool HasOpp(char * start, char * end, char x)
{
    char *p;
    for(p = start; p <= end; ++p)
    {
        if(Opp(*p, x))
            return true;
    }
    return false;
}
void solve(char * const ns, int caseIndex)
{
    ASSERT(strlen(ns) >= 1);
    Stack stack;
    char *p = ns;
    char c, top;
    while(*p)
    {
        if(stack.size() > 0)
        {
            top = stack.peek();
            c = Com(top, *p);
            if(c)
            {
                stack.pop();
                stack.push(c);
            }
            else if(stack.oppose(*p))
            {
                stack.clear();
            }
            else 
                stack.push(*p);
        }
        else 
        {
            stack.push(*p);
        }
        p++;
    }
    stack.print(caseIndex);

}

int main(int argc, const char* argv[])
{
    int T = 0 ,N = 0, C, D;
    int ret;
    int result = 0;
    int caseIndex = 1;
    char ds[10], cs[10];
    char ns[MAXN];
    ret = scanf("%d", &T);
    ASSERT(ret != EOF && T > 0 && T<=100);
    while(T--)
    {
        reset();
        scanf("%d", &C);
        while(C--)
        {
            scanf("%s", cs);
            ASSERT(strlen(cs) == 3);
            SetCom(cs[0], cs[1], cs[2]);
        }
        scanf("%d", &D);
        while(D--)
        {
            scanf("%s", ds);
            ASSERT(strlen(ds) == 2);
            SetOpp(ds[0], ds[1]);
        }
        scanf("%d%s", &N, ns);
        solve(ns, caseIndex++);
        
    }
	return 0;
}

