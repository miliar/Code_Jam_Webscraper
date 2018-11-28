#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<malloc.h>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<list>
#include<string>
#include<map>
#define min(a,b) (a>b?b:a)
#define max(a,b) (a>b?a:b)
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define F first
#define S second
#define SS ({int x;scanf("%d",&x);x;})
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
char col[500];
int mov[500];
vector<int> O,B;
int main()
{
    freopen("Alarge.in","r",stdin);
    freopen("output.out","w",stdout);
    int t=SS;
    for(int tc=1;tc<=t;tc++){
        int n;cin>>n;
        O.clear();B.clear();
        for(int i=0;i<n;i++){
            cin>>col[i]>>mov[i];
            //cout<<col[i]<<" "<<mov[i]<<endl;
            if(col[i]=='O'){
                O.PB(mov[i]);
            }
            else{
                B.PB(mov[i]);
            }
        }
        int a=0,b=0,bot1=1,bot2=1,cnt=0;
        for(int i=0;i<n;){
            int tmp=0,tmp2=0;
            if(col[i]=='O' && bot1==mov[i]){
                //cout<<"1\n";
                a++;
                if(b<B.size() && B[b]-bot2>0){
                    bot2++;
                }
                else if(b<B.size() && B[b]-bot2<0){
                    bot2--;
                }
                cnt++;
                i++;
            }
            else if(col[i]=='B' && bot2==mov[i]){
                //cout<<"2\n";
                b++;
                if(a<O.size() && O[a]-bot1>0){
                    bot1++;
                }
                else if(a<O.size() && O[a]-bot1<0){
                    bot1--;
                }
                cnt++;
                i++;
            }
            else if(col[i]=='O'){
                //cout<<"3\n";
                tmp=O[a]-bot1;
                bot1+=tmp;
                cnt+=abs(tmp);
                if(b<B.size())
                    tmp2=B[b]-bot2;
                tmp=min(abs(tmp),abs(tmp2));
                if(b<B.size() && B[b]>bot2){
                    bot2+=tmp;
                }
                else{
                    bot2-=tmp;
                }
            }
            else{
               // cout<<"4\n";
                tmp=B[b]-bot2;
                bot2+=tmp;
                cnt+=abs(tmp);
                if(a<O.size())
                    tmp2=O[a]-bot1;
                tmp=min(abs(tmp),abs(tmp2));
                if(a<O.size() && O[a]>bot1){
                    bot1+=tmp;
                }
                else{
                    bot1-=tmp;
                }
            }
        }
        cout<<"Case #"<<tc<<": "<<cnt<<endl;
    }
}
