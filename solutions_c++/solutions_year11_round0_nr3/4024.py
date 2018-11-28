#include <iostream>

using namespace std;

const int MAX = 1000;

void reset(int a[], int n)
{
  int i;
  for(i = 0; i < n; i++)
    a[i] = 0;
}

void inc(int a[], int n)
{
  int carry = 1;
  int i;
  for(i = 0; i < n; i++) {
    a[i] += carry;
    if(a[i] == 2) {
      carry = 1;
      a[i] = 0;
    }
    else {
      return;
    }
  }
  // overflow ?
}

void set_min(int a[], int n)
{
  int i;
  reset(a, n);
  inc(a, n);
}

void set_all(int a[], int n)
{
  int i;
  for(i = 0; i < n; i++)
    a[i] = 1;
}

void set_max(int a[], int n)
{
  reset(a, n);
  if(n >= 2)
    set_all(a, n - 1);
}

int cmp(int a[], int b[], int n)
{
  int i;
  for(i = n - 1; i >= 0; i--)
    if(a[i] > b[i])
      return(1);
    else if(a[i] < b[i])
      return(-1);
  return(0);
}

int sean_add(int a[], int bit[], int flag, int n)
{
  int i;
  int sum = 0;
  for(i = 0; i < n; i++)
    if(bit[i] == flag)
      sum = sum + a[i];
  return(sum);
}

int patrick_add(int a[], int bit[], int flag, int n)
{
  int i;
  int sum = 0;
  for(i = 0; i < n; i++)
    if(bit[i] == flag)
      sum = sum ^ a[i];
  return(sum);
}

void printa(int a[], int n)
{
  int i;
  for(i = n - 1; i >= 0; i--) {
    cout<<a[i]<<' ';
  }
  cout<<endl;
}

int max(int a, int b)
{
  return(a > b ? a : b);
}

int handle(int candy[], int n)
{
  //int candy[3] = {3, 5, 6};
  int bit[MAX], maximum[MAX];
  int psum0, psum1, ssum0, ssum1;
  int sum = 0;
  int cry = 1;

  set_min(bit, n);
  set_max(maximum, n);

  //printa(maximum, n);
  //printa(bit, n);
  //cout<<endl;
  int count = 0;
  while(cmp(bit, maximum, n) <= 0) {
    psum0 = patrick_add(candy, bit, 0, n);
    psum1 = patrick_add(candy, bit, 1, n);
    if(psum0 == psum1) {
      //printa(candy, n);
      //printa(bit, n);
      ssum0 = sean_add(candy, bit, 0, n);
      ssum1 = sean_add(candy, bit, 1, n);
      sum = max(sum, max(ssum0, ssum1));
      //cout<<"sum="<<sum<<endl;
      //cout<<"psum0="<<psum0<<' '<<"psum1="<<psum1<<' ';
      //cout<<"ssum0="<<ssum0<<' '<<"ssum1="<<ssum1<<endl;
      cry = 0;
    }
    inc(bit, n);
    //printa(bit, n);
    //cout<<endl;
    //count++;
    //cout<<"count: "<<count<<endl;
  }
  //cout<<"max : "<<sum<<endl;
  if(cry == 1)
    return(-1);
  return(sum);
}

int
main(int argc, char **argv)
{
  FILE *fp;
  int casenum;
  int candynum;
  int candy[MAX];
  int i, j, value;
  char ch;

  cin>>casenum;
  //cout<<"casenum: "<<casenum<<endl;

  for(i = 0; i < casenum; i++) {
    cin>>candynum;
    //cout<<"candy number = "<<candynum<<endl;
    for(j = 0; j < candynum; j++) {
      cin>>candy[j];
    }
    //cout<<"candy value : ";
    //for(j = 0; j < candynum; j++) {
    //  cout<<candy[j]<<" ";
    //}
    //cout<<endl;

    value = handle(candy, candynum);
    if(value == -1)
      cout<<"Case #"<<i+1<<": NO"<<endl;
    else
      cout<<"Case #"<<i+1<<": "<<value<<endl;
    reset(candy, MAX);
  }
}
