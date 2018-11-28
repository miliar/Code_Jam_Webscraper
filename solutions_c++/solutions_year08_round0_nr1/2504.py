#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

typedef struct SearchEngineS {
    char*                   strName;
    struct SearchEngineS*   pNext;
} SearchEngineT;

SearchEngineT* g_pHashSrc[256];
SearchEngineT* g_pHashDet[256];

void PutHash(SearchEngineT** ppHash, SearchEngineT* pNode)
{
    int nKey=pNode->strName[0]&0xff;
    pNode->pNext=ppHash[nKey];
    ppHash[nKey]=pNode;
}

SearchEngineT* GetHash(SearchEngineT** ppHash, const char* strName)
{
    int nKey=strName[0]&0xff;
    SearchEngineT* pNode=ppHash[nKey];
    SearchEngineT* pPreNode=NULL;

    while(NULL!=pNode) {
        if(0==strcmp(pNode->strName, strName)) {
            if(NULL==pPreNode)
                ppHash[nKey]=pNode->pNext;
            else
                pPreNode->pNext=pNode->pNext;

            return pNode;
        }

        pPreNode=pNode;
        pNode=pNode->pNext;
    }

    return NULL;
}

void FreeNodesInHash(SearchEngineT** ppHash)
{
    for(int i=0; i<256; ++i) {
        SearchEngineT* pNode=ppHash[i];
        while(NULL!=pNode) {
            SearchEngineT* pNext=pNode->pNext;
            free(pNode->strName);
            free(pNode);

            pNode=pNext;
        }
    }
}

bool RunCases(FILE *pfIn, FILE *pfOut)
{
    int nCaseNum=0;
    char buf[1024];

    fgets(buf, sizeof(buf), pfIn);
    sscanf(buf, "%d", &nCaseNum);
    for(int i=1; i<=nCaseNum; ++i) {
        int nSENum=0;

        memset(g_pHashSrc, 0, sizeof(g_pHashSrc));
        memset(g_pHashDet, 0, sizeof(g_pHashDet));

        // read search engine names
        fgets(buf, sizeof(buf), pfIn);
        sscanf(buf, "%d", &nSENum);
        for(int j=0; j<nSENum; ++j) {
            fgets(buf, sizeof(buf), pfIn);
            int nLen=strlen(buf);
            if((nLen>0) && (buf[nLen-1]=='\n'))
                buf[nLen-1]='\0';

            SearchEngineT* pNode=(SearchEngineT *)malloc(sizeof(SearchEngineT));
            if(NULL==pNode) {
                assert(0);
                return false;
            }

            pNode->strName=strdup(buf);
            if(NULL==pNode->strName) {
                assert(0);
                return false;
            }
            pNode->pNext=NULL;

            PutHash(g_pHashSrc, pNode);
        }

        SearchEngineT** ppSrc=g_pHashSrc;
        SearchEngineT** ppDet=g_pHashDet;

        // read queries
        int nQNum=0;
        fgets(buf, sizeof(buf), pfIn);
        sscanf(buf, "%d", &nQNum);

        int nSwitchNum=0;
        int nSrcCount=nSENum;
        for(int j=0; j<nQNum; ++j) {
            fgets(buf, sizeof(buf), pfIn);
            int nLen=strlen(buf);
            if((nLen>0) && (buf[nLen-1]=='\n'))
                buf[nLen-1]='\0';

            SearchEngineT* pNode=GetHash(ppSrc, buf);
            if(NULL==pNode)
                continue;

            PutHash(ppDet, pNode);
            --nSrcCount;
            if(0==nSrcCount) {
                ++nSwitchNum;

                // for the next query
                SearchEngineT** ppTemp=ppSrc;
                ppSrc=ppDet;
                ppDet=ppTemp;
                nSrcCount=nSENum;
                
                pNode=GetHash(ppSrc, buf);
                PutHash(ppDet, pNode);
                --nSrcCount;
            }
        }

        fprintf(pfOut, "Case #%d: %d\n",
                i, nSwitchNum);

        FreeNodesInHash(ppSrc);
        FreeNodesInHash(ppDet);
    }

    return true;
}

int main(int argc, char *argv[], char *arge[])
{
    if(!RunCases(stdin, stdout))
        return 1;

    return 0;
}
