#include "StdAfx.h"


CAlienLanguage::CAlienLanguage(void)
{
    m_pDictionary = NULL;
    m_iCaseCount = 0;
    m_pCases = NULL;
}

CAlienLanguage::~CAlienLanguage(void)
{
    if (m_pDictionary)
    {
        delete []m_pDictionary->pWords;
        delete m_pDictionary;
    }

    if (m_pCases)
    {
        delete []m_pCases->pParts;
        delete m_pCases;
    }
}

bool CAlienLanguage::Load(fstream &fInput)
{
    bool bRet = false;
    string sTemp;

    if (m_pDictionary = new ALIENLANGUAGE_DICTIONARY)
    {
        fInput >> m_pDictionary->iWordLength;
        fInput >> m_pDictionary->iCount;
        fInput >> m_iCaseCount;

        if (m_pDictionary->iCount > 0 && (m_pDictionary->pWords = new string[m_pDictionary->iCount]))
        {
            for (int i = 0; i < m_pDictionary->iCount; i++)
            {
                fInput >> m_pDictionary->pWords[i];
            }
        }

        if (m_iCaseCount > 0 && (m_pCases = new ALIENLANGUAGE_CASE[m_iCaseCount]))
        {
            for (int i = 0; i < m_iCaseCount; i++)
            {
                m_pCases[i].iMatchCount = 0;
                fInput >> sTemp;
                if (m_pCases[i].pParts = new string[m_pDictionary->iWordLength])
                {
                    int iPartIndex = 0;
                    bool bLock = false;
                    for (int j = 0; j < sTemp.length(); j++)
                    {
                        if (sTemp[j] == '(')
                            bLock = true;
                        else if (sTemp[j] == ')')
                            bLock = false;
                        else if (sTemp[j] >= 'a' && sTemp[j] <= 'z')
                        {
                            m_pCases[i].pParts[iPartIndex] += sTemp[j];
                        }
                        if (!bLock)
                            iPartIndex++;
                    }
                }
            }
        }
        bRet = true;
    }
    return bRet;
}

bool CAlienLanguage::Save(fstream &fOutput)
{
    for (int i = 0; i < m_iCaseCount; i++)
    {
        fOutput << "Case #" << i + 1 << ": " << m_pCases[i].iMatchCount << endl;
    }
    return true;
}

void CAlienLanguage::Transfer()
{
    bool bMatch = false;
    int iMidValue = 0, iTmp = 0;

    for (int i = 0; i < m_iCaseCount; i++)
    {
        for (int j = 0; j < m_pDictionary->iCount; j++)
        {
            bMatch = true;
            for (int k = 0; k < m_pDictionary->iWordLength; k++)
            {
                if (m_pCases[i].pParts[k].find(m_pDictionary->pWords[j][k]) == -1)
                {
                    bMatch = false;
                    break;
                }
            }
            if (bMatch)
                m_pCases[i].iMatchCount++;
        }
    }
}
