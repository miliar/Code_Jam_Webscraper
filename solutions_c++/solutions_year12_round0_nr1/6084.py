
// 201201Dlg.cpp : implementation file
//

#include "stdafx.h"
#include "201201.h"
#include "201201Dlg.h"
#include "afxdialogex.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CMy201201Dlg dialog




CMy201201Dlg::CMy201201Dlg(CWnd* pParent /*=NULL*/)
	: CDialogEx(CMy201201Dlg::IDD, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CMy201201Dlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CMy201201Dlg, CDialogEx)
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDOK, &CMy201201Dlg::OnBnClickedOk)
END_MESSAGE_MAP()


// CMy201201Dlg message handlers

BOOL CMy201201Dlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	// TODO: Add extra initialization here

	return TRUE;  // return TRUE  unless you set the focus to a control
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CMy201201Dlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

// The system calls this function to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CMy201201Dlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

#define msgbox(x) MessageBoxA(NULL, x, "", MB_OK);

char lm[26]={
	'y', 'n', 'f', 'i', 'c', //abcde
	'w', 'l', 'b', 'k', 'u', //fghij
	'o', 'm', 'x', 's', 'e', //klmno
	'v', 'z', 'p', 'd', 'r', //pqrst
	'j', 'g', 't', 'h', 'a', //uvwxy
	'q'};                    //z

char ml[26]={
	'y', 'h', 'e', 's', 'o', //abcde
	'c', 'v', 'x', 'd', 'u', //fghij
	'i', 'g', 'l', 'b', 'k', //klmno
	'r', 'z', 't', 'n', 'w', //pqrst
	'j', 'p', 'f', 'm', 'a', //uvwxy
	'q'                      //z
};
//abcd fghi klno qrst uvwxy z
void chgr(char* input)
{
	for(int i=0;i<strlen(input);i++)
		switch(input[i])
		{
		case ' ': break;
		case '\r': break;
		case '\n': break;
		case '\0': break;
		default:
			input[i] = ml[input[i]-'a'];
			break;
		}
}

const int MAX_LINE_COUNT=120;
void freadline(FILE* fp, char* str)
{
}
void CMy201201Dlg::OnBnClickedOk()
{

	char* input[30];
	char str[MAX_LINE_COUNT];
	int idx=0, res=1, count=0;
	FILE* fp = fopen("C:\\input\\A-small-attempt0.in", "r");
	fscanf_s(fp, "%d", &count);
	fgets(str, MAX_LINE_COUNT, fp);
	for(;idx<count;)
	{
		memset(str, 0, MAX_LINE_COUNT);
		fgets(str, MAX_LINE_COUNT, fp);
		input[idx]= new char[strlen(str)];
		strcpy(input[idx++], str);
	}
	fclose(fp);
	fp = fopen("C:\\input\\A-small-attempt0.out", "w");
	for(idx=0;idx<count;)
	{
		chgr(input[idx]);
		fprintf(fp, "Case #%d: %s", idx, input[idx++]);
	}
	fflush(fp);
	fclose(fp);
	CDialogEx::OnOK();
}
