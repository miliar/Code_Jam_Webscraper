//Headers
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
//#include <algorithm>
#include <climits>
#include <clocale>
//Defines
#define pow2(i) (1<<i)
#define bit(i) (1<<i)
#define isOdd(i) (i&1)
#define isEven(i) (!(i&1))
#define isPrime(i) ((i==2) || ((i&1) && !pTest[i])) //pTest has to be the bool array's name
#define sz(i) i.size()
#define vec(type,name) vector< type > name
#define rep(i,a,b) for(int i=a ; i<=b ; i++)
#define swap(type,a,b) {type t=a; a=b; b=t;}
#define sum(a,n) ( (n*(n+1)/2) - (a-1)*a/2 )
#define iscap(i) (i>='A'&&i<='Z')
#define issmall(i) (i>='a'&&i<='z')
#define isnum(i) (i>='0'&&i<='9')
#define issymbol(i) (!(i>='a'&&i<='z') && !(i>='A'&&i<='Z') && !(i>='0'&&i<='9'))
#define mk(i,j) make_pair(i,j)
#define ERROR 1e-11
//Type Defs
typedef long long lint;
typedef unsigned long long ulint;
typedef long double ldouble;

#define min(a,b) (a<b?a:b)
#define max(a,b) (a<b?b:a)

using namespace std;

char buf[100], tbuf[100];
//int cnt[10000];
map< pair<int,int> , bool > ver;

vector< pair<int,int> > lst2, lst3, lst4, lst5, lst6, lst7;



