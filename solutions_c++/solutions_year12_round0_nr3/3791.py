#include<cstdio>
#include<set>
#include<algorithm>
using namespace std;
int arr[10];
set<pair<int,int> > S;

int main()
{
	int A,B,i;
	int no,tc=1;
	scanf(" %d",&no);
	while(no--){
	int len=0,x;
	arr[0]=1;
	S.clear();
	for(i=1;i<10;i++) arr[i]=arr[i-1]*10;
	scanf( " %d %d",&A,&B);
	
	x=A;
	while(x) { len++;x/=10; }
	for(i=A;i<=B;i++)
	{
		int orig=i;
		int num=len;
		while(num--){
			int y=orig%10;
			orig/=10;
			orig=y*arr[len-1]+orig;
			pair<int,int> tmp=make_pair(min(orig,i),max(orig,i));
			if(orig<=B and orig>=A and orig!=i and !S.count(tmp)) {
				//printf("#%d:%d\n",orig,i);
				S.insert(make_pair(min(orig,i),max(orig,i)));
			}
		}
	
	}
	printf("Case #%d: %d\n",tc++,S.size());
	}
	return 0;
}
