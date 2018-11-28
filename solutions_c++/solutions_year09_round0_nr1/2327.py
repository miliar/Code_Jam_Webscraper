#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

int main()
{
	int L,D,N;
	cin>>L>>D>>N;
	int i,j;
	vector<string> words(D);
	for(i=0;i<D;i++)
	{
		cin>>words[i];
	}
	sort(words.begin(),words.end());
	//for(int i=0;i<words.size();i++)cout<<words[i]<<endl;
	for(i=0;i<N;i++)
	{
		string input="";
		cin>>input;
		//cout<<endl<<"input is "<<input;
		vector<bool> ans(D,1);
		int pos=0;
		for(j=0;j<input.size();j++)
		{
			string ck="";
			if(input[j]=='(' )
				{
				j++;
				while(input[j]!=')')
					{
						ck+=input.substr(j,1);
						j++;
					}
				}
			else
				ck+=input.substr(j,1);
				//cout<<endl<<"pair of characters "<<ck<<endl;
				int cnt_list=0;
				
				for(int m=0;m<words.size();m++)
				{
					if(pos>0 && ans[m]==0) continue;////go to next word coz it is discarded
					cnt_list=0;
					//cout<<endl<<"Next Word ";
					for(int k=0;k<ck.size();k++)
					{
						//cout<<"checking "<<ck[k]<<" with "<<words[m][pos];
						if(words[m].size()>=pos+1 && words[m][pos]!=ck[k])
							{
								//cout<<" count increased "<<endl;
								cnt_list++;
								
							}
					}
					if(cnt_list==ck.size())
						{
							ans[m]=0;
							//cout<<endl<<"neglecting "<<words[m];//<<"for "<<ck[k]<<" comparing with "<<words[m][pos];	
							}
				}
			pos++;		
		}
		int cnt=0;
		for(j=0;j<ans.size();j++)
			if(ans[j]==1) cnt++;
		cout<<"Case #"<<i+1<<": "<<cnt<<endl;	
	}
	return 0;
}
//////if first character is bigger than that in dictionary
						//if(pos==0 && words[m][0]<ck[k])
							//continue;
						//////  or vice-versa		
						//if(pos==0 && words[m][0]>ck[k])
							//break;
