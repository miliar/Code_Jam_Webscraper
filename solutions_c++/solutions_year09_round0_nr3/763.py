#include <iostream>
#include <sstream>
#include <fstream>
#include <conio.h>
//#include<>
using namespace std;


int main(int argc, char *argv[])
{
   
    ifstream in;
    ofstream out;
    in.open("C-large.in",ios::in);
    out.open("c.out",ios::out);
    int i,j,l,n,N,k,ans,M=10000;
    string s,t="welcome to code jam";

    in >> N;
    getline(in,s);
	int table[500][19];
		
    for (n=1;n<=N;n++)
    {
		getline(in,s);
	 	l=s.size();
		for (i=0;i<500;i++) for (j=0;j<19;j++) table[i][j]=0;
//	 	cout<<s<<" "<<l;
	// 	getch();

		for (i=0;i<l;i++)
		{
		 	for (j=0;j<19;j++)
		 	{
//				cout<<j<<" ";
	//			getch();

				if (s[i]==t[j])
				{
					if (j==0)
					{
						table[i][0]=1;
					}
					else
					{
						for (k=0;k<i;k++)
						{
							table[i][j]+=table[k][j-1];
							table[i][j]%=M;
						};						
						
					};							
				};
			};
		};

		ans=0;
		for (i=0;i<l;i++) 
		{
			ans+=table[i][18];
			ans%=M;
		};
		out<<"Case #"<<n<<": ";
		if (ans<1000) out<<"0";
		if (ans<100) out<<"0";
		if (ans<10) out<<"0";
		out<<ans<<"\n";
    };
    
    
    
    in.close();
    out.close();
//    getch();
    return EXIT_SUCCESS;
   
}
