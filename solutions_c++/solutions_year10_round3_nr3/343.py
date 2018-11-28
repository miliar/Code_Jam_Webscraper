#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define SIZE(X) ((int)(X.size()))
typedef long long int64;
#define two(X) (1<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
const double pi=acos(-1.0); 
const double eps=1e-11; 
template<class T> inline void getmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void getmax(T &a,T b){if(b>a) a=b;}
using namespace std;
int m,n,x,y,z ,testcase; 
int mp[500][500];
int dp[500][500];
bool use[500][500];
map<char,string> mp2;
map<int ,int > res;int row,col;
int findbest( ){ 
        int largest=-1;
        
                for(int i=0;i<m;i++) 
                        for(int j=0;j<n;j++)
                        {
                        if(use[i][j])continue;
                        if(i==0||j==0){
                                getmax(largest,1);continue;
                        }
                        if(use[i-1][j-1]){
                                dp[i][j]=1;continue;
                        }
                        dp[i][j]=dp[i-1][j-1]+1;
                        if(mp[i][j]!=mp[i-1][j-1])
                                dp[i][j]=1;
                        else{
                                int len=dp[i][j];bool bad;int ss=len;
                                for( ;ss>1;ss--){
                                  bad=false;
                                for(int k=j-1;k>=j-ss+1;k--){
                                        if(mp[i][k]==mp[i][k+1]||use[i][k]){
                                                bad=true;break;
                                        }
                                } 
                                        for(int k=i-1;k>=i-ss+1;k--)
                                                if(mp[k][j]==mp[k+1][j]||use[k][j])
                                                {
                                                        bad=true;break;
                                                } 
                                                if(!bad){
                                                        dp[i][j]=ss;break;
                                                } 
                                }
                                if(ss==1)
                                        dp[i][j]=1;
                        }
                        if(dp[i][j]>largest){
                                largest=dp[i][j];row=i;col=j;
                        }else if(dp[i][j]==largest){
                                if(i<row||(i==row&&j<col)){
                                        row=i;col=j;
                                }
                        }
                }
        return largest;
}
struct node{
        int val;
        int num;
        node(int vv,int nn):val(vv),num(nn){}
       bool operator < (const node& n){
                return val>n.val;
        }

};
void solve(){
        res.clear(); 
        memset(use,false,sizeof(use));
	memset(dp,0,sizeof(dp));
        REP(i,n)dp[0][i]=1;
        REP(i,m)dp[i][0]=1;  
        int large;
        while((large=findbest())!=-1){
                if(large==1){
                        int cnt=0;
                        REP(i,m)REP(j,n)
                                if(!use[i][j])cnt++;
                        res[1]=cnt;
                        return;
                }else{
                        for(int i=row;i>=row-large+1;i--)
                                for(int j=col;j>=col-large+1;j--){
                                        use[i][j]=true;
                                }
                        //cout<<large<<" "<<row<<" "<<col<<endl;
                        if(res.find(large)==res.end())
                                res[large]=1;
                        else
                                res[large]++;
                }
        }
} 
char A[400];
vector<node> ret;
int main(){
	#ifdef _LOCAL_Q_
	freopen("d:\\input.txt","r",stdin);
         freopen("d:\\output.txt","w",stdout);
	#endif  
        mp2['0']="0000";mp2['1']="0001";mp2['2']="0010";mp2['3']="0011";mp2['4']="0100";mp2['5']="0101";
        mp2['6']="0110";mp2['7']="0111";mp2['8']="1000";mp2['9']="1001";mp2['A']="1010";mp2['B']="1011";
        mp2['C']="1100";mp2['D']="1101";mp2['E']="1110";mp2['F']="1111";
        cin>>testcase;
        for(int i=1;i<=testcase;i++){
                cin>>m>>n;string tmp,str;
                REP(k,m){
                        cin>>str;
                        for(int i=0;i<n/4;i++){
                                tmp=mp2[str[i]];
                                for(int s=0;s<4;s++)
                                        mp[k][i*4+s]=tmp[s]-'0';
                        }
                }
                solve(); 

                 cout<<"Case #"<<i<<": "<<res.size()<<endl;
                 ret.clear();
                 for(map<int,int>::iterator itor=res.begin();itor!=res.end();itor++){
                         ret.push_back(node(itor->first,itor->second)); 
                 }
                 sort(ret.begin(),ret.end());
                 for(int i=0;i<ret.size();i++){
                        cout<<ret[i].val<<" "<<ret[i].num<<endl;
                 }
        }
	
	return 0;
}