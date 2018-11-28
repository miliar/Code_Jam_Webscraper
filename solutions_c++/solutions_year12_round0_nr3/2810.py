#include<iostream.h>
#include<fstream.h>
#include<stdlib.h>
#include<string.h>
#include<conio.h>
#include<math.h>
//using namespace std;
int main()
{
	fstream fin,fout;
	fin.open("C-large.in",ios::in);
	fout.open("C-large.out",ios::out);
	int T;
	double A,B,m,n;
	//clrscr();
	fin>>T;
	for(int i=0;i<T;i++)
	{
	   double cnt=0;
	   double max=1,max2,max1;
	   fin>>A;
	   fin>>B;
	   fout<<"Case #"<<i+1<<": ";
	   if(A/10==B/10 && fmod(B,10.0)!=0.0)
	   {
		fout<<cnt;
		//cout<<cnt<<endl;
		fout<<"\n";
		continue;
	   }
	   for(max=1;max<=A;max=max*10);
	   for(n=A;n<B;n++)
	   {
	      if(max*10<=n)
		max=max*10;
	      max1=max/10;
	      int f=0;
	      double tp=n,x,y,tl[7];
	      x=fmod(tp,10);
	      while(tp!=0)
	      {
		tp=floor(tp/10);
		if(x!=fmod(tp,10))
		{
			f=1;
			break;
		}
	       }
		if(f==0)
			continue;
		double tmp=n,tm=10;
		m=0;
		max2=max1;
		int c=0;
		while(tm<=max1)
		{
		   double r,q;
		   r=fmod(tmp,tm);
		   q=tmp/tm;
		   q=floor(q);
		   m=r*max2+q;
		   int f=0;
		   if(n<m && m<=B)
		   {
			for(int j=0;j<c;j++)
			  if(m==tl[j])
			    f=1;
			if(f!=1)
			{
				tl[c++]=m;
				//fout<<n<<"="<<m<<"\n";
				cnt++;
				f=0;
			}
		   }
		   tm=tm*10;
		   max2=max2/10;
		}
		
	   }

	   fout<<cnt;
	   //cout<<cnt<<endl;
	   fout<<"\n";
	}
	fin.close();
	fout.close();
	return(0);
}
