// 2012 Code Jam - Recycled Numbers

#include <afxwin.h>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

#define _CRT_SECURE_NO_WARNINGS

// The one and only application object
CWinApp
   theApp;

using namespace std;

INT Find(const CArray<INT, INT>& arynVals, INT nVal)
{
   for (int i = 0, size = arynVals.GetSize(); i < size; i++)
      if (arynVals[i] == nVal)
         return (i);

   return (-1);
}

INT GetRecycledNumbers(INT nIn, CArray<INT, INT>& arynOut)
{
   CString
      strIn,
      strOut;

   INT
      nOut;

   strIn.Format(_T("%d"), nIn);
   arynOut.RemoveAll();

   for (int i = 1, size = strIn.GetLength(); i < size; i++)
      {
      strOut.Format(_T("%s%s"), strIn.Mid(i), strIn.Mid(0, i));
      nOut = _ttoi(strOut);

      if (nOut > nIn && Find(arynOut, nOut) == -1)
         arynOut.Add(nOut);
      }

   return (arynOut.GetSize());
}

INT GetRecycledPairs(INT nA, INT nB)
{
   CArray<INT, INT>
      arynCandidates;

   INT
      nPairs = 0;

   for (int i = nA; i < nB; i++)
      for (int j = 0, size = GetRecycledNumbers(i, arynCandidates); j < size; j++)
         if (arynCandidates[j] <= nB)
            nPairs++;

   return (nPairs);
}

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
   FILE
      *fpi = _tfopen(_T("C-small.in"), _T("r")),
      *fpo = _tfopen(_T("C-small.out"), _T("w"));

   INT
      nT = 0,
      nA = 0,
      nB = 0;

   _ftscanf(fpi, _T("%d"), &nT);

   for (int i = 0; i < nT; i++)
      {
      _ftscanf(fpi, _T("%d"), &nA);
      _ftscanf(fpi, _T("%d"), &nB);
      _ftprintf_s(fpo, _T("Case #%d: %d\n"), i + 1, GetRecycledPairs(nA, nB));
      }

   return (0);
}
