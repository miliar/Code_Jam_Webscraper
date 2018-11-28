#include<iostream>
#include<map>
#include<string>
using namespace std;
int main()
{
	int t,tbc;
	cin>>t;
	tbc = t;
	while(t--)
	{
		map<string,char> mp;
		int flag[26]={0};
		string flag_pair[26];
		for(int i=0;i<26;i++)
			flag_pair[i] = "";

		int c;
		cin>>c;
		for(int i=0;i<c;i++)
		{
			char inp[4],ch,temp;
			cin>>inp;
			ch = inp[2];
			inp[2] = '\0';
			mp[inp] = ch;
	
			temp = inp[0];
			inp[0] = inp[1];
			inp[1] = temp;
			mp[inp] = ch;
		}	
	
		int d;
		cin>>d;
		for(int i=0;i<d;i++)
		{
			char inp[3];
			cin>>inp;
			flag[inp[0]-'A'] = flag[inp[1]-'A'] = 1;
			flag_pair[inp[0]-'A'] += inp[1];
			flag_pair[inp[1]-'A'] += inp[0];
		}
		
		int n;
		cin>>n;
		char arr[n+1],res[n+1];
		int ind = -1;
		cin>>arr;
	
		if(flag[arr[0]-'A']) flag[arr[0]-'A']++;
		res[++ind] = arr[0];

		res[ind+1] = '\0';
		for(int i=1;i<n;i++)
		{
			//cout<<res<<" ";
			char set[3] = {arr[i-1],arr[i],'\0'};
			if(res[0]=='\0')
			{
				res[ind] = arr[i];
				res[ind+1] = '\0';
				if(flag[arr[i]-'A']) flag[arr[i]-'A']++;
			}
			else if(mp[set]!='\0')
			{
				res[ind] = arr[i] = mp[set];
				res[ind+1] = '\0';

				//Reduce prev
				if(flag[arr[i-1]-'A']>1) flag[arr[i-1]-'A']--;
			}	
			else if(flag[arr[i]-'A'])
			{
				bool fl = false;
				for(int x=0;flag_pair[arr[i]-'A'][x]!='\0';x++)
					if(flag[flag_pair[arr[i]-'A'][x]-'A']>1)
					{
						fl = true;
						break;
					}

				if(fl)
				{
					ind = 0;
					res[ind] = '\0';
					for(int x=0;x<26;x++)
						if(flag[x])
							flag[x] = 1;
				}
				else
				{
					flag[arr[i]-'A']++;
					res[++ind] = arr[i];
					res[ind+1] = '\0';
				}
			}
			else
			{
				res[++ind] = arr[i];
				res[ind+1] = '\0';
			}
			//cout<<res<<endl;
		}
		
		cout<<"Case #"<<tbc-t<<": [";
		if(res[0]!='\0')
		{
			cout<<res[0];
			for(int i=1;res[i]!='\0';i++)
			{
				cout<<", "<<res[i];
			}
		}
		cout<<"]"<<endl;
	}
	return 0;
}
