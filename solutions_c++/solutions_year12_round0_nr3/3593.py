
// CodeJam1Dlg.cpp : ���� ����
//

#include "stdafx.h"
#include "CodeJam1.h"
#include "CodeJam1Dlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

char g_Rank[26];



// ���� ���α׷� ������ ���Ǵ� CAboutDlg ��ȭ �����Դϴ�.

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// ��ȭ ���� �������Դϴ�.
	enum { IDD = IDD_ABOUTBOX };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV �����Դϴ�.

// �����Դϴ�.
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialog(CAboutDlg::IDD)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
END_MESSAGE_MAP()


// CCodeJam1Dlg ��ȭ ����




CCodeJam1Dlg::CCodeJam1Dlg(CWnd* pParent /*=NULL*/)
	: CDialog(CCodeJam1Dlg::IDD, pParent)
	, m(_T(""))
	
{
	m_strRank = //"ykficwmbkuomxsevqpdrjgtxyq";
//                 abcdefghijklmnopqrstuvwxyz   
				//"yhesowcxduillbkrztnwjpfmaz";
				  "yhesocvxduiglbkrztnwjpfmaq";
//                 abcdefghijklmnopqrstuvwxyz   
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CCodeJam1Dlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	DDX_Text(pDX, IDC_EDIT1, m_strRank);
}

BEGIN_MESSAGE_MAP(CCodeJam1Dlg, CDialog)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	//}}AFX_MSG_MAP
	ON_BN_CLICKED(IDOK, &CCodeJam1Dlg::OnBnClickedOk)
	ON_BN_CLICKED(IDOK2, &CCodeJam1Dlg::OnBnClickedOk2)
	ON_BN_CLICKED(IDOK3, &CCodeJam1Dlg::OnBnClickedOk3)
	ON_BN_CLICKED(IDOK4, &CCodeJam1Dlg::OnBnClickedOk4)
	ON_BN_CLICKED(IDCANCEL, &CCodeJam1Dlg::OnBnClickedCancel)
END_MESSAGE_MAP()


// CCodeJam1Dlg �޽��� ó����

BOOL CCodeJam1Dlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// �ý��� �޴��� "����..." �޴� �׸��� �߰��մϴ�.

	// IDM_ABOUTBOX�� �ý��� ��� ������ �־�� �մϴ�.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// �� ��ȭ ������ �������� �����մϴ�. ���� ���α׷��� �� â�� ��ȭ ���ڰ� �ƴ� ��쿡��
	//  �����ӿ�ũ�� �� �۾��� �ڵ����� �����մϴ�.
	SetIcon(m_hIcon, TRUE);			// ū �������� �����մϴ�.
	SetIcon(m_hIcon, FALSE);		// ���� �������� �����մϴ�.

	// TODO: ���⿡ �߰� �ʱ�ȭ �۾��� �߰��մϴ�.
	
	return TRUE;  // ��Ŀ���� ��Ʈ�ѿ� �������� ������ TRUE�� ��ȯ�մϴ�.
}

void CCodeJam1Dlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialog::OnSysCommand(nID, lParam);
	}
}

// ��ȭ ���ڿ� �ּ�ȭ ���߸� �߰��� ��� �������� �׸�����
//  �Ʒ� �ڵ尡 �ʿ��մϴ�. ����/�� ���� ����ϴ� MFC ���� ���α׷��� ��쿡��
//  �����ӿ�ũ���� �� �۾��� �ڵ����� �����մϴ�.

