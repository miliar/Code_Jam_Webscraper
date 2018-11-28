#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

char words[5555][22];
bool flag[5555];
bool dict[26];
int getch(){
	int ch;
	while((ch=getchar())!=-1&&ch<=' ');
	return ch;
}
int main(){
	int L,D,T;
	scanf("%d%d%d",&L,&D,&T);
	for(int i=0;i<D;i++)
		scanf("%s",words[i]);
	for(int test=1;test<=T;test++){
		for(int i=0;i<D;i++)
			flag[i]=true;
		for(int i=0;i<L;i++){
			memset(dict,false,sizeof(dict));
			int ch=getch();
			if(ch!='(')
				dict[ch-'a']=true;
			else{
				while((ch=getch())!=')')
					dict[ch-'a']=true;
			}
			for(int j=0;j<D;j++)if(!dict[words[j][i]-'a'])
				flag[j]=false;
		}
		int cnt=0;
		for(int i=0;i<D;i++)if(flag[i])
			cnt++;
		printf("Case #%d: %d\n",test,cnt);
	}
}
