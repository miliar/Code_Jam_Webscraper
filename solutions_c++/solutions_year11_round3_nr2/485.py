#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>

using namespace std;
typedef long long ll;
ll cc[1200];
ll a[1200];
ll l,t,n,c;
   
   ll l0()
   {
    ll total=0;
    for(ll i=0;i<n;++i)total+=a[i]+a[i];
    return total;     
   }
   ll l1()
   {
    ll total=0;
    ll best=0;
    for(ll i=0;i<n;++i){
     
     if(total>=t){  if(best<a[i])best=a[i];}
     else if(total+a[i]+a[i]<=t);
     else { ll temp=t-total;
     if(temp%2==1)cout<<"error1";
     ll tem=a[i]-temp/2;
     if(best<tem)best=tem;}
     total+=a[i]+a[i];
            }     
            
     return total-best;
   }
   ll l2()
   {
        ll total=0;
    ll best=0;
    
    for(ll i=0;i<n-1;++i){
     
     ll ap=0;       
     if(total>=t)ap=a[i];
     else if(total+a[i]+a[i]<=t)ap=0;
     else { ll temp=t-total;
     if(temp%2==1)cout<<"error2a";
     ll tem=a[i]-temp/2;
     ap=tem;}
     
     total+=a[i]+a[i];     
     
     for(ll j=i+1;j<n;++j){
     ll total1=total-ap;

     ll bp=0;       
     if(total1>=t)bp=a[j];
     else if(total1+a[j]+a[j]<=t)bp=0;
     else { ll temp=t-total1;
     if(temp%2==1)cout<<"error2b";
     ll tem=a[j]-temp/2;
     bp=tem;}
     
     if(best<ap+bp)best=ap+bp;
             }
     

            }     
            
     return total+a[n-1]+a[n-1]-best;
   }
main()
{
	ifstream fin;ofstream fout;
	fin.open("D:\\B-small-attempt1.in");
//    fin.open("D:\\B-large.in");
	fout.open("D:\\B-small.out");
//	fout.open("D:\\B-large.out");
	
	ll tests;
	
	fin>>tests;
	
	for(ll cas=1;cas<=tests;++cas)
	{
   fin>>l>>t>>n>>c;
   for(ll i=0;i<c;++i){fin>>cc[i];}
   for(ll i=0;i<n;++i){a[i]=cc[i%c];}
   ll ret=2100000000;
    if(l==0)ret=l0();
    if(l==1)ret=l1();
    if(l==2)ret=l2();
    if(l>2)cout<<"error";
     fout<<"Case #"<<cas<<": "<<ret<<endl;
    }
 
	fin.close();
	fout.close();
	cin>>tests;
}
