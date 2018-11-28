# include <iostream>
#include <fstream>
#include <string>

using namespace std;
void main()
{
   ofstream mfile ("taner.txt");
   if (mfile.is_open())
  {
   std::ifstream input("file.txt");
   int t;
   int n;
   int s;
   int p;
   int i,szam,g,max;
   int j=0;
   int ered=0;
   input>>t;
   cout<<t;
   for(j=1; j<=t; j++){
	  mfile<<"Case #"<<j<<": ";
      input>>n;
	  cout<<n;
      input>>s;
	  input>>p;
	  ered=0;
	  cout<<n;
	  g=(p-2);
	  g=g*2;
	  g=g+p;
	  max=p-1;
	  max=max*2;
	  max=max+p;

	  if(max<=1)
	  {
		  if (max==-2){max=0; g=0;}
		  else {if (max==1){max=1;g=1;}}
	  }


	  for (i=0; i<n;i++){
		  input>>szam;

		  if(szam>=max)
		  {
			  ered++;
		  }
		  else 
		  {
			  if ((szam>=g)&&(s>0))
			  {
				  ered++;
				  s=s-1;
			  }
		  }
	  }
	  mfile<<ered<<'\n';
	  cout<<ered;
   }

   input.close(); 
  }
  else cout << "Unable to open file";
 
}