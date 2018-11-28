#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

#define SZ(c) c.size()
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define SORT(a) sort(a.begin(),a.end())
#define tests int test; scanf("%d",&test); while(test--)
#define dbg(n) cout<<#n<<" = "<<n<<endl;

using namespace std;

int strToInt(string str)
{
    int ans;
    stringstream s;
    s<<str;
    s>>ans;
    return ans;
}
string intToStr(int n)
{
    string str;
    stringstream s;
    s<<n;
    s>>str;
    return str;
}
int MAX(int a,int b)
{
    if(a >b) return a;
    return b;
}
int MIN(int a,int b)
{
    if(a <b) return a;
    return b;
}
int ABS(int a,int b)
{
    if(a >0) return a;
    return -a;
}


int main()
{
    freopen("read.txt","r",stdin);
    freopen("write.txt","w",stdout);
    int test;
    scanf("%d",&test);
    for(int k=1;k<=test;k++)
    {
        int a =0,b=0,cnt=0;
        // row
        cnt =0;
        vector<string> arr;
        string temp;

        //printf("\n");
        for(int i=0; i<4; i++)
        {
            cin>>temp;
            arr.push_back(temp);
           // cout<<temp<<endl;
        }

        bool awin,bwin, complete;
        awin = bwin = complete =false;

        for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(arr[i][j]!='.') cnt++;

        for(int i=0; i<4; i++)
        {
            a=0,b=0;
            for(int j=0; j<4; j++)
            {
                if(arr[i][j] == 'X' || arr[i][j] == 'T')
                    a++;
                 if(arr[i][j] == 'O' || arr[i][j] == 'T')
                    b++;
            }
            if(a == 4)
            {
                awin = true;
                break;
            }
            else if(b == 4)
            {
                bwin = true;
                break;
            }
        }
        if(cnt == 16)
            complete = true;

        // col
        for(int j=0; j<4; j++)
        {
            a= b=0;
            for(int i=0; i<4; i++)
            {
                if(arr[i][j] == 'X' || arr[i][j] =='T')
                    a++;
                 if (arr[i][j] == 'O' || arr[i][j]== 'T')
                    b++;
            }
            if(a == 4)
            {
                awin = true;
                break;
            }
            else if(b == 4)
            {
                bwin = true;
                break;
            }
        }//cout<<"k\n";

        // diagnol
        a=0, b=0;
        for(int i=0; i<4; i++)
        {
            if(arr[i][i] == 'X' || arr[i][i] == 'T')
                a++;
             if(arr[i][i] =='O' || arr[i][i] == 'T')
                b++;
        }
        if(a == 4)
        {
            awin = true;
           // break;
        }
        else if(b == 4)
        {
            bwin = true;
            //break;
        }

        // daignol Second

        a=0,b=0;
        for(int i=0; i<4; i++)
        {
            if(arr[i][3-i] == 'X' || arr[i][3-i] == 'T')
                a++;
             if(arr[i][3-i] == 'O' || arr[i][3-i] == 'T')
                b++;
        }
        if(a == 4)
        {
            awin = true;
            //break;
        }
        else if(b == 4)
        {
            bwin = true;
            //break;
        }
        //cout<<"there"<<endl;
       // cout<<awin<<" "<<bwin<<" "<<complete<<" "<<cnt<<" "<<a<<" "<<b<<endl;
        if(awin)
            printf("Case #%d: X won\n",k);
        else if(bwin)
            printf("Case #%d: O won\n",k);
        else if (complete)
            printf("Case #%d: Draw\n",k);
        else
            printf("Case #%d: Game has not completed\n",k);

    }
    return 0;
}



