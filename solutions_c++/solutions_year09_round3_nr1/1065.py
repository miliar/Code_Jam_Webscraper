#include<vector>
#include<map>
#include<set>
#include<queue>
#include<string>
#include<algorithm>
#include<cmath>
#include<fstream>
#include<iostream>
using namespace std;
typedef long long ll;

int main()
{
    ifstream  in("A-small-attempt6.in.txt",ios::in);
    ofstream  out("output.txt");
    int T,i=0;
	in>>T;
	string tp;
    while(i++<T)
	{
        in>>tp;
		int n=tp.size();
		map<char,int> num;
		for(int j=0;j<n;j++)
			if(num.find(tp[j])==num.end())
				num[tp[j]]=-1;
		int base=num.size();
		if(base==1&&n==1) {out<<"Case #"<<i<<": "<<1<<endl; continue;}
		if(base==1&&n>1) 
		{
			int res=0,j=0;
			while(j<n)
			{res+=pow(1.0*2,j);j++;}
			out<<"Case #"<<i<<": "<<res<<endl;continue;
		}
		int r=0,t=1,k=1;
		for(int j=0;j<n;j++)
		{           
			if(j==0)
			{
				r+=t*pow((double)base,(double)(n-k));
				num[tp[j]]=t;
				t=0;
			}
			else 
			{
				if(num[tp[j]]>=0)
					r+=num[tp[j]]*pow((double)base,(double)(n-k));
				else 
				{
					r+=t*pow((double)base,(double)(n-k));
					num[tp[j]]=t;
					if(t+1<base)
						t++;
					if(t==1) t++;
				}
			}
			k++;
		}
		out<<"Case #"<<i<<": "<<r<<endl;

	}
}



//int main()
//{
//    ifstream  in("input.txt",ios::in);
//    ofstream  out("output.txt");
//    int N,i=0,L,A;
//    while(i++<N)
//	{
//
//	}
//}
//
//
//
//int main()
//{
//    ifstream  in("input.txt",ios::in);
//    ofstream  out("output.txt");
//    int N,i=0,L,A;
//    while(i++<N)
//	{
//
//	}
//}