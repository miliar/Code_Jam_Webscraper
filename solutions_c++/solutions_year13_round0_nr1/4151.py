// DlgGoogleCodeJam.cpp : implementation file
//

#include "stdafx.h"
#include "InnoHelper.h"
#include "DlgGoogleCodeJam.h"


#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CDlgGoogleCodeJam dialog


CDlgGoogleCodeJam::CDlgGoogleCodeJam(CWnd* pParent /*=NULL*/)
	: CDialog(CDlgGoogleCodeJam::IDD, pParent)
{
	//{{AFX_DATA_INIT(CDlgGoogleCodeJam)
		// NOTE: the ClassWizard will add member initialization here
	//}}AFX_DATA_INIT
}


void CDlgGoogleCodeJam::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CDlgGoogleCodeJam)
	DDX_Control(pDX, IDC_CB_PROBLEMS, m_cbProblems);
	//}}AFX_DATA_MAP
}


BEGIN_MESSAGE_MAP(CDlgGoogleCodeJam, CDialog)
	//{{AFX_MSG_MAP(CDlgGoogleCodeJam)
	ON_BN_CLICKED(IDC_BTN_OPENINPUT, OnBtnOpeninput)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CDlgGoogleCodeJam message handlers


BOOL CDlgGoogleCodeJam::OnInitDialog() 
{
	int				i, iProblemId;
	CString		sText;

	CDialog::OnInitDialog();

	m_bCycling = false;

	//
	iProblemId = 2012020101;
	sText.Format("%d", iProblemId);
	i = m_cbProblems.AddString("2012 QR - Problem A. Speaking in Tongues");
	m_cbProblems.SetItemData(i, iProblemId);
	m_slSolvedProblemsIDs.AddHead(sText);

	//
	iProblemId = 2012020102;
	sText.Format("%d", iProblemId);
	i = m_cbProblems.AddString("2012 QR - Problem B. Dancing With the Googlers");
	m_cbProblems.SetItemData(i, iProblemId);
	m_slSolvedProblemsIDs.AddHead(sText);

	//
	iProblemId = 2012020103;
	sText.Format("%d", iProblemId);
	i = m_cbProblems.AddString("2012 QR - Problem C. Recycled Numbers");
	m_cbProblems.SetItemData(i, iProblemId);
	m_slSolvedProblemsIDs.AddHead(sText);

	//
	iProblemId = 2012020104;
	sText.Format("%d", iProblemId);
	i = m_cbProblems.AddString("2012 QR - Problem D. Hall of Mirrors");
	m_cbProblems.SetItemData(i, iProblemId);
	m_slSolvedProblemsIDs.AddHead(sText);

	//
	iProblemId = 2012020706;
	sText.Format("%d", iProblemId);
	i = m_cbProblems.AddString("2012 WF - Problem E. Shifting Paths");
	m_cbProblems.SetItemData(i, iProblemId);
	m_slSolvedProblemsIDs.AddHead(sText);

	//
	iProblemId = 2013010101;
	sText.Format("%d", iProblemId);
	i = m_cbProblems.AddString("2013 QR - Problem A");
	m_cbProblems.SetItemData(i, iProblemId);
	m_slSolvedProblemsIDs.AddHead(sText);

	return TRUE;  // return TRUE unless you set the focus to a control
	              // EXCEPTION: OCX Property Pages should return FALSE
}

void CDlgGoogleCodeJam::OnBtnOpeninput() 
{
	int							j, iProblemId;
	bool						bResult = true;
	CString					sMessage, sPathName, sProblemId;
	CStdioFile			fInputFile, fOutputFile;
	CFileDialog			dlgFileOpen(TRUE);
	CFileException	e;

	j = m_cbProblems.GetCurSel();
	if (j < 0)
	{
		AfxMessageBox("Please select a valid problem to solve!");
		return;
	}

	iProblemId = m_cbProblems.GetItemData(j);
	sProblemId.Format("%d", iProblemId);
	if (m_slSolvedProblemsIDs.Find(sProblemId) == NULL)
	{
		AfxMessageBox("Problem not solved yet.");
		return;
	}

	if (dlgFileOpen.DoModal() == IDOK)
	{
		sPathName = dlgFileOpen.GetPathName();

		// Open Input File
		if (!fInputFile.Open(sPathName, CFile::modeRead | CFile::typeText, &e))
		{
			bResult = false;
			sMessage.Format("Input file (%s) could not be opened.\n", sPathName);
			AfxMessageBox(sMessage);
		}
		
		// Open Output File
		if (bResult)
		{
			sPathName = sPathName.Left(sPathName.ReverseFind('.')) + ".out";

			if (!fOutputFile.Open(sPathName, CFile::modeCreate | CFile::modeWrite | CFile::typeText, &e))
			{
				bResult = false;
				sMessage.Format("Output file (%s) could not be opened or created.\n", sPathName);
				AfxMessageBox(sMessage);
			}
		}

		if (bResult)
		{
			switch (iProblemId)
			{
				case 2013010101: QR2013ProblemA(&fInputFile, &fOutputFile); break;
				case 2012020101: QR2012ProblemA(&fInputFile, &fOutputFile); break;
				case 2012020102: QR2012ProblemB(&fInputFile, &fOutputFile); break;
				case 2012020103: QR2012ProblemC(&fInputFile, &fOutputFile); break;
				case 2012020104: QR2012ProblemD(&fInputFile, &fOutputFile); break;

				case 2012020706: WF2012ProblemE(&fInputFile, &fOutputFile); break;

				default: AfxMessageBox("Problem not solved yet."); break;
			}
		}
	}
}

