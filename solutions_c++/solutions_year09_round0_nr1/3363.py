# include <fstream.h>
  int D,L,N,nr,i,j,ok,k,p;
  ifstream f("fis1.in");
  ofstream g("fis1.out");

  char s[500][16],sir[1000];


void main()
{
   f>>L>>D>>N;
   for(i=1;i<=D;i++) f>>s[i];
   for(i=1;i<=N;i++)
     { f>>sir;
       nr=0;
       for(j=1;j<=D;j++)
	 { // vad daca acest cuvant se poate obtine
	   ok=1;k=0;
	   for(p=0;p<L && ok;p++)
	     {if(sir[k]!='(')
		   {if(sir[k]!=s[j][p]) ok=0;}
		      else
			 { ok=0;
			   while(sir[k]!=')')
				     {  if(sir[k]==s[j][p]) ok=1;
					k++;}


			 }
	       k++;
	      }

	    if(ok) nr++;
	 }

	  g<<"Case #"<<i<<": "<<nr<<endl;
     }

     f.close();g.close();

}