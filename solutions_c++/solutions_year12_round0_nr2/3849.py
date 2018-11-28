#include<conio.h>
#include<iostream.h>
#include<fstream.h>
#include<string.h>

int main()
{
	int i, j, tc,len,n,s,p,sco,rem,ans,max;

	ifstream inf("input.in");
   ofstream opf("one.o");

   inf>>tc; cout<<tc<<"\n";
   
   for(i=0 ;i<tc ; i++)
   {
           opf<<"Case #"<<(i+1)<<": ";
           ans=0;
           inf>>n>>s>>p;  cout<<n<<" "<<s<<" "<<p<<" ";
           
           for(j=0 ; j<n ; j++)
           {
                   inf>>sco;  cout<<sco<<" ";
                   rem=sco%3;
                   if(rem==0)
                             max=sco/3;
                   else
                       max=(sco/3)+1;
                   if(max>=p)
                             ans++;
                   else
                   {
                       if(max!=0&&s>0&&rem!=1)
                       {
                                      
                                      max++;
                                      
                                      if(max>=p)
                                      {
                                                s--;
                                                ans++;
                                      }                                 
                       }
                   }
                   
           }
           opf<<ans<<"\n"; cout<<"\t\t"<<ans<<"\n";
   }
   cin>>i;
  return 0;
}
