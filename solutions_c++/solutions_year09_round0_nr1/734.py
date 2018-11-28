#include <iostream>
#include <sstream>
#include <fstream>
#include <conio.h>
//#include<>
using namespace std;

int min(int a, int b)
{
  return a<b?a:b;  
    
};

int main(int argc, char *argv[])
{
   
    ifstream in;
    ofstream out;
    in.open("A-large.in",ios::in);
    out.open("a.out",ios::out);
	int n,L,D,N,i,j,p,ans;
	
    in >>L>>D>>N;
	string words[5000];
	string pattern;
	bool letters[L][26],good;
	for (i=0;i<D;i++) in>>words[i];
    for (n=1;n<=N;n++)
    {
	 in>>pattern;
	 for (i=0;i<L;i++) for (j=0;j<26;j++) letters[i][j]=false;
	 p=0;
	 for (i=0;i<L;i++)
	 {
	  	 if (pattern[p]!='(') {letters[i][pattern[p]-'a']=true;}
	  	 else
	  	 {
		  	 p++;
			 while (pattern[p]!=')')
			 {
			  	   letters[i][pattern[p]-'a']=true;
			  	   p++;
			 }
		  	 
	     };
	     p++;
	  	 
	 };
	 ans=0;

	 for (i=0;i<D;i++)
	 {
	 	 good=true;
		 for (j=0;j<L;j++) if (!letters[j][words[i][j]-'a']) good=false;
		 if (good) ans++;
		 //if (n==4) if (good) cout<<words[i];
	 }
	 out<<"Case #"<<n<<": "<<ans<<"\n";
    };
    
    
  
    in.close();
    out.close();
//    getch();
    return EXIT_SUCCESS;
   
}
