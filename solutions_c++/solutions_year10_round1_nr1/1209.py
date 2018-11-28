#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#define LL long long
using namespace std;
void rotate(vector<string> &a)
{
	vector<string>b(a.size());
	for(int i=0;i<a.size();i++)
		for(int j=a.size()-1;j>=0;j--)
			b[i]+=a[j][i];
	a=b;
		
}
void gravity(vector<string> &a)
{
	vector<string>b(a.size());
	string temp="";
	for(int i=0;i<a.size();i++)
	{
		temp="";
		for(int j=a.size()-1;j>=0;j--)
		{
			if(a[i][j]!='.') b[i]=a[i][j]+b[i];
			else temp+='.';
		}
		b[i]=temp+b[i];
	}
	a=b;
}
bool check(int i, int j, vector<string> &a)
{
	if(i>=0 && i<a.size() && j>=0 && j<a.size())return true;
	return false;
}
bool countT(int i,int j,vector<string> &a,char f,int k_)
{
	int di[]={-1,-1,-1,+0,+1,+1,-1,0};
	int dj[]={-1,+0,+1,+1,+1,+0,-1,-1};
	int spos[8]={0};
	for(int p=0;p<a.size();p++)
		for(int k=0;k<8;k++)
		{
			int x=i+p*di[k];
			int y=j+p*dj[k];
			if(check(x,y,a))
			{
				if(a[x][y]==f)
				{
					spos[k]++;
					if(spos[k]>=k_) 
						return true;
				}
				else spos[k]=0;
			}
		}
	return false;
}
bool count(vector<string> &a,char f,int k)
{
	for(int i=0;i<a.size();i++)
		if(countT(i,0,a,f,k)) 
			return true;
	for(int j=0;j<a.size();j++)
		if(countT(0,j,a,f,k)) 
			return true;
	return false;
}
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T=0;
	cin>>T;
	for(LL ti=1;ti<=T;ti++)
	{
		int n,k;
		cin>>n>>k;
		vector<string> a(n);
		for(int i=0;i<n;i++)
			cin>>a[i];
		gravity(a);
		rotate(a);
		cout<<"Case #"<<ti<<": ";
		bool Red=count(a,'R',k);
		bool Blue=count(a,'B',k);
		if(Red && Blue) cout<<"Both";
		else if(!Red && !Blue) cout<<"Neither";
		else if(Red) cout<<"Red";
		else cout<<"Blue";
		cout<<endl;
	}
	cout.close();
	cin.close();
	return 0;
}