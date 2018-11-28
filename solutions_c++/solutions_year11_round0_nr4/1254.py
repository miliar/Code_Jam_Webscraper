#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<stdio.h>
#include<math.h>
#include<iomanip.h>


#define rep(i,n) for(i=0;i<n;i++)
#define res(i,a,b) for(i=a;i<b;i++)

typedef long long ll;

int srt[1000],arr[1000],chk[1000];
int c;
int us[10];
long double hit=0;


void sort(void)
{   int a,b,tem;

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

long double fac(long long n)
{
	if(n==0||n==1)
	return 1;
	else
	return(n*(n-1));
}



long double cal(ll n,ll k)
{
	if(k<=1)
	{
		return 0;
	}
	else
	{
		return(((long double)1/fac(n))+((long double)(3/2)*cal(n,k-1)));
	}
}


void check(void)
{
	int a;
	rep(a,c)
	{
		if(arr[a]==srt[a])
		{
			chk[a]=1;
		}
		else
		{
			chk[a]=0;
		}
	}

}



void shuffl(void)
{
	int a,b,k,tem,ct=0;

	ll v;
	rep(a,c)
	{
	if(chk[a]==1){ct++;}
	}

	if(c==ct){ return ;}


	v=0;

	rep(a,c)
	{	if(chk[a]!=1)
		{us[v]=a;  break;}
	}

	while(arr[us[v]]!=us[0]+1)
	{
	    v++;
	    us[v]=arr[us[v-1]];
	    us[v]--;


	}
	v++;
	rep(a,v)
	{
		chk[us[a]]=1;
	}

	hit=hit+((long double)1/cal(v,v));


	shuffl();


     return;
}




void main(void)
{


	ifstream in("E:\\codejam\\i.txt");
	freopen("o.txt", "w", stdout);
	clrscr();
	cout.setf(ios::showpoint);
	cout.precision(6);
	int t,i,j,n;
	in>>t;

	rep(i,t)
	{
		in>>c;

		rep(j,c)
		{
		in>>n;
		arr[j]=n;
		}

		hit=0;
		sort();
		check();
		shuffl();
		cout<<"Case #"<<i+1<<": "<<hit<<endl;
		hit=0;

	}





}