void CCodeJam1Dlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // �׸��⸦ ���� ����̽� ���ؽ�Ʈ

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Ŭ���̾�Ʈ �簢������ �������� ����� ����ϴ�.
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// �������� �׸��ϴ�.
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// ����ڰ� �ּ�ȭ�� â�� ���� ���ȿ� Ŀ���� ǥ�õǵ��� �ý��ۿ���
//  �� �Լ��� ȣ���մϴ�.
HCURSOR CCodeJam1Dlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}
char*  GetNumber(char* pData,int&nData)
{
	nData = atoi(pData);
	while(1)
	{
		if(*pData == 10 || *pData == 32)
			break;
		pData++;
	}
	pData++;
	return pData;
}
char* CountCharector(char* pData,int* pCnt)
{
	while(1)
	{
		if(*pData == NULL)
			break;
		if(*pData >= 'a' && *pData <= 'z')
		{
			pCnt[(*pData) - 'a']++;
		}
		
		pData++;
	}
	if(*pData != 0)
	{
		pData ++;
	}
	return pData;
}
char* SwapCharector(char* pSource,char* pDest,int *pCounter)
{
	int  nRank[26];
	for(int iter = 0 ; iter < 26 ; iter ++)
	{
		nRank[iter] = 0;
		for(int j = 0 ; j < 26 ; j ++)
		{
			if(j != iter)
			{	
				if(pCounter[iter] < pCounter[j])
				{
					nRank[iter] ++;
				}else if(pCounter[iter] == pCounter[j])
				{
					if(iter < j)
					{
						nRank[iter]++;
					}
				}
			}
		}
	}
	while(1)
	{
		if(*pSource == 10 || *pSource == NULL)
			break;
		if(*pSource >= 'a' && *pSource <= 'z')
		{
			*pDest = g_Rank[*pSource - 'a'];
		}else
		{
			*pDest = *pSource;
		}
		pDest++;
		pSource++;
	}
	pSource++;
	return pSource;
}
void CCodeJam1Dlg::OnBnClickedOk()
{
	
	CFile f;
	
	UpdateData();
	m = "";
	sprintf(g_Rank,"%s",m_strRank);
	if(f.Open(_T("d:\\A-small-attempt0.in"),CFile::modeRead))
	{
		char* chData = new char[f.GetLength()+1];
		if(f.Read(chData,f.GetLength()+1))
		{
			int nTestSize = 0;
			char* pData = GetNumber(chData,nTestSize);
			int nCharectorCount[26];
			memset(nCharectorCount,0,sizeof(int)*26);
			CFile fOut(_T("E:\\A-small-attempt0.Out"),CFile::modeCreate | CFile::modeReadWrite);

			for(int iter = 0 ; iter < nTestSize ; iter ++)
			{
				
				CountCharector(pData,nCharectorCount);
				char* pSwapChar = new char[200];
				memset(pSwapChar,0,200);
				char *pNextLine = SwapCharector(pData,pSwapChar,nCharectorCount);

				char chWriteData[64];
				sprintf(chWriteData,"Case #%d: ",iter +1);
				fOut.Write(chWriteData,strlen(chWriteData));
				fOut.Write(pSwapChar,strlen(pSwapChar));
				fOut.Write("\n",1);
				pData = pNextLine;
				m.Append(chWriteData);
				m.Append(pSwapChar);
				m.Append("\n\r");
				delete [] pSwapChar;
			}
		}

	}
	CDC* pDC = GetDC();
	CRect rt;
	GetClientRect(rt);
	pDC->FillSolidRect(rt,RGB(200,200,200));
	pDC->DrawText(m,rt,DT_WORDBREAK);
	UpdateData(FALSE);
}

