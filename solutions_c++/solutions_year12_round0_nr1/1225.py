//#define __DEBUG_MOD__
//#include "Header.h"

//==============header.h begin===================================
#ifndef __HEADER_H
#define __HEADER_H


#include <stdio.h>
#include <string.h>  //for strcmp
#include <iostream>
using namespace std;// IM:bug:���û�����std;,���� `stack' undeclared (first use this function) 


//�����������ڿ���Debug.h�еĺ�������Ϊ,����д��#include"Debug.h"��ǰ��,������Ч
//#define __DEBUG_MOD__
//#define __ONLINE__  //������online����Զ�ע�͵���__DEVCPP_GETCHAR__


#ifndef __ONLINE__
#define __DEVCPP_GETCHAR__
#endif


#define IN  //˵���Ǹò����������
#define OUT //˵���Ǹò����������
#define INOUT //˵���Ǹò����Ǽ������룬Ҳ�����


//#include "Debug.h"
//==============Debug.h===================================
#ifndef __DEBUG_HEAD_H
#define __DEBUG_HEAD_H
#include <stdio.h>
#include <string.h> //IM: bug:memsetҪ�õ����
#include <stdarg.h>  //IM: va_listҪ��,�䳤����

enum //IM:��һ��ҪдRETVALUE 
{
    SUCCESS = 0,
    FAIL = 1
};

#define FREE_PTR(p) free(p);p=NULL;
#define DELETE_PTR(p) delete p;p=NULL;
#define DELETE_PTR_ARRAY(p) delete[] p;p=NULL;


//��.cpp�е�������������˺����е���Ϊ
//#define __DEBUG_MOD__
//#define __ONLINE__
static FILE* s_fpLog = stdout; //stderr;
//ֻҪ������onlineģʽ������������ģʽ��û�ж������ģʽ��������ӡdebug��Ϣ, �����ӡdebug��Ϣ
void DEBUG(const char *fmt, ...)
{
//#if (defined(_DEBUG) && defined(_UNITTEST))
#if (!defined(__ONLINE__) && defined(__DEBUG_MOD__))
    //fprintf(s_fpLog,"Debug: ");
    va_list	ap;
    if (s_fpLog) {
        //s_lock.Lock(); 
        //fprintf(s_fpLog, "[%d]", thread_getid());
        va_start(ap, fmt);
        vfprintf(s_fpLog, fmt, ap);
        va_end(ap);
        //s_lock.Unlock();
        fflush(s_fpLog);
    }
//endif���߼��൱��:#if (defined(__ONLINE__) ||  !defined(__DEBUG_MOD__)),����ֻҪ������onlineģʽ������������ģʽ��û�ж������ģʽ��������ӡdebug��Ϣ, �����ӡdebug��Ϣ
#endif
}


void OUTPUT(const char *fmt, ...)
{
//#if (!defined(__ONLINE__) && defined(__DEBUG_MOD__))
    //fprintf(s_fpLog,"Debug: ");
    va_list	ap;
    if (s_fpLog) {
        //s_lock.Lock(); 
        //fprintf(s_fpLog, "[%d]", thread_getid());
        va_start(ap, fmt);
        vfprintf(s_fpLog, fmt, ap);
        va_end(ap);
        //s_lock.Unlock();
        fflush(s_fpLog);
    }
//#endif
}


const int MAXFILENAME = 100;
char g_StrFileIn[MAXFILENAME] = "";
char g_StrFileOut[MAXFILENAME] = "";
void SetFileInOutName(char *strNS)
{
#ifndef __ONLINE__
    //char strNS[MAXFILENAME] = "NS_Graph_Kruskal";//namespace������
    sprintf(g_StrFileIn,"%s.In.txt",strNS);
    sprintf(g_StrFileOut,"%s.Out.txt",strNS);
    printf("%s %s %s\n",__FUNCTION__,g_StrFileIn,g_StrFileOut);
#endif
}
int ReopenStdin()
{
#ifndef __ONLINE__
    FILE *in = freopen(g_StrFileIn,"r",stdin);
    if(!in){
        printf("Open %s Error!\n",g_StrFileIn);
        return 0;
    };
    return 1;
#endif
}
int ReopenStdout()
{
#ifndef __ONLINE__
    FILE *out = freopen(g_StrFileOut,"w",stdout);
    if(!out){
        printf("Open %s Error!\n",g_StrFileOut);
        return 0;
    };
    return 1;
#endif
}
int ReopenStdinStdout()
{
    if(ReopenStdin()){
        return ReopenStdout();
    }
    return 0;
}


#endif
//===================Debug.h end==============================


//#include "Func.h"
//==============Func.h ===================================
#ifndef _FUNC_H
#define _FUNC_H

