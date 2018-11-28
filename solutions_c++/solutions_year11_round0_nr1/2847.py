#include <vector>
#include <list>
#include <map>
#include <set>
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
#define mod(x) (((x)>0)?(x):(-1*(x)))
using namespace std;
struct robot{
    char color;int button;
};

int main()
{
    //freopen("Prob_A_Small.in","r",stdin);
    //freopen("Prob_A_Small.out","w",stdout);
    freopen("Prob_A_Large.in","r",stdin);
    freopen("Prob_A_Large.out","w",stdout);
    int times,count=0,terms;
    cin>>times;getchar();
    while(times--)
    {
        int button;char color;
        vector<robot> seq;robot tmp;
        cin>>terms;getchar();
        for(int i=0;i<terms;i++)
        {
            cin>>tmp.color>>tmp.button;
            seq.push_back(tmp);
        }
        int arr[100]={0},ans[100]={0},sum=0;
        int prev_blue=1,prev_orng=1;
        for(int i=0;i<terms;i++)
        {
            if(seq[i].color=='B'){arr[i]=mod(seq[i].button-prev_blue)+1;prev_blue=seq[i].button;}
            if(seq[i].color=='O'){arr[i]=mod(seq[i].button-prev_orng)+1;prev_orng=seq[i].button;}
        }
        for(int i=0;i<terms;i++)
        {
            int tmp,j;
            if(seq[i].color=='B')
            {
                j=i-1;tmp=0;
                while(j>=0 && seq[j].color!='B') {tmp+=ans[j];j--;}
                if(tmp>=arr[i]) ans[i]=1;
                else ans[i]=arr[i]-tmp;
            }
            if(seq[i].color=='O')
            {
                j=i-1;tmp=0;
                while(j>=0 && seq[j].color!='O') {tmp+=ans[j];j--;}
                if(tmp>=arr[i]) ans[i]=1;
                else ans[i]=arr[i]-tmp;
            }
        }
        for(int i=0;i<terms;i++) sum+=ans[i];
        cout<<"Case #"<<++count<<": "<<sum<<endl;
        seq.clear();
    }
    return 0;
}
