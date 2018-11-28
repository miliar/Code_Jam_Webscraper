#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<map>
using namespace std;
vector<vector<int> > alt;
vector<vector<char> > val;
int h,w;
char c='a';
char call(int a,int b)
  {
  if(val[a][b]>='a' && val[a][b]<='z')return val[a][b];
  int ver[5]={0,-1,0,0,1};
  int hor[5]={0,0,-1,1,0} ;
  int min=10000000;
  int nowx,nowy;
  for(int i=0;i< 5;i++)
    {
    int x=a+ver[i];
    int y=b+hor[i];
    if(x<0|| x>=h || y<0 || y>=w)
       continue;
    if(min>alt[x][y])
      {
      min=alt[x][y];
      nowx=x;
      nowy=y;
      }
    }
  if(nowx==a && nowy==b){val[a][b]=c;c++;return val[a][b];}
  else val[a][b]=call(nowx,nowy);
  return val[a][b];
  }
int main()
{
int t;
cin>>t;
int now=1;
while(now<=t)
  {
  c='a';
  alt.clear();
  val.clear();
  cin >>h;
  cin >>w;
  for(int i=0;i<h;i++)
    {
    vector<int> temp;
    vector<char> now;
    for(int j=0;j<w;j++){int bim; cin >>bim; temp.push_back(bim);now.push_back('A');}
    alt.push_back(temp);
    val.push_back(now);
    } 
for(int i=0;i<h;i++)
  for(int j=0;j<w;j++)
    if(!(val[i][j]>='a' && val[i][j]<='z'))
       call(i,j);
  cout<<"Case #"<<now<<":\n";
  for(int i=0;i<h;i++){for(int j=0;j<w;j++)cout<<val[i][j]<<" ";cout<<"\n";}
  now++;
  }
return 0; 
}
