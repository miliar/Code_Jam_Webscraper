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

	//struct key
	//{
		int aaa[5000];
	//	int index;
	//};
	//struct key
	//long bbb[1000];
	
	CList<int,int> m_intList;
};
