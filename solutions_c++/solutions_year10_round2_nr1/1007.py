#include<iostream>
#include<string>
#include<vector>
using namespace std;

const int N=10020;

class node
{
public:
	string input;
	vector<int> son;
};

vector<node> array;

int Insert(vector<string> input);
vector<string> Convert(string input);

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w+",stdout);	
	int i,j,k,cas,T;
	int dict,create;
	int result,ans;
	string t;
	vector<string> input;
	cin>>T;
	for(cas=1;cas<=T;cas++)
	{
		ans=0;
		array.clear();
		cin>>dict>>create;
		class node root;
		root.input="father";
		array.push_back(root);
		for(i=1;i<=dict;i++)
		{
			cin>>t;
			input=Convert(t);
			result=Insert(input);
		}
		for(i=1;i<=create;i++)
		{
			cin>>t;
			input=Convert(t);
			result=Insert(input);
			ans+=result;
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}

int Insert(vector<string> input)
{
	int i,j;
	int size=input.size(),length;
	int now=0,step=0,child;
	for(i=0;i<size;i++)
	{
		length=array[now].son.size();
		for(j=0;j<length;j++)
		{
			child=array[now].son[j];
			if(input[i]==array[child].input)
			{
				now=child;
				break;
			}
		}
		if(j==length)
		{
			class node t;
			t.input=input[i];
			array.push_back(t);
			child=array.size()-1;
			array[now].son.push_back(child);
			now=child;
			step++;
		}
	}
	return step;
}

vector<string> Convert(string input)
{
	string temp;
	vector<string> value;
	int size=input.size(),i,j;
	for(i=1;i<size;)
	{
		temp.erase();
		j=i;
		while(input[j]!='/'&&j<size)
		{
			temp+=input[j];
			j++;
		}
		value.push_back(temp);
		i=j+1;
	}
	//for(i=0;i<value.size();i++)
	//	cout<<value[i]<<endl;
	return value;
}
