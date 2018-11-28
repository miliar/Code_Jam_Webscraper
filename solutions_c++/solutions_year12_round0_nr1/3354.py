// 2012 Code Jam - Googlerese

#include <afxwin.h>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

#define _CRT_SECURE_NO_WARNINGS

// The one and only application object
CWinApp
   theApp;

using namespace std;

CString ScanLine(FILE *fpi)
{
   CString
      strOut;

   TCHAR
      tcIn;

   while (_ftscanf(fpi, _T("%c"), &tcIn) != EOF)
      {
      if (tcIn == _T('\n') || tcIn == _T('\r'))
         {
         if (!strOut.IsEmpty())
            break;
         }
      else
         strOut += tcIn;
      }

   return (strOut);
}

TCHAR TranslateChar(TCHAR tcIn)
{
   switch (tcIn)
      {
      case _T(' '): return (_T(' '));
      case _T('a'): return (_T('y'));
      case _T('b'): return (_T('h'));
      case _T('c'): return (_T('e'));
      case _T('d'): return (_T('s'));
      case _T('e'): return (_T('o'));
      case _T('f'): return (_T('c'));
      case _T('g'): return (_T('v'));
      case _T('h'): return (_T('x'));
      case _T('i'): return (_T('d'));
      case _T('j'): return (_T('u'));
      case _T('k'): return (_T('i'));
      case _T('l'): return (_T('g'));
      case _T('m'): return (_T('l'));
      case _T('n'): return (_T('b'));
      case _T('o'): return (_T('k'));
      case _T('p'): return (_T('r'));
      case _T('q'): return (_T('z'));
      case _T('r'): return (_T('t'));
      case _T('s'): return (_T('n'));
      case _T('t'): return (_T('w'));
      case _T('u'): return (_T('j'));
      case _T('v'): return (_T('p'));
      case _T('w'): return (_T('f'));
      case _T('x'): return (_T('m'));
      case _T('y'): return (_T('a'));
      case _T('z'): return (_T('q'));
      }

   return (_T('?'));
}

CString Translate(LPCTSTR lpszIn)
{
   CString
      strIn;

   for (int i = 0, size = _tcslen(lpszIn); i < size; i++)
      strIn += TranslateChar(lpszIn[i]);

   return (strIn);
}

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
   FILE
      *fpi = _tfopen(_T("A-small.in"), _T("r")),
      *fpo = _tfopen(_T("A-small.out"), _T("w"));

   CString
      strLine;

   INT
      nT = 0;

   _ftscanf(fpi, _T("%d"), &nT);

   for (int i = 0; i < nT; i++)
      {
      strLine = ScanLine(fpi);
      _ftprintf_s(fpo, _T("Case #%d: %s\n"), i + 1, Translate(strLine));
      }

   return (0);
}
