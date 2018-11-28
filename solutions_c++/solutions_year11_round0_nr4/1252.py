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
#include <fstream>
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;
#define ALL(c) (c).begin(), (c).end()
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define PB push_back
#define MP make_pair

double count_pattern[1001][1001];
double count_all[1001];
double exp_pattern[1001];

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int N;
    cin>>N;
    if(N==1)
    {
      int tmp;
      cin>>tmp;
//      cout<<"Case #"<<t<<": "<<0<<endl;
      printf("Case #%d: %.6f\n",t,0.0);
      continue;
    }
    memset(count_pattern,0,sizeof(count_pattern));
    memset(count_all,0,sizeof(count_all));
    memset(exp_pattern,0,sizeof(exp_pattern));
    VI vp;
    VI flags(N,0);
    VI set;
    REP(i,N)
    {
      int tmp;
      cin>>tmp;
      vp.PB(tmp);
    }
    //����������ւ���Ă��镔���ɂ���
    // ���בւ��Đ������Ȃ镔�����W���ɂ���
    //  ���g�p�m�[�hi���炽�ǂ��ă��[�v�ɂȂ��Ă��镔���𓯂��W���Ƃ݂Ȃ�
    REP(i,N)
    {
      if(flags[i]==0)
      {
        if(vp[i]==i+1)
        {
          flags[i] = 1;
          continue;
        }
        int start = i;
        int curr = i;
        int count = 1;
        while(1)
        {
          int flag = 0;
          REP(j,N)
          {
            if(vp[curr]==j+1)
            {
              flags[j] = 1;
              if(j==start)
              {
                flag = 1;
                break;
              }
              else
              {
                count++;
                curr = j;
                break;
              }
            }
          }
          if(flag)break;
        }
        set.push_back(count);
      }
    }
#ifdef DEBUG
REP(i,set.size())
cout<<"set["<<i<<"]="<<set[i]<<endl ;
#endif

    count_pattern[2][0] = 1;
    count_pattern[2][2] = 1;
    count_all[2] = 2;
    for(int i=3;i<=N;i++)
    {
#ifdef DEBUG
//cout<<"case2:i="<<i<<endl;
#endif
      count_pattern[i][i] = 1;
      count_all[i] = count_all[i-1] * i;
      double count = 1;
      double mul_num = 1;
      for(int j=1;j<=i-2;j++)//j�����ʒu�ŁA(i-j)���قȂ�ʒu
      {
#ifdef DEBUG
//cout<<"case2:j="<<j<<endl;
#endif
        //j�����ʒu�̃p�^�[����C(i,j)��
        mul_num *= (i-j+1);
        mul_num /= j;
        //(i-j)�قȂ�p�^�[���͉ߋ��̌v�Z����(i-j�̂������ׂĈقȂ�)���g��
        count_pattern[i][j] = mul_num * count_pattern[i-j][0];
        count += count_pattern[i][j];
      }
      //i���ׂĈقȂ���̂�i�̑S����P(i,i)����1�ȏ㓯�����̂̍��v������������
      count_pattern[i][0] = count_all[i] - count;
    }
#ifdef DEBUG
{
//if(N==4)
{
int i=N;
cout<<"count_pattern["<<i<<"]=";
REP(j,i+1)cout<<count_pattern[i][j]<<" ";
cout<<endl ;
}
}
#endif
    //Sn = b + a(b+1) + a^2(b+2)+ ... + a^n(b+n)...(n�������v�Z)
    // ������b��i����ёւ����Ƃ���(���Ȃ��Ƃ�1�͓����ɂȂ�Ƃ��̊��Ғl�ł���
    exp_pattern[2] = 2.0;
    for(int i=3;i<=N;i++)
    {
      double b = 1.0 / count_all[i];
      for(int j=1;j<=i-2;j++)//j�����ʒu�ŁA(i-j)���قȂ�ʒu
      {
        b += count_pattern[i][j] / count_all[i] * (exp_pattern[i-j] + 1);
      }
      double a = count_pattern[i][0] / count_all[i];
      exp_pattern[i] = (b + (a))/(1.0-a);
#ifdef DEBUG
cout<<"case3:i="<<i<<"  exp_pattern = "<<exp_pattern[i]<<endl;
#endif
    }
    double ret = 0.0;
    REP(i,set.size())
    {
      int tmp = set[i];
      ret += exp_pattern[tmp];
    }
    printf("Case #%d: %.6f\n",t,ret);
  }
  return 0;
}