void CDlgGoogleCodeJam::QR2012ProblemA(CStdioFile *pInputFile, CStdioFile *pOutputFile)
{
	int				i, n;
	CString		sReadText, sWriteText, sTempText;

	pInputFile->ReadString(sReadText);
	//AfxMessageBox(sReadText);
	n = atoi(sReadText);
	for (i = 1; i <= n; i++)
	{
		pInputFile->ReadString(sReadText);
		sTempText = TranslateFromGooglerese(sReadText);

		sWriteText.Format("Case #%d: %s\n", i, sTempText);
		pOutputFile->WriteString(sWriteText);
	}
}

__int64 iMaxCycleCount = 10000; //0000000;
T_SHIFTING_PATHS	arPaths[40];

void CDlgGoogleCodeJam::WF2012ProblemE(CStdioFile *pInputFile, CStdioFile *pOutputFile)
{
	int								i, j, n, m, iLeft, iRight, iCurElement;
	__int64						iCount;
	CString						sReadText, sWriteText, sTempText;


	pInputFile->ReadString(sReadText);
	AfxMessageBox(sReadText);
	n = atoi(sReadText);
	
	for (i = 1; i <= n; i++)
	{
		pInputFile->ReadString(sReadText);
		//AfxMessageBox(sReadText);
		m = atoi(sReadText);

		for (j = 0; j < m-1; j++)
		{
			pInputFile->ReadString(sReadText);
			sscanf(sReadText,"%d %d", &iLeft, &iRight);
			StructInit(&arPaths[j], iLeft, iRight);

			sWriteText.Format("L=%d R=%d V=%d", arPaths[j].iLeftPath, arPaths[j].iRightPath, arPaths[j].iVisitNumber);
			//AfxMessageBox(sWriteText);
		}

		/*
		if (CheckForInfinity(m, m))
		{
			sTempText = "Infinity";
		}
		else
		*/
		{
			m_bCycling = true;
			iCount = 0;
			iCurElement = 0;

			//Working with 5000 iterations, but more are needed
			//WalkThroughPaths(m, m, 0, iCount);

			while (m_bCycling && (iCount < iMaxCycleCount))
			{
				if (iCurElement == m - 1)
				{
					m_bCycling = false;
					break;
				}

				iCount++;
				arPaths[iCurElement].iVisitNumber++;

				if (arPaths[iCurElement].iVisitNumber % 2 == 0)
					iCurElement = arPaths[iCurElement].iRightPath - 1;
				else
					iCurElement = arPaths[iCurElement].iLeftPath - 1;
			}

			if (iCount >= iMaxCycleCount)
				sTempText = "Infinity";
			else
				sTempText.Format("%I64d", iCount);
		}

		sWriteText.Format("Case #%d: %s\n", i, sTempText);
		pOutputFile->WriteString(sWriteText);
	}
}

