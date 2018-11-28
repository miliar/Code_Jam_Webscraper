#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ans","w",stdout);
	int l,d,n;
	cin>>l>>d>>n;
	int k=1;
	int i;
	vector <string> di;
	string tm;
	for(i = 0 ; i < d; i++)
	{
		cin>>tm;
		di.push_back(tm);
	}
	while(k<=n)
	{
	
		int t[17][27] ={0};
		string q;
		cin>>q;
		int j=-1;
		int fz=0,fy=0;
		for(i = 0 ; i < q.length() ; i++)
		{
			if(q[i]=='('){fz=1;j++;continue;}
			if(q[i]==')')
			{
				fy=0;fz =0;continue;
			}

			if(fz==0&&fy==0)
				t[++j][q[i]-'a'] = 1;
			
			else if(fz==1){
				t[j][q[i]-'a'] = 1;
			}
		}
		int an= 0;
		for(i = 0 ; i < d; i++)
		{
			int fla =1;
			for(j = 0 ; j < l ; j++)
			{
				if(t[j][di[i][j]-'a']!=1){fla = 0 ; break;}
			}
			if(fla)an++;
		}
		printf("Case #%d: %d\n",k,an);
		k++;

	}

	return 0;
}