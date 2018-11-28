
// CodeJam1Dlg.cpp : 구현 파일
//

#include "stdafx.h"
#include "CodeJam1.h"
#include "CodeJam1Dlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

char g_Rank[26];



// 응용 프로그램 정보에 사용되는 CAboutDlg 대화 상자입니다.

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// 대화 상자 데이터입니다.
	enum { IDD = IDD_ABOUTBOX };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV 지원입니다.

// 구현입니다.
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


// CCodeJam1Dlg 대화 상자




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


// CCodeJam1Dlg 메시지 처리기

BOOL CCodeJam1Dlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// 시스템 메뉴에 "정보..." 메뉴 항목을 추가합니다.

	// IDM_ABOUTBOX는 시스템 명령 범위에 있어야 합니다.
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

	// 이 대화 상자의 아이콘을 설정합니다. 응용 프로그램의 주 창이 대화 상자가 아닐 경우에는
	//  프레임워크가 이 작업을 자동으로 수행합니다.
	SetIcon(m_hIcon, TRUE);			// 큰 아이콘을 설정합니다.
	SetIcon(m_hIcon, FALSE);		// 작은 아이콘을 설정합니다.

	// TODO: 여기에 추가 초기화 작업을 추가합니다.
	
	return TRUE;  // 포커스를 컨트롤에 설정하지 않으면 TRUE를 반환합니다.
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

// 대화 상자에 최소화 단추를 추가할 경우 아이콘을 그리려면
//  아래 코드가 필요합니다. 문서/뷰 모델을 사용하는 MFC 응용 프로그램의 경우에는
//  프레임워크에서 이 작업을 자동으로 수행합니다.

void CCodeJam1Dlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // 그리기를 위한 디바이스 컨텍스트

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// 클라이언트 사각형에서 아이콘을 가운데에 맞춥니다.
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// 아이콘을 그립니다.
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// 사용자가 최소화된 창을 끄는 동안에 커서가 표시되도록 시스템에서
//  이 함수를 호출합니다.
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