bool CDlgGoogleCodeJam::CheckForInfinity(int iElCount, int iValue)
{
	bool		bResult = true;
	int			iLastValue = 0;
	CString	s, sValues, sTest, sIgnore = "#";

	while ((iValue != iLastValue) && (iValue > 1))
	{
		iLastValue = iValue;

		s.Format("%d", iValue);
		sValues += s;

		if (sValues.GetLength() == 100)
		{
			sTest = sValues.Right(10);
			if (sValues.Find(sTest) < 90)
			{
				break;
			}
		}

		for (int i = 0; i < iElCount-1; i++)
		{
			if ((arPaths[i].iLeftPath == iValue)
				|| (arPaths[i].iRightPath == iValue))
			{
				s.Format("#%d#", i+1);
				if ((sIgnore.GetLength() > 2) && (sIgnore.Find(s) >= 0))
					continue;

				iValue = i+1;
				break;
			}
		}

		if (iValue == iLastValue)
		{
			s.Format("%d#", iValue);
			sIgnore += s;

			iValue = iElCount;
			sValues.Empty();
		}
	}

	if (iValue == 1)
		bResult = false;
	else
		bResult = true;

	return bResult;
}

void CDlgGoogleCodeJam::WalkThroughPaths(int iElCount, int iValue, int iCurElement, int &iTotal)
{
	if (!m_bCycling)
		return;

	if ((iCurElement == iValue - 1)
		|| (iTotal > iMaxCycleCount))
	{
		m_bCycling = false;
		return;
	}

	iTotal++;
	arPaths[iCurElement].iVisitNumber++;

	if (arPaths[iCurElement].iVisitNumber % 2 == 0)
		WalkThroughPaths(iElCount, iValue, arPaths[iCurElement].iRightPath - 1, iTotal);
	else
		WalkThroughPaths(iElCount, iValue, arPaths[iCurElement].iLeftPath - 1, iTotal);
}

CString CDlgGoogleCodeJam::TranslateFromGooglerese(CString sSourceText)
{
	CString sDestinationText;
	char		chLetter;

	for (int i = 0; i < sSourceText.GetLength(); i++)
	{
		switch (sSourceText[i])
		{
			case 'y': chLetter = 'a'; break;
			case 'n': chLetter = 'b'; break;
			case 'f': chLetter = 'c'; break;
			case 'i': chLetter = 'd'; break;
			case 'c': chLetter = 'e'; break;
			case 'w': chLetter = 'f'; break;
			case 'l': chLetter = 'g'; break;
			case 'b': chLetter = 'h'; break;
			case 'k': chLetter = 'i'; break;
			case 'u': chLetter = 'j'; break;
			case 'o': chLetter = 'k'; break;
			case 'm': chLetter = 'l'; break;
			case 'x': chLetter = 'm'; break;
			case 's': chLetter = 'n'; break;
			case 'e': chLetter = 'o'; break;
			case 'v': chLetter = 'p'; break;
			case 'z': chLetter = 'q'; break;
			case 'p': chLetter = 'r'; break;
			case 'd': chLetter = 's'; break;
			case 'r': chLetter = 't'; break;
			case 'j': chLetter = 'u'; break;
			case 'g': chLetter = 'v'; break;
			case 't': chLetter = 'w'; break;
			case 'h': chLetter = 'x'; break;
			case 'a': chLetter = 'y'; break;
			case 'q': chLetter = 'z'; break;
			default: chLetter = sSourceText[i]; break;
		}

		sDestinationText += chLetter;
	}

	return sDestinationText;
}

