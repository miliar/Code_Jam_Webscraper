#include<fstream>
using namespace std;
int main()
{
    
    int q=0,t,op,bp,bw,ow,l,c,n,k;
    char ch;
    ifstream fin("A-large.in");
    ofstream fout("outputnewal.txt");
    fin>>t;
    while(t--)
    {
              c=0;
              op=1;
              bp=1;
              ow=0;
              bw=0;
              fin>>n;
              q++;
              while(n--)
              {
                        
               
                fin>>ch;
                fin>>k;
                if(ch=='O')
                 {                 
                           l=k-op;
                           //cout<<"l= "<<l<<" k=  "<<k<<"bw = "<<bw<<endl;
                           if(l<0)
                           l=-1*l;
                           
                           op=k;
                           if(l>=bw)
                           l=l-bw+1;
                           else
                           if(l<bw)
                           l=1;
                           ow=ow+l;
                           c=c+l;
                           
                           
                           bw=0;
                           //cout<<"c= "<<c<<" L ="<<l<<endl;
                           }
                           if(ch=='B')
                           {
                               
                                      
                                      l=k-bp;
                             //         cout<<"l= "<<l<<" k=  "<<k<<"ow = "<<ow<<endl;
                                      if(l<0)
                                      l=-1*l;
                                      
                                      bp=k;
                                      
                                      if(l>=ow)
                                       l=l-ow+1;
                                       else
                                      if(l<ow)
                                       l=1;
                                       bw=bw+l;
                                       c=c+l;
                                       ow=0;
                               //       cout<<"c= "<<c<<" L ="<<l<<endl;
                                      }
                                      
                                      }
                                      fout<<"Case #"<<q<<":"<<" "<<c<<endl;
                                      
                                      
                         
    
    
    
}
    
    
    
    
    
                                                        fout<< flush;
                                                        fout.close();
                                                        return 0;
                                                        }
