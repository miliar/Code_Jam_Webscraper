
#include<cstdio>
#include<map>
using namespace std;

struct node{
	   char name[150];
	   bool operator<(const node &d)const{
	   		return strcmp(name,d.name)<0;
	   }
};

map<node,int> visit;
int n,m;
char s[150];

int main(){
	int T;
	scanf("%d",&T);
	for (int t=1;t<=T;++t){
		visit.clear();
		scanf("%d%d",&n,&m); gets(s);
		while (n--){
			  gets(s);
			  while (strlen(s)){
			  		node x; strcpy(x.name,s);
	  		  		visit[x]=1;
	  		  		for (int i=strlen(s)-1;i>=0;--i){
						if (s[i]=='/'){
			   			   s[i]='\0'; break;
			   			}
			   			s[i]='\0';
					}
	  		  }
  		}
  		int ans=0;
  		while (m--){
			  int add=0;
			  gets(s); node x; strcpy(x.name,s);
			  while (!visit[x]){
					++add; visit[x]=1;
					//puts(x.name);
					for (int i=strlen(x.name)-1;i>=0;--i){
						if (x.name[i]=='/'){x.name[i]='\0';break;}
						x.name[i]='\0';
					}
					if (strlen(x.name)==0) break;
	  		  }
	  		  ans+=add;
  		}
  		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
