//Data Structure includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
//Other Includes
#include<iostream>
#include<algorithm>
#include<iomanip>
#include<utility>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
//some common functionn
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
#define FOR(i,a,b)              for(int i=a;i<b;i++)
#define FORs(i,a,b)             for(int i=a;i>=b;i--)
#define fill(a,v)               memset(a,v,sizeof a)
#define abS(x)                  ((x)<0?-(x):(x))
#define mP                      make_pair
#define pB                      push_back
#define error(x)                cout << #x << " : " << (x) << endl
#define ALL(a)                  (a).begin(),(a).end()
#define SZ(a)                   ((int) a.size())
#define SORT(a)                  sort(ALL(a))

using namespace std;

typedef long long LL;



void chekarre(int * arr,int n)
{
    cout<<"[";
    for(int i=0;i<n;i++)
        cout<<arr[i]<<" ";
    cout<<"]"<<endl;
}

bool comp(int i,int j) { return (i>j); }


int main()
{
    freopen("input1.txt","r",stdin);
    freopen("output1.txt","w",stdout);

    int t,flag=0,x=0,i,j,flagd=0,flagh=0,flagv=0,flagdg=0;
    string s[5];
    char ch;
    cin >> t;
    while(x!=t){
        flag=0,flagd=0,flagh=0,flagv=0,flagdg=0;
        //fflush(stdin);
        for(i=0;i<4;i++){
            cin>>s[i];
        }


    for(i=0;i<4;i++){
        ch=s[i][0];
        if(ch=='.')flagd=1;
        if(ch!='.'){
        for(j=1;j<4;j++){
            if(s[i][j]=='.')flagd=1;
            if(s[i][j]==ch || s[i][j]=='T')
                flag=1;
            else{
                flag=0;
                break;
            }
        }
        if(flag==1){
            cout<<"Case #"<<x+1<<": "<<ch<<" won"<<endl;
            //return 0;
            flagh=1;
            break;
        }
    }
   }
    //if(flagh==1){continue;}
    if(flagh!=1){
    for(i=0;i<4;i++){
        ch=s[0][i];
        if(ch!='.'){
        for(j=1;j<4;j++){
            //if(s[j][i]=='.')flagd=1;
            if(s[j][i]==ch || s[j][i]=='T')
                flag=1;
            else{
                flag=0;
                break;
            }
        }
        if(flag==1){
            cout<<"Case #"<<x+1<<": "<<ch<<" won"<<endl;
            //return 0;
            flagv=1;
            break;
        }
    }
    }

   }
    if(flagh!=1 && flagv!=1){
    ch = s[0][0];
    if(ch!='.'){
    for(i=1;i<4;i++){
        if(s[i][i]==ch || s[i][i]=='T')
        flag=1;
        else{
            flag=0;
            break;
        }
    }
    if(flag==1){flagdg=1,cout<<"Case #"<<x+1<<": "<<ch<<" won"<<endl;}
    }
     ch = s[0][3];
     if(ch!='.'){
    for(i=1;i<4;i++){
        if(s[i][3-i]==ch || s[i][3-i]=='T')
        flag=1;
        else{
            flag=0;
            break;
        }
    }
    if(flag==1){flagdg=1,cout<<"Case #"<<x+1<<": "<<ch<<" won"<<endl;}
     }
   }

   if(flagh!=1 && flagv!=1 && flagdg!=1){
        if(flagd==1){
            cout<<"Case #"<<x+1<<": "<<"Game has not completed"<<endl;
        }
        else
         cout<<"Case #"<<x+1<<": "<<"Draw"<<endl;
   }
    x++;
    getchar();
  }
    return 0;
}

