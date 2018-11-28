#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <list>
#include <stack>
#include <cmath>
#include <map>
#include <set>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define DEBUG
#define REP(i,a) for(i=0;i<a;i++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define VE vector<int>
#define SZ size()
#define PB push_back
#define all(i) (i).begin(), (i).end()
#define PI acos(-1.0)
#define ii pair<int,int>
#define inf_ll (((1LL<<62)-1)<<1)+1
#define inf_i 1<<31-1

vector<string> m;
int cnt;
bool check(int i,char aux)
{
    int j,cnt1=0,cnt2=0,cnt3=0,cnt4=0;
    REP(j,4)
    {
        if(m[i][j]==aux)
            cnt1++;
        else if(m[i][j]=='T')
            cnt2++;
        if(m[j][i]==aux)
            cnt3++;
        else if(m[j][i]=='T')
            cnt4++;
        if(m[i][j]=='.' || m[j][i]=='.')
            cnt++;
    }
    if(cnt1==4 || cnt3==4)
        return true;
    else if((cnt1==3 && cnt2==1) || (cnt3==3 && cnt4==1))
        return true;
    else
        return false;
}

bool checkDiagonale(char aux)
{
    int i,cnt1=0,cnt2=0,cnt3=0,cnt4=0;
    REP(i,4)
    {
        if(m[i][i]==aux)
            cnt1++;
        else if(m[i][i]=='T')
            cnt2++;
        if(m[3-i][i]==aux)
            cnt3++;
        else if(m[3-i][i]=='T')
            cnt4++;
    }
    if(cnt1==4 || cnt3==4)
        return true;
    else if((cnt1==3 && cnt2==1) || (cnt3==3 && cnt4==1))
        return true;
    else
        return false;
}

int main()
{
/*
   freopen("A-large.in","r",stdin);
   freopen("output.txt","w",stdout);
*/
    int n,i,t,j;
    string cad1;
    scanf("%d\n",&n);
    REP(t,n)
    {
        REP(i,4)
        {
            getline(cin,cad1);
            m.PB(cad1);
        }
        bool flag=false;
        printf("Case #%d: ",t+1);
        cnt=0;
        REP(i,4)
        {
            if(check(i,'O'))
            {
                printf("O won\n"),flag=true;
                break;
            }
            else if(check(i,'X'))
            {
                printf("X won\n"),flag=true;
                break;
            }
        }
        if(flag==false)
        {
            if(checkDiagonale('O'))
                printf("O won\n"),flag=true;
            else if(checkDiagonale('X'))
                printf("X won\n"),flag=true;
        }

        if(flag==false)
        {
            if(cnt>0)
                printf("Game has not completed\n");
            else
                printf("Draw\n");
        }
        m.clear();
        cin.ignore();
    }
/*
	fclose(stdin);
	fclose(stdout);
*/
   return 0;
}
