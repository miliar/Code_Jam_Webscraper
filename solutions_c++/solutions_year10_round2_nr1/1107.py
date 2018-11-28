#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <ctime>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;

typedef struct t_dir
{
  string name;
  vector <struct t_dir> child;
}T_DIR;

T_DIR dir_root;
T_DIR dir_array[100*101];
int dir_table_index;
int dir_root_num;

void store_dir(string & s)
{
  int L = s.length();
  int index = 0;
  int i;
  T_DIR * p_dir = &dir_root;
  while(index<L)
  {
    char c;
    if(s[index]=='/')index++;
    string dirname="";
    while(((c=s[index])!='/')&&index<L)
    {
//cout<<c<<endl;
      dirname += c;
      index++;
    }
    //depthéüå≥Ç…ìØÇ∂Ç‡ÇÃÇ™Ç†ÇÈÇ©íTÇ∑
    int child_num = p_dir->child.size();
//cout<<"child_num ="<<child_num<<"  dirname="<<dirname<<endl;
    for(i=0;i<child_num;i++)
    {
      if(p_dir->child[i].name == dirname)break;
    }
    if(i==child_num)
    {
      T_DIR tmp;
      tmp.name=dirname;
      tmp.child.clear();
      p_dir->child.push_back(tmp);
    }
    p_dir = &(p_dir->child[i]);
  }
}

int  calc_mkdir_num(string & s)
{
  int L = s.length();
  int index = 0;
  int depth = 0;
  int i;
  T_DIR * p_dir = &dir_root;
  int ret = 0;
  while(index<L)
  {
    char c;
    if(s[index]=='/')index++;
    string dirname="";
    while(((c=s[index])!='/')&&index<L)
    {
//cout<<c<<endl;
      dirname += c;
      index++;
    }
    //depthéüå≥Ç…ìØÇ∂Ç‡ÇÃÇ™Ç†ÇÈÇ©íTÇ∑
    int child_num = p_dir->child.size();
    for(i=0;i<child_num;i++)
    {
      if(p_dir->child[i].name == dirname)break;
    }
    if(i==child_num)
    {
      //ìØÇ∂Ç‡ÇÃÇ™å©Ç¬Ç©ÇÁÇ»Ç©Ç¡ÇΩ
      //Ç†Ç∆ÇÕ/ÇÃêîÇêîÇ¶ÇÈ
      if(index<L)
      {
        while(index<L)
        {
          if(s[index]=='/')
          {
            ret++;
          }
          index++;
        }
      }
      ret++;//ç≈å„ÇÃ1Ç¬ÇÕ/Ç™Ç»Ç¢
      break;
    }
    p_dir = &(p_dir->child[i]);
  }
  store_dir(s);
//cout<<"calc_mkdir_num:"<<s<<" ret="<<ret<<endl;
  return ret;
}

int main(void)
{
  int T,t;
  cin>>T;
//cout<<"T="<<T<<endl;
  for(t=1;t<=T;t++)
  {
//cout<<"t="<<t<<endl;
    memset(dir_array,0,sizeof(dir_array));
    dir_root_num = 0;
    dir_table_index = 0;
    dir_root.name = "/";
    dir_root.child.clear();
    int N,M;
    int m,n;
    cin>>N;
    cin>>M;
//cout<<"N="<<N<<"  M="<<M<<endl;
    for(n=0;n<N;n++)
    {
      string s;
      cin>>s;
//cout<<"input1: "<<s<<endl;
      store_dir(s);
    }
    int ret = 0;
    for(m=0;m<M;m++)
    {
      string s;
      cin>>s;
//cout<<"input2: "<<s<<endl;
      ret += calc_mkdir_num(s);
    }

    cout<<"Case #"<<t<<": "<<ret<<endl;
  }
  return 0;
}
