#include<stdio.h>
#include<queue>
#include<fstream>
using namespace std;
int main()
{
 int T,i;
 char arr[]="Case #";
 ifstream infile;
 infile.open("input.txt");
 ofstream outfile("output.txt");
 if(infile.is_open())
 {
 infile>>T;
 for(i=1;i<=T;i++)
 {
           int R,k,N,g,c=0,sum=0;
           queue<int> p,q;
           infile>>R;
           infile>>k;
           infile>>N;
           while(N--)
           {
                     infile>>g;
                     p.push(g);
           }
           while(R--)
           {
            c=0;
            while(c+p.front()<=k)
            {         
                      c=c+p.front();
                      g=p.front();
                      p.pop();
                      q.push(g);
                      if(p.empty())
                                   break;
            }
            while(!q.empty())
            {
                      g=q.front();
                      q.pop();
                      p.push(g);
            }
            sum=sum+c;
           }           
           outfile<<arr<<i<<": "<<sum<<endl;
 }
}
infile.close();
outfile.close();
return 0;
}
