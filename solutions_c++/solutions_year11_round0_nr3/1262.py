#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<stdio.h>
#include<math.h>
#include<iomanip.h>


#define rep(i,n) for(i=0;i<n;i++)
#define res(i,a,b) for(i=a;i<b;i++)

typedef long long ll;

ll srt[1000],arr[1000];


void sort(ll c)
{   ll a,b,tem;

	rep(a,c)
	{ srt[a]=arr[a];}
	rep(a,c)
	{
		res(b,a,c)
		{
		   if(srt[a]>=srt[b])
		   {   tem=srt[b];
		       srt[b]=srt[a];
		       srt[a]=tem;
		   }
		}
	}
}




ll sum(ll x,ll y)
{
	ll i=0,r,j,lx,ly;
	ll data;
	ll xs[20],tem[20],ys[20],as[20];

       while(x>0)
	{
	    r=x%2;
	    xs[i]=r;
	    x=x/2;
	    i++;
	}
	lx=i;
	j=0;
	i=0;
       while(y>0)
	{
	    r=y%2;
	    ys[i]=r;
	    y=y/2;
	    i++;
	}
	ly=i;
	j=0;
	i=0;
	while(lx!=0&&ly!=0)
	{
	   as[i]=(xs[i]&&!ys[i])||(!xs[i]&&ys[i]);
	   lx--;
	   ly--;
	   i++;
	}
	while(lx!=0){as[i]=xs[i]; i++ ; lx--;}
	while(ly!=0){as[i]=ys[i]; i++ ; ly--;}



	ll ans=0;

	while(i--)
	{
	 tem[j]=as[i];
	 j++;

	 ans=(ans*2)+(as[i]);
	 }
	i=0;
	return(ans);

}



void main(void)
{


	ifstream in("i.txt");
	freopen("o.txt", "w", stdout);
	clrscr();
	cout.setf(ios::fixed);
	cout.unsetf(ios::showpoint);
	ll t,i,j,n,tn,nn;

	in>>t;
	rep(tn,t)
	{
	   in>>n;
	   rep(nn,n)
	   {
		in>>arr[nn];
	   }
	   ll sm=0;
	   sort(n);
	   rep(nn,n)
	   {
		sm=sum(sm,srt[nn]);
	   }
	   if(sm!=0)
	   {
		cout<<"Case #"<<tn+1<<": NO"<<endl;
	   }
	   else
	   {
		 res(nn,1,n)
		 {
		  sm=sm+srt[nn];
		 }
		cout<<"Case #"<<tn+1<<": "<<sm<<endl;


	   }



      }





}







