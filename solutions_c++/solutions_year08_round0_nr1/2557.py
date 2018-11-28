#include<iostream>
#include<iterator>
#include<algorithm>
#include<string>
#include<numeric>
#include<vector>
#include<deque>
#include<sstream>

using namespace std;




typedef vector<int> vi;
typedef vector<int>::iterator viit;	
typedef vector<int>::reverse_iterator rviit;		


typedef vector<char> vc;
typedef vector<char>::iterator vcit;	
typedef vector<char>::reverse_iterator rvcit;		

typedef vector<string> vs;
typedef vector<string>::iterator vsit;	
typedef vector<string>::reverse_iterator rvsit;		

ostream_iterator<int> oi(cout, " ");
ostream_iterator<char> oc(cout, " ");
ostream_iterator<string> os(cout, " ");


#define RR 5
#define CC 5
#define R 5
#define BS 256
 
#define sp " "
#define nl <<endl
#define ot cout<<
#define nll cout<<endl;

#define IMRAN
#undef IMRAN
void main()
{	
  
  	int ar[R]={0};
	int ar2[RR][CC]={0};
	stringstream ss;
	int i,j,k,res,a,b;
	char buf[BS]="";
	
//	while(cin.getline(buf,256))
//	{
		memset(buf,0,256);
		ss.clear();
		cin.getline(buf,256);
		ss<<buf;
		ss>>a;
#ifdef IMRAN
		ot "test cases" <<sp<<a<<endl;
#endif
		for(k=0;k<a;k++)
		{
			memset(buf,0,256);
			ss.clear();
			cin.getline(buf,256);
			ss<<buf;
			
			int s=0;
			ss>>s;
#ifdef IMRAN			
			ot "sengines" <<sp<<s<<endl;
#endif
			vs sarr;
			for(i=0;i<s;i++)
			{
				memset(buf,0,256);
				ss.clear();
				cin.getline(buf,256);
				ss<<buf;
				string str="",str1="";
				while(ss>>str)
				{
					str1+=str;
					str1+=" ";
				}
				sarr.push_back(str1);
			}
#ifdef IMRAN			
			ot "sengines name" <<endl;
			copy(sarr.begin(),sarr.end(),os);
#endif			
			memset(buf,0,256);
			ss.clear();
			cin.getline(buf,256);
			ss<<buf;
			
			int q=0;
			ss>>q;
#ifdef IMRAN			
			nll
			ot "queries" <<sp<<q<<endl;
#endif
			vs qarr;
			for(i=0;i<q;i++)
			{
				memset(buf,0,256);
				ss.clear();
				cin.getline(buf,256);
				ss<<buf;
				string str="",str1="";
				while(ss>>str)
				{
					str1+=str;
					str1+=" ";
				}
				qarr.push_back(str1);
			}
#ifdef IMRAN			
			ot "queries" <<endl;
			copy(qarr.begin(),qarr.end(),os);
			nll
#endif
			vi t(s);
			const int max=9999;
			fill(t.begin(),t.end(),max);
			int count=0;
			int m=0;
			bool ism=false;
			int start=0;
			for(int j=start;j<q;j++)
			{
						
				int index=-1;
				for(int p=0;p<s;p++)
				{
				//	cout<<qarr[j]<<sp<<sp<<sarr[p]<<endl;
					if (qarr[j] == sarr[p])
					{
						index=p;
						break;
					}
				}
				if (index==-1)
				{
					ot "index-1" nl;
					break;
				}
				ism=false;
				if (t[index]==max)
				{
					t[index]=j;
					m++;
					if (m==s)
					{
						viit it=max_element(t.begin(),t.end());
						if (*it == max)
						{
							break;
						}
						else
						{
							count++;
							m=0;
							ism=true;
							start=*it;
							fill(t.begin(),t.end(),max);
							j--;
						}
					}
				}


			}
#ifdef IMRAN
			cout<<"=============="<<endl;
#endif
			cout<<"Case #"<<k+1<<":"<<sp;
			if (ism)cout<<--count;
			else cout<<count;
			nll
#ifdef IMRAN	
			nll
			nll
#endif
		}
		
		
		memset(buf,0,256);
		ss.clear();
//	}	


}
