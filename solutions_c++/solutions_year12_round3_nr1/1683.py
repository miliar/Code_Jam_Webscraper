#include <cstdio>
#include <vector>
#include <set>
using namespace std;

void degui(vector< vector<int> > &vec,int index,vector<int> &result)
{
	result.push_back(index+1);
	if ((vec[index]).size() ==0)
	{
		/*if (result[0] == index+1)
		{
			;
		}*/
		return;
	}
	int size = vec[index].size();
	for (int i = 0; i < size; i++)
	{
		int tmp = vec[index][i];
		degui(vec,tmp-1,result);
	}
	
}

int main()
{
	int tc; scanf("%d",&tc);
	for (int tci = 0;tci < tc;tci++)
	{
		int n; scanf("%d",&n);
		vector<vector<int> > arr(n);
		vector<int> out(n);
		vector<int> in(n);
		for(int i=0; i < n;i++)
		{
			int index;scanf("%d",&index);
			out[i] = index;
			vector<int> tmp;
			int itmp = 0;
			while (index!=0)
			{
				scanf("%d",&itmp);
				tmp.push_back(itmp);
				index--;
			}
			arr[i] = tmp;
		}
		vector<int>::iterator iter = out.begin(); 
		for (;iter != out.end();iter++)
		{
			if (*iter >1)
				break;
		}
		if (iter == out.end())
		{
			printf("Case #%d: No\n",tci+1);
			continue;
		}
		int die;
		for (die = 0; die < n;die++)
		{
			vector<int> result;
			
			degui(arr,die,result);
		    /*if (result.size()>=2)
			{
				
				break;
			}*/
			set<int> st(result.begin(),result.end());
			if (result.size()!=st.size())
			{
				printf("Case #%d: Yes\n",tci+1);
				break;
			}
			
		}
		if (die==n)
			printf("Case #%d: No\n",tci+1);
		//degui(arr,0,result);
		
	}
}