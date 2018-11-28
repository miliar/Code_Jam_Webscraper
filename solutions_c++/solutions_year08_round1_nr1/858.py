#pragma once

#include <afxtempl.h>

class CMainClass
{
public:
	CMainClass(void);
	~CMainClass(void);

	int MainFn(int argc, TCHAR** argv, TCHAR** envp);

private:
	void Permutation(int* buf, int n);
	void SortA(int* buf, int n);
	void SortD(int* buf, int n);
	int MaxSubSum(int* buf, int n);

	int a[2000];
	int b[2000];
	
	CList<int,int> m_intList;
};
