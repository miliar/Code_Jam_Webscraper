#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<stdio.h>
#include<math.h>
#include<iomanip.h>


#define rep(i,n) for(i=0;i<n;i++)
#define res(i,a,b) for(i=a;i<=b;i++)

typedef long long ll;

char c[40][3];
char d[30][2];
char n[100];
ll l=-1;
ll cn,dn,nn;
int fl=0;

void chcom(char k)
{       ll a;
	if(l>=0)
	{
	rep(a,cn)
	{
		if(c[a][0]==k)
		{ if(c[a][1]==n[l])
			{n[l]=c[a][2]; fl=1;return;}
		}
		else if(c[a][1]==k)
		{ if(c[a][0]==n[l])
			{n[l]=c[a][2]; fl=1;return;}
		}
	}
	}
	l++;
	n[l]=k;
	fl=0;

	return;
}

void chopp(char k)
{
	ll a,b;
	if(l>0)
	{
	rep(b,l)
	{
	rep(a,dn)
	{
		if(d[a][0]==k)
		{ if(d[a][1]==n[b])
			{l=-1; return;}
		}
		else if(d[a][1]==k)
		{ if(d[a][0]==n[b])
			{l=-1; return;}
		}
	}
	}
	}
	return;
}

void main(void)
{


	ifstream in("e:\\codejam\\i.txt");
	freopen("o.txt", "w", stdout);
	clrscr();
	cout.setf(ios::fixed);
	cout.unsetf(ios::showpoint);

	ll t;
	in>>t;
	ll i;
	ll j;
	ll k;
	char ch;



	rep(i,t)
	{
		in>>cn;
		rep(j,cn)
		{
		   rep(k,3)
		   { in>>ch;
		     c[j][k]=ch;
		   }
		}
		in>>dn;
		rep(j,dn)
		{
		   rep(k,2)
		   { in>>ch;
		     d[j][k]=ch;
		   }
		}
	       in>>nn;
	       rep(j,nn)
	       {
	       in>>ch;
	       chcom(ch);
	       if(fl==0)
	       {
	       chopp(ch);
	       }
	       }
	       if(l>0)
	       {
	       cout<<"Case #"<<i+1<<": ["<<n[0];
	       res(j,1,l){cout<<", "<<n[j];}
	       cout<<"]"<<endl;
	       }
	       if(l==0)
	       {
	       cout<<"Case #"<<i+1<<": ["<<n[0]<<"]"<<endl;
	       }
	       if(l==-1)
	       {
	       cout<<"Case #"<<i+1<<": []"<<endl;
	       }
	       l=-1;

      }





}







