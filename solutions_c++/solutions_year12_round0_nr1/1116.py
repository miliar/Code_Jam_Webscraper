/**
* AliTokenizer �ӿ�ʾ������ 
* �з������ı�"�ջ��������", ��ӡ���ִʽ�� 
*/
#include <iostream>
#include "ali_tokenizer.h"
#include "ali_tokenizer_define.h"
using namespace std;
using namespace ws;

int main()
{
        //step1: ��������
        AliTokenizerFactory tokenizerFactory;
        tokenizerFactory.Init("/usr/local/libdata/AliWS/conf/AliTokenizer.conf"); 
        //step2: ��ȡ�Ա����ķִ�
        AliTokenizer *tokenizer = tokenizerFactory.GetAliTokenizer("TAOBAO_CHN"); 
        //step3: �����ִʽ������
        SegResult *pSegResult = tokenizer->CreateSegResult();
        //step4: �ִ� 
        const char * text  = "�ջ��������"; 
        tokenizer->Segment(text, strlen(text), UTF8 , SEG_TOKEN_SEMANTIC|SEG_TOKEN_RETRIEVE, pSegResult) ;
        //step5: �������ִʽ�� 
        string res;
        SegToken* pToken = pSegResult->GetFirstToken(MAIN_LIST);
        while (pToken)
        {
                res += string((const char*)pToken->pWord, pToken->length);
                res += " ";
                pToken = pToken->pRightSibling;
        }
        cout << res << endl;
        //step6: �ͷ��ڴ�ռ� 
        tokenizer->ReleaseSegResult(pSegResult);  //�ͷŷִʽ�� 
        
        return 0;
}