#include "StdAfx.h"


const string c_sWelcom = "welcome to code jam";

CWelcome::CWelcome(void)
{
    m_iCaseCount = 0;
    m_pCases = NULL;
}

CWelcome::~CWelcome(void)
{
    if (m_pCases)
        delete []m_pCases;
}

bool CWelcome::Load(fstream &fInput)
{
    bool bRet = false;
    string sTemp;

    fInput >> m_iCaseCount;
    getline(fInput, sTemp);
    if (m_iCaseCount > 0 && (m_pCases = new WELCOME_CASE[m_iCaseCount]))
    {
        for (int i = 0; i < m_iCaseCount; i++)
        {
            m_pCases[i].iCount = 0;
            getline(fInput, sTemp);
            m_pCases[i].sValue = sTemp;
        }
        bRet = true;
    }
    return bRet;
}

bool CWelcome::Save(fstream &fOutput)
{
    char szResult[5] = "\0";

    for (int i = 0; i < m_iCaseCount; i++)
    {
        sprintf_s(szResult, 5, "%04u", m_pCases[i].iCount);
        fOutput << "Case #" << i + 1 << ": " << szResult << endl;
    }
    return true;
}

void CWelcome::Transfer()
{
    int iIndex = 0, iIndexSearch = 0;

    for (int i = 0; i < m_iCaseCount; i++)
    {
        m_pCases[i].iCount = CheckSeparatedString((char *)m_pCases[i].sValue.data(), (char *)c_sWelcom.data());
    }
}

int CWelcome::CheckSeparatedString(char *pSource, char *pToSearch)
{
    int iRet = 0, iSrcLength = 0, iTSLength = 0, iCount = 0;
    char cToSearch = pToSearch[0];

    if ((iSrcLength = strlen(pSource)) >= (iTSLength = strlen(pToSearch)))
    {
        for (int i = 0; i < iSrcLength - iTSLength + 1; i++)
        {
            if (pSource[i] == pToSearch[0])
            {
                iCount = 1;
                while (++i < iSrcLength) 
                {
                    if (pSource[i] == pToSearch[0])
                        iCount++;
                    else if (pSource[i] == pToSearch[1])
                        break;
                }

                if (iTSLength > 1)
                    iCount *= CheckSeparatedString(pSource + i, pToSearch + 1);

                iRet += iCount;
            }
        }
    }
    return iRet;
}