#include<iostream>
#include<string>
#include<vector>
#include<map>

using namespace std;

int T,N,M;

int main()
{
	int i,j,k,p1,p2;
	long res;
	bool flag;
	string str,tmp;
	vector<string> dic;

	cin>>T;
	for(i=0;i<T;i++){
		cin>>N>>M;
		dic.clear();
		for(j=0;j<N;j++){
			cin>>str;
			dic.push_back(str);
			//cout<<str<<endl;
		}
		res=0;
		for(j=0;j<M;j++){
			cin>>str;
			p1=0;p2=1; 
			while(p2<str.size()){
				while(str[p2]!='/'&&p2<str.size()){ 
					p2++;
				}
				tmp=str.substr(0,p2);
				p2+=1;
				flag=true;
				for(k=0;k<dic.size();k++){
					if(tmp==dic[k]){
						flag=false;
						break;
					}
				}
				if(flag){ 
					dic.push_back(tmp); 
					res+=1;
				}
				//cout<<tmp<<" "<<dic.size()<<endl;
			}
		}
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}

	return 0;
}