#include<fstream.h>
#include<conio.h>
#include<ctype.h>
#include<math.h>
#include<string.h>
#include<stdio.h>
int nos,noq,l;
/*void cpy(int ar1[],int ar[])
{
    for(int i=0;ar[i]!=-1;i++)
       ar1[i]=ar[i];
} */
void ins(int ar[])
{
   for(int i=0;i<2001;i++)
      ar[i]=-1;
}
/*void btk(int ar[],int last,int sw)
{
     cout<<last<<"   "<<sw<<"          ";
     if(ar[0]==-1)
     {
	cout<<"done"<<endl;
	if(l>sw)
	   l=sw;
	return;
     }
     int x;

     for(int i=0;ar[i]!=-1;i++)
	 cout<<ar[i]<<" ";
     cout<<endl;

     if(ar[0]!=last && last!=-1)
     {
	 int ar1[2001];
	 ins(ar1);
	 cpy(ar1,ar);

	 btk(ar1+1,last,sw);
	 return;
     }
     for( i=0;i<nos;i++)
     {
	 if(ar[0]==i)
	    continue;

	 int ar1[2001];
	 ins(ar1);
	 cpy(ar1,ar);

	 btk(ar1+1,i,sw+1);

     }
     return;
} */
/*void btk(int ar[],int last,int sw)
{
   if(ar[0]==-1)
   {
      if(l>sw)
	 l=sw;
      return;
   }
   for(int i=0;ar[i]!=-1;i++)
      cout<<ar[i]<<" ";
   cout<<endl;
   if(last!=ar[0] && last!=-1)
       btk(ar+1,last,sw);
   else
   {
      for(int i=0;i<nos;i++)
      {
	 if(i==ar[0])
	    continue;
	 btk(ar+1,i,sw+1);
      }
   }
} */
void fill(int s[])
{
   for(int i=0;i<nos;i++)
     s[i]=i;
}
int complete(int s[])
{
    for(int i=0;i<nos;i++)
      if(s[i]!=-2)
	 return 0;
    for(int kj=0;kj<nos;kj++)
	 cout<<s[kj]<<" ";             // 102111122202
    return 1;
}
int btk(int ar[])
{
   for(int i=0,j=0,t=-1;ar[i]!=-1;)
   {
      int s[100];
      fill(s);
      if(t!=-1)
      s[t]=-2;
      for(int kj=0;kj<nos;kj++)
	 cout<<s[kj]<<" ";             // 102111122202
      cout<<endl;
      for(kj=0;kj<noq;kj++)
	 cout<<ar[kj]<<" ";            //  102111122202
      cout<<endl;
      int flag=0;
      for(;;i++)
      {
	 if(ar[i]==-1 ||complete(s))
	 {
	    flag=1;
	    break;
	 }
	 t=ar[i];
	 s[t]=-2;
      }
      if(!flag)
	 j++;
   }
   return j;
}
int main()
{
   clrscr();
   int nc;
   ifstream fin("temp.txt");
   remove("Out.txt");
   if(!fin)
   {
      cout<<"File nahi khuli";
      getch();
      return 1;
   }
   fin>>nc;
  // cout<<nc;
   for(int c=0;c<nc;c++)
   {
      ofstream fout("Out.txt",ios::app);
      int ar[2001];
      l=32000;
      ins(ar);
      char s[100][100],q[1000];
      fout<<"Case #"<<c+1<<": ";
      fin>>nos;
//    cout<<nos;
      fin.getline(q,100);
      for(int i=0;i<nos;i++)
      {
	 fin.getline(s[i],100);
	 cout<<s[i];
      }
      fin>>noq;
      fin.getline(q,100);
      for(i=0;i<noq;i++)
      {
	 fin.getline(q,100);
	 for(int j=0;j<nos;j++)
	 {
	    if(!strcmp(q,s[j]))
	    {
	       ar[i]=j;
	       break;
	    }
	 }
      }
      cout<<ar[0];
      int x=btk(ar);
      if(x==-1)
	 x=0;
      fout<<x<<"\n";
      cout<<x<<"\n";
      fout.close();
   }

   fin.close();
   getch();
   return 0;
}