#include <iostream>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

int hash[15][26];

void parse(string& patt){
  int ind=0;
  for(int i=0;i<patt.size();i++){
    if( patt.at(i)=='(' ){
      for(i++;patt.at(i)!=')';i++){
        hash[ind][patt.at(i)-'a']=1;
      }
    }else{
      hash[ind][patt.at(i)-'a']=1;
    }
    ind++;
  }
  return;
}
int main(void){
  int L,D,N;
  for(;cin>>L>>D>>N;){
    vector<string> v;
    for(int i=0;i<D;i++){ string s; cin>>s; v.push_back(s); }
    for(int X=1;X<=N;X++){
      int ans=0;
      printf("Case #%d: ",X);
      memset(hash,0,sizeof(hash));
      string pattern;
      cin>>pattern;
      parse(pattern);
      for(int j=0;j<D;j++){
        int m;
        for(m=0;m<L && hash[m][v[j][m]-'a'];m++);
        if(m==L){
          ans++;
        }
      }
      printf("%d\n",ans);
    }
  }
  return 0;
}
/*
#include <iostream>
#include <string>
using namespace std;
class CubeWalking{
public:
  string finalPosition(string movement){
    const int dx[]={ 0, 1, 0,-1};
    const int dy[]={-1, 0, 1, 0};
    int my_direction=0;
    int x,y;
    x=y=1;
    for(int i=0;i<movement.size();i++){
      switch(movement.at(i)){
      case 'L':
        my_direction=(my_direction-1)&3;
        break;
      case 'R':
        my_direction=(my_direction+1)&3;
        break;
      case 'W':
        x+=dx[my_direction]; y+=dy[my_direction];
        x = x<0?2:x>2?0:x;
        y = y<0?2:y>2?0:y;
        break;
      }
    }
    if(x==1&&y==1) return "GREEN";
    else if( (x+y)%2==0 ) return "RED";
    else return "BLUE";
  }
};
int main(void){
  string s;
  CubeWalking C;
  cout<< C.finalPosition("LLRR") <<endl;
  cout<< C.finalPosition("WWWWWWWWWWWW") <<endl;
  cout<< C.finalPosition("WLWRW") <<endl;
  cout<< C.finalPosition("WWLLWRWLWLLRWW") <<endl;
  
  return 0;
}
*/
/*
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int ans=0;
const int dx[]={ 1, 2, 2, 1,-1,-2,-2,-1};
const int dy[]={-2,-1, 1, 2, 2, 1,-1,-2};
vector<string> f;
class KnightsTour{
public:
  void search(int x,int y,int cnt){
    int m=999;
    vector<int> nx,ny;
    if(ans<cnt)ans=cnt;
    for(int k=0;k<8;k++){
      if(x+dx[k]<0 || x+dx[k]>=8 || y+dy[k]<0 || y+dy[k]>=8
         || f[y+dy[k]][x+dx[k]]!='.')continue;
      int tx=x+dx[k];
      int ty=y+dy[k];
      int c=0;
      for(int p=0;p<8;p++){
        if(tx+dx[p]<0 || tx+dx[p]>=8 || ty+dy[p]<0 || ty+dy[p]>=8
         || f[ty+dy[p]][tx+dx[p]]!='.' || tx+dx[p]==x&&ty+dy[p]==y)continue;
        c++;
      }
      if(m>=c){
        if(m==c){
          if(ny[0]>ty){
            nx.clear(); ny.clear();
            nx.push_back(tx); ny.push_back(ty);
          }
          else if(ny[0]==ty){
            if(nx[0]>tx){
              nx.clear(); ny.clear();
              nx.push_back(tx); ny.push_back(ty);
            }
          }
        }else{
          nx.clear(); ny.clear();
          nx.push_back(tx); ny.push_back(ty);
        }
        m=c;
      }
    }
    
    f[y][x]=cnt%10+'0';
    if(nx.size())search(nx[0],ny[0],cnt+1);
    return;
  }
  int visitedPositions(vector<string> v){
    f.clear();
    f=v;
    ans=0;
    int x,y;
    for(int i=0;i<v.size();i++){
      if(~v[i].find("K")){
        x=v[i].find("K"); y=i; break;
      }
    }
    search(x,y,1);
    return ans;
  }
};
int main(void){
  char*str[]={"..*...*."
,"**.....*"
,"*..*...."
,"*..*...."
,".....*.."
,"....*..K"
,"**.*...*"
,"..**...."};

  vector<string> v;
  KnightsTour K;
  for(int i=0;i<sizeof(str)/sizeof(str[0]);i++)v.push_back(str[i]);
  cout << K.visitedPositions(v) <<endl;
  return 0;
}
*/

