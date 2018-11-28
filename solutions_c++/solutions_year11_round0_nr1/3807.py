
#include <iostream>

using namespace std;

int main()
{
	freopen("A-small-attempt4.in","r",stdin);
	freopen("A-small-attempt4.out","w",stdout);
	int t,n;
	cin>>t;
	char op[101];
	int val[101];
	int cnt=0;
	while(t--)
	{
		cin>>n;
		int res=1;
		for(int i=0;i<n;i++)
		{
			cin>>op[i]>>val[i];
		}
		int no,po,nb,pb;
		no=nb=1;
		int index1,index2;
		index1=index2=0;
		po=pb=1;
		char nowro=op[0];
		int nowindex=0;
		for(;index1<n;index1++)
			if(op[index1]=='O')
			{
				po=val[index1];
				break;
			}
		for(;index2<n;index2++)
			if(op[index2]=='B')
			{
				pb=val[index2];
				break;
			}
		
		while(1)
		{
			if(nowro=='O')
			{
				if(nb<pb)
					nb++;
				else if(nb>pb)
					nb--;
				if(no<po)
					no++;
				else if(no>po)
					no--;
				else if(no==po)//push
				{
					for(index1++;index1<n;index1++)
						if(op[index1]=='O')
						{
							po=val[index1];
							break;
						}
					nowindex++;
					if(nowindex<n)
						nowro=op[nowindex];
				}
			}
			else 
			{
				if(no<po)
					no++;
				else if(no>po)
					no--;
				if(nb<pb)
					nb++;
				else if(nb>pb)
					nb--;
				else if(nb==pb)
				{
					for(index2++;index2<n;index2++)
						if(op[index2]=='B')
						{
							pb=val[index2];
							break;
						}
					nowindex++;
					if(nowindex<n)
						nowro=op[nowindex];
				}
			}
			if(index1>=n&&index2>=n)
				break;
			res++;
		}
		cnt++;
		cout<<"Case #"<<cnt<<": "<<res<<endl;
	}	
	
	return 0;
}
