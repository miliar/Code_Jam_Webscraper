#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
int numb(vector<int> nm)
{
	int ans=0;
	for(int i=0;i<nm.size();i++)
	ans=ans*10+nm[i];
	return ans;	
}
int main()
{
	int test,i=1;
	cin>>test;
	while(test--)
	{
		int num;
		cin>>num;
		vector<int> dig;
		int num2=num;
		while(num)
		{
			dig.push_back(num%10);
			num=num/10;	
		}
		vector<int> dig2=dig;
		reverse(dig.begin(),dig.end());
		next_permutation(dig.begin(),dig.end());
		int ck=0;
		if(num2>=numb(dig))
		{
				dig2.push_back(0);
				reverse(dig2.begin(),dig2.end());
		next_permutation(dig2.begin(),dig2.end());
		ck=1;
		}
		int ans=0;
		if(ck)
		ans=numb(dig2);
		else
		ans=numb(dig);
		//for(int k=0;k<dig.size();k++)cout<<dig[k]<<" ";
		cout<<"Case #"<<i++<<": "<<ans<<endl;	
	}
	return 0;
}
//////if first character is bigger than that in dictionary
						//if(pos==0 && words[m][0]<ck[k])
							//continue;
						//////  or vice-versa		
						//if(pos==0 && words[m][0]>ck[k])
							//break;
