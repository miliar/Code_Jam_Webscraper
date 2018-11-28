#include <iostream>
#include <vector>
using namespace std;
int L,D,N,res;
string DCh[5001];
string NCh[501];
char dest[20];
int f(int index, vector<string>& strArr,vector<int> matchArr)
{
	if(index == strArr.size()-1)	
	{
		for(int j=0;j<strArr[index].size();++j)
		{
			dest[index] = strArr[index][j];
			for(int k=0;k<matchArr.size();++k)
			{
				if(DCh[matchArr[k]].compare(dest)==0)
					return 1;
			}
			
		}
		return 0;
	}
	else if(index < strArr.size())
	{
		int res = 0;
		for(int j=0;j<strArr[index].size();++j)
		{
			dest[index] = strArr[index][j];
			vector<int>_matchArr;
			for(int k=0;k<matchArr.size();++k)
			{
				if(DCh[matchArr[k]][index] == dest[index])
				{
					_matchArr.push_back(matchArr[k]);
				}
			}
			if(_matchArr.size()>0)
			{
				res += f(index+1,strArr,_matchArr);
			}
		}
		return res;
	}
	return -1;
}
int main(int argc, char *argv[])
{
	//FILE* ifp = freopen("input.in","r",stdin);
	FILE* ifp = freopen("A-large.in","r",stdin);
	FILE* ofp = freopen("A-large.out","w",stdout);
	
	
	cin>>L>>D>>N;
	vector<int> matchArr;
	for(int i=0;i<D;++i)
	{
		cin>>DCh[i];
		matchArr.push_back(i);
	}
		
	for(int i=0;i<N;++i)
	{
		vector<string> strArr;
		cin>>NCh[i];
		for(int j=0;j<NCh[i].size();++j)
		{
			if(NCh[i][j] == '(')
			{				
				string str;
				for(j+=1;j<NCh[i].size()&&NCh[i][j]!=')';++j)
					str += NCh[i][j];		
				strArr.push_back(str);
			}
			else
			{
				string str;
				str += NCh[i][j];		
				strArr.push_back(str);
			}			
		}
		memset(dest,0,sizeof(dest));
		int res = 0;
		
		//res = f(0,strArr,matchArr);
		if(strArr.size() == L)
		{
			for(int i=0;i<D;++i)
			{
				bool tf = true;
				for(int j=0;j<L;++j)
				{
					if(strArr[j].find(DCh[i][j]) == string::npos)
					{
						tf = false;
						break;
					}
				}
				if(tf)++res;
			}
		}
		printf("Case #%d: %d\n",i+1,res);		
	}
	return 0;
}