#define ASSERT(c) assert(c)
#define FUNCBEGIN printf("===BEGIN %s (%s:%d)====\n",__FUNCTION__,__FILE__,__LINE__);
#define FUNCEND printf("===END %s (%s:%d)====\n",__FUNCTION__,__FILE__,__LINE__);
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)<(b)?(b):(a))
/*
  #include <stdlib.h>
  void qsort( void *buf, size_t num, size_t size, int (*compare)(const void *, const void *) ); 
  ���ܣ� ��buf ָ�������(����num ��,ÿ��Ĵ�СΪsize)���п��������������compare �ĵ�һ������С�ڵڶ������������ظ�ֵ��������ڷ�����ֵ��������ڷ�����ֵ��������buf ָ������ݰ��������� 
//�������ο�����qsort˵�� (X)��  ����,ʵ�����ǽ�������
5 6 2 3 9 7 2 1
qsort���:9 7 6 5 3 2 2 1
The return value of this function should represent whether elem1 is considered less than, equal, or grater than elem2 by returning, respectivelly, a negative value, zero or a positive value.
*/
int compare_more(const void *a,const void *b)
{
    //return (a<b);
    /*
      ����:const void*' is not a pointer-to-object type  
      ����һ�����⣬�����Զ�   void   ָ��ִ��ȡֵ������
      return ((int)(*a)-(int)(*b));
      Ҫ��ǿ��ת����ָ�룬Ȼ����ȡֵ 
      //return *((int*)a)-*((int*)b);   
      */
    return *((int*)a) < *((int*)b);    //
}


int QSortGreater(const void *a,const void *b)
{
//qsort������õĺ�������Ϊ�����>,<�޷����Ϊ0���������-�����п�����Խ���Σ�գ���������ҿ�������õġ�
//return *(int*)a-*(int*)b;
    const int m = *(const int*)a;
    const int n = *(const int*)b;
    return m>n?1:(m==n?0:-1);
}
/*
  5 6 2 3 9 7 2 1
  qsort(a,N,sizeof(int),Greater);
  ���:
  1 2 2 3 5 6 7 9
  ����
*/
int Greater(const void *a,const void *b)
{
    //IM 2012-2-4����Ľ����Ǵ����: �������>,����-����Ϊ���ſ��ܴ���Խ������⣬����һ���Ǻ�С�ģ���һ���Ǻܴ�ģ�������Խ���ˡ�
    /*Poj.cpp:namespace Qsort_Learn��:����С�ں����Ƚϣ�������
      [0]=4 | [1]=9 | [2]=9 | [3]=2 | [4]=12 | [5]=11 | [6]=11 | [7]=7 | [8]=1 | [9]=12 | [10]=7 | [11]=3 | [12]=3 | [13]=
      4 | [14]=0 | [15]=8 | [16]=1 | [17]=6 | [18]=8 | [19]=1 |
      After qsort:[19]=1 | [16]=1 | [14]=0 | [3]=2 | [13]=4 | [12]=3 | [11]=3 | [0]=4 | [8]=1 | [10]=7 | [7]=7 | [18]=8 | [17]
      =6 | [1]=9 | [2]=9 | [15]=8 | [5]=11 | [6]=11 | [9]=12 | [4]=12 |
      ��Ϊ���ź����:
      After qsort:[17]=0 | [8]=0 | [12]=1 | [10]=1 | [5]=2 | [6]=2 | [11]=2 | [2]=2 | [16]=3 | [0]=3 | [18]=4 | [4]=5 | [14]=7
      | [19]=7 | [7]=8 | [13]=8 | [1]=9 | [3]=9 | [9]=11 | [15]=12 |
    */
    return *(int*)a - *(int*)b;
    //return *(int*)a > *(int*)b;
}
//����
int compare_less(const void *a,const void *b)
{
    return   *((int*)b) - *((int*)a);
    //return   *((int*)b) > *((int*)a);
}
//�ַ�������
int CompStrGreater(const void *a,const void *b)
{
    return strcmp((char*)a,(char*)b);//��Ҫstring.h
}
int PrintInt(int v)
{
//        cout << "Visit:" << v << endl;
    printf("%d ",v);
}
int PrintStr(const char *a)
{
    printf("%s",a);
}

template <class T>
/*print int array
  format=%d or %c or ...
bug:�������ԸĽ�Ϊ,int flagIndex,int LogLevel,char *format 
Ӧ�÷����д�ķ��������
*/
void PrintArray(T *a,int size,int flagIndex = 1,const char *format="%d") 
{
    int first = 1;
    char strIndex[]="[%d]="; //"\"[%d]=";
    //int len = strlen(format)+1+strlen(strIndex) + 1; //last 1:len of \"
    //char *str = (char*)malloc(len*sizeof(char));
    char str[10];
    if(flagIndex){
        snprintf(str,sizeof(str)-1,"%s%s",strIndex,format); //"%s%s\"",
    }else{
        snprintf(str,sizeof(str)-1,"%s",format);
    }
    //cout << str << endl; ;//"[%d]=%d"
    for(int i = 0;i<size;i++){
        if(first){
            first = 0;
        }else{
            DEBUG(" ");
        }
        if(flagIndex){
            DEBUG(str,i,a[i]);
        }else{
            DEBUG(str,a[i]);
        }
    }
    DEBUG("\n");
}




