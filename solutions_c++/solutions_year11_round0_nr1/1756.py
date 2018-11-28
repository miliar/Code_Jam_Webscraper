#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<numeric>
#include<cmath>
#include<cstdio>
#include<utility>
using namespace std;
typedef long long ll;
#define pi acos(-1.0)
#define INF 1000000007
#define LINF 1000000000000000000LL
int gcd(int a,int b){return b==0?a:gcd(b,a%b);}
string I_S(ll n){stringstream s;s<<n;return s.str();}
ll S_I(string s) {ll ans;stringstream n(s);n>>ans;return ans;}
int num(int i){int r=0;while(i){r++;i&=i-1;}return r;}
int dx[]={-1,1,0,0};
int dy[]={0,0,-1,1};
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}
int main()
{
    ifstream fin("A-large.in");
	ofstream fou("output.txt");
	int T,N;
	fin>>T;
	for(int I=0;I<T;I++)
	{
        fin>>N;
		vector<pair<char,int> > sq;
		char A;int B;
        for(int i=0;i<N;i++)
		{
			fin>>A>>B;
			sq.push_back(make_pair(A,B));
		}
		int o=1,b=1,p=0,t=0;
		int next[100];
		memset(next,-1,sizeof(next));
        for(int i=0;i<N;i++)
		{
			for(int j=i+1;j<N;j++)
				if(sq[j].first!=sq[i].first) {next[i]=j;break;}
		}
		while(p+1<=N)
		{
            t++;
			if(sq[p].first=='O')
			{
				if(next[p]>=0)
				{
				if(b<sq[next[p]].second) b++;
				else if(b>sq[next[p]].second) b--;
				}
				if(o<sq[p].second) o++;
				else if(o>sq[p].second) o--;
				else p++;
				continue;
			}
			else if(sq[p].first=='B')
			{
				if(next[p]>=0)
				{
				if(o<sq[next[p]].second) o++;
				else if(o>sq[next[p]].second) o--;
				}
				if(b<sq[p].second) b++;
				else if(b>sq[p].second) b--;
				else p++;
			}
		}
		fou<<"Case #"<<I+1<<": "<<t<<endl;
	}
}
//int main()
//{
//    ifstream fin("A-large-practice.in(1)");
//	ofstream fou("output.txt");
//	int N,S;
//	fin>>N;
//	for(int I=0;I<N;I++)
//	{
//		fin>>S;
//		vector<string> segs;
//		vector<int> blue,red;
//		string temp;
//		for(int j=0;j<S;j++)
//		{
//			fin>>temp;
//			if(temp[temp.size()-1]=='B') blue.push_back((int)S_I(temp.substr(0,temp.size()-1)));
//			else if(temp[temp.size()-1]=='R') red.push_back((int)S_I(temp.substr(0,temp.size()-1)));
//			else
//			{
//				int jjj=0;
//				jjj++;
//			}
//		}
//		sort(blue.begin(),blue.end(),greater<int>());
//        sort(red.begin(),red.end(),greater<int>());
//		if(blue.size()==0||red.size()==0)  {fou<<"Case #"<<I+1<<": "<<0<<endl;continue;}
//		int n=S;
//		int p=1,i=0,j=0,ans=0,c=0;
//		while(n--)
//		{
//            if(p==1) 
//			{
//				if(i<blue.size()) {ans+=blue[i];p=-p;i++;c++;continue;}
//				else {fou<<"Case #"<<I+1<<": "<<ans-c<<endl; break;}
//			}
//			else if(p==-1)
//			{
//				if(j<red.size()) {ans+=red[j];p=-p;j++;c++;continue;}
//				else {fou<<"Case #"<<I+1<<": "<<ans-c-blue[i-1]+1<<endl; break;}
//			}
//		}
//		if(n<0) 
//		{
//			if(p==1) fou<<"Case #"<<I+1<<": "<<ans-c<<endl;
//			else fou<<"Case #"<<I+1<<": "<<ans-c-blue[i-1]+1<<endl;
//		}
//	}
//}

