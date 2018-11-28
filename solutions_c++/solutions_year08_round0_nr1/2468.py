#include <iostream>
#include <fstream>
#include <string>
using namespace std;

char* stringCopy(string,int);

void main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in.txt");
	fout.open("ouput.txt");
	
	//FILE CHUK
	
	int n=0,s=0,q=0;
	
	string *name,*que;
	fin>>n;
	int count=0;
	bool a;

	while(count<n)
	{
		fin>>s;

		int ans=0,j=1,check=1,c=0;

		name=new string[s+1];
		
		for (int i=0;i<=s;i++)
		{
			getline(fin,name[i],'\n');
		}
		
		fin>>q;

		que=new string[q+1];
		for (i=0;i<=q;i++)
		{
			getline(fin,que[i],'\n');
		}
		
		//FC
		
		int start=1;a=false;
		while(!a)
		{
			check=1;
			j=start;i=1;
			while(i<=s && !a)
			{
				j=start;
				
				if (q<=0 || s<2) break;

				while(name[i].compare(que[j])!=0)
				{
					j++;
					if (j>q)
					{
						a=true;
						break;
					}
				}
				
				if (j>=check && j<=q && !a)
				{
					check=j;
					c=i;
				}
				
				i++;
			}
			
			start=check;
			
			if (!a && q>0 && s>=2)
				ans++;

			else break;
		}
		
		fout<<"Case #"<<count+1<<": "<<ans<<endl;
	
		count++;
	}

	fin.close();
}