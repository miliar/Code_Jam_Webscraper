#include <fstream>
#include <string>
#include <map>
#include <iostream>
#include <memory>
using namespace std;

int main()
{
	ofstream fout("A-large.out.txt");
	ifstream fin("A-large.in.txt");
	int cases,n;
	int i,j;
	int s;
	map<string , int> hash;
	int qs,q[2000];
	fin>>n;
	string str;
	int c ;
	int k[2000];
	int cnt;
	char ch[2000];
	for(cases = 1; cases <= n ; cases++)
	{
				c = 0;
				hash.clear();
				fin>>s;
				fin.getline(ch,1000);
				for(i=0;i<s;i++)
				{
					fin.getline(ch,2000);
					string tmp(ch);
					
					hash[tmp] = i;
									
				}
				fin>>qs;
				fin.getline(ch,1000);
				
				for(i=0;i<qs;i++)
				{							
					fin.getline(ch,2000);
					string tmp(ch);
					//cout<<tmp<<endl;
					q[i] = hash[tmp];
					
				}
				i=0;
				int now = -1;
				cnt = -1;
				do
				{												
					cnt ++;
					memset(k,0,sizeof(k));
					if(now!=-1)
						k[now] = 1;
					while(i<qs)
					{
						
						if(k[ q[i] ] == 0)
						{
							
							cnt++;
							cout<<q[i]<<" "<<i<<" "<<cnt<<endl;
							k[q[i]] = 1;
						}
						i++;
						//cout<<cnt<<" "<<s<<endl;
						if(cnt==s)
						{
							cout<< i << endl;
							c++;
							cnt = 0;
							now = q[i-1];
							break;
						}
					}
				}
				while(i<qs);
				
				fout<<"Case #"<<cases<<": "<<c<<endl;
				
	}
	
}
