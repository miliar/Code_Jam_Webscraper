#include<iostream>
#include<fstream>
#include<string>

using namespace std;

void main()
{
	int i,j,k,N,S,p,num[101],norm,surp,ln,ls;
	char tmp;
	ifstream ifile("B-large.in");
	ofstream ofile("output.txt");
	if (ifile.is_open())
	{
		ifile>>i;
		//ifile>>tmp;
		//i=i-48;
		cout<<i<<endl;
		//getline(ifile,line[0]);
		for(j=0;j<i;j++)
		{
			ifile>>N;
			//ifile>>tmp;
			ifile>>S;
			//ifile>>tmp;
			ifile>>p;
			ln=p+2*max(p-1,0);
			ls=min(p+2*max(p-2,0),28);
			norm=0;
			surp=0;
			//ifile>>tmp;
			//cout<<N<<" "<<S<<" "<<p;
			for(k=0;k<N;k++)
			{
				ifile>>num[k];
				if(num[k]>=ln)
					norm++;
				else if(num[k]>=ls)
					surp++;
				//cout<<" "<<num[k];
				//ifile>>tmp;
			}
			ofile<<"Case #"<<j+1<<": "<<norm+min(surp,S)<<endl;
			//cout<<endl;
		}
	}
	cin>>tmp;
}