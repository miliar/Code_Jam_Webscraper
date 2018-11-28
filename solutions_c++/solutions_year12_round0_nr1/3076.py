
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
	if(f.Open(_T("d:\\A-small-attempt1.in"),CFile::modeRead))
	{
		char* chData = new char[f.GetLength()+1];
		if(f.Read(chData,f.GetLength()+1))
		{
			int nTestSize = 0;
			char* pData = GetNumber(chData,nTestSize);
			int nCharectorCount[26];
			memset(nCharectorCount,0,sizeof(int)*26);
			CFile fOut(_T("E:\\Kim1.Out"),CFile::modeCreate | CFile::modeReadWrite);

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
