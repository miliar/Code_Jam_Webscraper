#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;



int main()
{
	int L,D,N;
	cin>>L>>D>>N;

	vector<string> di;

    for(int i=0;i<D;i++)
	{
		string s;
		cin>>s;
		di.push_back(s);
	}

	for(int i=1;i<=N;i++)
	{
		
		string target;
		cin>>target;
		int k=0;
		int size = target.size();

		/*
		stack<string> v_la;
		v_la.push(target);
		int res = 0;
		while(!v_la.empty())
		{
			string t = v_la.top();
			v_la.pop();
			int pos1 = t.find('(');
			
			if(pos1!=-1){
				int pos2 = t.find(')');
				string str = t.substr(0,pos1);
				int size = t.size();
				for(int q=pos1+1;q<pos2;q++){
					string str1 = str;
					str1.push_back(t[q]);
					for(int q2=pos2+1;q2<size;q2++)
						str1.push_back(t[q2]);
					v_la.push(str1);
				}
			}
			else{
				if(find(di.begin(),di.end(),t) != di.end())
					res++;
			}
		}
		*/

		string* la = new string[L];
		for(int j=0;j<L;j++)
			la[j].clear();

		for(int j=0;j<size;j++)
		{
			if((target[j]!='(')&&(target[j]!=')'))
				la[k++].push_back(target[j]);
			else
			{
				if(target[j]=='(')
				{
					j++;
					while(target[j]!=')')
					{
						la[k].push_back(target[j]);
						j++;
					}
					k++;
				}
			}
		}
		int res=0;
		for(int j=0;j<D;j++)
		{
			string str = di[j];
			int flag = 0;
			for(int l=0;l<L;l++)
			{
				if(la[l].find(str[l]) == string::npos)
				{
					flag = 1;
					break;
				}
				
			}
			if(flag == 0)
				res++;
		}
		
		cout<<"Case #"<<i<<": "<<res<<endl;

	}


	//system("pause");
	return 1;
}