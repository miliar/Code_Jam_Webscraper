#include<iostream>
#include<string>
#include<vector>
#include<cstring>
#include<sstream>
using namespace std;

int main()
{
     int cases,cas;
     string s;
     cin>>cases;
     getline(cin,s,'\n');
     int h,w,i,j;
     for(cas=1;cas<=cases;cas++)
     {
     	//string s;
     	getline(cin,s,'\n');
     	
     	int a[3][11];
     	for(i=0;i<3;i++)
     		for(j=0;j<11;j++)
     			a[i][j]=0;
     	//char search='.';
     	for(i=0;i<s.size();i++)
     	{
     		if(s[i]=='w')
			{
				a[0][0]++;
			}
			else if(s[i]=='e')
			{
				a[0][1]+=a[0][0];
				a[1][1]+=a[0][5];
				a[2][1]+=a[0][8];	
			}
			else if(s[i]=='l')
			{
				a[0][2]+=a[0][1];
			}
			else if(s[i]=='c')
			{
				a[0][3]+=a[0][2];
				a[1][3]+=a[1][6];
			}
			else if(s[i]=='o')
			{
				a[0][4]+=a[0][3];
				a[1][4]+=a[0][7];
				a[2][4]+=a[1][3];
			}
			else if(s[i]=='m')
			{
				a[0][5]+=a[0][4];
				a[1][5]+=a[0][10];
			}
			else if(s[i]==' ')
			{
				a[0][6]+=a[1][1];
				a[1][6]+=a[1][4];
				a[2][6]+=a[2][1];	
			}
			else if(s[i]=='t')
			{
				a[0][7]+=a[0][6];
			}
			else if(s[i]=='d')
			{
				a[0][8]+=a[2][4];
			}
			else if(s[i]=='j')
			{
				a[0][9]+=a[2][6];
			}
			else if(s[i]=='a')
			{
				a[0][10]+=a[0][9];
			}
			//cout<<s[i]<<endl;
			int m,n;
			for(m=0;m<3;m++)
     		{	
     			for(n=0;n<11;n++)
     				a[m][n]=a[m][n]%10000;
     				//cout<<a[m][n]<<" ";
     			//cout<<endl;
     		}
     	}
     	ostringstream sout;
        sout<<a[1][5];
        string app( 4 - sout.str().size(),'0');
     	cout<<"Case #"<<cas<<": "<<app<<sout.str()<<endl;
     }
     return 0;
}
