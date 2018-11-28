#include<iostream>
#include<map>
#include<string>
using namespace std;
main()
{
	//temp.insert(pair<string,int>("ankur",6));
	//temp["anku"]=5;
	//cout<<temp["anku"]
	int n,s,q,i,j;
	scanf("%d",&n);
	map<string,int> temp;
	for(j=1;j<=n;j++)
	{
		temp.clear();
		int ans=0;
		temp.clear();
		string t,r;
		scanf("%d\n",&s);
		for(i=0;i<s;i++) 
			getline(cin, t, '\n');	
		scanf("%d\n",&q);
		if(!q)
			ans=0;
		else
		{
			for(i=0;i<q;i++)
			{	
				getline(cin, t, '\n');	
				if(i)
				{
					if(t!=r) {
						temp[r]=1;
						if(temp.size()==s) {
							ans++;
							temp.clear();
							temp[r]=1;

						}
					}
				}
				r=t;
			}
			temp[r]++;
			if(temp.size()==s)
				ans++;
		}
		printf("Case #%d: %d\n",j,ans);
	}
}
