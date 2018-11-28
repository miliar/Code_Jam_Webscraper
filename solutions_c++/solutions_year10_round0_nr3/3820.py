
#include<list>
#include<iterator>
#include<fstream>
using namespace std;

ifstream fin("C-small-attempt2.in");
ofstream  fout("c-small.out");
int main()
{
    int t,r,k;
    int n;
    int a;
    int b,c;
    int sum=0;
    int m=0;
    int cs=1;
    fin>>t;
    list<int> q;
    while(cs<=t)
    {
        fin>>r>>k>>n;
        while(n>0)
        {
            fin>>a;
            q.push_back(a);
            n--;
        }
        list<int>::iterator iter;
         m=0;
        while(r>0)
        {
            int count=0;
            sum=0;
            for(iter=q.begin();iter!=q.end();iter++)
            {
                 c=sum;
                 sum+=*iter;
                // cout<<sum<<' ';
                  if(sum<=k)
                  {
                      count++;
                      //cout<<count<<' ';
                  }
                  else
                  {
                      sum=c;
                     break;
                  }
            }
            m+=sum;
            for(int i=0;i<count;i++)
            {
               b=q.front();
               q.push_back(b);
               q.pop_front();
            }
            r--;
        }
            fout<<"Case #"<<cs<<": "<<m<<endl;
            q.clear();

        cs++;
     }
return 0;
}
