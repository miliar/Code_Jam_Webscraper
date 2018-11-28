#include <cstdio>
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
struct Node 
{
//	int nvalue;
	Node * node[26];
	Node()
	{
		//nvalue = 0;
		memset(node,0,sizeof(node));
	}
};
vector<string> g_vec_str;
int nCount = 0 ;
int L =0 ,D = 0 ,N = 0;
void dfs(int n, Node * pCurrent)
{
	unsigned int i = 0;
	if (n == L)
	{
		nCount ++;
		return;
	}
	for (i = 0; i < g_vec_str[n].size() ;++i)
	{
		if (NULL != pCurrent->node[g_vec_str[n][i] - 'a'])
		{
			dfs(n+1,pCurrent->node[g_vec_str[n][i] - 'a']);
		}
	}
}

int main(int argc , char ** argv)
{	
// 	freopen("in.txt","r",stdin);
// 	freopen("out.txt","w",stdout);
	scanf("%d %d %d",&L,&D,&N);
	unsigned int i=0,j=0;
	//create
	string strTemp = "";
	Node * root = new Node();
	//root ->nvalue = 1;
	for (i = 0 ; i < D ; ++i)
	{
		cin>>strTemp;
		Node * pCurrent = root;
		for (j = 0 ; j < strTemp.size() ; ++j)
		{
			if (NULL == pCurrent->node[strTemp[j] - 'a'])
			{
				pCurrent->node[strTemp[j] - 'a'] = new Node();
			}			
			pCurrent = pCurrent->node[strTemp[j] - 'a'];
		//	pCurrent->nvalue = 1;
		}
	}
	//process
	for (i = 1; i <= N; ++i)
	{
		cin>>strTemp;
		nCount = 0;
		bool bstart = false;
		Node * pCurrent = root;
		g_vec_str.clear();
		nCount = 0 ;
		g_vec_str.resize(L);
		int nPos = 0;
		for (j = 0 ; j < strTemp.size() ; ++j)
		{
			if (strTemp[j] == '(')
			{
				bstart = true;
			}
			else if (strTemp[j] == ')')
			{
				bstart = false;
			}
			else
			{
				g_vec_str[nPos]+=strTemp[j];				
			}
			if (bstart == false)
			{
				nPos ++;
			}
		}
		dfs(0,root);
		printf("Case #%d: %d\n",i,nCount);
	}
	return 0;
}