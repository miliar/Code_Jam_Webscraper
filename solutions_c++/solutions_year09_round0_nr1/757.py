#include <iostream>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <memory>
#include <sstream>

using namespace std;

struct node
{
	node* ch[26];
	bool isOn;
	node()
	{
		for(int i = 0;i < 26;i++) ch[i] = NULL;
		isOn = false;
	}
};

char str[16],word[16][28];

string input;

int L,D,N,cnt;

void TrInsert(node* root)
{
	int len = strlen(str),cur;
	node* curNode = root;
	for(int i = 0;i < len;i++)
	{
		cur = str[i] - 'a';
		if(curNode->ch[cur] == NULL) curNode->ch[cur] = new node();
		curNode = curNode->ch[cur];
	}
	curNode->isOn = true;
}

void solve(node* root,int h)
{
	int chNum = word[h][0],cur;
	for(int i = 1;i <= chNum;i++)
	{
		cur = word[h][i] - 'a';
		if(root->ch[cur] == NULL) continue;
		if(root->ch[cur]->isOn) {cnt++;continue;}
		solve(root->ch[cur],h +1);
	}
}

int main()
{
//	freopen("D:\\VC project\\ForTest\\Debug\\input2.in","r",stdin);
//	freopen("D:\\VC project\\ForTest\\Debug\\out.txt","w",stdout);
	int i,j,cur;
	node* root = new node();
	cin >> L >> D >> N;
	for(i = 0;i < D;i++)
	{
		scanf("%s",str);
		TrInsert(root);
	}
	for(i = 1;i <= N;i++)
	{
		cin >> input;
		cur = 0;
		for(j = 0;j < L;j++)
		{
			if(input[cur] != '(') word[j][0] = 1,word[j][1] = input[cur],cur++;
			else
			{
				cnt = 0;
				while(input[++cur] != ')')
				{
					cnt++,word[j][cnt] = input[cur];
				}
				word[j][0] = cnt;
				cur++;
			}
		}
		cnt = 0;
		solve(root,0);
		cout << "Case #" << i << ": " << cnt << endl;
	}
	return 0;
}