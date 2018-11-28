#include<iostream>
using namespace std;
/*class snaper
{
 public:
 bool haspower;
 bool state;
 snaper(): haspower(false),state(false) {}
 void changestate()
 {
  if(haspower) state=!state;

 }

};
snaper S[10];
*/
 long s[31]={0,1,3,7,15,31,63,127,255,511,1023,2047,4095,8191,16383,32767,65535,131071,262143,524287,1048575,2097151,4194303,8388607,16777215,33554431,67108863,134217727,268435455,536870911,1073741823};
long bSarch(long k)
{
 int l=1;int r=30;
 int mid=(l+r)/2;
 while(mid>l)
 {
  if(k<s[mid]) {r=mid;mid=(l+r)/2;continue;}
  if(k>s[mid]) {l=mid;mid=(l+r)/2;}
  else break;
 }
 return mid;
}

long Sarch(long k)
{
 long tmp=k;
 long tmp0;
 long index=bSarch(k);
 while(s[index]!=tmp)
 {
     tmp0=tmp-1-s[index];
     tmp=tmp0;
     index=bSarch(tmp);
 }

  return index;

}
int main()
{




    int T;
    cin>>T;
    long N,K;
    int i=0;
    //int pos;
    for(i=0;i<T;++i)
    { cin>>N>>K;
    if (K%2==0)
    {
        cout<<"Case #"<<i+1<<": OFF"<<endl;
        continue;

    }

    else
    {
    long j=Sarch(K);
    if(N<=j)
    {

    cout<<"Case #"<<i+1<<": ON"<<endl;
    continue;

    }
    else
    {

         cout<<"Case #"<<i+1<<": OFF"<<endl;
    continue;

    }
    }

}
return 0;
}
