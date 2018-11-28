#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
 int wynik;	
 int n;
 scanf("%d",&n);
 for (int i=0;i<n;i++)
 {
   wynik=0;		
   int m,h,d;
   scanf("%d%d%d",&m,&h,&d);
   int a;
   int nor=3*d-2;
   int spec=3*d-4;
   for (int j=0;j<m;j++)
   {	 	
		scanf("%d",&a);
		if (a==0)
		continue;
		if(a>=nor)
		wynik ++;
		else
		if(h>0 && a>=spec)
		{
		  h--;
		  wynik++;	
	    }	
   }
   if (d==0)
   cout << "Case #"<<i+1<<":"<<" "<<m<<endl;	
   else
   cout << "Case #"<<i+1<<":"<<" "<<wynik<<endl;		
 }
 //system ("pause");
return 0;	
}