void CCodeJam1Dlg::OnBnClickedOk2()
{
	CFile f;
	
	UpdateData();
	m = "";
	sprintf(g_Rank,"%s",m_strRank);
	if(f.Open(_T("d:\\B-large.in"),CFile::modeRead))
	{   
		char* chData = new char[f.GetLength()+1];
		if(f.Read(chData,f.GetLength()+1))
		{
			int nTestSize = 0; 
			char* pData = GetNumber(chData,nTestSize);
			int nCharectorCount[26];
			memset(nCharectorCount,0,sizeof(int)*26);
			CFile fOut(_T("E:\\B-large.Out"),CFile::modeCreate | CFile::modeReadWrite);

			for(int iter = 0 ; iter < nTestSize ; iter ++)
			{
				int nN = 0;
				int nS = 0;
				int nP = 0;
				pData = GetNumber(pData,nN);
				pData = GetNumber(pData,nS);
				pData = GetNumber(pData,nP);
				int* nScore = new int[nN];
				int nBest = 0;
				int nDisableFaultCount = 0;
				int nCount = 0;
				for(int j = 0 ; j < nN ; j++)
				{
					pData = GetNumber(pData,nScore[j] );
					if(nScore[j] - nP * 3 >= -2)
					{
						nCount++;
					}else if(nScore[j] - nP * 3 >= -4 && nS >0 && nScore[j] > 1 )
					{
						nCount++;
						nS--;
					}
				}
				char chWriteData[64];
				if(iter +1 ==nTestSize)
				{
					sprintf(chWriteData,"Case #%d: %d",iter +1,nCount);
				}
				else
				{
					sprintf(chWriteData,"Case #%d: %d\n",iter +1,nCount);
				}
				fOut.Write(chWriteData,strlen(chWriteData));
				delete[] nScore;
			}
		}

	}
	CDC* pDC = GetDC();
	CRect rt;
	GetClientRect(rt);
	pDC->FillSolidRect(rt,RGB(200,200,200));
	pDC->DrawText(m,rt,DT_WORDBREAK);
	UpdateData(FALSE);
	
}
BOOL AddData(int nData,int*pBuffer,int nSize)
{
	if(nData < nSize)
	{
		pBuffer[nData]++;
		return pBuffer[nData] == 2;


	}
	return FALSE;
}
void CCodeJam1Dlg::OnBnClickedOk3()
{
	int nCount = 0;
	


	CFile f;
	
	UpdateData();
	m = "";
	sprintf(g_Rank,"%s",m_strRank);
	if(f.Open(_T("d:\\C-small-attempt0.in"),CFile::modeRead))
	{
		char* chData = new char[f.GetLength()+1];
		if(f.Read(chData,f.GetLength()+1))
		{
			int nTestSize = 0;
			char* pData = GetNumber(chData,nTestSize);
			int nCharectorCount[26];
			memset(nCharectorCount,0,sizeof(int)*26);
			CFile fOut(_T("E:\\C-small-attempt0.Out"),CFile::modeCreate | CFile::modeReadWrite);

			for(int iter = 0 ; iter < nTestSize ; iter ++)
			{
				int nMaxData = 0;
				int nMinData = 0;

				pData = GetNumber(pData,nMinData);
				pData = GetNumber(pData,nMaxData);
				nCount = 0;
				for(int j = nMinData ; j <= nMaxData ; j ++)
				{
					CString strTemp;
					char chData[64];
					char chTemp[64];
					sprintf(chData,"%d",j);
					int nLength = strlen(chData);
					chTemp[nLength ] = NULL;
					for(int q= 0 ; q<nLength; q++)
					{
						for(int l= 0 ; l<nLength;l++)
						{
							chTemp[l] = chData[(l+q)%nLength];

						}
						
						int nData = atoi(chTemp);
						if(nData > j && nData <= nMaxData) 
						{
							nCount++;
						}
					}
				}
				
				char chWriteData[64];
				sprintf(chWriteData,"Case #%d: %d\n",iter +1,nCount);	
				fOut.Write(chWriteData,strlen(chWriteData));
				
			}
		}

	}


	
	CString strData;
	strData.Format("%d",nCount);
}/*
double abs(double dData)
{
	if(dData < 0)
	{
		dData *= -1;
	}
	return dData;
}*/
#include <math.h>
int GetMyView(double dX,double dY,double dDirectionX,double dDirectionY, int nDistance
			  ,double dMyWidth,double dMyHeight,char chMirror[30][30])
{
	double dMyPosX = dX;
	double dMyPosY = dY;

	double dTravelDistance = 0;
	double dTemp = sqrt(dDirectionX*dDirectionX + dDirectionY*dDirectionY);
	int nCnt = 0;
	int nMyView = 0;
	BOOL bCornner = FALSE;
	HWND hWnd = GetDesktopWindow();
	HDC hDC = GetDC(hWnd);
	CBrush hr;
	hr.CreateSolidBrush(RGB(200,200,200));
	
	//FillRect(hDC,CRect(0,0,1000,1000),(HBRUSH)hr.GetSafeHandle());
	MoveToEx(hDC,dX*300 + 100,dY*300+ 100,NULL);
	while(dTravelDistance <= nDistance)
	{
		dTravelDistance += dTemp;
		dX += dDirectionX;
		dY += dDirectionY;
		
		
		if(dTravelDistance > nDistance)
		{
			break;
		}

		
		CPen pen;
		pen.CreatePen(PS_SOLID,2,RGB(rand()%255,rand()%255,rand()%255));
		SelectObject(hDC,pen.GetSafeHandle());
		LineTo(hDC,dX*300+ 100,dY*300+ 100);
		int nUpdataCnt = 0;
		if(dDirectionX >0 && abs(dX - (int)dX) < 0.001)
		{
			int nX = dX +1;
			int nY = dY+0.5;
			if(chMirror[nY][nX] == 1)
			{
				
				if(abs(dY - (int)dY) < 0.001 && chMirror[nY][nX] == 1 )
				{
					if( dDirectionY > 0 && chMirror[nY-1][nX] == 1)
					{
						TRACE("Total : %f POSX : %f POSY : %f Cnt : %d nX : %d  nY : %d\n",dTravelDistance,dX,dY,nCnt,nX,nY);
						dDirectionX *= -1;
						nUpdataCnt =1;
					}

					if( dDirectionY < 0 && chMirror[nY+1][nX] == 1)
					{
						TRACE("Total : %f POSX : %f POSY : %f Cnt : %d nX : %d  nY : %d\n",dTravelDistance,dX,dY,nCnt,nX,nY);
						dDirectionX *= -1;
						nUpdataCnt =1;
					}


				}else
				{
						TRACE("Total : %f POSX : %f POSY : %f Cnt : %d nX : %d  nY : %d\n",dTravelDistance,dX,dY,nCnt,nX,nY);
						dDirectionX *= -1;
						nUpdataCnt =1;
				
				}
				
				
			}

		}else if(dDirectionX < 0 && abs(dX - (int)dX) < 0.001)
		{
			int nX = dX+0.5;
			int nY = dY+0.5 ;
			if(chMirror[nY][nX] == 1)
			{
				if(abs(dY - (int)dY) < 0.001 && chMirror[nY][nX] == 1 )
				{
					if( dDirectionY > 0 && chMirror[nY-1][nX] == 1)
					{
						TRACE("Total : %f POSX : %f POSY : %f Cnt : %d nX : %d  nY : %d\n",dTravelDistance,dX,dY,nCnt,nX,nY);
						dDirectionX *= -1;
						nUpdataCnt =1;
					}

					if( dDirectionY < 0 && chMirror[nY+1][nX] == 1)
					{
						TRACE("Total : %f POSX : %f POSY : %f Cnt : %d nX : %d  nY : %d\n",dTravelDistance,dX,dY,nCnt,nX,nY);
						dDirectionX *= -1;
						nUpdataCnt =1;
					}


				}else
				{
						TRACE("Total : %f POSX : %f POSY : %f Cnt : %d nX : %d  nY : %d\n",dTravelDistance,dX,dY,nCnt,nX,nY);
						dDirectionX *= -1;
						nUpdataCnt =1;
				
				}
			}
		}


		if(dDirectionY >0 && abs(dY - (int)dY) < 0.001)
		{
			int nX = dX+0.5;
			int nY = dY +1;
			if(chMirror[nY][nX] == 1)
			{
				int nDir = 1;
				if(nUpdataCnt)
					nDir = -1;
				if(abs(dX - (int)dX) < 0.001)
				{
					if( dDirectionX * nDir > 0 && chMirror[nY][nX-1] == 1)
					{
						TRACE("Total : %f POSX : %f POSY : %f Cnt : %d nX : %d  nY : %d\n",dTravelDistance,dX,dY,nCnt,nX,nY);
						dDirectionY *= -1;
						nUpdataCnt =1;
					}

					if( dDirectionX * nDir < 0 && chMirror[nY][nX+1] == 1)
					{
						TRACE("Total : %f POSX : %f POSY : %f Cnt : %d nX : %d  nY : %d\n",dTravelDistance,dX,dY,nCnt,nX,nY);
						dDirectionY *= -1;
						nUpdataCnt =1;
					}


				}else
				{
						TRACE("Total : %f POSX : %f POSY : %f Cnt : %d nX : %d  nY : %d\n",dTravelDistance,dX,dY,nCnt,nX,nY);
						dDirectionY *= -1;
						nUpdataCnt =1;
				
				}
				
			}
		}else if(dDirectionY < 0 && abs(dY - (int)dY) < 0.001)
		{
			int nX = dX+1;
			int nY = dY+0.5;
			if(chMirror[nY][nX] == 1)
			{
				int nDir = 1;
				if(nUpdataCnt)
					nDir = -1;
				if(abs(dX - (int)dX) < 0.001)
				{
					if( dDirectionX * nDir > 0 && chMirror[nY][nX-1] == 1)
					{
						TRACE("Total : %f POSX : %f POSY : %f Cnt : %d nX : %d  nY : %d\n",dTravelDistance,dX,dY,nCnt,nX,nY);
						dDirectionY *= -1;
						nUpdataCnt =1;
					}

					if( dDirectionX * nDir < 0 && chMirror[nY][nX+1] == 1)
					{
						TRACE("Total : %f POSX : %f POSY : %f Cnt : %d nX : %d  nY : %d\n",dTravelDistance,dX,dY,nCnt,nX,nY);
						dDirectionY *= -1;
						nUpdataCnt =1;
					}


				}else
				{
						TRACE("Total : %f POSX : %f POSY : %f Cnt : %d nX : %d  nY : %d\n",dTravelDistance,dX,dY,nCnt,nX,nY);
						dDirectionY *= -1;
						nUpdataCnt =1;
				
				}
			}
		}
		nCnt += nUpdataCnt;
		//TRACE("Total : %f POSX : %f POSY : %f Cnt : %d\n",dTravelDistance,dX,dY,nCnt);
		if(abs(dMyPosX - dX) < 0.001 && abs(dMyPosY - dY) < 0.001)
		{
			nMyView =nCnt ;
			
			return nCnt;
			
			
			
			
			
			
			
		}
		
	}
	return nMyView ;
}
char* GetMirror(char* pData,char* nMirror)
{
	while(1)
	{
		if(*pData == 10)
			break;
		switch(*pData)
		{
		case '#':
			*nMirror = 1;
			break;
		
		case 'X':
			*nMirror = 2;
			break;
		case '.':
		default:
			*nMirror = 0;
			break;


		}
		nMirror++;
		pData++;

	}
	pData++;

	return pData;
}
double GetDistance(double dW,double dH)
{
	return sqrt(dW*dW+dH*dH);
}
void CCodeJam1Dlg::OnBnClickedOk4()
{

	int nCount = 0;
	


	CFile f;
	
	UpdateData();
	m = "";
	sprintf(g_Rank,"%s",m_strRank);
	if(f.Open(_T("d:\\D-small-attempt0.in"),CFile::modeRead))
	{
		char* chData = new char[f.GetLength()+1];
		if(f.Read(chData,f.GetLength()+1))
		{
			int nTestSize = 0;
			char* pData = GetNumber(chData,nTestSize);
			int nCharectorCount[26];
			memset(nCharectorCount,0,sizeof(int)*26);
			CFile fOut(_T("E:\\D-small-attempt0.Out"),CFile::modeCreate | CFile::modeReadWrite);

			for(int iter = 0 ; iter < nTestSize ; iter ++)
			{
					int nHeight = 0;
					int nWidth = 0;
					int nDistance = 0;
					pData = GetNumber(pData,nHeight);
					pData = GetNumber(pData,nWidth);
					pData = GetNumber(pData,nDistance);
					

					double dCurrentPositionX = 0.5;
					double dCurrentPositionY = 0.5;


					char chDataSet[30][30];

					BOOL bFindMyPos = FALSE;
					for(int nH = 0 ; nH < nHeight ; nH++)
					{
						pData = GetMirror(pData,chDataSet[nH]);
						if(bFindMyPos == FALSE)
						{
							for(int nW = 1; nW < nWidth -1; nW++)
							{
								if(chDataSet[nH][nW] == 2)
								{
									dCurrentPositionX = nW - dCurrentPositionX;
									dCurrentPositionY = nH - dCurrentPositionY;
								}
							}
						}
						
					}
					
					
					int nView =0;
					
					
					double dMyWidth = nWidth -1;
					double dMyHeight = nHeight -1;

					double dDirectionX = 0;
					double dDirectionY = 0.5;
					int nLoopCnt = dMyWidth > dMyHeight ? dMyWidth*2 : dMyHeight*2;
					
					if(iter != 2)
						continue;

					for(int w = 0 ; w < nWidth ; w ++)
					{
						TRACE("\n");
						for(int h = 0 ; h <nHeight ; h ++)
						{
							TRACE("%d",chDataSet[h][w]);
						}
					}
					HDC hDC = ::GetDC(::GetDesktopWindow());
					CBrush hr;
					hr.CreateSolidBrush(RGB(200,200,200));
					
					FillRect(hDC,CRect(0+ 100,0+ 100,(dMyWidth-1)*300+ 100,(dMyHeight-1)* 300+ 100),(HBRUSH)hr.GetSafeHandle());
					
					for(int j = 1 ; j<= nLoopCnt; j ++)
					{

						dDirectionX = 0.5/j;
						dDirectionY = 0.5;
						nView += GetMyView(dCurrentPositionX,dCurrentPositionY,dDirectionX ,dDirectionY,nDistance
							,dMyWidth,dMyHeight,chDataSet);

						dDirectionX = -0.5/j;
						dDirectionY = 0.5;
						nView += GetMyView(dCurrentPositionX,dCurrentPositionY,dDirectionX ,dDirectionY,nDistance
							,dMyWidth,dMyHeight,chDataSet);

						dDirectionX = 0.5;
						dDirectionY = 0.5/j;
						nView += GetMyView(dCurrentPositionX,dCurrentPositionY,dDirectionX ,dDirectionY,nDistance
							,dMyWidth,dMyHeight,chDataSet);

						dDirectionX = 0.5;
						dDirectionY = -0.5/j;
						nView += GetMyView(dCurrentPositionX,dCurrentPositionY,dDirectionX ,dDirectionY,nDistance
							,dMyWidth,dMyHeight,chDataSet);

					}



					
					dDirectionX = 0;
					dDirectionY = 0.5;
					nView += GetMyView(dCurrentPositionX,dCurrentPositionY,dDirectionX ,dDirectionY,nDistance
						,dMyWidth,dMyHeight,chDataSet);

					dDirectionX = 0;
					dDirectionY = -0.5;
					nView += GetMyView(dCurrentPositionX,dCurrentPositionY,dDirectionX ,dDirectionY,nDistance
						,dMyWidth,dMyHeight,chDataSet);

					dDirectionX = -0.5;
					dDirectionY = 0;
					nView += GetMyView(dCurrentPositionX,dCurrentPositionY,dDirectionX ,dDirectionY,nDistance
						,dMyWidth,dMyHeight,chDataSet);

					dDirectionX = 0.5;
					dDirectionY = 0;
					nView += GetMyView(dCurrentPositionX,dCurrentPositionY,dDirectionX ,dDirectionY,nDistance
						,dMyWidth,dMyHeight,chDataSet);

				
				
				char chWriteData[64];
				sprintf(chWriteData,"Case #%d: %d\n",iter +1,nView);	
				fOut.Write(chWriteData,strlen(chWriteData));
				
			}
		}

	}




	
	

	
	

	 


}

void CCodeJam1Dlg::OnBnClickedCancel()
{
	for(int iter = 0 ; iter <8 ; iter ++)
	{
		for(int j = 0; j< 8 ;j++)
		{

		}
	}
}