int main()
{
    //     TEST CASE     //
    int kase=1, kounter=1;
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w+",stdout);

    int i, j, k, l, cnum, tmp, len;
    char c;
    int cont, lo, hi;
    map< pair<int,int> , bool >::iterator it;


    //it = ver.find( make_pair(1,2) );





    /*for (i=10 ; i<=99 ; i++)
    {
        for (j=10 ; j<=99 ; j++)
        {
            ver[ make_pair(i,j) ] = false;
        }
    }*/

    len = 2;

    for (l=10 ; l<=99 ; l++)
    {
        cnum = l;
        sprintf(buf,"%d",cnum);

        for (i=len-1 ; i>0 ; i--)
        {
            strcpy(tbuf, &buf[i]);
            c = buf[i];
            buf[i] = '\0';
            strcpy(&tbuf[len-i],buf);
            buf[i] = c;

            tmp = atoi(tbuf);

            it = ver.find( make_pair(cnum,tmp) );
            if (it != ver.end()) continue;

            if (tmp>=10 && tmp<=99 && cnum <= 99 && cnum >=10 && tmp!=cnum)
            {
                //printf("%d %d\n",tmp,cnum);
                //getchar();

                ver[ make_pair(cnum,tmp) ] = ver[ make_pair(tmp,cnum) ] = true;

                lst2.push_back(make_pair(cnum,tmp));

                /*for (j=min(tmp,cnum) ; j<=max(tmp,cnum) ; j++)
                {
                    cnt[j]++;
                }*/
            }
        }
    }

    //printf("%d\n",cnt[40]-cnt[10]);





    /*for (i=100 ; i<=999 ; i++)
    {
        for (j=100 ; j<=999 ; j++)
        {
            ver[ make_pair(i,j) ] = false;
        }
    }*/

    len = 3;

    //bool chkbuf[1000];
    //for (k=0 ; k<=1000 ; k++) chkbuf[k]=false;

    for (l=100 ; l<=999 ; l++)
    {
        cnum = l;
        sprintf(buf,"%d",cnum);

        for (i=len-1 ; i>0 ; i--)
        {
            strcpy(tbuf, &buf[i]);
            c = buf[i];
            buf[i] = '\0';
            strcpy(&tbuf[len-i],buf);
            buf[i] = c;

            tmp = atoi(tbuf);

            it = ver.find( make_pair(cnum,tmp) );
            if (it != ver.end()) continue;

            if (tmp>=100 && tmp<=999 && cnum <= 999 && cnum >=100 && tmp!=cnum)
            {
                //if (chkbuf[tmp]==false) chkbuf[tmp]=true;
                //else { printf("EPIC FAIL\n"); getchar(); }
                //printf("%d %d\n",tmp,cnum);
                //getchar();

                ver[ make_pair(cnum,tmp) ] = ver[ make_pair(tmp,cnum) ] = true;

                lst3.push_back(make_pair(cnum,tmp));

                /*for (j=min(tmp,cnum) ; j<=max(tmp,cnum) ; j++)
                {
                    cnt[j]++;
                }*/
            }
        }
    }

    len = 4;

    for (l=1000 ; l<=9999 ; l++)
    {
        cnum = l;

        //printf("%d\n",cnum);
        sprintf(buf,"%d",cnum);

        for (i=len-1 ; i>0 ; i--)
        {
            strcpy(tbuf, &buf[i]);
            c = buf[i];
            buf[i] = '\0';
            strcpy(&tbuf[len-i],buf);
            buf[i] = c;

            tmp = atoi(tbuf);

            it = ver.find( make_pair(cnum,tmp) );
            if (it != ver.end()) continue;

            //printf("%d %d\n",cnum, tmp);

            if (tmp>=1000 && tmp<=9999 && cnum <= 9999 && cnum >=1000 && tmp!=cnum)
            {
                //if (chkbuf[tmp]==false) chkbuf[tmp]=true;
                //else { printf("EPIC FAIL\n"); getchar(); }
                //printf("%d %d\n",tmp,cnum);
                //getchar();

                ver[ make_pair(cnum,tmp) ] = ver[ make_pair(tmp,cnum) ] = true;

                lst4.push_back(make_pair(cnum,tmp));
                //cout << "Humpa" << endl;


            }
        }
    }

    len = 5;

    for (l=10000 ; l<=99999 ; l++)
    {
        cnum = l;

        //printf("%d\n",cnum);
        sprintf(buf,"%d",cnum);

        for (i=len-1 ; i>0 ; i--)
        {
            strcpy(tbuf, &buf[i]);
            c = buf[i];
            buf[i] = '\0';
            strcpy(&tbuf[len-i],buf);
            buf[i] = c;

            tmp = atoi(tbuf);

            it = ver.find( make_pair(cnum,tmp) );
            if (it != ver.end()) continue;

            //printf("%d %d\n",cnum, tmp);

            if (tmp>=10000 && tmp<=99999 && cnum <= 99999 && cnum >=10000 && tmp!=cnum)
            {
                //if (chkbuf[tmp]==false) chkbuf[tmp]=true;
                //else { printf("EPIC FAIL\n"); getchar(); }
                //printf("%d %d\n",tmp,cnum);
                //getchar();

                ver[ make_pair(cnum,tmp) ] = ver[ make_pair(tmp,cnum) ] = true;

                lst5.push_back(make_pair(cnum,tmp));
                //cout << "Humpa" << endl;


            }
        }
    }

    len = 6;

    for (l=100000 ; l<=999999 ; l++)
    {
        cnum = l;

        //printf("%d\n",cnum);
        sprintf(buf,"%d",cnum);

        for (i=len-1 ; i>0 ; i--)
        {
            strcpy(tbuf, &buf[i]);
            c = buf[i];
            buf[i] = '\0';
            strcpy(&tbuf[len-i],buf);
            buf[i] = c;

            tmp = atoi(tbuf);

            it = ver.find( make_pair(cnum,tmp) );
            if (it != ver.end()) continue;

            //printf("%d %d\n",cnum, tmp);

            if (tmp>=100000 && tmp<=999999 && cnum <= 999999 && cnum >=100000 && tmp!=cnum)
            {
                //if (chkbuf[tmp]==false) chkbuf[tmp]=true;
                //else { printf("EPIC FAIL\n"); getchar(); }
                //printf("%d %d\n",tmp,cnum);
                //getchar();

                ver[ make_pair(cnum,tmp) ] = ver[ make_pair(tmp,cnum) ] = true;

                lst6.push_back(make_pair(cnum,tmp));
                //cout << "Humpa" << endl;


            }
        }
    }

    len = 7;

    for (l=1000000 ; l<=2000000 ; l++)
    {
        cnum = l;

        //printf("%d\n",cnum);
        sprintf(buf,"%d",cnum);

        for (i=len-1 ; i>0 ; i--)
        {
            strcpy(tbuf, &buf[i]);
            c = buf[i];
            buf[i] = '\0';
            strcpy(&tbuf[len-i],buf);
            buf[i] = c;

            tmp = atoi(tbuf);

            it = ver.find( make_pair(cnum,tmp) );
            if (it != ver.end()) continue;

            //printf("%d %d\n",cnum, tmp);

            if (tmp>=1000000 && tmp<=2000000 && cnum <= 2000000 && cnum >=1000000 && tmp!=cnum)
            {
                //if (chkbuf[tmp]==false) chkbuf[tmp]=true;
                //else { printf("EPIC FAIL\n"); getchar(); }
                //printf("%d %d\n",tmp,cnum);
                //getchar();

                ver[ make_pair(cnum,tmp) ] = ver[ make_pair(tmp,cnum) ] = true;

                lst7.push_back(make_pair(cnum,tmp));
                //cout << "Humpa" << endl;


            }
        }
    }

    //printf("READY\n");


    scanf("%d",&kase);
    //printf("%d\n",kase);



    while (kase--)
    {
        //printf("--> %d\n",kase);

        scanf("%d %d",&hi,&lo);
        if (lo>hi) swap(int,hi,lo);

        //printf("%d - %d\n",hi, lo);

        printf("Case #%d: ",kounter++);

        if (hi<10)
        {
            printf("0\n");
            continue;
        } else if (hi<100)
        {
            for (i=0, cont=0 ; i<lst2.size() ; i++)
            {
                if (lst2[i].first>=lo && lst2[i].first<=hi && lst2[i].second>=lo && lst2[i].second<=hi)
                {
                    cont++;
                }
            }
            printf("%d\n",cont);
            continue;
        } else if (hi<1000)
        {
            for (i=0, cont=0 ; i<lst3.size() ; i++)
            {
                if (lst3[i].first>=lo && lst3[i].first<=hi && lst3[i].second>=lo && lst3[i].second<=hi)
                {
                    cont++;
                }
            }
            printf("%d\n",cont);
            continue;
        } else if (hi<10000)
        {
            for (i=0, cont=0 ; i<lst4.size() ; i++)
            {
                if (lst4[i].first>=lo && lst4[i].first<=hi && lst4[i].second>=lo && lst4[i].second<=hi)
                {
                    cont++;
                }
            }
            printf("%d\n",cont);
            continue;
        } else if (hi<100000)
        {
            for (i=0, cont=0 ; i<lst5.size() ; i++)
            {
                if (lst5[i].first>=lo && lst5[i].first<=hi && lst5[i].second>=lo && lst5[i].second<=hi)
                {
                    cont++;
                }
            }
            printf("%d\n",cont);
            continue;
        } else if (hi<1000000)
        {
            for (i=0, cont=0 ; i<lst6.size() ; i++)
            {
                if (lst6[i].first>=lo && lst6[i].first<=hi && lst6[i].second>=lo && lst6[i].second<=hi)
                {
                    cont++;
                }
            }
            printf("%d\n",cont);
            continue;
        } else if (hi<10000000)
        {
            for (i=0, cont=0 ; i<lst7.size() ; i++)
            {
                if (lst7[i].first>=lo && lst7[i].first<=hi && lst7[i].second>=lo && lst7[i].second<=hi)
                {
                    cont++;
                }
            }
            printf("%d\n",cont);
            continue;
        }

    }



    return 0;
}
