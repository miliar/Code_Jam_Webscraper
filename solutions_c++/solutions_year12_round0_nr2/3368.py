using namespace std;
#include<iostream>
#include<cstdio>
#include<cstdlib>
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,n,s,p,g,normal,surprise,minn,mins;
	scanf("%d",&t);
	for(int k=0;k<t;k++){
		normal=surprise=0;
		printf("Case #%d: ",k+1);
		scanf("%d %d %d",&n,&s,&p);
		minn=p+(2*(p-1));
		mins=p+(2*(p-2));
		//cout<<minn<<" "<<mins<<endl;
		if(p==1)
			minn=mins=1;
		if(p==0)
			minn=mins=0;
		//cout<<minn<<" "<<mins<<endl;
		for(int i=0;i<n;i++){
			scanf("%d",&g);
			if(g>=minn){
				normal++;
				//cout<<"n\n";
			}				
			else if(g>=mins){
				surprise++;
				//cout<<"s\n";
			}				
		}
		if(surprise>s)
			surprise=s;
		printf("%d\n",normal+surprise);
	}
	return 0;
}