/*
  flag��ʾ�Ƿ��ӡ�±�ֵ
  ��ӡ����Ϊ1������Ϊ1
  
  ������һ�����壬��Ϊ���Ǵ�ӡ��ά��������                                      
  *((int*)a + M*i + j)                                                          
  �������������int a[MAXN][MAXN];                                                
  but in fact we only use [N][N],so *((int*)a + M*i + j) is not correct.
  ������ݵĲ�����(N,N),ʵ�ʻᰴ��[MAXN*MAXN]һ��һ�д�ӡ
  �޸�֮.
  Now only support N*N Matrix
*/
void PrintTwoArray(int **array,int Row,int Col,int flag=0)
{
    int first = 1;
    for(int i = 0;i<Row;i++){
        for(int j = 0;j<Col;j++){
	  if(first){first = 0;}
	  else{DEBUG(" ");}
	  if(flag == 1){
//   *((int*)array + n*i + j);
              DEBUG("[%d,%d]=%d",i,j,*((int*)array + Col*i + j));
                /*core:
                  (gdb) p a[0]
                  $9 = (int *) 0x0
                  (gdb) p a   
                  $10 = (int **) 0x501920
                */
                //TRACE2("[%d,%d]=%d",i,j,a[i][j]);
            }
            else{
                DEBUG("%4d",*((int*)array + Col*i + j));
            }
        }
        first = 1;
        DEBUG("\n");
    }
}
/*
  �ж����������еĸ���ֵ�Ƿ����
*/
//template class <T>
template <class T>
bool IsEqual(const T *a,int size_a,const T *b,int size_b)
{
    if(size_a != size_b)
    {
        return false;
    }
    for(int i=0;i<size_a;i++)
    {
        if(a[i] != b[i])
	{
            return false;
	}
    }
    return true;
}


template <class T>
void Swap(T *a,T *b)
{
    T t = *a;
    *a = *b;
    *b = t;
}



//��������Ҫ�ȵ���srand(time(NULL));
#include <stdlib.h>
int Random(int m) //����[0,m-1]֮��������
{
    int k = rand();
    double t = (double)k/RAND_MAX; //bug:k/RAND_MAX; ����Ҫ��(double)��ǿ��ת��������ȫ��Ϊ0
    //DEBUG("%d %d %lf ",k,RAND_MAX,t);
    return(int)(t*(m-1)+0.5); //IM,Ϊʲô������(int)(t*m)??
}




#include <vector>
int PrintVector(vector<int> &v)
{
    vector<int>::iterator iter;
    for(iter=v.begin() ; iter != v.end(); iter++) {
        cout << *iter << " ";
    }
}

#include <list>
int PrintList(list<int> &L,char *sep="=")
{
    list<int>::iterator iter;
    for(iter=L.begin() ; iter != L.end(); iter++) {
        cout << *iter << sep;
    }
    //cout << "end" << endl;
}

/*test N is prime or not
 */
#include <math.h>
bool IsPrime(int N)
{
    for(int i=2;i*i<=N;i++){
        if(!(N%i)){ //bug:����N%i
            return false;
        }
    }
    return true;
}


//��ӡһ�����б��
#define PrintLineSep DEBUG("=================\n");
#endif
//==============Func.h end===================================


//==============Header.h end===================================

#endif



namespace NS_SpeakingInTongues
{
/*Speaking in Tongues
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
*/
    int main()
    {
        //A-small.in.txt
        SetFileInOutName("A-small");
        ReopenStdinStdout();
        char mapping[26] = {'y','h','e','s','o','c','v',  \
                            'x','d','u','i','g','l','b',  \
                            'k','r','z','t','n','w',      \
                            'j','p','f', 'm','a','q'};
        int N,i,j;
        //bug:�������������޷��������У����º����fgets��һ��ֻȡ��һ�����з�scanf("%d",&N);        //cin >> N; 

        const int MAXN = 110;
        char str[MAXN],ch;
        j=1;

        if(fgets(str,MAXN,stdin) == NULL){
            exit(0);
        }
        sscanf(str,"%d",&N);
        while((N--)>0){
            if(fgets(str,MAXN,stdin) == NULL){
                break;
            }
            i=0;
            printf("Case #%d: ",j);
            while(str[i]!='\0'){
                ch = str[i];
                if(isalpha(ch)){
                    ch = tolower(ch);
                    ch = mapping[ch-'a'];
                }
                printf("%c",ch);
                i++;
            }
            j++;
        }
    }
}

int main()
{
    NS_SpeakingInTongues::main();
}
