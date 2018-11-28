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

vector<PI> node;

int used_flag[512][512];
UINT32 bitmap[512][512/32];

//size bitŽæ“¾
// Žæ“¾bit‚ÍãˆÊ‘¤‚É‚­‚é‚æ‚¤‚É‚·‚é
inline UINT32 getbits(int y,int x,int size)
{
  int x_index = x>>5;
  int x_mod   = x & 31;
  UINT32 val0 = bitmap[y][x_index];
  UINT32 val1 = bitmap[y][x_index + 1];
  //val0‚©‚ç32-x_mod bit
  UINT32 ret = val0<<x_mod;
  ret >>= (32-size);
  ret <<= (32-size);
  if(x_mod+size>32)
  {
    ret |= val1>>(32-x_mod);
  }
#ifdef DEBUG_PRINT
printf("val0=%x, val1=%x, ret = %x, x_mod = %d, size=%d\n",val0,val1, ret, x_mod,size);
#endif
  return ret;
}

inline void set_used_flag(int y,int x,int size)
{
  int i,j;
  for(j = y;j<y+size;j++)
  {
    for(i=x;i<x+size;i++)
    {
      used_flag[j][i] = 1;
    }
  }
}

inline int is_set_used_flag(int y,int x,int size)
{
  int i,j;
  for(j = y;j<y+size;j++)
  {
    for(i=x;i<x+size;i++)
    {
      if(used_flag[j][i] == 1)return 1;
    }
  }
  return 0;
}

int search_square(int square_size , int M, int N)
{
  int y,x;
  int ret = 0;
  UINT32 check0 = 0x55555555<<(32-square_size);
  UINT32 check1 = 0xaaaaaaaa<<(32-square_size);
#ifdef DEBUG_PRINT
printf("square_size=%d, M=%d, N=%d,check0=%x,check1=%x\n",square_size,M,N,check0,check1);
#endif
  for(y = 0 ; y<=(M - square_size) ; y++)
  {
    for(x = 0 ; x<=(N - square_size) ; x++)
    {
#ifdef DEBUG_PRINT
printf("y=%d, x=%d\n",y,x);
#endif

      UINT32 bit = getbits(y,x,square_size);
#ifdef DEBUG_PRINT
printf("bit=%x\n",bit);
#endif
      if(bit==check0)
      {
        UINT32 tmp_check0 = check1;
        UINT32 tmp_check1 = check0;
        int find_flag = 1;
        for(int y2=y+1;y2<y+square_size;y2++)
        {
          UINT32 bit2 = getbits(y2,x,square_size);
#ifdef DEBUG_PRINT
printf("bit2=%x, tmp_check0=%x\n",bit2,tmp_check0);
#endif
          if(bit2!= tmp_check0)
          {
            find_flag = 0;
            break;
          }
          swap(tmp_check0,tmp_check1);
        }
        if(find_flag==1)
        {
          if(is_set_used_flag(y,x,square_size) == 0)
          {
            set_used_flag(y,x,square_size);
            ret++;
          }
        }
#ifdef DEBUG_PRINT
printf("find_flag=%d, ret=%d\n",find_flag,ret);
#endif
      }
      else if(bit==check1)
      {
        UINT32 tmp_check0 = check0;
        UINT32 tmp_check1 = check1;
        int find_flag = 1;
        for(int y2=y+1;y2<y+square_size;y2++)
        {
          UINT32 bit2 = getbits(y2,x,square_size);
          if(bit2!= tmp_check0)
          {
            find_flag = 0;
            break;
          }
          swap(tmp_check0,tmp_check1);
        }
        if(find_flag==1)
        {
          if(is_set_used_flag(y,x,square_size) == 0)
          {
            set_used_flag(y,x,square_size);
            ret++;
          }
        }
      }
    }
  }
//  while(square_size>32)
//  {
//  }
  return ret;
}

int main(void)
{
  int T,t;
  cin>>T;
#ifdef DEBUG_PRINT
cout<<"T="<<T<<endl;
#endif
  for(t=1;t<=T;t++)
  {
    memset(used_flag,0,sizeof(used_flag));
    memset(bitmap,0,sizeof(bitmap));
#ifdef DEBUG_PRINT
cout<<"t="<<t<<endl;
#endif
    int i,j;
    int M;
    int N;
    int m,n;
    cin>>M;
    cin>>N;
#ifdef DEBUG_PRINT
cout<<"N="<<N<<"  M="<<M<<endl;
#endif
    for(m=0;m<M;m++)
    {
      UINT32 val = 0;
      int count = 28;
      int bitmap_index = 0;
      string s;
      cin>>s;
      for(i=0;i<N/4;i++)
      {
        char c = s[i];
        if(c>='0'&&c<='9')
        {
          val += (c - '0')<<count;
        }
        else //if(c>='A'&&c<='F')
        {
          val += (c - 'A' + 10)<<count;
        }
        count -= 4;
        if(count<0)
        {
#ifdef DEBUG_PRINT
printf("val=%x\n",val);
#endif
          bitmap[m][bitmap_index++] = val;
          val = 0;
          count = 28;
        }
      }
      if(count>=0)
      {
#ifdef DEBUG_PRINT
printf("val=%x\n",val);
#endif
        bitmap[m][bitmap_index] = val;
      }
    }
    vector<PI> result_pair(0);
    for(i=min(M,N);i>=1;i--)
    {
      int tmp_ret;
      tmp_ret = search_square(i,M,N);
      if(tmp_ret)
      {
        result_pair.push_back(make_pair(i,tmp_ret));
      }
    }
    cout<<"Case #"<<t<<": "<<result_pair.size()<<endl;
    for(i=0;i<result_pair.size();i++)
    {
      cout<<result_pair[i].first<<" "<<result_pair[i].second<<endl;
    }
  }
  return 0;
}
