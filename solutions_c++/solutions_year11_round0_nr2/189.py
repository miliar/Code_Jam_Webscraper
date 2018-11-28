#include<cstdio>
#include<algorithm>
#include<vector>
#define L 100

using namespace std;

int T,i,c,d,j,k,n;
int I=0;
char ch[L][4],en[L][4];
vector<char> list;
char cha,last,insert,a,b;

int main(){
	scanf("%d",&T);
	while (T--){
		scanf("%d",&c);
		for (i=0;i<c;++i){
			scanf(" %s",ch[i]);
			if (ch[i][0]>ch[i][1])
				swap(ch[i][0],ch[i][1]);
		}
		scanf("%d",&d);
		for (i=0;i<d;++i){
			scanf(" %s",en[i]);
			if (en[i][0]>en[i][1])
				swap(en[i][0],en[i][1]);
		}
		scanf("%d",&n);
		last=-1;
		list.clear();
		for (i=0;i<n;++i){
			scanf(" %c",&cha);
				a=cha;
				b=last;
				insert = -1;
				if (a>b) swap(a,b);
				for (j=0;j<c;++j)
					if (ch[j][0]==a && ch[j][1]==b){
						insert=ch[j][2];
						break;
					}
				if (insert!=-1){
					list.push_back(insert);
					last=-1;
					continue;
				}
				a=cha;
				bool bt=true;
				for (j=0;bt && j<d;++j)
					if (en[j][0]==a || en[j][1]==a){
						for (k=0;bt && k<list.size();++k)
							if ((en[j][0]==list[k]&&en[j][1]==a) || (en[j][0]==a && en[j][1]==list[k])){
								list.clear();
								last=-1;
								bt=false;
								break;
							}
						if (en[j][0]==last&&en[j][1]==a || en[j][0]==a && en[j][1]==last){
							list.clear();
							last=-1;
							bt=false;
							break;
						}
					}
				if (bt){
					if (last!=-1)
						list.push_back(last);
					last=cha;
				}
			
		}
		printf("Case #%d: [",++I);
		if (last!=-1)
			list.push_back(last);
		for (i=0;i<list.size();++i){
			printf("%c",list[i]);
			if (i<list.size()-1)
				printf(", ");
		}
		printf("]\n");
	}
}
