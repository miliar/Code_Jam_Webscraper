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
        SetFileInOutName("NS_SpeakingInTongues");
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
            printf("Case #%d: ",j++);
            while(str[i]!='\0'){
                ch = str[i];
                if(isalpha(ch)){
                    ch = tolower(ch);
                    ch = mapping[ch-'a'];
                }
                printf("%c",ch);
                i++;
            }
        }
    }
}


namespace NS_GoogleDancingWithGooglers
{
/*
Input
4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21
    int main()
    {
        SetFileInOutName("NS_GoogleDancingWithGooglers");
        ReopenStdinStdout();
        int T,N,Surp,p,i,j,k,sum,count,SurpChoice=0,remain;
        scanf("%d",&T);
        j=1;
        while((T--)>0){
            scanf("%d %d %d",&N,&Surp,&p);
            //DEBUG("N=%d Surp=%d p=%d\n",N,Surp,p);
            printf("Case #%d: ",j++);
            count = 0;
            SurpChoice = 0;//��ʾ���������ֵ����p������£����Ա�ѡΪSurp����Ҳ���Բ�ѡΪSurp��choice
            for(i=0;i<N;i++){
                scanf("%d",&sum);
                //bug:���sum<4��ʱ�������⣬���sum=0,k=-1��remain=2,����ʵ��������ϣ������k=-2,a=k+1=-1,b=0,c=1������a=0,b=0,c=0
                if(sum>=4){
                    k=(int)(sum-4)/3;
                }else{
                    k=-(6-sum)/3;
                }
                
                remain = (sum+6-4)%3;//bug:(sum-4)%3�����remain��sum<4��ʱ�������⣬����Ϊ2 1 1 8 0,sum=0 k=-1,remain=-1,�����remainƥ�䲻��0��1
                
                //DEBUG("sum=%d k=%d,remain=%d\n",sum,k,remain);
                //bug��������Ҫ��֤���ǵ�Surp��Ŀ�����Ǻ��������Ŀһ�µ�.������Ϊ2 1 1 8 0ʱ����sum=0�ǣ����ǿ���ȡ0,0,0���������Surpû��--������Ǵ���ġ�
                if(p<=k+2){
                    if(remain==0){
                        //���ʱ��������ѡ��:(k,k+2,k+2){Surp��ѡ�񽫶�һ��}��(k+1,k+1,k+2)
                        if(k>=0){
                            count++;
                            SurpChoice++;
                            //Surp--;
                        }else if(k == -1){
                            count++;
                        }else{
                            //������Ҫ��
                        }
                    }else if(remain==1){
                        if(k+1>=0){
                            count++;
                            SurpChoice++;
                        }
                        //bug:������Ϊ2 1 1 8 0,Ȼ��sum=0 k=-1,remain=-1,k+2>=p:count++:2����Ϊ(a,b,c)�л���ֵ<0���������������k+1>=0����Ϊ���cΪk+2����remain==0:a=k+1,remain==1:a=k+1,remain==2,a=k+2
                        //sum=0 k=-2,remain=2
                        //k+2>=p:count++:2 bug:���ʱ������Ҫ���ˣ���������ȡ(0,0,0)
                        //DEBUG("k+2>=p:count++:%d\n",count);
                    }else{//remain==2 && k+2>=0)){z{
                        if(k+1>=0){
                            count++;
                            SurpChoice++;
                        }else if(k==-2){
                            count++;
                        }else{
                            //
                        }
                    }
                }else if(k+3<p || remain==0){//remain==0��ʱ�򲻴��������p=k+3�����
                    //DEBUG("Continue:k+3=%d p=%d remain=%d\n",k+3,p,remain);
                }else{ //p=k+3;
                    //sum=0 k=-1,remain=-1
                    //k+3=p:count++:2 Surp--=0
                    if(Surp>0 && k+1>=0){//��remain��=0��p==k+3ʱ,����a=p+1
                        Surp--;
                        count++;
                        //DEBUG("k+3=p:count++:%d Surp--=%d\n",count,Surp);
                    }
                }
            }
            //���������Surp��û�б�Ϊ<=0�����ʱ��˵��������Ҫ����Щ���ж�ѡ��һЩSurp����SurpChoice�ͼ�¼�˿��Ա�ѡ������Surp�����ǲ���Ӱ�쵽���ǵ�count����ΪѡSurpChoice��ʱ�����ǵ�countҲ��������++���������ﲻ��Ҫ��count--
            //DEBUG("Surp=%d SurpChoice=%d \n",Surp,SurpChoice);
            printf("%d\n",count);
        }
    }
*/

