#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int x=1,l,n,d,i,k,h;
	char *str = new char[1024]; 
	
	vector<string> dic;
	vector<int> index;
	vector<int>::iterator it,end;
		
	string s;

	scanf("%d %d %d ",&l,&d,&n);
	for(i=0;i<d;i++){
		scanf("%s ",str);
		s=str;

		dic.push_back(s);
	}
	//sort(dic.begin(),dic.end());
	

	for(i=0;i<n;i++){
		index.clear();
		for(h=0;h<d;h++){
			index.push_back(0);
		}

		scanf("%s ",str);
		int size = strlen(str);
		int pos=0;
		int cont=0, contVariables=0, contFijo=0;
		bool flag=false;
		
		for(int j=0; j<size; j++){
			if(str[j]=='('){
				flag = true;
				continue;
			}else if(str[j]==')'){
				flag = false;
				pos++;
				continue;
			}
			
			for( h=0;h<d;h++){
				if(dic[h][pos]==str[j]){
					index[h]++;
					if(index[h]==l){
						cont++;
					}
				}
			}

			if(!flag){
				pos++;
			}
		}
		
		printf("Case #%d: %d\n",x++,cont);
	}

	return 0;
}
