// 2012 Code Jam - Dancing with the Googlers

#include <afxwin.h>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

#define _CRT_SECURE_NO_WARNINGS

// The one and only application object
CWinApp
   theApp;

using namespace std;

int MaxDancers(INT nN, INT nS, INT np, INT nt[])
{
   INT
      nDancers = 0;

   for (INT i = 0; i < nN; i++)
      {
      INT
         nScore  = nt[i],
         nHighNS,
         nHighS;

      switch (nScore % 3)
         {
         case 0:  nHighNS = nScore / 3;     nHighS = nScore ? min(10, nHighNS + 1) : 0; break;
         case 1:  nHighNS = nScore / 3 + 1; nHighS = nHighNS; break;
         case 2:  nHighNS = nScore / 3 + 1; nHighS = min(10, nHighNS + 1); break;
         default: ASSERT(FALSE);
         }

      if (nHighNS >= np)
         nDancers++;
      else if (nHighS == np && nS)
         {
         nS--;
         nDancers++;
         }
      }

   return (nDancers);
}

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
   FILE
      *fpi = _tfopen(_T("B-large.in"), _T("r")),
      *fpo = _tfopen(_T("B-large.out"), _T("w"));

   INT
      nT = 0,
      nN = 0,
      nS = 0,
      np = 0,
      nt[100];

   _ftscanf(fpi, _T("%d"), &nT);

   for (int i = 0; i < nT; i++)
      {
      _ftscanf(fpi, _T("%d"), &nN);
      _ftscanf(fpi, _T("%d"), &nS);
      _ftscanf(fpi, _T("%d"), &np);

      for (int j = 0; j < nN; j++)
         _ftscanf(fpi, _T("%d"), &nt[j]);

      _ftprintf_s(fpo, _T("Case #%d: %d\n"), i + 1, MaxDancers(nN, nS, np, nt));
      }

   return (0);
}
