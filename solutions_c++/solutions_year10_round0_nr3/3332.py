#include<iostream>
#include<cmath>

using namespace std;

void main()
{
   double R,k;
   int N,T;
   double g[1000];
   unsigned int index;
   double pasadas;
   int i=0,j=0,m=0;
   double total=0,suma=0;

   cin>>T;

   for(i=0;i<T;i++)
   {
		cin>>R>>k>>N;
		for(j=0;j<N;j++)
			cin>>g[j];
		suma=0;
		total=0;
		index=0;
		for(m=0;m<R;m++)
		{
			pasadas=0;
			suma=0;
		   while(suma<=k && pasadas<N)
		   {
		       suma+=g[index];
			   pasadas++;
			   index++;
			   if(index==N)
				   index=0;
		   }
		   if(suma>k)
		   {
			   if(index==0)
				   index=N-1;
			   else
				   index--;
			   suma-=g[index];
		   }
		   total+=suma;
		}//fin for m

		cout<<"Case #"<<i+1<<": "<<total<<endl;
   }
}