/*
//real    0m30.031s
//user    0m29.187s
//sys     0m0.046s
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
class PermutationSum{
public:
  int add(int n){
    string s;
    int ans=0;
    for(;n>0;n/=10)s+=(n%10)+'0';
    sort(s.begin(),s.end());
    do{
      ans+=atoi(s.c_str());
    }while(next_permutation(s.begin(),s.end()));
    
    return ans;
  }
};
int main(void){
  PermutationSum ps;
  int n;
  for(;cin>>n;){
    cout<<ps.add(n)<<endl;
  }
  return 0;
}
*/
/*
  //0.321
#include <iostream>
#include <cstring>
using namespace std;
class PermutationSum{
public:
  int combination(int n,int r){
    return n==r?1:r==1?n:combination(n-1,r-1)+combination(n-1,r);
  }
  int add(int n){
    int tmp=n;
    int number[10];
    int size,count;
    int ans=0,a;
    
    a=size=count=0;
    memset(number,0,sizeof(number));
    for(;tmp>0;tmp/=10){
      number[tmp%10]++;
      if(number[tmp%10]==1)count++;
      size++;
      a*=10; a++;
    }
    for(int i=0;i<10;i++){
      if(number[i]==0 || i==0)continue;
      int minus = number[i]>1 ? 0:1;
      number[i]--;
      int k=0;
      int d=1;
      int s=size-1;
      for(int j=0;j<count-minus-1;j++){
        for(;k<10;k++){
          if(number[k]==0)continue;
          break;
        }
        d*=combination(s,number[k]);
        s-=number[k];
        k++;
      }
      ans+=d*i;
      number[i]++;
    }
    return a * ans ;
  }
};

int main(void){
  int n;
  PermutationSum ps;
  for(;cin>>n;){
    cout<< ps.add(n) <<endl;
  }
  return 0;
}
*/
/*
#include <iostream>
#include <cmath>
bool isPandig (unsigned&);
int main(){
  unsigned fn(1), fnSub1(1), fnSub2(1);
  unsigned fibIndex(2);
  const double SQRT5 = sqrt(5), PHI = (1+SQRT5)/2;
  
  while (true) {
    if (isPandig(fn)) {
      double tmp = fibIndex*log10(PHI) - log10(SQRT5);
      unsigned first9Digs = static_cast<unsigned>(pow(10,tmp-floor(tmp)+8));
      if (isPandig(first9Digs))
        break;
    }
    fn = (fnSub1 + fnSub2)%1000000000;
    fnSub2 = fnSub1;
    fnSub1 = fn;
    fibIndex++;
  }
  std::cout << fibIndex;
  return 0;
}

bool isPandig (unsigned& n){
  unsigned digitCheck = 0;
  
  while (n) {
    digitCheck |= (1UL << n%10);
    n /= 10;
  }
  return digitCheck == 0x3FE;
}
*/
/*
//Euler 124
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

#define MAX 11
typedef struct rd{
  int number,count;
}RAD;

RAD rad[MAX];

bool cmp(RAD a,RAD b){
  if(a.count<b.count)return true;
  else if(a.count>b.count)return false;
  else if(a.number<b.number)return true;
  else return false;
}

void pri(void){
  int n,x;
  for(n=1;n<MAX;n++){
    rad[n].number=n;
    rad[n].count=1;
    int m=n;
    for(x=2;x*x<=m;x++){
      if(m%x==0){
        rad[n].count*=x;
        for(;m%x==0;m/=x);
      }
    }
    if(m>1)rad[n].count*=m;
  }
}

int main(void){

  pri();
  sort(rad+1,rad+MAX,cmp);
  cout<<rad[6].number<<endl;
  return 0;
}
*/

