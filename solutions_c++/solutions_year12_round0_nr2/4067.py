# include<iostream>
# include<cstdio>
# include<cmath>
# include<fstream>
# include<sstream>
using namespace std;
int main()
{
    int t,i=0; 
    freopen("sub.in","r",stdin);
    int nor[31]={0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10};
    int sp[31]={0,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,10,10};
    cin>>t;
    ofstream myfile;
    myfile.open("o.txt");
    while(t--)
    {
              ++i;
              myfile<<"Case #"<<i<<": ";
              int n,s,p,c=0,j;
              cin>>n>>s>>p;
              //myfile<<n<<" "<<s<<" "<<p<<" ";
              int ti;
              for(j=0;j<n;++j)
              {
                             // myfile<<"\nF\n";
                              cin>>ti;//myfile<<ti<<" ";
                              if(p<=nor[ti])
                              ++c;//myfile<<"B\t"<<p<<" "<<s<<endl;}
                              else
                              {
                                  if(p==sp[ti] && s)
                                  {
                                       ++c;
                                       --s;//myfile<<s<<" \n";
                                  }
                              }                
              }
              //myfile<<endl;
              myfile<<c<<endl;
    cin.ignore();
    }
    
    myfile.close();
    return 0;
}
                              
                              
                              
              
