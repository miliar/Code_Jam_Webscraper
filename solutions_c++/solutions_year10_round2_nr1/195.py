#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

int main(){
	int t,res,n,m;
	char buff[200];
	string st;
	vector<string> created;

	scanf("%d",&t);
	for (int tc=1;tc<=t;tc++){
		created.clear();
		res=0;
		scanf("%d %d",&n,&m);
		for (int i=0;i<n;i++){
			scanf("%s",buff);
			st=string(buff);
			st+="/";
			created.push_back(st);
		}
		for (int i=0;i<m;i++){
			int tres=0;
			scanf("%s",buff);
			st=string(buff);
			st+="/";
			for (int k=1;k<(int)st.length();k++)
				if (st[k]=='/') tres++;
			for (int j=0;j<(int)created.size();j++){
				int ttres=0;
				int k=1,kk=min(st.length(),created[j].length());
				for (;k<kk;k++)
					if (st[k]!=created[j][k]) break;
				for (;k<(int)st.length();k++)
					if (st[k]=='/') ttres++;
				if (ttres<tres) tres=ttres;
			}
			res+=tres;
			created.push_back(st);
		}
		printf("Case #%d: %d\n",tc,res);
	}
	return 0;
}