/*
//Euler 125
#include <iostream>
#include <cmath>
#include <set>
#define MAX 1e8
using namespace std;
int main(void){
  long long sum,ans;
  set<long> st;
  ans=0;

  for(long n=1;n*n<MAX;n++){
    sum=n*n;
    for(long m=n+1;m*m<MAX;m++){
      sum+=m*m;
      if(sum>MAX)break;
      string str;
      for(long tmp=sum;tmp!=0;tmp/=10){
        str+=(tmp%10)+'0';
      }
      string rstr(str.rbegin(),str.rend());
      if(rstr==str){
        //cout<<sum<<endl;
        st.insert(sum);
      }
    }
  }
  set<long>::iterator it;
  for(it=st.begin();it!=st.end();it++)ans+=*it;
  cout<<ans<<endl;
  
  return 0;
}
*/
/*
#include <iostream>
#include <algorithm>
using namespace std;
int n,k,box[30][10],indbox[30],dp[30],st[30],max_index;

bool cmp(const int &a,const int &b){
  int i;
  for(i=0;i<k;i++){
    if(box[a][i]<box[b][i])return 1;
    else if(box[a][i]>box[b][i])return 0;
  }
  return box[a][0]<box[b][0];
}

bool box_cmp(const int &a,const int &b){
  int i;
  for(i=0;i<k&&box[a][i]<box[b][i];i++);
  return i==k?1:0;
}

void print_LIS_ans(const int &a){
  if(st[a]==-1)cout<<indbox[a]+1;
  else{
    print_LIS_ans(st[a]);
    cout<<" "<<indbox[a]+1;
  }
}
int main(){

  for(;cin>>n>>k;){
    for(int i=0;i<n;i++){
      indbox[i]=i;
      dp[i]=1;
      st[i]=-1;
      for(int j=0;j<k;j++)cin>>box[i][j];
      sort(box[i],box[i]+k);
    }
    sort(indbox,indbox+n,cmp);
    for(int i=1;i<n;i++){
      for(int j=0;j<i;j++){
        if(box_cmp(indbox[j],indbox[i])&&dp[i]<dp[j]+1){
          dp[i]=dp[j]+1;
          st[i]=j;
        }
      }
    }
    max_index=0;
    for(int i=1;i<n;i++){
      if(dp[max_index]<=dp[i])max_index=i;
    }
    cout<<dp[max_index]<<endl;
    print_LIS_ans(max_index);
    cout<<endl;
  }
  return 0;
}
/*
#include <cstdio>
#include <algorithm>
using namespace std;
int n,d;
int b[30][10],myindex[30],dp[30],record[30];
inline bool compare(const int &i1,const int &i2){
  for(register int i=0;i<d;++i){
    if(b[i1][i]<b[i2][i])
      return 1;
    else if(b[i1][i]>b[i2][i])
      return 0;
  }
  return i1<i2;
}
inline bool box_compare(const int &i1,const int &i2){
  for(register int i=0;i<d;++i)
    if(b[i1][i]>=b[i2][i])
      return 0;

  return 1;
}
void print_LIS_ans(int &flag){
  if(record[flag]==-1)
    printf("%d",myindex[flag]+1);
  else{
    print_LIS_ans(record[flag]);
    printf(" %d",myindex[flag]+1);
  }
}
int main(){
  int i,j,maxflag;
  while(scanf("%d%d",&n,&d)==2){
    for(i=0;i<n;++i){
      myindex[i]=i;
      dp[i]=1;
      record[i]=-1;
      for(j=0;j<d;++j)
        scanf("%d",&b[i][j]);
      sort(b[i],b[i]+d);
    }
    sort(myindex,myindex+n,compare);
    // LIS
    for(i=1;i<n;++i){
      for(j=0;j<i;++j)
        if(box_compare(myindex[j],myindex[i]) && dp[i]<dp[j]+1){
          dp[i]=dp[j]+1;
          record[i]=j;
        }
    }
    for(i=1,maxflag=0;i<n;++i){
      if(dp[i]>dp[maxflag])
        maxflag=i;
    }
    printf("%d\n",dp[maxflag]);
    print_LIS_ans(maxflag);
    puts("");
  }
  return 0;
}
/*
#include <iostream>
#include <cmath>
using namespace std;
void prime(long x,int m){
  long a,n=x*m;
  int i=0;
  if(m==-1)cout<<"-1 x ";
  for(a=2;a<=sqrt((double)n);a++){
    for(;n%a==0;n/=a){
      if(i==0){cout<<a; i++;}
      else cout<<" x "<<a;
    }
  }
  if(x*m==n){cout<<n;}
  else if(n>1)cout<<" x "<<n;
  cout<<endl;
}
int main(){
  long n;
  for(;cin>>n,n;){
    cout<<n<<" = ";
    prime(n,n<0?-1:1);
  }
  return 0;
}

#include <iostream>
#include <cstring>
using namespace std;
char dig[10001][100000];
void mkdig(void){
  int i,j,x,t,cnt;
  memset(dig,-1,sizeof(dig));
  dig[1][0]=dig[0][0]='1';
  for(i=2;i<=10000;i++){
    t=cnt=0;
    for(j=0;dig[i-1][j]!=-1;j++){
      x=(dig[i-1][j]-'0')*i+t;
      dig[i][j]=(x%10)+'0';
      t=x/10;
      if(!cnt&&dig[i][j]!='0'){cnt=1;}
      if(cnt)cnt++;
      if(cnt>10){t=0; break;}
    }
    for(;t>0;j++,t/=10){
      if(dig[i][j]==-1){dig[i][j]=(t%10)+'0';}
      else{
        x=(dig[i][j]-'0')+t;
        dig[i][j]=(x%10)+'0';
      }
    }
  }
}
int main(){
  int n,i,j,t,x;
  mkdig();
  for(;cin>>n;){
    for(i=0;dig[n][i]=='0';i++);
    cout.width(5);
    cout<<n<<" -> ";
    cout<<dig[n][i]<<endl;
  }
  return 0;
}

#include <iostream>
#include <stack>
#include <string>
using namespace std;
int main(){
  int n;
  cin>>n;
  cin.ignore();
  for(;n--;){
    string str;
    stack<char> st;
    getline(cin,str);
    int i;
    for(i=0;i<str.size();i++){
      if(st.empty()){
        if(str[i]=='('||str[i]=='[')st.push(str[i]);
        else break;
      }
      else if(str[i]=='('||str[i]=='[')st.push(str[i]);
      else{
        if(str[i]==')'){
          if(st.top()=='(')st.pop();
          else break;
        }
        else if(str[i]==']'){
          if(st.top()=='[')st.pop();
          else break;
        }
      }
    }
    cout<<(i==str.size()&&st.empty()?"Yes":"No")<<endl;
  }
  return 0;
}

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main(){
  string str;
  int f1,f2,i;
  for(;cin>>str;){
    f1=f2=0;
    string tmp=str;
    for(i=0;i<str.size();i++){
      if(str[i]=='0')str[i]='O';
    }
    string rstr(str.rbegin(),str.rend());
    if(str==rstr)f1=1;
    for(i=0;i<rstr.size();i++){
      if(rstr[i]=='B'||rstr[i]=='C'||rstr[i]=='D'||rstr[i]=='F'||rstr[i]=='G'
         ||rstr[i]=='K'||rstr[i]=='N'||rstr[i]=='P'||rstr[i]=='Q'||rstr[i]=='R'
         ||rstr[i]=='4'||rstr[i]=='6'||rstr[i]=='7'||rstr[i]=='9')break;
      if(rstr[i]=='E')rstr[i]='3';
      else if(rstr[i]=='J')rstr[i]='L';
      else if(rstr[i]=='L')rstr[i]='J';
      else if(rstr[i]=='S')rstr[i]='2';
      else if(rstr[i]=='Z')rstr[i]='5';
      else if(rstr[i]=='2')rstr[i]='S';
      else if(rstr[i]=='3')rstr[i]='E';
      else if(rstr[i]=='5')rstr[i]='Z';
    }
    if(i==rstr.size()&&str==rstr)f2=1;
    cout<<tmp<<" -- "<<(f1&&f2?"is a mirrored palindrome.":f1?"is a regular palindrome."
                                                            :f2?"is a mirrored string."
                                                            :"is not a palindrome.")<<endl<<endl;
  }
  return 0;
}


#include <iostream>
using namespace std;
long long nw[30001];
const int coin[]={5,10,20,50,100,200,500,1000,2000,5000,10000};

int main(){
  int i,j;
  double m;
  nw[0]=1;
  for(i=0;i<11;i++){
    for(j=coin[i];j<=30000;j+=5){
      nw[j]+=nw[j-coin[i]];
    }
  }

  for(;cin>>m,m;){
    int n=100*m+0.5;
    printf("%6.2f%17lld\n",m,nw[n]);
  }
  return 0;
}

#include <iostream>
using namespace std;
long long bigmod(long long b,long long p,long long m){
  if(p==1)return b;
  else{
    if(p%2==0){
      long long tmp=bigmod(b,p/2,m)%m;
      return (tmp*tmp)%m;
    }
    else{
      return ((b%m)*(bigmod(b,p-1,m)%m))%m;
    }
  }
}
int main(){
  long long b,p,m;
  for(;cin>>b>>p>>m;){
    if(p>0){
      cout<<bigmod(b,p,m)<<endl;
    }
    else{
      cout<<1%m<<endl;
    }
  }
  return 0;
}

#include <iostream>
using namespace std;
int hash[367][10];
void fac(void){
	int i;
  int dig[1000];
  for(int i=0;i<1000;i++)dig[i]=-1;
  dig[0]=1;
  hash[0][1]=1;
  for(i=1;i<=366;i++){
    for(int j=0;dig[j]!=-1;j++)dig[j]*=i;
    for(int j=0;dig[j]!=-1;j++){
      if(dig[j]>=10){
        if(dig[j+1]==-1)dig[j+1]=dig[j]/10;
        else dig[j+1]+=dig[j]/10;
      }
      dig[j]%=10;
    }
    for(int k=0;dig[k]!=-1;k++){
      hash[i][dig[k]]++;
    }
  }
  return ;
}
int main(){
	int n;
  fac();
  for(;cin>>n,n;){
    cout<<n<<"! --"<<endl;
    for(int i=0;i<10;i++){
      if(i==0||i==5)cout<<"   ";
      else cout<<"    ";
      cout<<"("<<i<<")";
      cout.width(5);
      cout<<hash[n][i];
      if(i==4||i==9)cout<<endl;
    }
  }
  return 0;
}	

#include <iostream>
#define MAX 180
using namespace std;
int f1[MAX],f2[MAX],fc[5001][MAX];
void fibnacci(void){
  for(int i=0;i<5001;i++)for(int j=0;j<MAX;j++)fc[i][j]=-1;
  for(int i=0;i<MAX;i++)f1[i]=f2[i]=-1;
  f1[0]=0;
  f2[0]=1; fc[0][0]=0; fc[1][0]=1;
  int j;
  for(int i=2;i<=5000;i++){
    for(j=0;!(f1[j]==-1&&f2[j]==-1);j++){
      fc[i][j]=(f1[j]==-1?0:f1[j])+(f2[j]==-1?0:f2[j]);
    }
    int t=0;
    for(j=0;fc[i][j]!=-1;j++){
      if(fc[i][j]>=1000000){
        t=fc[i][j]/1000000;
        fc[i][j]%=1000000;
        if(fc[i][j+1]==-1)fc[i][j+1]=t;
        else fc[i][j+1]+=t;
      }
    }
    for(int k=0;f2[k]!=-1;k++)f1[k]=f2[k];
    for(int k=0;fc[i][k]!=-1;k++)f2[k]=fc[i][k];
  }
}
int main(){
  int n,j;
  fibnacci();
  for(;cin>>n;){
    int flag=0;
    cout<<"The Fibonacci number for "<<n<<" is ";
    for(j=MAX-1;fc[n][j]==-1;j--);
    for(int i=j;i>=0;i--){
      if(fc[n][i]==-1)continue;
      if(flag==0){cout<<fc[n][i]; flag=1;}
      else if(fc[n][i]>=100000)cout<<fc[n][i];
      else if(fc[n][i]>=10000)cout<<"0"<<fc[n][i];
      else if(fc[n][i]>=1000)cout<<"00"<<fc[n][i];
      else if(fc[n][i]>=100)cout<<"000"<<fc[n][i];
      else if(fc[n][i]>=10)cout<<"0000"<<fc[n][i];
      else if(fc[n][i]>=1)cout<<"00000"<<fc[n][i];
      else cout<<"000000";
    }
    cout<<endl;
  }
  return 0;
}

#include <iostream>
using namespace std;
int main(){
  int cnt;
  long long n,i;
  cnt=1;
  for(i=2;;i++){
    n=i;
    for(;n%2==0;n/=2);
    for(;n%3==0;n/=3);
    for(;n%5==0;n/=5);
    if(n==1){
      cnt++;
      //cout<<i<<" ";
    }
    if(cnt==1500)break;
  }
  cout<<i<<endl;
  return 0;
}

#include <iostream>
using namespace std;
int array[120][120];
int pr[120];
int main(){
  int N;
  long long S,s,t;
  for(;cin>>N;){
    S=-127*N*N;
    for(int i=0;i<N;i++)for(int j=0;j<N;j++)cin>>array[i][j];
    for(int y=0;y<N;y++){
      for(int i=0;i<N;i++)pr[i]=0;
      for(int z=y;z<N;z++){
        t=0;
        s=-127*N*N;
        for(int j=0;j<N;j++){
          pr[j]+=array[z][j];
          t+=pr[j];
          if(t>s)s=t;
          if(t<0)t=0;
        }
        if(S<s)S=s;
      }
    }
    cout<<S<<endl;
  }
  return 0;
}
      
#include <iostream>
#include <cstring>
using namespace std;
int mp[8][8],flag,check[8][8];
int xx[64],yy[64],m,n;
const int dy[]={-1,0,1,0};
const int dx[]={0,1,0,-1};
void solve(int x,int y,int atai,int nowsum,int num){
  int tx,ty;
  if(flag==1)return;
  if(nowsum<=atai){
    if(nowsum==atai){
      if(num+1==m){flag=1; return;}
      else solve(xx[num+1],yy[num+1],-1*mp[yy[num+1]][xx[num+1]],0,num+1);
    }
    else{
      for(int k=0;k<4;k++){
        tx=dx[k]+x;
        ty=dy[k]+y;
        if(tx>=0&&tx<n&&ty>=0&&ty<n&&check[ty][tx]==0&&nowsum+mp[ty][tx]<=atai){
          check[ty][tx]=1;
          solve(tx,ty,atai,nowsum+mp[ty][tx],num);
          check[ty][tx]=0;
        }
      }
    }
  }
  return ;
}
int main(){
  int s1;
  for(;cin>>n,n;){
    m=flag=s1=0;
    memset(check,0,sizeof(check));
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
        cin>>mp[i][j];
        s1+=mp[i][j];
        if(mp[i][j]<0){
          xx[m]=j; yy[m]=i;
          check[i][j]=1;
          m++;
        }
      }
    }
    if(s1==0)solve(xx[0],yy[0],-1*mp[yy[0]][xx[0]],0,0);
    cout<<(s1==0&&flag?"YES":"NO")<<endl;
  }
  return 0;
}

#include <iostream>
#include <string>
using namespace std;
typedef struct t{
  string name;
  int xy[4],ko;
}T;
T Tag[100];
int m,ind;
string parse(string str){
	string tmp;
  int p,k;
  if(ind<str.size()){
    if(str[ind]=='<'&&str[ind+1]!='/'){
      ind++;
      for(Tag[m].name.clear();str[ind]!='>';ind++)Tag[m].name+=str[ind];
      ind++;
      p=m;
      for(int i=0;i<4;i++){
        int e=0;
        for(;str[ind]>='0'&&str[ind]<='9';ind++){
          Tag[m].xy[i]=10*e+(str[ind]-'0');
          e=Tag[m].xy[i];
        }
        if(str[ind]==',')ind++;
      }
      m++;
    }
    else{
      for(ind+=2;str[ind]!='>';ind++)tmp+=str[ind];
      ind++;
      return tmp;
    }
    for(k=0;Tag[p].name!=tmp;k++){
      tmp=parse(str);
    }
    Tag[p].ko=k-1;
  }
  return "";
}
int main(){
  int n,x,y,min;
  string ans;
  for(;cin>>n,n;){
    cin>>ans;
    m=ind=0;
    for(;ind<ans.size();)parse(ans);
    for(int i=0;i<n;i++){
      cin>>x>>y;
      min=1000;
      for(int j=0;j<m;j++){
        if(Tag[j].xy[0]<=x&&Tag[j].xy[2]>=x
           &&Tag[j].xy[1]<=y&&Tag[j].xy[3]>=y){
          if(min>=Tag[j].ko){
            min=Tag[j].ko;
            ans=Tag[j].name;
          }
        }
      }
      if(min==1000)cout<<"OUT OF MAIN PANEL 1"<<endl;
      else cout<<ans<<" "<<min<<endl;
    }
  }
  return 0;
}

#include <iostream>
#include <cstring>
using namespace std;
int main(){
	int N,H,sum;
  int flag[501];
  int a[200],b[200];
  char str[200][3];
  for(;cin>>N>>H,N||H;){
    for(int i=0;i<H;i++){
      cin>>str[i]>>a[i]>>b[i];
    }
    sum=N*N*N-N*H;
    for(int i=0;i<H-1;i++){
     	for(int s=0;s<=N;s++)flag[s]=0;
      for(int j=i+1;j<H;j++){
        if(!strcmp(str[i],str[j])){
          if(a[i]==a[j]&&b[i]==b[j]){
            for(int s=1;s<=N;s++)flag[s]=1;
            break;
          }
        }
        else if(str[i][0]==str[j][0]){ 
          if(a[i]==a[j])flag[b[j]]=1;
        }
        else if(str[i][1]==str[j][0]){
          if(b[i]==a[j])flag[b[j]]=1;
        }
        else if(str[i][0]==str[j][1]){
          if(a[i]==b[j])flag[a[j]]=1;
        }
        else if(str[i][1]==str[j][1]){
          if(b[i]==b[j])flag[a[j]]=1;
        }
      }
      for(int k=1;k<=N;k++)sum+=flag[k];
    }
    cout<<sum<<endl;
  }
  return 0;
}

//no 105
#include <iostream>
using namespace std;
int main(){
  int R,H,L,lmax,rmin,flag;
	int sa_line[10002],ten_line[10002];
  lmax=0;
  rmin=10002;
  for(int i=0;i<10002;i++)sa_line[i]=ten_line[i]=0;
  for(;cin>>R>>H>>L;){
    ten_line[R]=(ten_line[R]<H&&sa_line[R-1]<H?H:ten_line[R]);
    for(int i=R;i<L;i++){
      if(sa_line[i]<H){
        sa_line[i]=H;
        ten_line[i]=(ten_line[i]<H?H:ten_line[i]);
      }
    }
    if(rmin>R)rmin=R;
    if(lmax<L)lmax=L;
  }
  
  int tmp=0,iti=0;
  for(int i=rmin;i<=lmax;i++){
    if(sa_line[i]==ten_line[i]){
      if(tmp!=sa_line[i]){
        if(i!=rmin)cout<<" ";
        cout<<(iti?iti:i)<<" "<<sa_line[i];
        tmp=sa_line[i];
        iti=0;
      }
    }
    else if(ten_line[i]>sa_line[i]){
      if(tmp!=ten_line[i]){
        if(i!=rmin)cout<<" ";
        cout<<i<<" "<<ten_line[i];
        tmp=ten_line[i];
        iti=i;
        ten_line[i]=sa_line[i];
        i--;
      }
    }
  }
  cout<<endl;
  return 0;
}

//no623
#include <iostream>
using namespace std;
int main(){
  int dig[2000];
  int n;
  for(;cin>>n;){
    cout<<n<<"!"<<endl;
    int x,top,t;
    dig[0]=n;
    top=1;
    if(n>0){
      for(;--n;){
        t=0;
        for(int i=0;i<top;i++){
          x=dig[i]*n+t;
          dig[i]=x%10000;
          t=x/10000;
        }
        if(t!=0){dig[top++]=t;}
      }
      int i;
      cout<<top<<endl;
      for(i=top-1;i>=0;i--){
        if(i==top-1)cout<<dig[i];
        else if(dig[i]>=1000)cout<<dig[i];
        else if(dig[i]>=100)cout<<"0"<<dig[i];
        else if(dig[i]>=10)cout<<"00"<<dig[i];
        else if(dig[i]>0)cout<<"000"<<dig[i];
        else cout<<"0000";
      }
    }
    else cout<<"1";
    cout<<endl;
  }
  return 0;
}

//299
#include <iostream>
using namespace std;
int main(){
  int N,L,i,j,tmp,cnt;
  int train[50];
  for(;cin>>N;){
    for(;N--;){
      cnt=0;
      cin>>L;
      for(i=0;i<L;i++)cin>>train[i];
      for(i=0;i<L-1;i++){
        for(j=L-1;j>i;j--){
          if(train[j]<train[j-1]){
            tmp=train[j];
            train[j]=train[j-1];
            train[j-1]=tmp;
            cnt++;
          }
        }
      }
      cout<<"Optimal train swapping takes "<<cnt<<" swaps."<<endl;
    }
  }
  return 0;
}

//no272
#include <iostream>
using namespace std;
int main(){
  int c,x;
  for(x=0;(c=getchar())!=EOF;){
    if(c=='\"'){
      if(x%2==0){
        putchar('`');
        putchar('`');
      }
      else{
        putchar('\'');
        putchar('\'');
      }
      x++;
    }
    else putchar(c);
  }
  return 0;
}

//no112
#include <iostream>
#include <cstring>
using namespace std;
int n,flag;
void search(char*str,int sum){
  int nd;
  if(flag)return;
  else{
    if(*str=='('){
      char *ts;
      str++;
      ts=str;
      if((*str>='0'&&*str<='9')||*str=='-')nd=atoi(str);

      for(;(*str>='0'&&*str<='9')||*str=='-';str++);
      int x=0;
      for(;*ts!='\0';ts++){
        if((*ts>='0'&&*ts<='9')||*ts=='-')continue;
        if(*ts=='(')x++;
        else if(*ts==')')x--;
        if(x==0)break;
      }
      ts++;
      if(*(str+1)==')'&&*(ts+1)==')'){
        if(sum+nd==n){flag=1;}
        return ;
      }
      if(*(str+1)!=')')search(str,sum+nd);
      if(*(ts+1)!=')')search(ts,sum+nd);
    }
  }
}
int main(){
  char str[100000];
  for(;cin>>n;){
    memset(str,0,sizeof(str));
    flag=0;
    int c,x,i;
    for(x=i=0;;){
      c=getchar();
      if(c=='('||c==')'||(c>='0'&&c<='9')||c=='-'){
        str[i++]=c;
        if(c=='(')x++;
        else if(c==')')x--;
        if(x==0)break;
      }
    }
    str[i]='\0';
    search(str,0);
    cout<<(flag?"yes":"no")<<endl;
  }
  return 0;
}
//no102
#include <iostream>
using namespace std;
int main(){
  int flag;
  long long bin[9];
  long long tmp[6],min;

  for(;cin>>bin[0];){
    for(int i=1;i<9;i++)cin>>bin[i];
    tmp[0]=bin[1]+bin[2]+bin[3]+bin[4]+bin[6]+bin[8];
    tmp[1]=bin[1]+bin[2]+bin[3]+bin[5]+bin[6]+bin[7];
    tmp[2]=bin[0]+bin[1]+bin[4]+bin[5]+bin[6]+bin[8];
    tmp[3]=bin[0]+bin[1]+bin[3]+bin[5]+bin[7]+bin[8];
    tmp[4]=bin[0]+bin[2]+bin[4]+bin[5]+bin[6]+bin[7];
    tmp[5]=bin[0]+bin[2]+bin[3]+bin[4]+bin[7]+bin[8];
    min=tmp[0];
    flag=0;
    for(int i=1;i<6;i++){
      if(tmp[i]<min){
        min=tmp[i];
        flag=i;
      }
    }
    cout<<(flag==0?"BCG":flag==1?"BGC":flag==2?"CBG":flag==3?"CGB":flag==4?"GBC":"GCB")<<" "<<min<<endl;
  }
  return 0;
}

#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int main(){
  int col[25][25],n;
  for(;cin>>n;){
    memset(col,-1,sizeof(col));
    for(int i=0;i<n;i++)col[i][0]=i;
    for(;;){
      string str1,str2;
      int a,b,ai,aj,bi,bj;
      cin>>str1;
      if(str1=="quit")break;
      cin>>a>>str2>>b;
      for(int i=0;i<n;i++){
        for(int j=0;col[i][j]!=-1;j++){
          if(col[i][j]==a){ai=i; aj=j;}
          else if(col[i][j]==b){bi=i; bj=j;}
        }
      }
      if(a==b||ai==bi)continue;
      if(str1=="pile"&&str2=="over"){
        for(;col[bi][bj]!=-1;bj++);
        for(int q=bj;col[ai][aj]!=-1;q++){
          col[bi][q]=col[ai][aj];
          col[ai][aj]=-1;
          aj++;
        }
      }
      else{
        if(str1=="move"){
          for(int taj=aj+1;col[ai][taj]!=-1;taj++){
            col[col[ai][taj]][0]=col[ai][taj];
            col[ai][taj]=-1;
          }
        }
        if(str2=="onto"){
          for(int tbj=bj+1;col[bi][tbj]!=-1;tbj++){
            col[col[bi][tbj]][0]=col[bi][tbj];
            col[bi][tbj]=-1;
          }
        }
        if(str1=="pile"&&str2=="onto"){
          for(bj++;col[ai][aj]!=-1;){
            col[bi][bj]=col[ai][aj];
            col[ai][aj]=-1;
            bj++; aj++;
          }
        }
        else if(str1=="move"&&str2=="onto"){
          bj++;
          col[bi][bj]=col[ai][aj];
          col[ai][aj]=-1;
        }
        else if(str1=="move"&&str2=="over"){
          for(;col[bi][bj]!=-1;bj++);
          col[bi][bj]=col[ai][aj];
          col[ai][aj]=-1;
        }
      } 
    }
    for(int i=0;i<n;i++){
      cout<<i<<":";
      for(int j=0;col[i][j]!=-1;j++)cout<<" "<<col[i][j];
      cout<<endl;
    }
    cout<<endl;
  }
  return 0;
}

#include <iostream>
#include <cstdlib>
#include <ctime>
#define MAX 30
using namespace std;
int main(){
  int data[MAX];
  int i,j,tmp;
  srand(time(NULL));
  for(i=0;i<MAX;i++)data[i]=rand()%1000;
  for(i=0;i+1<MAX;i++){
    for(j=MAX-1;j>i;j--){
      if(data[j-1]>data[j]){
        tmp=data[j];
        data[j]=data[j-1];
        data[j-1]=tmp;
      }
    }
  }
  for(i=0;i<MAX;i++)cout<<data[i]<<",";
  cout<<endl;
  cin>>tmp;
  int left,right,flag=0;
  left=0; right=MAX-1;
  for(;left<=right;){
    if(data[(left+right)/2]>tmp){
      right=(left+right)/2-1;
    }
    else if(data[(left+right)/2]<tmp){
      left=(left+right)/2+1;
    }
    else{
      flag=1;
      break;
    }
  }
  cout<<(flag?data[(left+right)/2]:-1)<<endl;
  return 0;
}

#include <iostream>
#include <string>
#include <cctype>
#include <cstdlib>
using namespace std;
int main(){
  string str;
  int atai[100];
  char kigo[100];
  cin>>str;
  int p,q;
  p=q=0;
  for(int i=0;i<str.size();i++){
    if(isdigit(str[i])){
      atai[p++]=atoi(str.c_str()+i);
      for(;isdigit(str[i]);i++);
      i--;
    }
    else if(str[i]=='('){
      kigo[q++]='(';
    }
    else if(str[i]==')'){
      p--;
      for(;;q--){
        if(kigo[q-1]=='-'){atai[p-1]-=atai[p];q--;break;}
        else if(kigo[q-1]=='+'){atai[p-1]+=atai[p];q--;break;}
        else if(kigo[q-1]=='*'){atai[p-1]*=atai[p];q--;break;}
      }
    }
    else{
      if(str[i]=='+'){
        if(q>0&&kigo[q-1]!='('){
          p--;
          if(kigo[q-1]=='-')atai[p-1]-=atai[p];
          else if(kigo[q-1]=='+')atai[p-1]+=atai[p];
          else atai[p-1]*=atai[p];
          kigo[q-1]=str[i];
        }
        else{
          kigo[q++]=str[i];
        }
      }
      else if(str[i]=='-'){
        if(q>0&&kigo[q-1]!='('){
          p--;
          if(kigo[q-1]=='-')atai[p-1]-=atai[p];
          else if(kigo[q-1]=='+')atai[p-1]+=atai[p];
          else atai[p-1]*=atai[p];
          kigo[q-1]=str[i];
        }
        else kigo[q++]=str[i];
      }
      else if(str[i]=='*'){
        if(q>0&&kigo[q-1]!='('){
          if(kigo[q-1]=='+'||kigo[q-1]=='-'){
            kigo[q++]=str[i];
          }
          else{
            p--;
            atai[p-1]*=atai[p];
          }
        }
        else kigo[q++]=str[i];
      }
    }
  }
  for(q--;q>=0;q--){
    if(kigo[q]!='('){
      p--;
      if(kigo[q]=='*')atai[p-1]*=atai[p];
      else if(kigo[q]=='-')atai[p-1]-=atai[p];
      else if(kigo[q]=='+')atai[p-1]+=atai[p];
    }
  }
  cout<<atai[0]<<endl;
  return 0;
}

//no160 factor and factorial
#include <iostream>
#include <cstring>
using namespace std;
int pri[100];
void prime(void){
  int i,j;
  for(i=2;i<100;i++)pri[i]=1;
  pri[0]=pri[1]=0;
  for(i=4;i<100;i+=2)pri[i]=0;
  for(i=3;i*i<100;i+=2){
    for(j=i*2;j<100;j+=i)pri[j]=0;
  }
}
int main(){
  int N,s;
  int hash[100];
  prime();
  for(;cin>>N,N;){
    memset(hash,0,sizeof(hash));
    for(int n=N;n!=1;n--){
      s=n;
      for(int m=2;m*m<=s;m++){
        for(;s%m==0;s/=m)hash[m]++;
      }
      if(s!=1)hash[s]++;
    }
    cout.width(3);
    cout<<N;
    cout<<"! =";
    int cnt=0;
    for(int i=2;i<=N;i++){
      if(pri[i]==0)continue;
      if(cnt%15==0&&cnt!=0){
        cout<<endl<<"      ";
      }
      cout.width(3);
      cout<<hash[i];
      cnt++;
    }
    cout<<endl;
  }
  return 0;
}

//no195 anagram
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <cctype>
using namespace std;
bool cmp(const string& a,const string& b){
  for(int i=0;i<a.size();i++){
    if(a[i]!=b[i]){
      if(islower(a[i])&&islower(b[i])){
        return a[i]<b[i];
      }
      else if(isupper(a[i])&&isupper(b[i])){
        return a[i]<b[i];
      }
      else if(isupper(a[i])&&islower(b[i])){
        char t=tolower(a[i]);
        if(t!=b[i])return t<b[i];
        else return a[i]<b[i];
      }
      else if(islower(a[i])&&isupper(b[i])){
        char t=tolower(b[i]);
        if(a[i]!=t)return a[i]<t;
        else return a[i]<b[i];
      }
    }
  }
}
int main(){
  int n;
  set<string> st;
  vector<string> ans;
  set<string>::iterator it;
  for(;cin>>n;){
    for(;n--;){
      string str;
      st.clear();
      ans.clear();
      cin>>str;
      sort(str.begin(),str.end());
      st.insert(str);
      for(;next_permutation(str.begin(),str.end());){
        st.insert(str);
      }
      it=st.begin();
      for(;it!=st.end();it++)ans.push_back(*it);
      sort(ans.begin(),ans.end(),cmp);
      for(int i=0;i<ans.size();i++)cout<<ans[i]<<endl;
    }
  }
  return 0;
}

//no100 3n+1
#include <iostream>
using namespace std;
int main(){
  int i,j,tmp;
  long long cnt,max;
  for(;cin>>i>>j;){
    max=0;
    cout<<i<<" "<<j<<" ";
    if(i>j){tmp=i; i=j; j=tmp;}
    for(int p=i;p<=j;p++){
      cnt=1;
      for(long long n=p;n!=1;){
        if(n%2)n=3*n+1;
        else n/=2;
        cnt++;
      }
      if(max<cnt)max=cnt;
    }
    cout<<max<<endl;
  }
  return 0;
}
      
//LC-D
#include <iostream>
#include <string>
using namespace std;
int main(){
	int data[5][10]={
		{ 1, 0, 1, 1, 0, 1, 1, 1, 1, 1},
		{11, 1, 1, 1,11,10,10, 1,11,11},
		{ 0, 0, 1, 1, 1, 1, 1, 0, 1, 1},
		{11, 1,10, 1, 1, 1,11, 1,11, 1},
		{ 1, 0, 1, 1, 0, 1, 1, 0, 1, 1}
	};
	int n;
	string str;
	for(;cin>>n>>str,n||(str[0]-'0');){
		for(int i=0;i<2*n+3;i++){
			if(i%(n+1)==0){
				for(int j=0;j<str.size();j++){
					cout<<" "<<string(n,(data[(i/(n+1)?i/(n+1)==1?2:4:0)][str[j]-'0']?'-':' '))<<" ";
          if(j+1<str.size())cout<<" ";
				}
			}
			else{
				for(int j=0;j<str.size();j++){
					cout<<(data[(i<(2*n+3)/2?1:3)][str[j]-'0']==1?" ":"|")<<string(n,' ')<<(data[(i<(2*n+3)/2?1:3)][str[j]-'0']==10?" ":"|");
          if(j+1<str.size())cout<<" ";
				}
			}
			cout<<endl;
		}
    cout<<endl;
	}
	return 0;
}

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
  int T,N,K,p,q;
  cin>>T;
  for(;T--;){
    vector<int> data;
    cin>>N>>K;
    cin>>p;
    for(int i=0;i<N-1;i++){
      cin>>q;
      data.push_back(q-p);
      p=q;
    }
    long long sum=0;
    if(N>K){
      sort(data.begin(),data.end());
      for(int i=0;i<N-K;i++)sum+=data[i];
    }
    cout<<sum<<endl;
  }
  return 0;
}

#include <iostream>
#include <string>
#include <vector>
using namespace std;
const int dy[]={-1,0,1,0};
const int dx[]={0,1,0,-1};
int main(){
  int T,W,H,m;
  int sensha_y,sensha_x;
  for(;cin>>T;){
    for(;T--;){
      vector<string> map;
      string str;
      cin>>H>>W;
      for(int i=0;i<H;i++){
        cin>>str;
        if(~str.find_first_of("^>v<",0)){
          sensha_y=i;
          sensha_x=str.find_first_of("^><v",0);
        }
        map.push_back(str);
      }
      cin>>m>>str;
      for(int i=0;i<m;i++){
        if(str[i]!='S'){
          int sy=sensha_y+(str[i]=='U'?-1:str[i]=='D'?1:0);
          int sx=sensha_x+(str[i]=='L'?-1:str[i]=='R'?1:0);
          if(sy>=0&&sy<H&&sx>=0&&sx<W&&map[sy][sx]=='.'){
            map[sensha_y][sensha_x]='.';
            sensha_y=sy;
            sensha_x=sx;
          }
          map[sensha_y][sensha_x]=(str[i]=='U'?'^':str[i]=='D'?'v':str[i]=='L'?'<':'>');
        }
        else if(str[i]=='S'){
          char ki=map[sensha_y][sensha_x];
          int dir=(ki=='^'?0:ki=='>'?1:ki=='v'?2:3);
          int tx,ty;
          tx=sensha_x+dx[dir];
          ty=sensha_y+dy[dir];
          for(;tx>=0 && tx<W && ty>=0 && ty<H ;){
            if(map[ty][tx]=='*'||map[ty][tx]=='#'){
              if(map[ty][tx]=='*')map[ty][tx]='.';
              break;
            }
            tx+=dx[dir];
            ty+=dy[dir];
          }
        }
      }
      for(int i=0;i<H;i++)cout<<map[i]<<endl;
    }
  }
  return 0;
}
*/