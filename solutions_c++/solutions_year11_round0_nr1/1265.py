#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<stdio.h>
#include<math.h>
#include<iomanip.h>


#define rep(i,n) for(i=1;i<=n;i++)
#define res(i,a,b) for(i=a;i<=b;i++)

typedef long long ll;


struct bt
{
	ll time;
	ll pos;
	ll to;
}o={0,1,0},b={0,1,0};

ll turn,sec;
ll tp;

void process(struct bt *p)
{
	if(tp>p->pos)
	{
		while(p->pos<tp)
		{
			p->pos++;
			p->time++;
		}
	}
	else if(tp<p->pos)
	{
		while(p->pos>tp)
		{
			p->pos--;
			p->time++;
		}
	}
       else if(tp==p->pos)
       {

	  while(p->time<p->to)
	 {
		p->time++;
	 }

       }

	 while(p->time<p->to)
	 {
		p->time++;
	 }


       p->time++;

}




void main(void)
{


	ifstream in("E:\\codejam\\i.txt");
	freopen("o.txt", "w", stdout);
	clrscr();
	cout.setf(ios::fixed);
	cout.unsetf(ios::showpoint);
	ll t;
	ll n;
	ll i;
	char tb;
	in>>t;
	ll tn;
	rep(tn,t)
	{

	   in>>n;
	   rep(i,n)
	   {
		in>>tb>>tp;
		if(tb=='O'||tb=='o')
		{
		      process(&o);
		      b.to=o.time;
		}
		else
		{
		       process(&b);
		       o.to=b.time;
		}
	   }
	   if(b.time>o.time)
	   { 	sec=b.time; }
	   else
	   {	sec=o.time; }

	  cout<<"Case #"<<tn<<": "<<sec<<endl;
	   o.time=0;
	   b.time=0;
	   o.pos=1;
	   b.pos=1;
	   o.to=0;
	   b.to=0;
	}



}







