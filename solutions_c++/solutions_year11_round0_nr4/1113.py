#include<iostream>
#include<fstream>
using namespace std;
int main()
{ofstream out("outfile.out",ios::out);
	int t,i;
	cin>>t;
	 for(i=0;i<t;i++)
	 {
		 int n,j,a[1000]={0},counter=0;
		 cin>>n;
		 for(j=0;j<n;j++)
		   {
			   cin>>a[j];
			   if(a[j]!=j+1)counter++;
		 }
		 out<<"Case #"<<i+1<<": "<<counter<<endl;
	 }
 	return 0;
}