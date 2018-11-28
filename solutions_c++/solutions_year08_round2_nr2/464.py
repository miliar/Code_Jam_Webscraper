// God.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "God.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#endif


#include <stdio.h>
#include <math.h>

int disjoint[1024];

int findroot(int r)
{
    while( disjoint[r] != r )
    {
        r = disjoint[r];
    }
    return r;
}

// The one and only application object

CWinApp theApp;

using namespace std;

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
	int nRetCode = 0;

	// initialize MFC and print and error on failure
	if (!AfxWinInit(::GetModuleHandle(NULL), NULL, ::GetCommandLine(), 0))
	{
		// TODO: change error code to suit your needs
		_tprintf(_T("Fatal Error: MFC initialization failed\n"));
		nRetCode = 1;
	}
	else
	{
		// TODO: code your application's behavior here.

        //init
        bool isprime[1024];
        memset(isprime, true, 1024);
        isprime[0] = false;
        isprime[1] = false;
        for (int i = 2; i < 1024; i++)
        {
            if (!isprime[i]) continue;
            for (int j = i+i; j < 1024; j+=i)
            {
                isprime[j] = false;
            }
        }

        //start
        FILE * fi = argc > 1? fopen(argv[1], "r"): stdin;
        int n;
        fscanf(fi, "%d", &n);
        for (int casee = 1; casee <= n; casee++)
        {
            int a, b, p;
            fscanf(fi, "%d %d %d", &a, &b, &p);
            //disjoint set
            for (int c = (b-a+1); --c >= 0; )
            {
                disjoint[c] = c;
            }
            //find upper bound prime
            int up = 1023;
            /*for (up = p; up < 1024; up++)
            {
                if (!isprime[up]) continue;
                if ((a+up-1)/up == b/up) break;
            }*/
            //prime test
            //int count = 0;
            for (int c = a; c <= b; c++)
            {
                for (int pt = p; pt <= up; pt++)
                {
                    if (!isprime[pt]) continue;
                    if (c%pt == 0)
                    {
                        int div = c/pt;
                        for (; pt*div >= a; div--)
                        {
                            //disjoint[c-a] = pt*div-a;
                            int roota = findroot(c-a);
                            int rootb = findroot(pt*div-a);
                            disjoint[roota] = rootb;
                            //printf("dup:%d\n", c);
                            //break;
                        }
                    }
                }
            }
            //count
            int count = 0;
            bool marked[1024];
            memset(marked, 0, 1024);
            for (int p = (b-a+1); --p >= 0; )
            {
                int rr = findroot(p);
                if (!marked[rr])
                {
                    count++;
                    marked[rr] = true;
                }
            }
            printf("Case #%d: %d\n", casee, count); //(b-a+1)-count);
        }

	}

	return nRetCode;
}
