#include<iostream.h>
#include<fstream.h>
#include<stdlib.h>
#include<string.h>
#include<conio.h>
int main()
{
	fstream fin,fout;
	fin.open("B-small.in",ios::in);
	fout.open("B-small.out",ios::out);
	int N,T,S,P,*t,**tmp;
	clrscr();
	fin>>T;
	for(int i=0;i<T;i++)
	{
	   fin>>N;
	   int s=0,cnt=0;
	   t=(int*) malloc(sizeof(int)*(N+1));
	   tmp=(int**) malloc(sizeof(int**)*(N+1));
	   fin>>S;
	   fin>>P;
	   for(int j=0;j<N;j++)
	   {
		tmp[j]=(int*) malloc(sizeof(int)*3);
		fin>>t[j];
		tmp[j][0]=t[j]/3;
		tmp[j][1]=(t[j]-tmp[j][0])/2;
		tmp[j][2]=t[j]-tmp[j][1]-tmp[j][0];
		if(s<S && tmp[j][2]<P && tmp[j][2]+1>=P && (tmp[j][2]-1==tmp[j][0] || tmp[j][1]==tmp[j][1]))
		{
			if(tmp[j][1]-1>=0 && tmp[j][2]<=10)
			{
				s++;
				tmp[j][1]--;
				tmp[j][2]++;
			}
		}
		if(tmp[j][0]>=P || tmp[j][1]>=P || tmp[j][2]>=P)
			cnt++;
	   }
	   while(s<S)
	   {
	      s++;
	      tmp[j][1]--;
	      tmp[j][2]++;
	   }
	   fout<<"Case #"<<i+1<<": ";
	   fout<<cnt;
	   fout<<"\n";
	}
	fin.close();
	fout.close();
	return(0);
}