#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

typedef pair<char,char> PCC;

struct Node {
	char a,b,c;
	Node(){}
	Node(char a,char b,char c='a')
		:a(a),b(b),c(c){}
};

vector<Node> comb,oppo;
deque<char> ans;
int T;

bool isComb(char a,int b,char& dstChr)
{
	for(vector<Node>::const_iterator itr=comb.begin() ;itr!=comb.end() ;
		itr++)
	{
		if(itr->a==a && itr->b==b || itr->a==b && itr->b==a)
		{
			dstChr=itr->c;
			return true;
		}
	}
	return false;
}

bool isOppo(char a)
{
	for(int i=0 ;i<(int)ans.size() ;i++)
	{
		char b=ans.at(i);
		for(vector<Node>::const_iterator itr=oppo.begin() ;itr!=oppo.end() ;
			itr++)
		{
			if(itr->a==a && itr->b==b || itr->a==b && itr->b==a)
			{
				return true;
			}
		}
	}
	return false;
}

void process()
{
	int k;cin>>k;
	for(int i=0 ;i<k ;i++)
	{
		char cur;scanf(" %c",&cur);
		if(ans.empty())
			ans.push_back(cur);
		else
		{
			char combChr;
			if(isComb(ans.back(),cur,combChr))
			{
				ans.pop_back();
				ans.push_back(combChr);
			}
			else if(isOppo(cur))
			{
				ans.clear();
			}
			else 
			{
				ans.push_back(cur);
			}
		}
	}

	size_t sz=ans.size();
	//printf("sz = %d\n",sz);
	putchar('[');
	for(int i=0 ;i<(int)ans.size() ;i++)
	{
		printf("%c",ans.at(i));
		if(i!=(int)ans.size()-1)
			printf(", ");
	}
	puts("]");
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int cas=1;

	cin>>T;
	while(T--)
	{
		comb.clear();
		oppo.clear();
		ans.clear();

		int k;cin>>k;
		for(int i=0 ;i<k ;i++)
		{
			char buf[8];
			scanf("%s",buf);
			comb.push_back(Node(buf[0],buf[1],buf[2]));
		}
		cin>>k;
		for(int i=0 ;i<k ;i++)
		{
			char buf[8];
			scanf("%s",buf);
			oppo.push_back(Node(buf[0],buf[1]));
		}
		printf("Case #%d: ",cas++);
		process();
	}
}
