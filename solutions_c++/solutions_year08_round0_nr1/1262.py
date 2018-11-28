#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<conio.h>
#include<map>
using namespace std;

int main()
{
    int N,M,Q=0;
    fstream in("ia.in",ios::in);
    fstream out("oooa.out",ios::out);

    in>>N;

    for(int n=0;n<N;n++)
    {
            in>>M;

            char s[100][100];
            char junk[1000];
            in.getline(junk,2000,'\n');

            for(int i=0;i<M;++i)
            in.getline(s[i],2000,'\n');

            in>>Q;

            in.getline(junk,2000,'\n');

            char q[1000][100];

            for(int i=0;i<Q;++i)
            in.getline(q[i],2000,'\n');

            map<string,int> m;
            int flag[100];

            int j=0,count=0;
            for(int i=0;i<M;i++)
            {
             m[s[i]]=i;
             flag[i]=1;
            }
            
            while(j<Q)
            {
                      flag[m[q[j]]]=0;

                      int sum=0;
                      for(int i=0;i<M;i++)
                      sum+=flag[i];

                      if(sum==0)
                      {
                                count++;
                              for(int i=0;i<M;i++)
                              {
                               flag[i]=1;
                               }
                         j--;
                      }

                      j++;
            }
           out<<"Case #"<<n+1<<": "<<count<<endl;
           count=0;
    }
    in.close();
    out.close();
system("pause");
return 0;
}
