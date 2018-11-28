#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

#define LD long double
#define LL long long

int n;
int d[35];
vector<int> v[35];

vector<int> mult(vector<int> a, vector<int> b)
{
  vector<int> res;
  res.resize(a.size()+b.size()-1);
  for(int i=0;i<a.size();i++)
    for(int j=0;j<b.size();j++)
      res[i+j] += a[i]*b[j];
  int r=0;
  for(int i=0;i<res.size();i++) {
    int tmp=res[i]+r;
    res[i]=tmp%10;
    r=tmp/10;
  }
  while(r) {
    res.push_back(r%10);
    r/=10;
  }
  return res;
}

void print(vector<int> u)
{
  for(int i=u.size()-1;i>=0;i--)
    printf("%d", u[i]);
  printf("\n");
}

int main()
{
  int tt;
  scanf("%d", &tt);
  LD aaa=3+sqrt(5);
  //printf("%.100llf\n", aaa);
  //5.23606797749978969640
  //string tmp="523606797749978969640";
  //string tmp="1234567890";
  //string tmp="5236067977499789805051477742381393909454345703125";
  string tmp="52360679774997896964091736.68731276235440618359";
  //printf("%d\n", tmp.length());
  for(int i=tmp.length()-1;i>=0;i--)
    v[1].push_back(tmp[i]-'0');
  d[1]=46; 
  v[2] = mult(v[1],v[1]);
  d[2]=2*46;
  //printf("d=%d, len=%d, num=", d[2], v[2].size());
  //print(v[2]);
  for(int i=3;i<35;i++) {
    v[i] = mult(v[i-1], v[1]);
    d[i] = d[i-1]+46;
    //printf("d=%d, len=%d, num=", d[i], v[i].size());
    //print(v[i]);
  }

  for(int t=1;t<=tt;t++) {
    scanf("%d", &n);
    printf("Case #%d: ", t);
    for(int i=2;i>=0;i--)
      if(d[n]+i>=v[n].size()) printf("0");
      else printf("%d", v[n][d[n]+i]);
    printf("\n");
  }
  return 0;
}
