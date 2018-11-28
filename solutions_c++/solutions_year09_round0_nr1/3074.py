#include <iostream>
#include<vector>
#include <string>
#include<cstdio>
using namespace std;
typedef vector<int> vi;

int l,d,n;
char** dict;

class mystruct
{
	public:
		bool** data;
		bool** temp;
		mystruct()
		{
			data=new bool*[d];
			temp=new bool*[d];
			for(int i=0;i<d;i++)
			{
				data[i]=new bool[l+1];
				temp[i] = new bool[l+1];
				data[i][0] = true;
				for(int j=1;j<l+1;j++)
					data[i][j]=false;
			}
		}
		~mystruct()
		{
			for(int i=0;i<d;i++)
				delete [] data[i];
			delete [] data;
		}
		void reinitialize() {
			for(int i=0;i<d;i++) {
				data[i][0] = true;
				for(int j=1;j<l+1;j++)
					data[i][j]=false;
			}
			return;
		}
		void next(string s) {
//			cout<<"next called with "<<s<<endl;
			for(int i=0;i<d;i++)
				for(int j=0;j<l+1;j++)
					temp[i][j]=false;
					
			for(int i=0;i<d;i++) {
				for(int j=0;j<l;j++) {
					if(!data[i][j])
						continue;
					for(int k=0;k<s.length();k++) {
						if(dict[i][j] == s[k]) {
							temp[i][j+1] = true;
						}
					}
				}
			}
			
			for(int i=0;i<d;i++)
				for(int j=0;j<l+1;j++)
					data[i][j]=temp[i][j];
			
			return;
		}
		int countend() {
			int cnt = 0;
			for(int i=0;i<d;i++)
				if(data[i][l])
					cnt++;
			return cnt;
		}
};

int main()
{
	scanf("%d %d %d",&l,&d,&n);
	dict = new char*[d];
	for(int i=0;i<d;i++) {
		dict[i] = new char[l+1];
		scanf("%s",dict[i]);
	}
	mystruct all;
	string s = "";
	char c = getchar();
	c = getchar();
	bool brst = false;
	int caseno = 1;
	bool start = false;
	while((c=getchar())!=EOF) {
//		cout<<c<<endl;
		if((int)c == 13)
			continue;
		if(c == '\n') {
			start = false;
			if(s.length()>0) all.next(s);
			s = "";
			printf("Case #%d: %d\n",caseno,all.countend());
			caseno++;
			all.reinitialize();
			continue;
		}
		else if(c==')') {
			start = true;
			if(s.length()>0)	all.next(s);
			s = "";
			brst = false;
			continue;
		}
		else if(c=='(') {
			start = true;
			brst = true;
			continue;
		}
		else {
			start = true;
			s+=c;
			if(!brst) {
				all.next(s);
				s = "";
			}
			continue;
		}
	}
	if(start) {
		all.next(s);
		printf("Case #%d: %d\n",caseno,all.countend());
	}
	return 0;
}
