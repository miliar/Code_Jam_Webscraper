#include<iostream>
#include<fstream>

using namespace std;
int main()
{
	char combination[36][4];
	char opposing[28][3];
	char invoke[101];
	char element_list[101];
	int C,D,N;
	int i,j,k,pos;
	int t;
	int testcases;
	bool element, oppose;
	
	ifstream fin("B-large.in");
	ofstream fout("B-large-out.in");
	
	fin>>testcases;
	for(int z=1; z<=testcases;z++)
	{
		fin>>C;
		for(i=0;i<C;i++)
		 fin>>combination[i];
		 
		fin>>D;
		for(i=0;i<D;i++)
		 fin>>opposing[i];
	 
	 fin>>N;
	 fin>>invoke;
	 
		t=-1;
		
		for(i=0;i<N;i++)
		{
			element = false;
			oppose = false;
			t++;
			element_list[t] = invoke[i];

			for(j=0; j<C && t>=1; j++)
			{
				if((element_list[t] == combination[j][0] && element_list[t-1] == combination[j][1]) || (element_list[t] == combination[j][1] && element_list[t-1] == combination[j][0]))
				{
					element = true;
					element_list[t-1]=combination[j][2];
					t--;
					break;
				}
			}
			for(j=0; j<D && element==false && oppose == false && t>=1 ; j++)
			{
				for(k=t-1; k>=0; k--)
				{
				if((element_list[t] == opposing[j][0] && element_list[k] == opposing[j][1]) || (element_list[t] == opposing[j][1] && element_list[k] == opposing[j][0]))
				{
					oppose = true;
					t=-1;
 				break;
				}
				}
			}
			}
			if(t!=-1)
			{
			fout<<"Case #"<<z<<": ["<<element_list[0];
			for(i=1;i<=t;i++)
				fout<<", "<<element_list[i];
			fout<<"]"<<endl;
			}
			else
			fout<<"Case #"<<z<<": []"<<endl;
}
 return 0;
}
