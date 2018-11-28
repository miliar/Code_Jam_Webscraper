#include<fstream>
#include<algorithm>
#include<string>
using namespace std;
ifstream fin("B.in");
ofstream f2out("B2.out");
ofstream fout("B.out");
int dig[10];
int main()
{
   int T;
   fin>>T;
   for(int k=0;k<T;k++)
   {
      string N,n2,base,p;
      memset(dig,0,sizeof(dig));
      fin>>N;
      int d=0,zero=0,mx=0;
      for(int i=0;i<N.size();i++)
      {
        if(N[i]-'0'==0)zero=1;
        if(!dig[N[i]-'0']&&N[i]!='0')d++;
        dig[N[i]-'0']++;
        if(N[i]!='0')
        mx=max(mx,dig[N[i]-'0']);
      }
      f2out<<"Case #"<<k+1<<": "<<N<<endl;
      if((d<2&&!zero)||(d<2&&zero&&mx<2)){
      fout<<"Case #"<<k+1<<": "<<N[0]<<"0"<<N.substr(1,N.size()-1)<<endl;
      continue;}
      
      n2=N;
      //n2=next(N);
      base=N;
      sort(&base[0],&base[base.size()]);
      if(base[0]=='0')
      swap(base[0],base[1]);
      while(n2==N)
      {
         p=n2;
         next_permutation(&n2[0],&n2[n2.size()]);
         if(n2<N)
         {
            n2=base[0];
            n2+="0";
            n2+=base.substr(1,N.size()-1);
            base=n2;
         }
      }
      fout<<"Case #"<<k+1<<": "<<n2<<endl;
   }
   return 0;
}