    int main()
    {
        SetFileInOutName("NS_GoogleDancingWithGooglers");
        ReopenStdinStdout();
        int T,N,Surp,p,i,j,k,sum,count,SurpChoice=0,remain;
        scanf("%d",&T);
        j=1;
        while((T--)>0){
            scanf("%d %d %d",&N,&Surp,&p);
            //DEBUG("N=%d Surp=%d p=%d\n",N,Surp,p);
            printf("Case #%d: ",j++);
            count = 0;
            SurpChoice = 0;//��ʾ���������ֵ����p������£����Ա�ѡΪSurp����Ҳ���Բ�ѡΪSurp��choice
            for(i=0;i<N;i++){
                scanf("%d",&sum);
                //bug:���sum<4��ʱ�������⣬���sum=0,k=-1��remain=2,����ʵ��������ϣ������k=-2,a=k+1=-1,b=0,c=1������a=0,b=0,c=0
                if(sum>=4){
                    k=(int)(sum-4)/3;
                }else{
                    k=-(6-sum)/3;
                }
                remain = (sum+6-4)%3;//bug:(sum-4)%3�����remain��sum<4��ʱ�������⣬����Ϊ2 1 1 8 0,sum=0 k=-1,remain=-1,�����remainƥ�䲻��0��1
                //DEBUG("sum=%d k=%d,remain=%d\n",sum,k,remain);
                //bug��������Ҫ��֤���ǵ�Surp��Ŀ�����Ǻ��������Ŀһ�µ�.������Ϊ2 1 1 8 0ʱ����sum=0�ǣ����ǿ���ȡ0,0,0���������Surpû��--������Ǵ���ġ�
                if(p<=k+2){
                    if( ((remain==0 || remain == 1)&&k+1>=0)|| (remain==2 && k+2>=0) ){
                        count++;
                    }
                }else if(k+3==p && remain!=0 && Surp>0 && k+1>=0){//remain==0��ʱ�򲻴��������p=k+3�����
                        Surp--;
                        count++;
                }
            }
            //���������Surp��û�б�Ϊ<=0�����ʱ��˵��������Ҫ����Щ���ж�ѡ��һЩSurp����SurpChoice�ͼ�¼�˿��Ա�ѡ������Surp�����ǲ���Ӱ�쵽���ǵ�count����ΪѡSurpChoice��ʱ�����ǵ�countҲ��������++���������ﲻ��Ҫ��count--
            //DEBUG("Surp=%d SurpChoice=%d \n",Surp,SurpChoice);
            printf("%d\n",count);
        }
    }
}


#include <list>
#include <map>
namespace NS_RecycledNumbers
{
    /*
      4
      1 9
      10 40 :zjl:<12,21>,<13,31>,<23,32>,
      100 500 
      1111 2222
      Case #1: 0
      Case #2: 3
      Case #3: 156
      Case #4: 287
    */
    int main()
    {
        SetFileInOutName("NS_RecycledNumbers");
        ReopenStdinStdout();
        int T,A,B,i,j,k,n,m,newm,q,count=0,nCase,AFirst,BFirst;//B����λ
        scanf("%d",&T);
        nCase=1;
        list<int> L;
        list<int>::iterator iter;
        map<int,int> mapInt;
        while((T--)>0){
            scanf("%d %d",&A,&B);
            printf("Case #%d: ",nCase++);
            count=0;
            k=0;//����λ
            i = A;
            while(i>0){
                i = i/10;
                k++;
            }
            //B����λ
            BFirst = (int)((double)B/(pow(10,k-1)));
            AFirst = (int)((double)A/(pow(10,k-1)));
            //DEBUG("A=%d  B=%d k=%d AFirst=%d BFirst=%d\n",A,B,k,AFirst,BFirst);
            //bug:A �� n < m �� B? ��������n����ȡ��B��
            //IM:1111 2222�ҵĴ���Case #4: 288,bug����:
            //Pair 1111 1212 2121 2222
            //Pair 1111 1212 2121 2222
            //����mû��ȥ��
            for(n=A;n<B;n++){
                i=n;
                L.clear();
                //DEBUG("n=%d\n",n);
                while(i>0){
                    L.push_front(i%10);
                    i = i/10;
                }
                mapInt.clear();
                for(j=0;j<k-1;j++){//�������ƶ�k-1��
                    q = L.front();
                    L.pop_front();
                    L.push_back(q);
                    q = L.front();
                    if(q==0 || q<AFirst || q>BFirst){
                        //DEBUG("q<AFirst || q>BFirst:AFirst=%d BFirst=%d  q=%d\n",AFirst,BFirst,q);
                        continue;
                    }else if(q>AFirst && q<BFirst){
                        if(mapInt[m] == 0){
                            count++;
                            mapInt[m] = 1;
                        }
                        continue;
                    }
                    m = 0;
                    for(iter=L.begin();iter!=L.end();iter++){
                        m = m*10+*iter;
                    }
                    //DEBUG("m=%d\n",m);
                    //A �� n < m �� B. 
                    if(m > n && m<=B && mapInt[m] == 0){
                        //if(mapInt[m] == 0){
                        count++;
                        //DEBUG("count++:%d\n",count);
                        //printf("Pair %d %d %d %d\n",A,n,m,B);
                        mapInt[m] = 1;
                        //}else{
                        //  DEBUG("Already exist in map:%d\n",m);
                        //}
                    }
                }
            }
            printf("%d\n",count);
        }
            
    }
}
int main()
{
    //NS_SpeakingInTongues::main();
    //NS_GoogleDancingWithGooglers::main();
    NS_RecycledNumbers::main();
}
