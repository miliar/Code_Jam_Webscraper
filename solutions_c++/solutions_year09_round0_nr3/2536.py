//Design By Robert Jiang 2009.09.03
//googlecodeJam 2009 資格賽
//Dev-C++
//第三題：C. Welcome to Code Jam
//
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<sstream>
#include<iostream>
#include<utility>
#include<bitset>

using namespace std;

#define int64 long long
#define pi pair<int,int>
#define vi vector<int>
#define vpi vector<pi>
#define fst first
#define snd second
#define pb push_back
#define SIZE(a) (int)(a.size())
#define LENGTH(a) (int)(a.length())
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n);i>=0;i--)
#define FOR(i,n,m) for(int i=(n);i<=(m);i++)
#define FORD(i,n,m) for(int i=(n);i>=(m);i--)
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define ABS(a) ( (a)<0 ? -(a) : (a))
#define STRUMIEN(A,B) istringstream A(B)
#define SORT(A) sort(A.begin(),A.end())


////////////////////////////////////////////////////////////////////////////////

#include <iomanip>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <deque>


using namespace std;

const int MAXLineChar=500;
char stBuf[MAXLineChar+2];
char *st;

 int64  DP[MAXLineChar+1];
 int64  DP2[MAXLineChar+1];
 int64  DP3[MAXLineChar+1];
// 陣列 DP 動態記錄字串可能的組合數。
// 因為空白有三個。所以分為[3]

int minFun(int a, int b, int c,int d){
    int min1=MIN(a,b);
    int min2=MIN(c,d);
    min1=MIN(min1,min2);
    return min1;
}


int main() {
//"welcome to code jam" 分析的結果如下：
//a b c d e f g h i j k l m n o p q r s t u v w x y z " "
//1 0 2 1 3 0 0 0 0 1 0 1 2 0 3 0 0 0 0 1 0 0 1 0 0 0  3
//去掉頭尾，
//然後只留下 "acdejlmotw "
// 3次者： "eo "
// 2次者： "cm"
// 1次者："adjltw"
    //ifstream fin("in.txt");
    //ofstream fout("out.txt");
    int testCase=-1;
    //cin >> testCase; //配合gets()時，也要gets()並且加上atoi()
    gets(stBuf);
    testCase=atoi(stBuf);
    int i_testCase=testCase;
    while (i_testCase -- )  {
        cout << "Case #" << (testCase-i_testCase) << ": ";
        gets(stBuf);

        //cout << stBuf;

        //前處理：
        //(1)去頭--找第一個w
        //(2)去尾--留最後一個m
        //去尾：
        char *pp=stBuf;
        char *ppTail=stBuf;
        while (*pp){

            if (*pp=='m') ppTail=pp;
            pp++;
        }
        *(ppTail+1)='\0';
        //cout << "去尾後" << stBuf << endl;
        //去頭：
        pp=stBuf;
        while (*pp){
            if (*pp=='w')
                break;
            pp++;
        }
        //cout << "去頭後" << pp << endl;
        st=pp;

        //// 用DP計算子序列的次數！

        //dp 的陣列先歸0
        //int DP[MAXLineChar+1];
        //int DP2[MAXLineChar+1];
        //int DP3[MAXLineChar+1];
        //memset(DP,0,MAXLineChar+1);
        //memset(DP2,0,MAXLineChar+1);
        //memset(DP3,0,MAXLineChar+1);
        int i;
        for (i=0;i<MAXLineChar+1;i++){
            DP[i]=0; DP2[i]=0;DP3[i]=0;
        }
        //"welcome to code jam" 分析的結果如下：
        // 3次者： "eo "
        // 2次者： "cm"
        // 1次者："adjltw"
        char * p=st; i=0;
        while (*p){
            //cout << *p;
             int64  dpsum,dp2sum,dp3sum;
            dpsum=0,dp2sum=0,dp3sum=0;
            switch(*p){
            //--先 1次者：
            case 'a':for (int j=0;j<i;j++) if (st[j]=='j') dpsum += DP[j];break;
            case 'd':for (int j=0;j<i;j++) if (st[j]=='o') dpsum += DP3[j];break;
            case 'j':for (int j=0;j<i;j++) if (st[j]==' ') dpsum += DP3[j];break;
            case 'l':for (int j=0;j<i;j++) if (st[j]=='e') dpsum += DP[j];break;
            case 't':for (int j=0;j<i;j++) if (st[j]==' ') dpsum += DP[j];break;
            case 'w':dpsum=1;break;
            //-- 2 次者：

            case 'c':
                for (int j=0;j<i;j++) if (st[j]=='l') dpsum += DP[j];
                for (int j=0;j<i;j++) if (st[j]==' ') dp2sum += DP2[j];
                break;
            case 'm':
                for (int j=0;j<i;j++) if (st[j]=='o') dpsum += DP[j];
                for (int j=0;j<i;j++) if (st[j]=='a') dp2sum += DP[j];
                break;

            //-- 3 次者：
            case 'e':
                for (int j=0;j<i;j++)if (st[j]=='w') dpsum += DP[j];
                for (int j=0;j<i;j++) if (st[j]=='m') dp2sum += DP[j];
                for (int j=0;j<i;j++) if (st[j]=='d') dp3sum += DP[j];
                break;

            case 'o':
                for (int j=0;j<i;j++) if (st[j]=='c') dpsum += DP[j];
                for (int j=0;j<i;j++) if (st[j]=='t') dp2sum += DP[j];
                for (int j=0;j<i;j++) if (st[j]=='c') dp3sum += DP2[j];
                break;
            case ' ':
                for (int j=0;j<i;j++) if (st[j]=='e') dpsum += DP2[j];
                for (int j=0;j<i;j++) if (st[j]=='o') dp2sum += DP2[j];
                for (int j=0;j<i;j++) if (st[j]=='e') dp3sum += DP3[j];
                break;
            default:
                dpsum=0;dp2sum=0;dp3sum=0;
                 break;
            }

            DP[i]=dpsum  % 10000;
            DP2[i]=dp2sum % 10000;
            DP3[i]=dp3sum % 10000 ;

            i++; p++;

            /*
            cout << "------------------" << endl;
            for (int j=0;j<i;j++){
                cout << DP[j];
            }
            cout<< endl;
            for (int j=0;j<i;j++){
                cout << DP2[j];
            }
            cout<< endl;
            for (int j=0;j<i;j++){
                cout << DP3[j];
            }
            */
        }
        //為了避免太多的m 所以要把所有的m中DP2[]都相加！
         int64  BigM =0;//=DP2[i-1];
        p=st; i=0;
        while (*p){
            if (*p=='m' && DP2[i]>0) {
                BigM=(BigM+DP2[i] )% 10000;
            }
            p++;i++;
        }
        //cout << "子序列的數量是"  <<setw(4) <<setfill('0') << DP2[i-1] %10000 << endl; //% 10000 << endl;
        //cout << setw(4) <<setfill('0') << DP2[i-1]  << endl; //% 10000 << endl;
        cout << setw(4) <<setfill('0') << BigM %10000  << endl; //% 10000 << endl;
     }
    // Algorithm:
    //system("PAUSE");
    return 0;
}

