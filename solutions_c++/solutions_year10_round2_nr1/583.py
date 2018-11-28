#include<iostream>
#include<map>
#include<string>
using namespace std;
map<string,int>mm;
map<string,int>::iterator aa;
int main(){
	freopen("A-large2.in","r",stdin);
	freopen("a-large2.out","w",stdout);
	int casenum;
	//scanf("%d",&casenum);
	cin>>casenum;
	int casei;
	for(casei=0;casei<casenum;casei++){
		mm.clear();
		int n,m,i,j;
		cin>>n>>m;
		string str;
		string str1;
		mm["/root"]=1;
		for(i=0;i<n;i++){
			cin>>str;
			
			for(j=0;j<str.size();j++){
				if(str[j]=='/'&&j){
					str1=str.substr(0,j);
					if(mm[str1]==0){
						mm[str1]=1;
					}
				}
				
			}
			mm[str]=1;
		}
/*
		for(aa=mm.begin();aa!=mm.end();aa++){
			cout<<aa->first<<endl;
		}
*/
		int cnt=0;
		for(i=0;i<m;i++){
			cin>>str;
			for(j=0;j<str.size();j++){
				if(str[j]=='/'&&j){
					str1=str.substr(0,j);
					if(mm[str1]==1){
	
						continue;
					}
					else{
						mm[str1]=1;
						cnt++;
					}
				}
				
			}
			if(mm[str]!=1){
				mm[str]=1;
				cnt++;
			}

		}
		//printf("Case #%d: %d\n",casei+1,cnt);
		cout<<"Case #"<<casei+1<<": "<<cnt<<endl;
	}
 //   system("pause");
    return 0;
}
