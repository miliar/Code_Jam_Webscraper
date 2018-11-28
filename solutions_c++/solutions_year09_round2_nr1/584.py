#include<iostream>
#include<string>
#include<vector>
using namespace std;

struct DTree
{
	double weight;
	bool end;
	string feature;
	DTree* left;
	DTree* right;
};

string desc;

void parse(DTree* DT, int left,int right)
{
	/*
	cout<<left<<" "<<right<<endl;
	for(int i=left;i<=right;i++)
		cout<<desc[i];
	cout<<endl;
	*/
	int st,en;
	for(int i=left;i<=right;i++)
		if((desc[i]>='0'&&desc[i]<='9')||desc[i]=='.')
		{
			st=i;
			break;
		}
	for(int i=st;i<=right;i++)
		if(desc[i]==' '||desc[i]=='\n'||desc[i]==')')
		{
			en=i-1;
			break;
		}
	string tt="";
	for(int i=st;i<=en;i++)
		tt+=(char)desc[i];
	sscanf(tt.c_str(),"%lf",&DT->weight);
	DT->end=true;
	for(int i=en+1;i<=right;i++)
		if(desc[i]>='a'&&desc[i]<='z')
		{
			st=i;
			DT->end=false;
			break;
		}
	if(DT->end)
		return;
	for(int i=st;i<=right;i++)
		if(desc[i]==' '||desc[i]=='\n')
		{
			en=i-1;
			break;
		}
	DT->feature="";
	for(int i=st;i<=en;i++)
		DT->feature+=desc[i];
	DT->left=new DTree();
	for(int i=en+1;i<=right;i++)
		if(desc[i]=='(')
		{
			st=i;
			break;
		}
	int cnt=0;
	for(int i=st;i<=right;i++)
	{
		if(desc[i]=='(')
			cnt++;
		else if(desc[i]==')')
			cnt--;
		if(cnt==0)
		{
			en=i;
			break;
		}
	}
	parse(DT->left,st,en);
	DT->right=new DTree();
	for(int i=en+1;i<=right;i++)
		if(desc[i]=='(')
		{
			st=i;
			break;
		}
	for(int i=right-1;i>=left;i--)
		if(desc[i]==')')
		{
			en=i;
			break;
		}
	parse(DT->right,st,en);
}

vector<string> animal;
double ans;

void go(DTree* DT,double p)
{
	p*=DT->weight;
	if(!DT->end)
	{
		bool flag=false;
		for(int i=0;i<(int)animal.size();i++)
			if(animal[i]==DT->feature)
			{
				flag=true;
				go(DT->left,p);
			}
		if(flag) go(DT->left,p);
		else go(DT->right,p);
	}
	else
		ans=p;
}

int main()
{
	int T,no=0;
	cin>>T;
	while(T--)
	{
		printf("Case #%d:\n",++no);
		desc="";
		int N;
		cin>>N;
		getchar();
		string tmp;
		for(int i=0;i<N;i++)
		{
			getline(cin,tmp);
			desc+=tmp;
		}
		DTree* T = new DTree();
		parse(T, 0,(int)desc.size()-1);
		int nAnimals;
		cin>>nAnimals;
		for(int i=0;i<nAnimals;i++)
		{
			animal.clear();
			string name;
			cin>>name;
			int nFeatures;
			cin>>nFeatures;
			for(int j=0;j<nFeatures;j++)
			{
				string fea;
				cin>>fea;
				animal.push_back(fea);
			}
			go(T,1);
			printf("%.7lf\n",ans);
		}
	}
	return 0;
}