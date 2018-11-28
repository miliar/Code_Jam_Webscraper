#include<fstream>
using namespace std;
int main()
{
    int t,v=0,n,l,h,flag,i,j,note,ar[100],c;
    ifstream fin("C-small-attempt0.in");
    ofstream fout("output3.txt");
    fin>>t;
    while(t--)
    {
              v++;
              flag=0;
              fin>>n>>l>>h;
              for(i=0;i<n;i++)
              fin>>ar[i];
              for(j=l;j<=h;j++)
              {
                               c=0;
                              for(i=0;i<n;i++)
                              {
                                              if((ar[i]%j==0)||(j%ar[i]==0))
                                              c++;
                                              }
                                              if(c==n)
                                              {
                                                      flag=1;
                                                      note=j;
                                                      break;
                                                      
                                                      }}
                                                      if(flag==1)
                                                      fout<<"Case #"<<v<<": "<<j<<endl;
                                                      else
                                                      fout<<"Case #"<<v<<": "<<"NO"<<endl;
                                                      }
                                                      return 0;
                                                      }
                                                      
                                                      
