
#include<string>
#include<iostream>
#include<sstream>
#include<set>
using namespace std;
#define ni(x) scanf("%d\n",&x)
//#define assert(x) if(!(x)){puts("err"); exit(0)};

char tmp[10240];

struct TNode
{
	int left,right;
	string feature;
	double weight;
	void out()
	{
		cout<<feature<<": "<<weight<<" "<<left<<" "<<right<<endl; 
	}
};
TNode tree [10240];
int top;
int build_tree(int cp)//char pos, tree pos
{
	assert(tmp[cp++] == '(');
	//while(tmp[cp]==' ') cp++;
	int start = cp;
	while(isdigit(tmp[cp]) || tmp[cp]=='.') cp++;
	istringstream ss(string(tmp+start, tmp+cp));
	int now = top;
	top ++;
	ss>>tree[now].weight;
	
	//while(tmp[cp]==' ') cp++;
	if(tmp[cp] == ')')
	{
		tree[now].left = -1;
		tree[now].right = -1;
		//tree[now].out();
		return cp+1;
	}
	start = cp;
	while(islower(tmp[cp]) ) cp++;
	
	tree[now].feature = string(tmp+start, tmp+cp);
	//while(tmp[cp]==' ') cp++;
	tree[now].left = top;
	cp = build_tree(cp);
	tree[now].right = top;
	cp = build_tree(cp);
	//while(tmp[cp]==' ') cp++;
	//tree[now].out();
	assert(tmp[cp++] == ')');
	return cp;
}

set<string> fs;

double cute(double p, int idx)
{
	TNode & tn = tree[idx];
	if(tn.left == -1)
	{
		//tn.out();
		//cout<<"#"<<p<<endl;
		return p*tn.weight;
	}
	if(fs.find(tn.feature) != fs.end())
		return cute(p*tn.weight, tn.left);
	return cute(p*tn.weight, tn.right);
}

int main()
{
	
    int nks;
	ni(nks);
    //
    for(int k=1;k<=nks;k++)
    {
    	int lines;
		ni(lines);
    	char * p = tmp;
    	for(int l=lines;l!=0;l--)
    	{
			gets(tmp+10000);
			char * q = tmp+10000;
			for(; *q; ++q)
				if((*q) != ' ') 
				{
					*p = *q;
					//putchar(*p);
					++p;
				}
		}
		
		//cout<<tmp<<endl;
		top = 0;
		build_tree(0);
		int animals; 
		ni(animals);
		printf("Case #%d:\n", k);
		for(int i=0;i<animals;++i)
		{
			int nfs;
			scanf("%s",tmp);
			scanf("%d",&nfs);
			
			fs.clear();
			for(int f=0;f<nfs;++f)
			{
				scanf("%s",tmp);
				fs.insert(string(tmp));
			}
			printf("%.7f\n", cute(1.0, 0));
			
		}
		
	}
}