void CDlgGoogleCodeJam::QR2012ProblemB(CStdioFile *pInputFile, CStdioFile *pOutputFile)
{
	int				i, j, n;
	int				iGooglersCount, iSurprisingTriplets, iMinScore, iScores[100], iMaxCount;
	CString		sReadText, sWriteText, sTempText;
	CString		sDigit;

	pInputFile->ReadString(sReadText);
	//AfxMessageBox(sReadText);
	n = atoi(sReadText);
	for (i = 1; i <= n; i++)
	{
		pInputFile->ReadString(sReadText);
//	/*
		sscanf(sReadText,	"%d %d %d"
											" %d %d %d %d %d %d %d %d %d %d"
											" %d %d %d %d %d %d %d %d %d %d"
											" %d %d %d %d %d %d %d %d %d %d"
											" %d %d %d %d %d %d %d %d %d %d"
											" %d %d %d %d %d %d %d %d %d %d"
											" %d %d %d %d %d %d %d %d %d %d"
											" %d %d %d %d %d %d %d %d %d %d"
											" %d %d %d %d %d %d %d %d %d %d"
											" %d %d %d %d %d %d %d %d %d %d"
											" %d %d %d %d %d %d %d %d %d %d", 
						&iGooglersCount, &iSurprisingTriplets, &iMinScore, 
											&iScores[0], &iScores[1],  &iScores[2],  &iScores[3],  &iScores[4],  &iScores[5],  &iScores[6],  &iScores[7],  &iScores[8],  &iScores[9], 
											&iScores[10], &iScores[11], &iScores[12], &iScores[13], &iScores[14], &iScores[15], &iScores[16], &iScores[17], &iScores[18], &iScores[19], 
											&iScores[20], &iScores[21], &iScores[22], &iScores[23], &iScores[24], &iScores[25], &iScores[26], &iScores[27], &iScores[28], &iScores[29], 
											&iScores[30], &iScores[31], &iScores[32], &iScores[33], &iScores[34], &iScores[35], &iScores[36], &iScores[37], &iScores[38], &iScores[39], 
											&iScores[40], &iScores[41], &iScores[42], &iScores[43], &iScores[44], &iScores[45], &iScores[46], &iScores[47], &iScores[48], &iScores[49], 
											&iScores[50], &iScores[51], &iScores[52], &iScores[53], &iScores[54], &iScores[55], &iScores[56], &iScores[57], &iScores[58], &iScores[59], 
											&iScores[60], &iScores[61], &iScores[62], &iScores[63], &iScores[64], &iScores[65], &iScores[66], &iScores[67], &iScores[68], &iScores[69], 
											&iScores[70], &iScores[71], &iScores[72], &iScores[73], &iScores[74], &iScores[75], &iScores[76], &iScores[77], &iScores[78], &iScores[79], 
											&iScores[80], &iScores[81], &iScores[82], &iScores[83], &iScores[84], &iScores[85], &iScores[86], &iScores[87], &iScores[88], &iScores[89], 
											&iScores[90], &iScores[91], &iScores[92], &iScores[93], &iScores[94], &iScores[95], &iScores[96], &iScores[97], &iScores[98], &iScores[99]
					);
//		*/

		iMaxCount = 0;
		
		for (j = 0; j < iGooglersCount; j=j+1)
		{
			if (iMinScore == 0)
			{
				iMaxCount = iGooglersCount;
				break;
			}

			if (iScores[j] == 0)
			{
				continue;
			}

			if (iScores[j] >= 3*iMinScore - 2)
				iMaxCount++;
			else
				if ((iSurprisingTriplets > 0)
					&& (iScores[j] >= 3*iMinScore - 4))
				{
					iMaxCount++;
					iSurprisingTriplets--;
				}
		}

		sWriteText.Format("Case #%d: %d\n", i, iMaxCount);
		pOutputFile->WriteString(sWriteText);
	}
}

int Power(int iNumber, int iPower)
{
	int iResult = 1;

	if (iPower == 0)
		return 1;

	if (iPower == 1)
		return iNumber;
	else
	{
		while (iPower > 0)
		{
			iResult *= iNumber;
			iPower--;
		}

		return iResult;
	}
}

void CDlgGoogleCodeJam::QR2012ProblemC(CStdioFile *pInputFile, CStdioFile *pOutputFile)
{
	int				i, j, k, T, iResult, A, B, x, iDigitsCount, iNumber, iHead, iTail;
	CString		sReadText, sWriteText, sTempText;

	pInputFile->ReadString(sReadText);
	sscanf(sReadText, "%d", &T);

	for (i = 1; i <= T; i++)
	{
		pInputFile->ReadString(sReadText);
		sscanf(sReadText, "%d %d", &A, &B);

		iResult = 0;
		iDigitsCount = 0;

		x = A;
		while (x > 0)
		{
			iDigitsCount++;
			x = x/10;
		}

		for (j = A; j <= B; j++)
		{
			for (k = 1; k < iDigitsCount; k++)
			{
				iHead		= j / Power(10, k);
				iTail		= j % Power(10, k);

				iNumber = iTail*Power(10, iDigitsCount-k) + iHead;

				if (iNumber == j)
					break;

				if ((j < iNumber) && (iNumber <= B))
					iResult++;
			}
		}

		sWriteText.Format("Case #%d: %d\n", i, iResult);
		pOutputFile->WriteString(sWriteText);
	}
}

void CDlgGoogleCodeJam::QR2012ProblemD(CStdioFile *pInputFile, CStdioFile *pOutputFile)
{
	int				i, T, iResult;
	CString		sReadText, sWriteText, sTempText;

	pInputFile->ReadString(sReadText);
	sscanf(sReadText, "%d", &T);

	for (i = 1; i <= T; i++)
	{
		pInputFile->ReadString(sReadText);
//		sscanf(sReadText, "%d %d", &A, &B);

		iResult = 0;


		sWriteText.Format("Case #%d: %d\n", i, iResult);
		pOutputFile->WriteString(sWriteText);
	}
}

