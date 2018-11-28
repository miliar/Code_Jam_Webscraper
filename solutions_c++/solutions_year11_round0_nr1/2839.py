#include <cstdlib>
#include <iostream>
#include <math.h>

using namespace std;

struct s
{
      char rob; int pos;
      
      }seq[105];

int t,n;
int ans;
int op,bp;


void init()
{ans=-1;
 op=bp=0;
 
 cin>>n;
 getchar();
 for(int i=1;i<=n;i++)
 {char r;
  int num;
  cin>>r;
  getchar();
  cin>>num;
  getchar();
 // cout<<r<<num<<endl;
  //getchar();


  seq[i].rob=r;
  seq[i].pos=num;
  //cout<<seq[i].rob<<seq[i].pos<<endl;
      
  }
}


int cal()
{
    int op=1,bp=1;
    int s=0;
    int os=0,bs=0;
    //bool f=false;
    for(int i=1;i<=n;i++)
    {
       if(seq[i].rob=='O') 
          {
          os+=abs(seq[i].pos-op)+1;
           
          if(i==1) s+=os;
          
           if((i>1)&&(seq[i-1].rob=='B'))
           {
          
          // cout<<"os "<<os<<endl;
           if(os>bs) s=os;
           else os=bs+1;
                // cout<<"#";}
           
           }
            op=seq[i].pos;
           
          if(i==n) s=os;
          
           }//*/
       else
          { // cout<<"bs "<<bs<<" "<<seq[i].pos<<" "<<bp<<endl;
             bs+=abs(seq[i].pos-bp)+1;
              //cout<<"bs2 "<<bs<<endl;
             if(i==1) s+=bs;   
          
             if((i>1)&&(seq[i-1].rob=='O'))
              {
             // cout<<"bs "<<bs<<endl;
              if(bs>os)
                s=bs;
              else 
               bs=os+1;
              // cout<<"#";}
                
               }
            bp=seq[i].pos;
          //  cout<<"bp "<<bp<<endl;
          if(i==n) s=bs;
         //  */
         
           }
 // cout<<"i="<<i<<",s="<<s<<endl;      
    }
    return s;
}


void output(int i)
{cout<<"Case #"<<i<<": "<<ans<<endl;
     }
int main(int argc, char *argv[])
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);

cin>>t;
for(int i=1;i<=t;i++)
{   init();
        
    ans=cal(); 
     output(i);   }
   // system("PAUSE");
    return EXIT_SUCCESS;
}
