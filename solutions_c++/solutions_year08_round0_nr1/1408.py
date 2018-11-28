#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int n,s,q;
	ifstream in("in.txt");
	ofstream out("out.txt");
	in>>n;
	for (int l=0;l<n;l++)
	{
		in>>s;
		vector <string> searchm,quer;
		char str[101];
		in.getline(str,100);
		for (int i=0;i<s;i++)
		{
			in.getline(str,100);
			searchm.push_back(str);
		}
		in>>q;
		if (q==0)
		{
			out<<"Case #"<<l+1<<": "<<0<<endl;
			continue;
		}
		in.getline(str,100);
		for (int i=0;i<q;i++)
		{
			in.getline(str,100);
			quer.push_back(str);
		}
		int mas[110][1010];
		for (int i=0;i<s;i++)
		{
			for (int j=0;j<q;j++)
				mas[i][j]=q+1;
		}
		for (int i=0;i<s;i++)
		{
			if (quer.size()>=1)
				if (searchm[i].compare(quer[0])!=0)
				mas[i][0]=0;
		}
		
		for (int i=1;i<q;i++)
		{
			
			string qur=quer[i];
			for (int j=0;j<s;j++)
			{
				int kol=INT_MAX;
				if (searchm[j].compare(qur)==0)
				{
					continue;
				}
				kol=mas[j][i-1];
				for (int k=0;k<s;k++)
				{	
					if (k==j)
						continue;
					kol=min(mas[k][i-1]+1,kol);
				}
				mas[j][i]=kol;
				
			}
		}
		int kl=INT_MAX;
		for (int i=0;i<s;i++)
		{
			kl=min(kl,mas[i][q-1]);
		}
		out<<"Case #"<<l+1<<": "<<kl<<endl;
	}
	return 0;
}