void CDlgGoogleCodeJam::QR2013ProblemA(CStdioFile *pInputFile, CStdioFile *pOutputFile)
{
	int				i, j, k, n;
	bool			bXWon, bOWon, bEmptyCellFound;
	CString		sReadText, sWriteText, sTempText;
	CString		sBoard[4], sBoard2[4];

	pInputFile->ReadString(sReadText);
	//AfxMessageBox(sReadText);
	n = atoi(sReadText);
	for (i = 1; i <= n; i++)
	{
		for (j=0; j<4; j++)
		{
			pInputFile->ReadString(sBoard[j]);
		}

		pInputFile->ReadString(sReadText);

		// Init
		bXWon = false;
		bOWon = false;
		bEmptyCellFound = false;

		// Check sBoard
		for (j=0; j<4; j++)
		{
			if (( sBoard[j] == "XXXX")
				|| (sBoard[j]	== "TXXX")
				|| (sBoard[j] == "XTXX")
				|| (sBoard[j] == "XXTX")
				|| (sBoard[j] == "XXXT"))
			{
				bXWon = true;
				break;
			}

			if (( sBoard[j] == "OOOO")
				|| (sBoard[j]	== "TOOO")
				|| (sBoard[j] == "OTOO")
				|| (sBoard[j] == "OOTO")
				|| (sBoard[j] == "OOOT"))
			{
				bOWon = true;
				break;
			}

			if (sBoard[j].Find('.') >= 0)
				bEmptyCellFound = true;
		}

		if (!bXWon && !bOWon)
		{
			// Transponder
			for (j=0; j<4; j++)
			{
				sBoard2[j].Empty();

				for (k=0; k<4; k++)
					sBoard2[j] += sBoard[k][j];

				//AfxMessageBox(sBoard2[j]);
			}
			// Check sBoard2
			for (j=0; j<4; j++)
			{
				if (( sBoard2[j] == "XXXX")
					||( sBoard2[j] == "TXXX")
					|| (sBoard2[j] == "XTXX")
					|| (sBoard2[j] == "XXTX")
					|| (sBoard2[j] == "XXXT"))
				{
					bXWon = true;
					break;
				}

				if (( sBoard2[j] == "OOOO")
					|| (sBoard2[j] == "TOOO")
					|| (sBoard2[j] == "OTOO")
					|| (sBoard2[j] == "OOTO")
					|| (sBoard2[j] == "OOOT"))
				{
					bOWon = true;
					break;
				}
			}

		}

		// Check diagonals
		if (((sBoard[0][0] == 'X') || (sBoard[0][0] == 'T'))
			&& ((sBoard[1][1] == 'X') || (sBoard[1][1] == 'T'))
			&& ((sBoard[2][2] == 'X') || (sBoard[2][2] == 'T'))
			&& ((sBoard[3][3] == 'X') || (sBoard[3][3] == 'T'))
			)
			bXWon = true;

		if (((sBoard[0][0] == 'O') || (sBoard[0][0] == 'T'))
			&& ((sBoard[1][1] == 'O') || (sBoard[1][1] == 'T'))
			&& ((sBoard[2][2] == 'O') || (sBoard[2][2] == 'T'))
			&& ((sBoard[3][3] == 'O') || (sBoard[3][3] == 'T'))
			)
			bOWon = true;

		if (((sBoard[0][3] == 'X') || (sBoard[0][3] == 'T'))
			&& ((sBoard[1][2] == 'X') || (sBoard[1][2] == 'T'))
			&& ((sBoard[2][1] == 'X') || (sBoard[2][1] == 'T'))
			&& ((sBoard[3][0] == 'X') || (sBoard[3][0] == 'T'))
			)
			bXWon = true;

		if (((sBoard[0][3] == 'O') || (sBoard[0][3] == 'T'))
			&& ((sBoard[1][2] == 'O') || (sBoard[1][2] == 'T'))
			&& ((sBoard[2][1] == 'O') || (sBoard[2][1] == 'T'))
			&& ((sBoard[3][0] == 'O') || (sBoard[3][0] == 'T'))
			)
			bOWon = true;

		// Prepare result
		if (bXWon)
			sTempText = "X won";
		else if (bOWon)
			sTempText = "O won";
		else if (bEmptyCellFound)
			sTempText = "Game has not completed";
		else
			sTempText = "Draw";


		// Print result
		sWriteText.Format("Case #%d: %s\n", i, sTempText);
		pOutputFile->WriteString(sWriteText);
	}
}
